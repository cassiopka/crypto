def format_blocks(text: str) -> str:
    """Разделение строки на блоки по 5 символов."""
    return ' '.join([text[i:i+5] for i in range(0, len(text), 5)])
