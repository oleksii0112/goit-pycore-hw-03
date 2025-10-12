from datetime import datetime
your_date = input("Enter a date (YYYY-MM-DD): ")

def get_days_from_today(date):
    try:
        current_date = datetime.today().date()
        your_date_str = datetime.strptime(date, "%Y-%m-%d").date()
        delta = current_date - your_date_str
        return (delta.days)
    except:
        print("Invalid date format. Please use 'YYYY-MM-DD'.")
print(get_days_from_today(your_date))