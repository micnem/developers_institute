import datetime

today_date = datetime.datetime.now()
jan1 = datetime.datetime(2021, 1, 1, 0, 0, 0)
time_until = today_date - jan1
print(time_until)