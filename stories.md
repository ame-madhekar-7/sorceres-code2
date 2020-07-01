## greet path
* greet
  - utter_greet
* goodbye
  - utter_goodbye

## book
* booking
  - utter_ask_name
* enter_name
  - action_store_name
  - slot{"name": "Max Meier"}
  - utter_ask_date
* enter_date
  - action_store_date
  - utter_ask_time
* enter_time
  - action_store_time
  - utter_ask_email
* enter_email
  - action_store_email
  - action_book_appointment
  - utter_book_appt
* thanks
  - utter_thanks
* goodbye
  - utter_goodbye

## book appointment
* greet
  - utter_greet
* booking
  - utter_ask_name
* enter_name
  - action_store_name
  - slot{"name": "Max Meier"}
  - utter_ask_date
* enter_date
  - action_store_date
  - utter_ask_time
* enter_time
  - action_store_time
  - utter_ask_email
* enter_email
  - action_store_email
  - action_book_appointment
  - utter_book_appt
* thanks
  - utter_thanks
* goodbye
  - utter_goodbye

## book appointment 2
* greet
  - utter_greet
* booking
  - utter_ask_name
* enter_name
  - action_store_name
  - slot{"name": "Max Meier"}
  - utter_ask_date
* enter_date
  - action_store_date
  - utter_ask_time
* enter_time
  - action_store_time
  - utter_ask_email
* enter_email
  - action_store_email
  - action_book_appointment
  - utter_book_appt
* goodbye
  - utter_goodbye

## book appointment 3
* booking
  - utter_ask_name
* enter_name
  - action_store_name
  - slot{"name": "Max Meier"}
  - utter_ask_date
* enter_date
  - action_store_date
  - utter_ask_time
* enter_time
  - action_store_time
  - utter_ask_email
* enter_email
  - action_store_email
  - action_book_appointment
  - utter_book_appt
* goodbye
  - utter_goodbye

## say goodbye
* goodbye
  - utter_goodbye

## bot challenge
* bot_challenge
  - utter_bot_challenge
* greet
  - utter_greet
* goodbye
  - utter_goodbye

## fallback
  - utter_default