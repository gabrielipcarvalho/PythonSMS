from twilio.rest import Client
from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()

# Retrieve the credentials from the environment
account_sid = os.getenv('TWILIO_ACCOUNT_SID')
auth_token = os.getenv('TWILIO_AUTH_TOKEN')

client = Client(account_sid, auth_token)

message = client.messages.create(
            from_='+1234567890', #number generated at twilio
            body='Texting you, yet again!!', #message you want to send
            to='+1234567890' #number you want to send the message
)

print(message.sid)

