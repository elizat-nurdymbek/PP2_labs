import datetime

now = datetime.datetime.now()

without = now.replace(microsecond=0)

print(without)