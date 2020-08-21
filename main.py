from application.salary import calculate_salary
from application.people import get_employees
from pprint import pprint
import datetime


if __name__ == '__main__':
    date = datetime.datetime.today()
    print(f'Дата: {date.date()}')
    calculate_salary(123.2)
    employees = get_employees()
    pprint(employees)
