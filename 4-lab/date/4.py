import datetime

date1_str = input("Enter the first date: ")  #(YYYY-MM-DD HH:MM:SS)
date2_str = input("Enter the second date: ")

date1 = datetime.datetime.strptime(date1_str, "%Y-%m-%d %H:%M:%S")
date2 = datetime.datetime.strptime(date2_str, "%Y-%m-%d %H:%M:%S")

difference_in_seconds = (date2 - date1).total_seconds()

print(difference_in_seconds)