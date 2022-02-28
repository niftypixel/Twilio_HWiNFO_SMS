#Imports we need to proceed
import sys
from configparser import ConfigParser
from twilio.rest import Client

# Assign variables from configuration file
config = ConfigParser()
config.read("config.txt")
twilio_number = config.get('Config', 'twilio_number')
twilio_sid = config.get('Config', 'twilio_sid')
twilio_token = config.get('Config', 'twilio_token')
your_number = config.get('Config', 'your_number')
your_message = config.get('Config', 'your_message')

#Check if argument passed and generate different message
if len(sys.argv) > 1:
    your_message = sys.argv[1]

#Send the SMS
client = Client(twilio_sid, twilio_token) 
message = client.messages.create( 
 from_= twilio_number, 
 body= your_message,      
 to= your_number 
)