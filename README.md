
     ________  __        __                        __      _______
    /        |/  |      /  |                      /  |    /       \\
    $$$$$$$$/ $$ |____  $$/   ______    _______  _$$ |_   $$$$$$$  | __    __  __    __
       $$ |   $$      \ /  | /      \  /       |/ $$   |  $$ |__$$ |/  |  /  |/  |  /  |
       $$ |   $$$$$$$  |$$ |/$$$$$$  |/$$$$$$$/ $$$$$$/   $$    $$< $$ |  $$ |$$ |  $$ |
       $$ |   $$ |  $$ |$$ |$$ |  $$/ $$      \   $$ | __ $$$$$$$  |$$ |  $$ |$$ |  $$ |
       $$ |   $$ |  $$ |$$ |$$ |       $$$$$$  |  $$ |/  |$$ |__$$ |$$ \__$$ |$$ \__$$ |
       $$ |   $$ |  $$ |$$ |$$ |      /     $$/   $$  $$/ $$    $$/ $$    $$/ $$    $$ |
       $$/    $$/   $$/ $$/ $$/       $$$$$$$/     $$$$/  $$$$$$$/   $$$$$$/   $$$$$$$ |
                                                                              /  \__$$ |
                ~ Website : https://garduno.me                                $$    $$/
                                                                               $$$$$$/


# ThirstBuy : RTX 3080

ThirstBuy is a python script that will go onto MicroCenter's website & checks an HTML class to see when status changes from out of stock -> in stock. Script can be ran on a Jenkins server and you can switch out the while true statement, or you can just keep it running in the background.

## Prerequisites:
- Have the following python3 modules installed: lxml, emoji, twilio, beautifulsoup4   
  - `$ pip install lxml emoji twilio beautifulsoup4` (if you don't have them python will install them for you)
- Valid (personal/work) phone number
- Twilio account + Twilio phone number (see instructions below).  
  - Skip to step #4 of instructions if you already have both of these.

## Instructions:
1.) [Sign up](https://www.twilio.com/try-twilio) or [log in](https://www.twilio.com/login) to Twilio.   
2.) After account has been confirmed via email, visit your [console](https://www.twilio.com/console) to find your API crendentials (under `project info`).    
3.) Obtain a phone number via Twilio (2 methods):   
- Method 1: [Trial](https://www.twilio.com/console/phone-numbers/trial-number/modal?capability[]=sms)  
- Method 2: [Purchase](https://www.twilio.com/console/phone-numbers/search)  
4.) Deploy! (`$ python3 `<a href="https://github.com/luisegarduno/ThirstBuy/releases/download/1.0/ThirstBuy.py" target="_top"><b>`ThirstBuy.py`</b></a>)   
5.) Insert your Twilio crendentials + Phone Numbers when prompted to
