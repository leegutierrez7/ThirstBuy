# ThirstBuy
Checks HTML class to see when status changes from out of stock -> in stock. Basic script to run on a Jenkins server and you can switch out the while true statement, or you can just keep it running in the background.

## Prerequisites:
- Twilio account & phone number ([see twilio instructions](#twilio-instructions)).  
- Have the following python3 modules installed: lxml, twilio, requests, beatifulsoup4  

## Twilio Instructions:  
1.) [Sign up](https://www.twilio.com/try-twilio) or [log in](https://www.twilio.com/login) to Twilio.   
2.) After account has been confirmed via email, visit your [console](https://www.twilio.com/console) to find your API crendentials (under `project info`).    
3.) Obtain a phone number via Twilio (2 methods):   
- Method 1: [Trial](https://www.twilio.com/console/phone-numbers/trial-number/modal?capability[]=sms)  
- Method 2: [Purchase](https://www.twilio.com/console/phone-numbers/search)  


## Instructions:
1.) Insert your Twilio crendentials within `Client("", "")`   
- It should look something like this: `client = Client("abc1234","abc1234");`

2.) Insert phone numbers near the bottom of script:   
- `to=""`    : Phone number you want the text messages to be sent to  
- `from_=""` : Twilio phone number sending the text messages ([see twilio instructions](#twilio-instructions))  

