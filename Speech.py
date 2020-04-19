# Python code to listen and send the mail to receiver

import speech_recognition as sr 
import pyttsx3
from pyttsx3 import voice
import time
import smtplib

# Initialize the recognizer  
r = sr.Recognizer()  
  
# Function to convert text to speech 
def SpeakText(command): 
      
    # Initialize the engine 
    engine = pyttsx3.init()
    engine.say(command) 
    engine.runAndWait()

# Taking information from the user about the mail
print("\n\nHello! Welcome to Voice Based Mailing Service")
SpeakText("Hello! Welcome to Voice Based Mailing Service")
time.sleep(0.5)

print("You need to login first, so we need your Email and Password...")
SpeakText("You need to login first, so we need your email and password")
time.sleep(1)

# Enter the credentials
SpeakText("\nPlease Enter your Email")
sender = input("\nEmail   : ")

SpeakText("\nAlright! Now enter your password")
password = input("\nPassword: ")
time.sleep(1)

# Get the message from the user
# Exception handling to handle 
# exceptions at the runtime 
try: 
          
    # use the microphone as source for input. 
    with sr.Microphone() as source2: 
          
        # wait for a second to let the recognizer 
        # adjust the energy threshold based on 
        # the surrounding noise level  
        r.adjust_for_ambient_noise(source2, duration=0.2) 
          
        #listens for the user's input 
        SpeakText("You are good to go.");
        time.sleep(1)
        SpeakText("Tell me the message.") 
        print("\nMessage :		Listening...")
        audio2 = r.listen(source2) 
           
        # Using ggogle to recognize audio 
        message = r.recognize_google(audio2) 
        message = message.lower()
        print("\n" + message)
              
except sr.RequestError as e: 
    print("Could not request results; {0}".format(e)) 
          
except sr.UnknownValueError: 
    print("unknown error occured") 

# Get the sender details
SpeakText("Well Done! Please enter receiver EMail Address.")
receiver = input("\nReceiver's Email: ")

# Function to display an error message when the mail is not sent
def ShowError():
	print("\nWe are having problem sending your mail.");
	SpeakText("We are having problem sending your mail.")
	time.sleep(1)

	print("\nPlease check your mail and authenticate the program and enable less secure apps for your account.")
	SpeakText("Please check your mail and authenticate the program and enable less secure apps for your account.")
	time.sleep(1)

	print("\nHope it helps, Thank You")
	SpeakText("Hope it helps, Thank You")

# Prompt the user for the service
SpeakText("Now Please choose your mailing service.")
choose = int(input("\n\n1. Gmail\n2. Yahoo\n3. Outlook\nChoose your server : "))

SpeakText("Ok, we are sending your mail.")
SpeakText("You will be informed once the mail is sent.")


# Try to send the EMail through different service
if choose == 1:
	
	# Try sending the mail through Gmail
	try:
		# Sending mail from your Gmail account  
	 
		# creates SMTP session 
		s = smtplib.SMTP('smtp.gmail.com', 587) 
		s.ehlo()
  
		# start TLS for security 
		s.starttls() 
  
		# Authentication 
		s.login(str(sender), str(password)) 
  
		# sending the mail 
		s.sendmail(str(sender), str(receiver), str(message)) 
  
		# terminating the session 
		s.quit() 

		# Prompt to the user
		print("\nThe mail was sent successfully...")
		SpeakText("Mail Sent successfully, Thank You for using this program")

	# If not sent inform the user
	except:
		ShowError()
	

elif choose == 2:
	# Try sending the mail through Yahoo
	try:
		# Sending mail from your Yahoo account  
	 
		# creates SMTP session 
		s = smtplib.SMTP('smtp.mail.yahoo.com', 587) 
		s.ehlo()
  
		# start TLS for security 
		s.starttls() 
  
		# Authentication 
		# Authentication 
		s.login(str(sender), str(password)) 
  
		# sending the mail 
		s.sendmail(str(sender), str(receiver), str(message)) 
  
		# terminating the session 
		s.quit() 
	# If not sent inform the user
	except:
		ShowError()
	
elif choose == 3:
	# Try sending the mail through Outlook
	try:
		# Sending mail from your Outlook account  
	 
		# creates SMTP session 
		s = smtplib.SMTP('smtp-mail.outlook.com', 587) 
		s.ehlo()
  
		# start TLS for security 
		s.starttls() 
  
		# Authentication 
		s.login(str(sender), str(password)) 
  
		# sending the mail 
		print(message)
		s.sendmail(str(sender), str(receiver), str(message)) 
  
		# terminating the session 
		s.quit() 
	# If not sent inform the user
	except:
		ShowError()

else:
	print("\nInavlid Option\nThank You...")
	SpeakText("We do not support any other services.")
	time.sleep(1)
	SpeakText("Thanks for using the Program.")
	