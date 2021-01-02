# ThirstBuy
Checks HTML class to see when status changes from out of stock -> in stock. Basic script to run on a Jenkins server and you can switch out the while true statement, or you can just keep it running in the background.

## Prerequisites:
- Twilio account & phone number (see twilio instructions).
- Have the following python3 modules installed: lxml, twilio, requests, beatifulsoup4

## Twilio Instructions:
1.) Visit Twilio.com and sign up for a free account.
2.) After account has been confirmed via email, visit your console (twilio.com/console). Under `Project Info`, your Twilio API credentials will be shown, which you will need later.  
3.) Obtain a phone number via Twilio (2 methods): 
- Method 1: Obtain a trial phone number (https://www.twilio.com/console/phone-numbers/trial-number/modal?capability[]=sms)
- Method 2: Purchase a phone number via Twilio (https://www.twilio.com/console/phone-numbers/search)


## Instructions:
1.) Visit your Twilio console to obtain your credentials.
2.) Insert your crendentials within `Client("", "")`
- Should look something like this: `client = Client("abc1234","abc1234");` 
3.) Insert phone numbers near the bottom of script:
- "To"   : Phone number you want the text messages to be sent to
- "From" : Twilio phone number sending the text messages (see twilio instructions)

