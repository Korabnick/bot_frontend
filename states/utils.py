from core.buttons import get_main_keyboard, go_back_keyboard, get_stats_keyboard
from states.general import MainState

previous_states = {
    'CalorieState:add_calories': 'CalorieState:view_calories',
    'NotificationState:set_time': 'NotificationState:confirm_time',
    'CaloriesState:choose_period': 'CalorieState:view_calories',
}

state_to_keyboard = {
    'CalorieState:add_calories': get_main_keyboard(),
    'NotificationState:set_time': get_main_keyboard(),
    'CaloriesState:choose_period': get_stats_keyboard(),
    'CaloriesState:enter_calories': go_back_keyboard(),
    MainState.start_menu: get_main_keyboard(),  
}

state_to_message = {
    'CalorieState:add_calories': 'Enter the number of calories',
    'NotificationState:set_time': 'Set the notification time',
    'CaloriesState:choose_period': 'Select a period for statistics:',
    'CaloriesState:enter_calories': 'Enter the number of calories you have consumed:',
    MainState.start_menu: 'Returned to the main menu',
}