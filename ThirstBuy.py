import sys
import time
import os.path
import subprocess

# Current working directory
cwd = os.path.dirname(os.path.realpath(__file__))

title = '''
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
'''

print(title + "\n")

# Twilio Credentials
account_sid = ""
auth_token = ""

# Phone Numbers
my_number = ""
twilio_number = ""

# Check to see if program has been ran before 
if os.path.isfile('secret.file'):
    os.system('cls' if os.name == 'nt' else 'clear')

    with open('secret.file') as file:
        account_sid = file.readline()
        auth_token = file.readline()
        my_number = file.readline()
        twilio_number = file.readline()
    file.close()

else:
    # Clear screen & sleep
    os.system('cls' if os.name == 'nt' else 'clear')
    time.sleep(1.5)

    # Print introduction message & create file named 'secret.file'
    print(title + "\n")
    print("First time setting up? I got you.\n")
    creds = open("secret.file", "w+")
    time.sleep(1.5)
    os.system('cls' if os.name == 'nt' else 'clear')


    print(title + "\n")
    print("Please wait while I check if you have all the necessary stuff :)\n")
    time.sleep(1.5)
    os.system('cls' if os.name == 'nt' else 'clear')

    # implement pip as a subprocess & install necessary packages:
    subprocess.check_call([sys.executable, '-m', 'pip', 'install','lxml'])
    subprocess.check_call([sys.executable, '-m', 'pip', 'install','emoji'])
    subprocess.check_call([sys.executable, '-m', 'pip', 'install','urllib3'])
    subprocess.check_call([sys.executable, '-m', 'pip', 'install','twilio'])
    subprocess.check_call([sys.executable, '-m', 'pip', 'install','beautifulsoup4'])
    os.system('cls' if os.name == 'nt' else 'clear')
    time.sleep(1)

    print(title + "\n")
    # Print examples of accepted formatting for requested user input
    print("Okay, the stuff is downloaded")
    os.system('cls' if os.name == 'nt' else 'clear')
    time.sleep(1.5)

    print(title + "\n")
    print("Let's get your credentials, here's some examples of the formatting ")
    print("     > [Account SID] : AB1234a12a12a1234567a9a94573a1234a")
    print("     > [Authentication Token] : AB1234a12a12a1234567a9a94573a1234a")
    print("     > [Personal Phone Number] : 9721231234")
    print("     > [TWILIO Phone Number] : 9721231234\n")
    print("** Need help? Check out the README (https://github.com/luisegarduno/ThirstBuy/blob/main/README.md)\n")

    print("Please enter the following information ")
    account_sid = str(input("     > [Account SID] : "))
    creds.write(account_sid + "\n")

    auth_token = str(input("     > [Authenticantion Token] : "))
    creds.write(auth_token + "\n")

    my_number = str(input("     > [Personal Phone Number] : "))
    creds.write(my_number + "\n")

    twilio_number = str(input("     > [TWILIO Phone Number] : "))
    creds.write(twilio_number)

    print("\n\nDone! Now if all the information is correct, program will start in a couple seconds :)")
    time.sleep(2)
    os.system('cls' if os.name == 'nt' else 'clear')
    creds.close()

# -------------- Launch actual script now --------------- #
import emoji
from bs4 import BeautifulSoup
from twilio.rest import Client
from urllib.request import urlopen

client = Client(account_sid, auth_token)                    # Twilio Client

print(title + "\n")
print("*Scanning every 2 minutes*\n")

item = 'RTX 3080: '
no  = emoji.emojize(':x:', use_aliases=True)                 # Emoji: Red "X"
yes = emoji.emojize(':white_check_mark: ', use_aliases=True) # Emoji: Green check

# Website URL : Microcenter
#url = 'https://www.microcenter.com/search/search_results.aspx?N=&cat=&Ntt=rtx+3080&searchButton=search'
url = 'https://www.microcenter.com/search/search_results.aspx?Ntt=rtx+3080&Ntk=all&sortby=match&N=44&myStore=true'

n = 1
while True:
    if n % 20 == 0:
        os.system('cls' if os.name == 'nt' else 'clear')
        print(title + "\n")
        print("*Scanning every 2 minutes*\n")

    response = urlopen(url).read()
    soup = BeautifulSoup(response, "lxml")                      # A parser tree (lxml format) helps search for a string.

    online = soup.findAll("div", {"class": "stock"})            # Depending on the website, find the field that is changes when the item is in stock.
    clearance = soup.findAll("div", {"class": "clearance"})     # Depending on the website, find the field that is changes when the item is in stock.

    if (str(online).find("in stock") == -1 and str(clearance).find("$") == -1):  # If .find() returns -1, item isn't in stock.
        e = emoji.emojize(time.strftime("%-I:%M%p") + ' :satellite: ', use_aliases=True)
        print(e + str(n) + '\t\t\t' + item + no)
        n += 1

    else:                                                                       # Else, item is in stock (send out text message)
        txt = item
        if str(online).find("in stock") != -1:
            txt = "Online "
            if str(clearance).find("$") != -1:
                txt = txt + "& Clearance "
        elif str(clearance).find("$") != -1:
            txt = txt + "Clearance "

        print(txt + yes + url)
        client.messages.create(to=my_number,            # YOUR phone number
                               from_=twilio_number,     # Twilio phone number
                               body=txt+yes+url)        # Text Message being delivered

    time.sleep(120)                                     # Scans website every 2 minutes
