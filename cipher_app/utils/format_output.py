def format_output(text: str) -> str:
    """Форматирование выходной строки."""
    formatted_text = text.replace('тире', '-').replace('зпт', ',').replace('тчк', '.')
    return formatted_text
