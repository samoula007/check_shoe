from keep_alive import keep_alive
from scrapper import check_shoe_size
import time

# the email you want to send the results to and the sender, please use your own sender email
myEmail = 'postmaster@sandbox5397432e98084f0aa685b1e225a37ae8.mailgun.org'
myPassword = 'c7438b0b847aaff7ac4e1ba16ca382c7-5e7fba0f-0b871cfb'
targetEmail = 'YOUR_EMAIL'
# Input wanted size AND the shoe link
targetSize = '14'
url = "https://www.nike.com/ca/t/air-force-1-07-shoe-rWtqPn/CW2288-001"

# switch to kill the program once an email is sent
available = 0

if (available == 0):
    keep_alive()


while True:
    # once shoe is available, discontinue the script
    if check_shoe_size(url, targetSize, myEmail, myPassword, targetEmail) == True:
        available = 1
        break
    # check if size is available once an hour
    time.sleep(3600)
