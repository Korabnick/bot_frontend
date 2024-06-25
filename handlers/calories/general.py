from typing import Any, List, Dict


async def make_message_and_get_data(
        items: List[Dict[str, Any]],
        max_counter: int,
        chat_id: int,
        add_item_end: bool = False,
) -> tuple[str, Dict[str, int], int]:
    message_text = "" if add_item_end else "Select the item you want to complete and write its number: \n\n"
    data_for_state = {}

    for item in items:
        item_time = await get_str_time(item['time'])
        timezone_offset = str(item['timezone_offset']) if item['timezone_offset'] < 0 else f'+{item["timezone_offset"]}'
        if not add_item_end:
            message_text += f"""
                {max_counter}. "{item['name']}"\n
                Время: {item_time} (UTC {timezone_offset})\n\n
            """
        else:
            message_text += f"""
                {max_counter}. "{item['name']}"\n
                Время: {item_time} (UTC {timezone_offset})\n\n
            """
        data_for_state[f"{chat_id}_item_{max_counter}"] = item['id']
        max_counter += 1
    message_text += "..."

    return message_text, data_for_state, max_counter


async def get_str_time(item_time: str) -> str:
    return item_time.split('T')[0] + " " + item_time.split('T')[1][:-7]
