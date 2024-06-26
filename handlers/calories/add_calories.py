from aiogram import F, types
from aiogram.fsm.context import FSMContext

from core.buttons import ADD_CALORIES, go_back_keyboard, get_main_keyboard
from handlers.calories.router import calories_router
from states.calories import CaloriesState
from utils.request import do_request
from core.config import settings

from datetime import datetime


@calories_router.message(F.text == ADD_CALORIES)
async def add_calories(message: types.Message, state: FSMContext):
    await state.set_state(CaloriesState.enter_calories)
    await message.answer(
        text="Enter the number of calories you have consumed:",
        reply_markup=go_back_keyboard(),
    )


@calories_router.message(CaloriesState.enter_calories)
async def save_calories(message: types.Message, state: FSMContext) -> None:
    if message.text.isdigit():
        calories = int(message.text)
        timestamp = datetime.utcnow().isoformat() + 'Z'

        async with do_request(
                url=f'{settings.BOT_BACKEND_HOST}/calories',
                json={
                    'amount': calories,
                    'timestamp': timestamp,
                    'timezone_offset': 0
                },
                headers={
                    'user-from-id': str(message.from_user.id),
                    'accept': 'application/json',
                    'Content-Type': 'application/json'
                },
                method='POST'
        ) as response:
            if response.status == 201:
                await state.clear()
                await message.answer(
                    f'Entered {calories} calories.',
                    reply_markup=get_main_keyboard()
                )
            else:
                await message.answer(
                    'An error has occurred. Please try again.',
                    reply_markup=go_back_keyboard()
                )
    else:
        await message.answer(
            'Please enter a number.',
            reply_markup=go_back_keyboard()
        )