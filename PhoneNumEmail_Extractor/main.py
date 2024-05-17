# extracting the text from url
import pyperclip, re
import requests
from bs4 import BeautifulSoup

url =input("Enter url: ")
headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36"}
response = requests.get(url, headers=headers)
soup = BeautifulSoup(response.content, "html.parser")


# Get all text
all_text = soup.get_text()
#print(all_text)

# Finds phone numbers and email addresses from the url.

phoneRegex = re.compile(r'''(
    (\d{2}|\+\d{2})?                  # country code
    (\s|-|\.)?                        # separator
    (\d{5}\s\d{5}|\d{10})             # phone number 
    )''', re.VERBOSE)


# Create email regex.
emailRegex = re.compile(r'''(
   [a-zA-Z0-9._%+-]+      # username
   @                      # @ symbol
   [a-zA-Z0-9.-]+         # domain name
   (\.[a-zA-Z]{2,4})       # dot-something
)''', re.VERBOSE)

# Find matches in clipboard text.
#text = str(pyperclip.paste())

matches = {"phoneNumbers":[],
           "mails":[]}
for groups in phoneRegex.findall(all_text):
    phoneNum = groups[0]
    if phoneNum not in matches["phoneNumbers"]:
        matches["phoneNumbers"].append(phoneNum)
for groups in emailRegex.findall(all_text):
    email = groups[0]
    if email not in matches["mails"]: 
        matches["mails"].append(email)

def print_list(li):
    for item in li:
        print(item)

if len(matches["phoneNumbers"]) > 0:
    print("Phone Numbers: ")
    print_list(matches["phoneNumbers"])
else:
    print("Phone Numbers do not exist")

if len(matches["mails"]) > 0:
    print()
    print("Mails: ")
    print_list(matches["mails"])
else:
    print("Mails do not exist")