from flask import Flask, render_template
from flask_ask import Ask, statement, question

from els_helper import get_next_available_time, do_booking

app = Flask(__name__)
ask = Ask(app, '/')

"""
NextAvailable intent
"""
@ask.intent('NextAvailable')
def next_available():
  
  # Get available times to book
  available_slots = get_next_available_time()
  
  # If there're available times, select the first one and 
  # return it to Alexa
  if len(available_slots) > 0:
    slot      = available_slots[0]
    time      = slot['date_str']
    response  = render_template('next_available', time=time)
  else:
    # No available times, return error to Alexa 
    response  = render_template('not_found')
  
  # Return response
  return statement(response)

"""
BookTime intent.
User says: "Alexa ask booking service to book me time today 
at half past one"
"""
@ask.intent('BookTime')
def book_time(date, time):

  # Do booking on date and time specified
  booking = do_booking(date, time)

  # Return response
  response = render_template('booked', date=date, time=time)
  return statement(response)

if __name__ == '__main__':
  app.run(host='127.0.0.1', port=8080, debug=True)