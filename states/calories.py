from aiogram.fsm.state import State, StatesGroup


class CaloriesState(StatesGroup):
    choose_period = State()
    view_calories = State()
    add_calories = State()
    enter_calories = State()
    done = State()


class NotificationState(StatesGroup):
    set_time = State()
    confirm_time = State()

    
class NotificationTimeState(StatesGroup):
    set_hour = State()
    set_minute = State()


class MainState(StatesGroup):
    start_menu = State()
