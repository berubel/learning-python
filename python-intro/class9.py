from datetime import date, time, datetime, timedelta

def working_with_date():
    today = date.today()
    print(today.strftime('%d/%m/%Y'))
    print(today.strftime('%A, %B %Y'))

def working_with_time():
    clock = time(hour=15, minute=18, second=30)
    print(clock.strftime('%H:%M:%S'))


def working_with_datetime():
    today = datetime.now()
    print(today.strftime('%B %d, %Y - %H:%M:%S'))
    print(today.strftime('%c'))
    print(today.weekday())
    week = ('Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday')
    print(week[today.weekday()])
    created_date = datetime(2002, 2, 22, 18, 50, 0)
    print(created_date.strftime('%B %d, %Y - %A at %H:%M'))
    str_date = '21/08/2022'
    converted_date = datetime.strptime(str_date, '%d/%m/%Y')
    print(converted_date, type(converted_date))
    age = datetime.now() - created_date
    print(age)
    new_date = datetime.now() - timedelta(days=100, hours=5)
    print(new_date)

if __name__ == '__main__':
    working_with_date()
    working_with_time()
    working_with_datetime()

