import datetime


def check_date(user_input):
    try:
        datetime.datetime.strptime(user_input, '%d.%m.%Y')
        return True
    except ValueError:
        return False


def date_ipput():
    user_input = input('Введите дату в формате ДД.ММ.ГГГГ: ')
    return user_input