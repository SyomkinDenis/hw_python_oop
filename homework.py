import datetime as dt
from typing import Optional


class Record:
    def __init__(self, amount: int, comment: str, date: Optional[str] = None):
        date_format = '%d.%m.%Y'
        self.amount = amount
        if date is not None:
            self.date = dt.datetime.strptime(date, date_format).date()
        else:
            self.date = dt.date.today()
        self.comment = comment

    def __repr__(self):
        return f'{self.date}: {self.amount} ({self.comment})'


class Calculator:
    def __init__(self, limit: int):
        self.limit = limit
        self.records = []

    def add_record(self, record: Record):
        self.records.append(record)

    def get_today_stats(self):
        today = dt.date.today()
        today_records = [r.amount for r in self.records if r.date == today]
        return sum(today_records)

    def get_week_stats(self):
        today = dt.date.today()
        seven_days_ago = today - dt.timedelta(days=7)
        week_records = [r.amount for r in self.records if
                        today >= r.date >= seven_days_ago]
        return sum(week_records)

    def remain_limit(self):
        return self.limit - self.get_today_stats()


class CaloriesCalculator(Calculator):
    def get_calories_remained(self):
        remain_limit = self.remain_limit()
        if remain_limit > 0:
            return('Сегодня можно съесть что-нибудь ещё, '
                   f'но с общей калорийностью не более {remain_limit} кКал')
        return 'Хватит есть!'


class CashCalculator(Calculator):
    USD_RATE = 76.90
    EURO_RATE = 92.38

    def get_currency(self, currency: str):
        if currency == 'eur':
            return self.EURO_RATE, 'Euro'
        elif currency == 'usd':
            return self.USD_RATE, 'USD'
        return 1, 'руб'

    def get_today_cash_remained(self, currency: str):
        remain_limit = self.remain_limit()
        currency_rate, currency_name = self.get_currency(currency)
        currency_limit = round(remain_limit / currency_rate, 2)
        if currency_limit == 0:
            return 'Денег нет, держись'

        if currency_limit > 0:
            return f'На сегодня осталось {currency_limit} {currency_name}'

        else:
            currency_limit = abs(currency_limit)
            return f'Денег нет, держись: твой долг - {currency_limit} ' \
                   f'{currency_name}'
