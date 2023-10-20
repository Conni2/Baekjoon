import datetime
today = datetime.datetime.now()
kr__timedelta = datetime.timedelta(hours=9)
today_kr = today+kr__timedelta
print(today_kr.strftime("%Y-%m-%d"))