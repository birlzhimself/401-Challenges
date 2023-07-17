#!/usr/bin/env python3

# Script : OpsChallenge37.py
# Purpose: Learn how to use requests library.
# Why    : Automate requests and saving responses.

# The below Python script shows one possible method to return the cookie from a site that supports cookies.

import requests
import webbrowser    

# targetsite = input("Enter target site:") # Uncomment this to accept user input target site
targetsite = "http://www.whatarecookies.com/cookietest.asp" # Comment this out if you're using the line above
response = requests.get(targetsite)
cookie = response.cookies

def bringforthcookiemonster(): # Because why not!
    print('''

              .---. .---.
             :     : o   :    me want cookie!
         _..-:   o :     :-.._    /
     .-''  '  `---' `---' "   ``-.
   .'   "   '  "  .    "  . '  "  `.
  :   '.---.,,.,...,.,.,.,..---.  ' ;
  `. " `.                     .' " .'
   `.  '`.                   .' ' .'
    `.    `-._           _.-' "  .'  .----.
      `. "    '"--...--"'  . ' .'  .'  o   `.

        ''')

bringforthcookiemonster()
print("Target site is " + targetsite)
print(cookie)

response = requests.get(targetsite, cookies=cookie)

with open('response.html', 'w', encoding='utf-8') as f:
    f.write(response.text)

webbrowser.open('response.html', new=2)
