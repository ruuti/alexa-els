from datetime import datetime
import calendar

"""
Return str of dateObj
"""
def format_date(dateObj, frmt='%Y-%m-%d'):
  return dateObj.strftime(frmt)

"""
Parse date string from date
(like "today at 1PM" or "on Tue at 5.30PM")
"""
def get_date_str(date_time):

  # Get todays date YYYY-MM-DD
  today = format_date(datetime.today())

  # Date YYYY-MM-DD
  date = format_date(date_time)

  # If todays date
  if today == date :
    date_str = 'today'
  else :
    weekday = date_time.weekday()
    weekday_name = calendar.day_name[weekday]
    date_str = 'on %s' % (weekday_name)

  time = format_date(date_time, '%I:%M %p')
  
  # Return string for example "on Monday at 1:00PM"
  return "%s at %s" % (date_str, time)

"""
Returns if datetime is in a future
"""
def is_upcoming(date):
  if date > datetime.today():
    return True
  return False