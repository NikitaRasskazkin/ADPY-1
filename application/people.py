import json


def get_employees():
    with open('application/db/employees.json', 'r', encoding='utf-8') as f:
        employees = json.load(f)
    return employees


if __name__ == '__main__':
    get_employees()
