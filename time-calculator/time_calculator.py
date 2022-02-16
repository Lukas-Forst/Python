def add_time(start, duration, day=None):
  #check the length of start and duration to add a 0 infront to prevent ":"
  #being added at slicing
  if len(duration) < 5:
    duration = "0"+duration 
  if len(start) < 7:
    start = "0" + start

  #print(duration)
  #seperate am and pm from time 
  start_time = start[:-2]
  time_zone = start[-2:]
  start_time = start_time.strip()
  
  start_time_hour = start_time[:-3]
  start_time_minute = start_time[-2:]
  minutes_add = duration[-2:]
  hour_add = duration[:-3]

  minute_new = int(minutes_add) + int(start_time_minute)

  hour_new = int(hour_add) + int(start_time_hour)
  
  hour_change = False


  #adding 12 hours if the start time contains PM
  if time_zone == "PM":
    hour_new += 12
  #check if minutes added are greater than 60
  if minute_new > 60:
    hour_new += 1
    minute_new = minute_new - 60
    hour_change = True

  days = hour_new // 24

  if days > 1:
    days_string = "({} days later)".format(days)
  elif days == 1:
    days_string = "(next day)"
  else:
    days_string = ""

  print(hour_new < 24)
  #get final hour
  while (hour_new > 24):
    hour_new = hour_new - 24
    #print(hour_new)

  #get_am / PM
  am_pm = "AM" if hour_new < 12 else "PM"

  #print(hour_new, am_pm, hour_new < 13)
  #substract 12 from PM to bring it to the right format
  if hour_new == 24:
    am_pm = "AM"
    hour_new = hour_new -12


  if (hour_new > 13) and (am_pm == "PM"):
    hour_new = hour_new -12 
  
  #if (hour_new == 12) and (am_pm == "PM"):
  #  am_pm = "AM"

  #if (hour_new == 12) and (days )

  # to get the final day
  while (days > 7):
    days = days - 7

  if day != None:
    num_day = get_day_num(day.lower())
    if num_day + days > 7:
      new_num = (num_day + days)-7
      day_n = get_day(new_num)
    else:
      day_n = get_day(num_day + days)
  #new_time = days_string
  #print("TEST", (hour_new == 12) and (am_pm == "PM"))
  #print(start, duration)
  print(minute_new, hour_new, days)
  if minute_new < 10:
    minute_string = "0{}".format(minute_new)
  else:
    minute_string = str(minute_new)

  


  if day != None:
    new_time = "{}:{} {}, {} {}".format(hour_new, minute_string, am_pm, day_n.capitalize(),days_string)
  else:
    new_time = "{}:{} {} {}".format(hour_new, minute_string, am_pm, days_string)


  return new_time.strip()


def get_day_num(day):
  week_dict = {
    "monday":1,
    "tuesday":2,
    "wednesday":3,
    "thursday":4,
    "friday":5,
    "saturday":6,
    "sunday":7
  }
  return week_dict[day]


def get_day(day):
    week_dict = {
    1: "monday",
    2: "tuesday",
    3: "wednesday",
    4: "thursday",
    5: "friday",
    6: "saturday",
    7: "sunday"
  }
    return week_dict[day]
