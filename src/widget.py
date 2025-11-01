def mask_card_number(card_number: str) -> str:
    """Маскирует номер карты, оставляя последние 4 цифры видимыми."""
    return "**** **** **** " + card_number[-4:]


def mask_account_number(account_number: str) -> str:
    """Маскирует номер счета, оставляя видимыми только последние 5 цифр."""
    return "**** **** **** **** **** " + account_number[-5:]


def mask_account_card(info: str) -> str:
    """Обрабатывает информацию о картах и счетах и возвращает замаскированный номер.

    Аргументы:
        info (str): Строка, содержащая тип и номер карты или счета.

    Возвращает:
        str: Замаскированный номер карты или счета.
    """
    parts: list[str] = info.split()

    if len(parts) < 2:
        raise ValueError("Неверный формат входной строки.")

    type_info: str = parts[0]
    number: str = parts[1]

    if type_info in ["Visa", "MasterCard", "Maestro", "AmericanExpress"]:
        return mask_card_number(number)
    elif type_info == "Счет":
        return mask_account_number(number)
    else:
        raise ValueError("Неизвестный тип информации.")


from datetime import datetime

def get_date(date_string: str) -> str:
    """Преобразует строку с датой из формата 'YYYY-MM-DDTHH:MM:SS.ssssss' в формат 'ДД.ММ.ГГГГ'."""
    # Парсим входную строку в объект datetime
    dt: datetime = datetime.fromisoformat(date_string)

    # Форматируем дату в нужный формат
    return dt.strftime("%d.%m.%Y")
