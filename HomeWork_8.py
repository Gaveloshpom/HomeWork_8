from datetime import datetime, timedelta, date

users = [{"name": "Michael", "birthday": datetime(year=2022, day=8, month=11)},
          {"name": "Andrew", "birthday": datetime(year=2022, day=7, month=11)},
          {"name": "Mike", "birthday": datetime(year=2022, day=9, month=11)},
          {"name": "Jhon", "birthday": datetime(year=2022, day=10, month=11)},
          {"name": "Eminem", "birthday": datetime(year=2022, day=11, month=11)},
          {"name": "Some_guy", "birthday": datetime(year=2022, day=12, month=11)},
          ]

def get_birthdays_per_week(employee_list: list):

    result = {}

    for i in employee_list:
        employee_birthday = i["birthday"] #беремо ДР працівника
        employee_birthday = datetime(year=datetime.now().year, month=employee_birthday.month, day=employee_birthday.day)
        one_week_checker = (employee_birthday - datetime.now()).days

        if one_week_checker >= 7:
            continue #Відсіюємо ДР що не припадають на цей тиждень

        if employee_birthday.strftime("%A") in ("Saturday", "Sunday"):
            employee_birthday = weekend_check(employee_birthday)

        result.setdefault((employee_birthday.strftime("%A"), employee_birthday.date()), []).append(i["name"])
    no_name(result=result)
def weekend_check(birthday_date): #Переносимо ДР з вихідних на робочий день
    if birthday_date.strftime("%A") == "Saturday":
        birthday_date += timedelta(days=2)
        return birthday_date
    if birthday_date.strftime("%A") == "Sunday":
        birthday_date += timedelta(days=1)
        return birthday_date

def no_name(result):
    for k, v in sorted(result.items(), key=lambda x: x[0][1]):
        print(" {}, {}: {}".format(*k, ', '.join(v)))

if __name__ == "__main__":
    get_birthdays_per_week(users)