import re

def validate_phone(phone: str) -> bool:
    """Валидация российского номера телефона."""
    pattern = r'^\+?7\d{10}$'
    return bool(re.match(pattern, phone.replace('-', '').replace(' ', '')))

def validate_snils(snils: str) -> bool:
    """Валидация СНИЛС."""
    pattern = r'^\d{3}-\d{3}-\d{3} \d{2}$'
    return bool(re.match(pattern, snils))

def validate_email(email: str) -> bool:
    """Валидация email."""
    pattern = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
    return bool(re.match(pattern, email))
