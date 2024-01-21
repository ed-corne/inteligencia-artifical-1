# Import the pywhatkit library for sending WhatsApp messages
import pywhatkit

# Import the datetime and time libraries
from datetime import datetime
import time

# List of phone numbers to send messages to
phoneNumbers = ["+520000000000", "+52000000000", "+520000000000"]

# Iterate over each phone number in the list
for i in phoneNumbers:
    # Calculate the seconds for one minute from now
    seconds = time.time() + 60
    
    # Convert the seconds to a datetime object
    date = datetime.fromtimestamp(seconds)
    
    # Send a WhatsApp text message
    pywhatkit.sendwhatmsg(i,
                          "Hola soy el chatbot personal de Edwin",
                          date.hour,
                          date.minute)
    
    # Pause the program for 1 second
    time.sleep(1)
    
    # Send a WhatsApp image with a caption
    pywhatkit.sendwhats_image(i, "dias.jpg", "Que tengas un gran dia")
