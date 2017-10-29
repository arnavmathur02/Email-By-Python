import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
		
user_email = input("Enter your email address: ")
receiver_email = []

# make a variable for the server to connect to using (in this case ) Gmail server
# And then providing the port number to connect to 
# server = smtplib.SMTP(mailserver, port_number)
# There are certain ports like (80, 25, 587, 465)
# 587 is new and provides better security requirements
server = smtplib.SMTP('smtp.gmail.com', 587)

# to make your connection secure 
# Using the "starttls()" function that provides a secure connection and avoids data loss
# "tls" stands for Transport Security Layer
server.starttls()

# Then login to your account
password = input("Enter your password: ")
try:
	server.login(user_email, password)
	print ("\nConnected, Login Successful.")
	number = int(input("\n\nEnter the number of people to send email"))
	for num in range(number):
		# Enter the receiver's mail address
		receiver_email = input("\n\nEnter the receiver's email address: ")

	# Enter the subject
	subject = input("\n\nEnter the subject here: ")

	# ENter the message to send to the receiver
	message = input("\nEnter your message: ")

	# Msg variable is used to divide the message into subjct+ message
	msg = MIMEMultipart()
	msg['From'] = user_email
	msg['To'] = receiver_email
	msg['Subject'] = subject

	# text vriable is used here as to convert everything to string
	msg.attach(MIMEText(message,'plain'))
	text = msg.as_string()
	#######message = subject + " \n\n" + message
	try:
		# Send the mail using the "sendmail()" function
		server.sendmail(user_email, receiver_email, text)
		print("\n\nMail sent Successfully.")
	except:
		print("\n\nMail Unsuccesful!!")

except:
	print("\nInvalid Password, Not Connected.")

# Close the connection
server.close()
