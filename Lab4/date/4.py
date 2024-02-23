from datetime import datetime

def difference_in_second(date1, date2):
    first = datetime.strptime(date1,"%Y-%m-%d %H:%M:%S")
    second = datetime.strptime(date2,"%Y-%m-%d %H:%M:%S")

    delta = abs(first - second).total_seconds()
    return delta

one = input("First date = ")
two = input("Second date = ")

total = difference_in_second(one, two)
print(f"Total second = {total}")