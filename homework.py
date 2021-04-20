import datetime as dt

class Calculator:
    def __init__(self, limit):
        self.limit = limit
        self.records = []
        print(limit)

    def add_record(self, record):#Сохранять новую запись
        self.records.append(record)
        print(self.records)

    def get_today_stats(self):#Считать, сколько денег\калорий потрачено сегодня
        for i in self.records:
            for ammout in i:
                if

    def get_week_stats(self):#Считать, сколько денег\калорий потрачено за последние 7 дней
        pass

class Record:
    def __init__(self, amount, date, comment):
        self.amount = amount
        self.date = date
        self.comment = comment

    def process_records(self):
        record = [self.amount, self.date, self.comment]
        return record

class CaloriesCalculator(Calculator):
    pass

class CashCalculator(Calculator):
    pass




cash_calculator = Calculator(1000)

r1 = Record(amount=145, comment='Безудержный шопинг', date='08.03.2019')
r2 = Record(amount=500, comment='Безудержный шопинг', date='08.03.2020')

cash_calculator.add_record(r1.process_records())
cash_calculator.add_record(r2.process_records())