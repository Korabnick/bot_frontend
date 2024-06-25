# from aiogram import F, types

# from core.buttons import CHANGE_NOTIFICATION_TIME, timezone_kb, timezone_hours
# from core.config import settings
# from handlers.calories.router import calories_router
# from utils.request import do_request


# @calories_router.message(F.text == CHANGE_NOTIFICATION_TIME)
# async def change_notification_time(message: types.Message):
#     await message.answer(
#         'Select a new time zone for notifications:',
#         reply_markup=timezone_kb,
#     )


# @calories_router.callback_query(F.data.in_(timezone_hours))
# async def process_timezone_change(callback: types.CallbackQuery):
#     async with do_request(
#             url=f'{settings.BOT_BACKEND_HOST}/user/notification_time',
#             params={'timezone': int(callback.data)},
#             headers={
#                 'user_from_id': str(callback.from_user.id),
#                 'Authorization': f'Bearer {settings.AUTH_KEY}'},
#             method='PATCH'
#     ) as response:
#         if response.status == 200:
#             await callback.answer('Notification time has been changed')
#         else:
#             await callback.answer('An error has occurred. Please try again.')
