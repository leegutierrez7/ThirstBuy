import time
import emoji
from bs4 import BeautifulSoup
from twilio.rest import Client
from urllib.request import urlopen

# -------------- INSERT INFORMATION HERE --------------- #
# Twilio Credentials
account_sid = ""
auth_token  = ""

# Phone Numbers
my_number = ""
twilio_number = ""
# ------------------------------------------------------ #

client = Client(account_sid, auth_token)                                        # Twilio Client

no  = emoji.emojize('RTX 3080: Out of Stock :x:', use_aliases=True)             # Out of Stock + Red "X" emoji
yes = emoji.emojize('RTX 3080: In Stock :white_check_mark:', use_aliases=True)  # In Stock + Green check mark emoji

# Website URL : Microcenter // RTX 3080
url = 'https://www.microcenter.com/search/search_results.aspx?N=&cat=&Ntt=rtx+3080&searchButton=search'

while True:
    response = urlopen(url).read()
    soup = BeautifulSoup(response, "lxml")              # A parser tree (lxml format) helps search for a string.
    mydivs = soup.findAll("div", {"class": "stock"})    # Depending on the website, find the field that is changes when the item is in stock.

    if (str(mydivs).find("in stock") == -1):            # If .find() returns -1, item isn't in stock.
        print(no)

    else:                                               # Else, item is in stock (send out text message)
        client.messages.create(to=my_number,            # YOUR phone number
                               from_=twilio_number,     # Twilio phone number
                               body=yes)                # Text Message being delivered

    time.sleep(120)                                     # Scans website every 2 minutes
