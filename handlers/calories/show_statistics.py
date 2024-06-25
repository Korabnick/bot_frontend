from aiogram import F, types
from aiogram.fsm.context import FSMContext

from core.buttons import SHOW_STATS, get_stats_keyboard, GO_BACK, DAILY_STATS, WEEKLY_STATS, MONTHLY_STATS, go_back_keyboard, get_main_keyboard
from handlers.calories.router import calories_router
from states.calories import MainState, CaloriesState
from utils.request import do_request, do_request_get
from core.config import settings


@calories_router.message(F.text == SHOW_STATS)
async def show_stats(message: types.Message, state: FSMContext):
    await state.set_state(CaloriesState.choose_period)
    await message.answer(
        text="Select a period for statistics:",
        reply_markup=get_stats_keyboard(),
    )


@calories_router.message(CaloriesState.choose_period)
async def show_period_stats(message: types.Message, state: FSMContext) -> None:
    period = message.text
    if period in [DAILY_STATS, WEEKLY_STATS, MONTHLY_STATS]:
        period_param = {
            DAILY_STATS: 'day',
            WEEKLY_STATS: 'week',
            MONTHLY_STATS: 'month'
        }
        print(f"Requesting stats for period: {period_param[period]}")
        async with do_request_get(
                url=f'{settings.BOT_BACKEND_HOST}/stats',
                params={'period': period_param[period]},
                headers={
                    'user-from-id': str(message.from_user.id),  # Исправлено на 'user-from-id'
                    'Authorization': f'Bearer {settings.AUTH_KEY}'},
                method='GET'
        ) as response:
            print(f"Response status: {response.status}")
            if response.status == 200:
                stats = await response.json()
                print(f"Response data: {stats}")

                # Формирование красивого сообщения для вывода статистики
                if period == DAILY_STATS:
                    period_label = "Daily"
                elif period == WEEKLY_STATS:
                    period_label = "Weekly"
                elif period == MONTHLY_STATS:
                    period_label = "Monthly"
                else:
                    period_label = "Unknown"

                total_calories = stats.get('total', 0.0)
                daily_average_calories = stats.get('daily_average', 0.0)

                response_text = (
                    f"Your {period_label.lower()} statistics:\n"
                    f"Total calories: {total_calories}\n"
                    f"Daily average: {daily_average_calories}"
                )

                await message.answer(
                    response_text,
                    reply_markup=get_main_keyboard()
                )
            else:
                await message.answer(
                    'An error has occurred. Try again.',
                    reply_markup=go_back_keyboard()
                )
    elif message.text == GO_BACK:
        await state.set_state(MainState.start_menu)
        await message.answer(
            'Returned to the main menu.',
            reply_markup=get_main_keyboard()
        )
