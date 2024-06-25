# from aiogram import F, types
# from aiogram.fsm.context import FSMContext

# from core.buttons import timezone_kb, CHANGE_NOTIFICATION_TIME, timezone_hours
# from handlers.change_timezone.router import user_router
# from utils.request import do_request
# from core.config import settings


# @user_router.message(F.text == CHANGE_NOTIFICATION_TIME)
# async def change_notification_time(message: types.Message, state: FSMContext):
#     print("Received CHANGE_NOTIFICATION_TIME command")
#     await message.answer(
#         'Please enter your new notification time in format hh:mm'
#     )


# @user_router.callback_query(F.data.in_(timezone_hours))
# async def process_notification_time(callback):
#     async with do_request(
#             url=f'{settings.BOT_BACKEND_HOST}/user/notification_time',
#             params={'hour': callback.data.split(':')[0], 'minute': callback.data.split(':')[1]},
#             headers={'user_from_id': str(callback.from_user.id)}
#     ) as response:
#         if response.status == 200:
#             await callback.answer('Notification time was changed!')
#         else:
#             await callback.answer('An error has occurred. Please try again')
