def print_month_name(month_number):
    months = {
        1: "January",
        2: "February",
        3: "March",
        4: "April",
        5: "May",
        6: "June",
        7: "July",
        8: "August",
        9: "September",
        10: "October",
        11: "November",
        12: "December"
    }

    if month_number in months:
        print(months[month_number])
    else:
        print("Invalid month number. Month number should be between 1 and 12.")

# Example usage
while True:
    month_number = int(input("Enter the month number (1-12): "))
    print_month_name(month_number)