time = input().split(" ")
cooking_time = int(input())
now_hour = int(time[0])
now_minute = int(time[1])
minutes = now_hour*60 + now_minute + cooking_time
done_hours = (minutes // 60) % 24
done_minutes = minutes % 60
print("{} {}".format(done_hours, done_minutes))