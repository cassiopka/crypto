def format_input(text: str) -> str:
    """Форматирование входной строки."""
    formatted_text = text.lower().replace('.', 'тчк').replace(',', 'зпт').replace('-', 'тире').replace(' ', '')
    return formatted_text
