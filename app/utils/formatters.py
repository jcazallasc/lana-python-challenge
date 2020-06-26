from babel.numbers import format_currency, format_decimal
from django.conf import settings


def format_price(
    price: int,
    currency_code: str = settings.DEFAULT_CURRENCY_CODE,
    locale: str = settings.DEFAULT_LOCALE,
) -> str:
    _price = price / 100 if price > 0 else price
    return format_currency(_price, currency_code, locale=locale)
