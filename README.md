Fork of anddav87/SendTempWarn for personal use.
============

TODO:
============
1. Add automatic data upload to google sheets with formulas already calculated from
2. Externalize the static variables that are in the script in a external configuration file. I have not decided yet what format. 
3. upload a systemd service to automate the execution of this script upon startup with a raspberry pi zero w.


Original README.md below
============
I have uploaded the original post here as original_posting.pdf as notes for later to complete this task, and to also provide source credit to bembel@homebrewtalk. Thank you.
  https://www.homebrewtalk.com/forum/threads/pasteurization-time-and-temperature-for-cider.581913/


SendTempWarn
============

Send a Warning Email from the Raspberry Pi if the Temperature exceeds a limit

Using a DS18B20 sensor I got from eBay, and the code gleaned from an Adafruit Tutorial I could successfully read the temperature on my Pi.  Not satisfied with leaving it there, I incorporated some code that I had adapted to use to send me regular pics from my Webcam so that I get an email alert if the temperature gets above or below a limit that I have set.

This is my first proper go at Python so use it with care and any comments welcome.

I hope I have credited people where appropriate, if I haven't please get in touch.

Thanks!

Andy

andy@hymaswood.co.uk

