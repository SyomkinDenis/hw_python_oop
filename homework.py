import datetime as dt
from typing import Optional


class Record:
    def __init__(self, amount, comment, date: Optional[str] = None):
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
    def __init__(self, limit):
        self.limit = limit
        self.records = []
        print(self.records)

    def add_record(self, record: Record):
        self.records.append(record)

    def get_today_stats(self):
        today_records = [r for r in self.records if r.date == dt.date.today()]
        for r in today_records:
            print(r)
        today_sum = 0
        for r in today_records:
            today_sum += r.amount
        return today_sum

    def get_week_stats(self):
        today = dt.date.today()
        seven_days_ago = today - dt.timedelta(days=7)
        week_records = [r for r in self.records if
                        today >= r.date >= seven_days_ago]
        week_sum = 0
        for r in week_records:
            week_sum += r.amount
        return week_sum

    def remain_limit(self):
        print(self.limit, self.get_today_stats())
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
    CURRENCY_NAME = {'rub': 'руб', 'eur': 'Euro', 'usd': 'USD'}

    def get_rate(self, currency):
        if currency != 'rub':
            return(getattr(self,
                           f'{self.CURRENCY_NAME[currency].upper()}_RATE'))
        return 1

    def get_today_cash_remained(self, currency='rub'):
        remain_limit = self.remain_limit()
        currency_limit = round(remain_limit / self.get_rate(currency), 2)

        if currency_limit > 0:
            return('На сегодня осталось '
                   f'{currency_limit} '
                   f'{self.CURRENCY_NAME[currency]}')

        elif currency_limit < 0:
            return('Денег нет, держись: твой долг - '
                   f'{abs(currency_limit)} '
                   f'{self.CURRENCY_NAME[currency]}')
        else:
            return 'Денег нет, держись'
