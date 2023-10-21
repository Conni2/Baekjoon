time = input().split(" ")
cooking_time = int(input())
now_hour = int(time[0])
now_minute = int(time[1])
now_sec = int(time[2])
seconds = now_hour*3600 + now_minute*60 + now_sec + cooking_time 
done_hours = (seconds // 3600) % 24
done_minutes = (seconds % 3600) // 60
done_sec = (seconds % 3600) % 60 
print("{} {} {}".format(done_hours, done_minutes, done_sec))