# Python code to listen and send the mail to receiver

import speech_recognition as sr
import pyttsx3
from pyttsx3 import voice
import time
import smtplib
import getpass as gp

# Initialize the recognizer
r = sr.Recognizer()
  
# Function to convert text to speech
def SpeakText(command):
    # Initialize the engine
    engine = pyttsx3.init()
    engine.say(command)
    engine.runAndWait()

# Function to send the mail
def Sendmail(server, port, xsender, xpassword, xreceiver, xmessage):
	# Sending mail

	# Creates SMTP session
	s = smtplib.SMTP(server, port)
	s.ehlo()

	# start TLS for security
	s.starttls()

	# Authentication
	s.login(str(xsender), str(xpassword))
  
	# sending the mail 
	s.sendmail(str(xsender), str(xreceiver), str(xmessage))
  
	# terminating the session 
	s.quit()

	# Prompt to the user
	print("\nThe mail was sent successfully...")
	SpeakText("Mail Sent successfully, Thank You for using this program")

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
password = gp.getpass()
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
        SpeakText("Tell me the subject.") 
        print("\nSubject :		Listening...")
        audio2 = r.listen(source2) 
           
        # Using ggogle to recognize audio 
        subject = r.recognize_google(audio2) 
        subject = subject.lower()
        print("\nYour Subject: " + subject)

        SpeakText("Tell me the message body.") 
        print("\nBody :		Listening...")
        audio2 = r.listen(source2) 
           
        # Using ggogle to recognize audio 
        body = r.recognize_google(audio2) 
        body = body.lower()
        print("Your Body: \n" + body)
              
except sr.RequestError as e: 
    print("Could not request results; {0}".format(e)) 
    subject = "Ignore this mail..."
    body = "Sorry :( Sent by-mistake..."
          
except sr.UnknownValueError: 
    print("unknown error occured") 
    subject = "Ignore this mail..."
    body = "Sorry :( Sent by-mistake..."

# Get the sender details
SpeakText("Well Done! Please enter receiver EMail Address.")
receiver = input("\nReceiver's Email: ")

# Add the subject and body to complete the message
message = 'Subject: ' + subject + "\nDear " + receiver + ', \n\n' + body + '\nSent from: https://github.com/subhamsagar524/Voice-Based-Mailing-from-Terminal'

# Prompt the user to choose the service
SpeakText("Now Please choose your mailing service.")
choose = int(input("\n\n1. Gmail\n2. Yahoo\n3. Outlook\nChoose your server : "))

SpeakText("Ok, we are sending your mail.")
SpeakText("You will be informed once the mail is sent.")

# Try to send the EMail through different service
if choose == 1:
	
	# Try sending the mail through Gmail
	try:
		Sendmail('smtp.gmail.com', 587, sender, password, receiver, message)

	# If not sent inform the user
	except:
		ShowError()
	

elif choose == 2:
	# Try sending the mail through Yahoo
	try:
		Sendmail('smtp.mail.yahoo.com', 587, sender, password, receiver, message)

	# If not sent inform the user
	except:
		ShowError()
	
elif choose == 3:
	# Try sending the mail through Outlook
	try:
		Sendmail('smtp-mail.outlook.com', 587, sender, password, receiver, message)
		
	# If not sent inform the user
	except:
		ShowError()

else:
	print("\nInavlid Option\nThank You...")
	SpeakText("We do not support any other services.")
	time.sleep(1)
	SpeakText("Thanks for using the Program.")
	