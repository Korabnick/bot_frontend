from aiogram import types
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

ADD_CALORIES = 'add calories'
SHOW_STATS = 'calorie statistics'
CHANGE_NOTIFICATION_TIME = 'change the notification time'
GO_BACK = "return"

DAILY_STATS = 'statistics for the day'
WEEKLY_STATS = 'statistics for the week'
MONTHLY_STATS = 'statistics for the month'


def get_main_keyboard() -> types.ReplyKeyboardMarkup:
    kb = [
        [types.KeyboardButton(text=ADD_CALORIES)],
        [types.KeyboardButton(text=SHOW_STATS)],
        [types.KeyboardButton(text=CHANGE_NOTIFICATION_TIME)],
    ]
    return types.ReplyKeyboardMarkup(keyboard=kb, resize_keyboard=True)


def get_stats_keyboard() -> types.ReplyKeyboardMarkup:
    kb = [
        [types.KeyboardButton(text=DAILY_STATS)],
        [types.KeyboardButton(text=WEEKLY_STATS)],
        [types.KeyboardButton(text=MONTHLY_STATS)],
        [types.KeyboardButton(text=GO_BACK)],
    ]
    return types.ReplyKeyboardMarkup(keyboard=kb, resize_keyboard=True)


def go_back_keyboard() -> types.ReplyKeyboardMarkup:
    return types.ReplyKeyboardMarkup(
        keyboard=[[types.KeyboardButton(text=GO_BACK)]],
        resize_keyboard=True
        )


timezone_hours = [
    str(number)
    if number <= 0 else f'+{number}'
    for number in range(-12, 13)
    ]

timezoneButtons = [
    InlineKeyboardButton(text=timedelta, callback_data=timedelta)
    for timedelta in timezone_hours
    ]

out = [timezoneButtons[i:i + 3] for i in range(0, len(timezoneButtons), 3)]
timezone_kb = InlineKeyboardMarkup(inline_keyboard=out)
