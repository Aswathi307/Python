print("name:T P Aswathi\n","sec:o\n","usn:1AY24AI109")
from datetime import datetime

today = datetime.today()
print("Today's Date:", today.date())
print("Day of the Week:", today.strftime("%A")) 




print("name:T P Aswathi\n","sec:o\n","usn:1AY24AI109")
from datetime import datetime, timedelta

def birthday_info(birth_date_str):
    birth_date = datetime.strptime(birth_date_str, "%Y-%m-%d")
    today = datetime.today()

 
    age = today.year - birth_date.year
    if (today.month, today.day) < (birth_date.month, birth_date.day):
        age -= 1

    next_birthday = datetime(today.year, birth_date.month, birth_date.day)
    if next_birthday < today:
        next_birthday = datetime(today.year + 1, birth_date.month, birth_date.day)

    time_until = next_birthday - today
    total_seconds = int(time_until.total_seconds())
    days = time_until.days
    hours = (total_seconds % 86400) // 3600
    minutes = (total_seconds % 3600) // 60
    seconds = total_seconds % 60

    print(f"Your age: {age} years")
    print(f"Time until next birthday: {days} days, {hours} hours, {minutes} minutes, {seconds} seconds")

birthday_info("2005-08-15")




print("name:T P Aswathi\n","sec:o\n","usn:1AY24AI109")
from datetime import datetime, timedelta

def find_double_day(birth1_str, birth2_str):
    b1 = datetime.strptime(birth1_str, "%Y-%m-%d")
    b2 = datetime.strptime(birth2_str, "%Y-%m-%d")

    if b1 > b2:
        older, younger = b2, b1
    else:
        older, younger = b1, b2

    diff = younger - older
    double_day = younger + diff
    print("Double Day is on:", double_day.date())


find_double_day("2000-01-01", "2004-01-01")




print("name:T P Aswathi\n","sec:o\n","usn:1AY24AI109")
from datetime import datetime, timedelta # Import datetime and timedelta

def n_times_older_day(birth1_str, birth2_str, n):
    b1 = datetime.strptime(birth1_str, "%Y-%m-%d")
    b2 = datetime.strptime(birth2_str, "%Y-%m-%d")

    if b1 > b2:
        older, younger = b2, b1
        invert = True
    else:
        older, younger = b1, b2
        invert = False

    diff = younger - older
    target_diff_seconds = diff.total_seconds() / (n - 1)
    target_diff = timedelta(seconds=target_diff_seconds)

    n_day = older + target_diff

    if invert:
        print(f"{n} times older day is on: {n_day.date()} (younger person born first)")
    else:
        print(f"{n} times older day is on: {n_day.date()}")


n_times_older_day("2000-01-01", "2004-01-01", 3) 
