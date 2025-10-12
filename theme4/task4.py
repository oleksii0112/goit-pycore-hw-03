from datetime import datetime, timedelta

def get_upcoming_birthdays(users):
    today_date= datetime.today().date()
    upcoming_birthdays = []

    for user in users:
        birthday = datetime.strptime(user["birthday"], "%Y.%m.%d").date()
        current_year_birthday = birthday.replace(year=today_date.year)

        if current_year_birthday < today_date:
            current_year_birthday = current_year_birthday.replace(year=today_date.year + 1)

        days_until_birthday = (current_year_birthday - today_date).days
        
        if 0 < days_until_birthday <= 7:
                
            if current_year_birthday.weekday() == 5:  # Saturday
                current_year_birthday += timedelta(days=2)
            elif current_year_birthday.weekday() == 6:  # Sunday
                current_year_birthday += timedelta(days=1)

            upcoming_birthdays.append({"name": user["name"], 
                            "congratulation_date": current_year_birthday.strftime("%Y.%m.%d")})
    return upcoming_birthdays                                     
users = [
    {"name": "John Doe", "birthday": "1985.01.23"},
    {"name": "Jane Smith", "birthday": "1990.01.27"},
    {"name": "Alex Grey", "birthday": "1972.10.18"},
    {"name": "Sam Smith", "birthday": "2001.06.15"},
    {"name": "Anna Doe", "birthday": "1988.12.08"},
    {"name": "Lisa Kudrow", "birthday": "1983.07.30"} 
]
upcoming_birthdays = get_upcoming_birthdays(users) 
print("Список привітань на цьому тижні:", upcoming_birthdays)

