# MicroCenter : RTX 3080
Checks HTML class to see when status changes from out of stock -> in stock. Basic script to run on a Jenkins server and you can switch out the while true statement, or you can just keep it running in the background.

## Prerequisites:
- Have the following python3 modules installed: lxml, emoji, twilio, beautifulsoup4   
  - `$ pip install lxml emoji twilio beautifulsoup4`
- Valid (personal/work) phone number
- Twilio account + Twilio phone number ([see instructions](#instructions)).  
  - Skip to step #4 of instructions if you already have both of these.

## Instructions:
1.) [Sign up](https://www.twilio.com/try-twilio) or [log in](https://www.twilio.com/login) to Twilio.   
2.) After account has been confirmed via email, visit your [console](https://www.twilio.com/console) to find your API crendentials (under `project info`).    
3.) Obtain a phone number via Twilio (2 methods):   
- Method 1: [Trial](https://www.twilio.com/console/phone-numbers/trial-number/modal?capability[]=sms)  
- Method 2: [Purchase](https://www.twilio.com/console/phone-numbers/search)  
4.) Insert your Twilio crendentials + Phone Numbers within labeled area   
5.) Deploy! (`$ python3 RTX_3080.py`)
