import os
from ELSPy.ELS import ELS
from datetime import datetime, timedelta
from date_helper import get_date_str, is_upcoming, format_date

"""
Returns boolean if slot should is bookable
"""
def is_bookable(availibity, start_datetime):
  
  # Is slot marked as free and start_datetime is in future
  if availibity['IsFree'] and is_upcoming(start_datetime):
    return True
  return False

"""
Retuns an array of available slots in a future
"""
def get_available_slots(bookings):
  
  availibity_arr = []
  
  # Loop each day
  for booking in bookings:
    for slot in booking['BookPasses']['BookDayPass']:
      
      # Parse datetime object when booking starts
      start_date = booking['BookDate']
      start_time = slot['StartTime']
      start_datetime = datetime.strptime('%s %s' % (start_date, start_time), '%Y-%m-%d %H:%M')

      for availibity in slot['PassAvailability']['Availability']:

        if is_bookable(availibity, start_datetime):

          availibity_arr.append({
            'date_str' : get_date_str(start_datetime)
          })
  
  return availibity_arr

"""
Returns next available time that can be booked
"""
def get_next_available_time():
  
  # Init ELS
  wsdl = os.environ['WSDL']
  username = os.environ['WSDL_USERNAME']
  password = os.environ['WSDL_PASSWORD']
  client = ELS(wsdl, username, password)

  # Set daterange: now - (now+7days)
  start_date = datetime.today()
  end_date = start_date + timedelta(days=7)

  # TODO: should happen on ELS library.
  choises = client.get_choises()

  # Get booking infromation from ELS
  bookings = client.get_bookings(1, format_date(start_date),
   format_date(end_date))

  # Filter out past and booked slots
  available = get_available_slots(bookings)
  return available

"""
Book selected slot 
"""
def do_booking(date, time):
  bookingtime_object = datetime.strptime(date+' '+time, '%Y-%m-%d %H:%M')
  return get_date_str(bookingtime_object)