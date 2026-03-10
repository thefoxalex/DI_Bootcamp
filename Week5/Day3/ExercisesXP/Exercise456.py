import datetime

def display_current_date():
    current_date = datetime.date.today()

    print(f"Today's date is: {current_date}.")

display_current_date()


now = datetime.datetime.now()

next_year = now.year + 1
new_year = datetime.datetime(next_year, 1, 1)

time_left = new_year - now

print(f"Time left until January 1, {next_year}: {time_left}")

def calculate_minutes_lived():
    birth_date_str = input("Enter your birth date (DD-MM-YYYY): ")
    
    try:
        birth_date = datetime.datetime.strptime(birth_date_str, "%d-%m-%Y")
        now = datetime.datetime.now()
        delta = now - birth_date
        
        minutes_lived = int(delta.total_seconds() / 60)
        
        if minutes_lived < 0:
            print("Wait... are you from the future? 🚀")
        else:
            print(f"You have lived for approximately {minutes_lived:,} minutes. 🌟")
            
    except ValueError:
        print("Invalid format! Please use YYYY-MM-DD (e.g., 1998-12-31).")

calculate_minutes_lived()
