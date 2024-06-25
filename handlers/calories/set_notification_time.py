# from aiogram import types
# from aiogram.fsm.context import FSMContext

# from core.buttons import go_back_keyboard, get_main_keyboard
# from handlers.notifications.router import notification_router
# from states.calories import NotificationState
# from utils.request import do_request
# from core.config import settings


# @notification_router.message(commands=['set_notification_time'])
# async def set_notification_time(message: types.Message, state: FSMContext):
#     await state.set_state(NotificationTimeState.set_hour)
#     await message.answer(
#         text="Enter the hour for daily notifications (0-23):",
#         reply_markup=go_back_keyboard()
#     )

# @notification_router.message(NotificationTimeState.set_hour)
# async def set_hour(message: types.Message, state: FSMContext):
#     if message.text.isdigit() and 0 <= int(message.text) <= 23:
#         await state.update_data(hour=int(message.text))
#         await state.set_state(NotificationTimeState.set_minute)
#         await message.answer(
#             text="Enter the minute for daily notifications (0-59):",
#             reply_markup=go_back_keyboard()
#         )
#     else:
#         await message.answer(
#             text="Please enter a valid hour (0-23):",
#             reply_markup=go_back_keyboard()
#         )

# @notification_router.message(NotificationTimeState.set_minute)
# async def set_minute(message: types.Message, state: FSMContext):
#     if message.text.isdigit() and 0 <= int(message.text) <= 59:
#         user_data = await state.get_data()
#         hour = user_data['hour']
#         minute = int(message.text)

#         async with do_request(
#                 url=f'{settings.BOT_BACKEND_HOST}/user/notification_time',
#                 json={
#                     'hour': hour,
#                     'minute': minute
#                 },
#                 headers={
#                     'user-from-id': str(message.from_user.id),
#                     'accept': 'application/json',
#                     'Content-Type': 'application/json'
#                 },
#                 method='POST'
#         ) as response:
#             if response.status == 200:
#                 await message.answer(
#                     text=f"Notification time set to {hour:02d}:{minute:02d}.",
#                     reply_markup=get_main_keyboard()
#                 )
#                 await state.clear()
#             else:
#                 await message.answer(
#                     text="An error occurred while setting the notification time. Please try again.",
#                     reply_markup=go_back_keyboard()
#                 )
#     else:
#         await message.answer(
#             text="Please enter a valid minute (0-59):",
#             reply_markup=go_back_keyboard()
#         )




# # from aiogram import F, types
# # from aiogram.fsm.context import FSMContext

# # from core.buttons import CHANGE_NOTIFICATION_TIME, go_back_keyboard, get_main_keyboard, timezone_hours, timezone_kb
# # from handlers.calories.router import calories_router
# # from utils.request import do_request
# # from core.config import settings

# # from datetime import datetime


# # @calories_router.message(F.text == CHANGE_NOTIFICATION_TIME)
# # async def change_notification_time(message: types.Message, state: FSMContext):
# #     print("Received CHANGE_NOTIFICATION_TIME command")
# #     await message.answer(
# #         'Please enter your new notification time in format hh:mm'
# #     )


# # @calories_router.callback_query(F.data.in_(timezone_hours))
# # async def process_notification_time(callback):
# #     async with do_request(
# #             url=f'{settings.BOT_BACKEND_HOST}/user/notification_time',
# #             params={'hour': callback.data.split(':')[0], 'minute': callback.data.split(':')[1]},
# #             headers={'user_from_id': str(callback.from_user.id)}
# #     ) as response:
# #         if response.status == 200:
# #             await callback.answer('Notification time was changed!')
# #         else:
# #             await callback.answer('An error has occurred. Please try again')
