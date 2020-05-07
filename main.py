# Check if a TOR site is up and running 
# Can be used to check status of both open web and dark web sites
# @author Dinson David Kurian <dinson@technisanct.com>
# May 6th, 2020

import requests
import sys

# get url from CLI parameter
url = sys.argv[1]

session = requests.session()
session.proxies = {}

session.proxies['http'] = 'socks5h://127.0.0.1:9050'
session.proxies['https'] = 'socks5h://127.0.0.1:9050'

print("\nConnecting to TOR...")

# they would know we are a Python script, what library we are using, and some version info. 
# We can change this.
# We will create some request headers and change the User-agent:
headers = {}
headers['User-agent'] = 'HotJava/1.1.2 FCS'
# Then we include the headers in the request:

try:
    
    r = session.get(url, headers=headers)
    print("\nConnection SUCCESS! : " + url)
    print("\nStatus Code: " + str(r.status_code))
    # uncomment following for loop to view all headers
    # for key in r.headers:
    #     print(key + ": " + r.headers[key])

except:
    
    print("\nConnection FAILED!")

print("\nDone!\n")