# Question 5 — Days passed since birthday (only whole years, exclude birth year and current year)

def days_since_birthday(birthday):
    """
    Calculates how many days have passed since birthday, counting only whole years
    (excludes birth year and current year)
    :param birthday: string in format "DD-MM-YYYY"
    :return: number of days from whole years only
    """
    parts = birthday.split("-")
    birth_year = int(parts[2])
    current_year = 2026

    total_days = 0
    for year in range(birth_year + 1, current_year):
        # check if leap year (divisible by 4, but not 100, unless also 400)
        if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
            total_days += 366
        else:
            total_days += 365

    return total_days


# Test with birthday 10-08-2005
# Whole years counted: 2006, 2007, 2008, ..., 2025 (20 years)
result = days_since_birthday("10-08-2005")
print(f"Days from whole years: {result}")
