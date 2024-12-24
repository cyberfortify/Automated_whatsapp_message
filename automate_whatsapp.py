from twilio.rest import Client
from datetime import datetime, timedelta
import time

account_sid = os.getenv('TWILIO_ACCOUNT_SID')
auth_token = os.getenv('TWILIO_AUTH_TOKEN')
client = Client(account_sid, auth_token)

def sendWhatsappMessage(recipient_number, message_body):
    try:
        message = client.messages.create(
            from_='whatsapp:+14155238886',
            body = message_body,
            to = f'whatsapp:{recipient_number}'
        )
        print(f'Message sent successfully! Message SID: {message.sid}')
    except Exception:
        print('An error occurred')
        
name = input('Enter the recipient name: ')
recipient_number = input('Enter the recipient whatsapp number with country code(+91): ')
message_body = input(f'Enter the message you want to send to {name}: ')

date_str = input('Enter the date to send the message(yyyt-mm-dd): ')
time_str = input('Enter the time to send the message(24 hour format HH:MM): ')

schedule_datetime = datetime.strptime(f'{date_str} {time_str}',"%Y-%m-%d %H:%M")
current_datetime = datetime.now()

time_difference = schedule_datetime - current_datetime
delay_seconds = time_difference.total_seconds()

if delay_seconds <= 0:
    print("The time is in past. please enter a future date and time: ")
else:
    print(f'Message scheduled to be sent to {name} at {schedule_datetime}.')
    time.sleep(delay_seconds)    
    sendWhatsappMessage(recipient_number, message_body)
