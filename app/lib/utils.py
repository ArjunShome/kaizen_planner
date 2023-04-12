import random
import re
from datetime import datetime
from string import ascii_letters

import pytz

from app.lib.constants import VALID_OTP_CHARS, OTP_CHARS_COUNT


def utc_timestamp() -> datetime:
    """
    Returns:
        datetime - datetime object which is converted UTC time based on local time.
    """
    return pytz.utc.localize(datetime.utcnow())


def extract_digits(text):
    if not isinstance(text, str):
        return

    res = ''.join(filter(lambda i: i.isdigit(), text))
    return res


def us_format_phone(phone_num):
    if not isinstance(phone_num, str):
        return

    phone_num = extract_digits(phone_num)
    format_phone = '-'.join(re.findall(r'\d{4}$|\d{3}', phone_num))
    return format_phone or None


def flatten_list(inp_list):
    flat_list = []
    for item in inp_list:
        if isinstance(item, str):
            flat_list.append(item)
        else:
            try:
                item = iter(item)
            except TypeError:
                flat_list.append(item)
            else:
                flat_list.extend(flatten_list(item))

    return flat_list


def to_list(inp_obj):
    if isinstance(inp_obj, str):
        return [inp_obj]

    try:
        iter(inp_obj)
    except TypeError:
        return [inp_obj]

    return flatten_list(inp_obj)


def emails_to_list(emails):
    if not emails:
        return []

    if isinstance(emails, str):
        emails = map(lambda email: email.strip(), emails.split(','))
        return to_list(emails)

    return emails


def generate_otp(valid_otp_chars=VALID_OTP_CHARS, otp_char_count=OTP_CHARS_COUNT):
    chars = list(valid_otp_chars)
    random.shuffle(chars)
    otp_chars = [chars[random.randrange(0, len(chars))] for i in range(otp_char_count)]
    return ''.join(otp_chars)


def get_name_with_timestamp(name):
    utcnow = datetime.utcnow()
    return f'{name}_{utcnow.strftime("%Y%m%d_%H%M%S")}'


def extract_date(text):
    pattern = '\\d{8}'
    date_str = re.findall(pattern, text)
    if not date_str:
        return None, None

    return date_str[0], datetime.strptime(date_str[0], '%Y%m%d').date()


def generate_random_chars(char_length=32, is_alnum=True):
    chars = ''.join(map(str, range(10)))
    if is_alnum:
        chars = f'{chars}{ascii_letters}'

    random_chars = [random.choice(chars) for _ in range(char_length)]

    return ''.join(random_chars)
