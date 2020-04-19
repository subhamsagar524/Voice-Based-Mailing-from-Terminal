# Python code to listen and send the mail to receiver

import speech_recognition as sr 
import pyttsx3
from pyttsx3 import voice
import time

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

print("You need to login first, so we need your username and password...")
SpeakText("You need to login first, so we need your username and password")
time.sleep(1)

# Enter the credentials
SpeakText("\nPlease Enter your Username")
sender = input("\nUsername  : ")

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
        print("\nMessage :  ...Speak Now...")
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

SpeakText("Ok, we are sending your mail.")
time.sleep(1)
SpeakText("You will be informed once the mail is sent.")



# Function to send a mail using smtp
def Send(xsender, xpassword, xreceiver, xmessage, smtp_server, smtp_port): 
    
    try:
    	# Try to send the mail  
    	# Creates SMTP session 
    	s = smtplib.SMTP(smtp_server, smtp_port) 
    	s.ehlo()
  
    	# Start TLS for security 
    	s.starttls() 
  
    	# Authentication 
    	s.login(xsender, xpassword) 
  
    	# Sending the mail 
    	s.sendmail(xreceiver, xsender, xmessage) 
  
    	# Terminating the session 
    	s.quit() 

    except smtplib.SMTPAuthenticationError as e:

    	# Prints the errors
    	print("SMTP error occured: " + str(e))

# Prompt the user for the service
choose = input("\nChoose your server : \n\t1. Gmail\n\t2. Yahoo\n\t3. Outlook")

# Try to send the EMail through different service
if choose == 1:
	
# Try sending the mail through Gmail
	try:
		Send(sender, password, receiver, message, "smtp.gmail.com", 587)
	# If not sent inform the user
	except:
		print("\nWe are having problem sending your mail.");
		SpeakText("We are having problem sending your mail.")
		time.sleep(1)

		print("\nPlease check your mail and authenticate the program and enable less secure apps for your account.")
		SpeakText("Please check your mail and authenticate the program and enable less secure apps for your account.")
		time.sleep(1)

		print("\nHope it helps, Thank You")
		SpeakText("Hope it helps, Thank You")

elif choose == 2:
	# Try sending the mail through Yahoo
	try:
		Send(sender, password, receiver, message, "smtp.mail.yahoo.com", 587)
	# If not sent inform the user
	except:
		print("\nWe are having problem sending your mail.");
		SpeakText("We are having problem sending your mail.")
		time.sleep(1)

		print("\nPlease check your mail and authenticate the program and enable less secure apps for your account.")
		SpeakText("Please check your mail and authenticate the program and enable less secure apps for your account.")
		time.sleep(1)

		print("\nHope it helps, Thank You")
		SpeakText("Hope it helps, Thank You")

elif choose == 3:
	# Try sending the mail through Yahoo
	try:
		Send(sender, password, receiver, message, "smtp-mail.outlook.com", 587)
	# If not sent inform the user
	except:
		print("\nWe are having problem sending your mail.");
		SpeakText("We are having problem sending your mail.")
		time.sleep(1)

		print("\nPlease check your mail and authenticate the program and enable less secure apps for your account.")
		SpeakText("Please check your mail and authenticate the program and enable less secure apps for your account.")
		time.sleep(1)

		print("\nHope it helps, Thank You")
		SpeakText("Hope it helps, Thank You")

else:
	print("\nInavlid Option\nThank You...");
	SpeakText("We do not support any other services.")
	time.sleep(1)
	SpeakText("Thanks for using the Program.")
	