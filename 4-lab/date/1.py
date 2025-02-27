import datetime
x = datetime.date.today()

new = x - datetime.timedelta(days=5)

print(new)
print(new.strftime("%A"))
print(new.strftime("%d"))