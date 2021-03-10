#Write script to check if the website is accessible

import urllib.request
url = input("enter the url")

status_code = urllib.request.urlopen(url).getcode()

b=status_code == 200

print(b)
    


