# Project:  		SendTempWarn
# Description:  	Send an email if the temperature exceeds a certain limit
# Name:  			Andy Davies
# Version:   		1.0
# Release Date:   13-Mar-2013
# Email:   		andy@hymaswood.co.uk
# Credits:   		http://learn.adafruit.com/adafruits-raspberry-pi-lesson-11-ds18b20-temperature-sensing
#  				http://code.activestate.com/recipes/473810/


import os
import time
import glob
import datetime

os.system('modprobe w1-gpio')
os.system('modprobe w1-therm')

base_dir = '/sys/bus/w1/devices/'
device_folder = glob.glob(base_dir + '28*')[0]
device_file = device_folder + '/w1_slave'

while True:

  def read_temp_raw():
  	f = open(device_file, 'r')
  	lines = f.readlines()
  	f.close()
  	return lines

  def read_temp():
  	lines = read_temp_raw()
  	while lines[0].strip()[-3:] != 'YES':
  		time.sleep(0.2)
  		lines = read_temp_raw()
  	equals_pos = lines[1].find('t=')
  	if equals_pos != -1:
  		temp_string = lines[1][equals_pos+2:]
  		temp_c = float(temp_string) / 1000.0
  		return temp_c

  if read_temp() > 23:

  	print "High Temperature noted - sending warning email"

  	

  	## {{{ http://code.activestate.com/recipes/473810/ (r1)
  	# Send an HTML email with an embedded image and a plain text message for
  	# email clients that don't want to display the HTML.

  	from email.MIMEMultipart import MIMEMultipart
  	from email.MIMEText import MIMEText
  	from email.MIMEImage import MIMEImage

  	# Define these once; use them twice!
  	strFrom = 'user@googlemail.com'
  	strTo = 'anotheruser@domain.com'

  	# Create the root message and fill in the from, to, and subject headers
  	msgRoot = MIMEMultipart('related')
  	msgRoot['Subject'] = '!Temperature Warning!'
  	msgRoot['From'] = strFrom
  	msgRoot['To'] = strTo
  	msgRoot.preamble = 'This is a multi-part message in MIME format.'

  	# Encapsulate the plain and HTML versions of the message body in an
  	# 'alternative' part, so message agents can decide which they want to display.
  	msgAlternative = MIMEMultipart('alternative')
  	msgRoot.attach(msgAlternative)

  	msgText = MIMEText('A high temperature has been recorded on the Raspberry Pi')
  	msgAlternative.attach(msgText)

  	# We reference the image in the IMG SRC attribute by the ID we give it below
  	msgText = MIMEText('Here is the latest Temp Reading: %s' % read_temp(),'html')
  	msgAlternative.attach(msgText)

  	# Send the email (this example assumes SMTP authentication is required)
  	import smtplib
  	smtp = smtplib.SMTP()
  	smtp.connect('smtp.gmail.com')
  	smtp.starttls()
  	smtp.login('username', 'password')
  	smtp.sendmail(strFrom, strTo, msgRoot.as_string())
  	smtp.quit()
  	## end of http://code.activestate.com/recipes/473810/ }}}
  	
  	#wait and do it again

  	time.sleep(60)
