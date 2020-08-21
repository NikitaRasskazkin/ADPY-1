def calculate_salary(salary: float):
    ndfl = 0.13
    print(f'Ваша зарплата {salary * (1 - ndfl):.2f} рублей')


if __name__ == '__main__':
    calculate_salary(123.2)
