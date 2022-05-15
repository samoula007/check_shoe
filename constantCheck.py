from scrapper import check_shoe_size
import time

# the email you want to send the results to and the sender
myEmail = 'YOUR_MAIL@gmail.com'
myPassword = 'YOUR_PASSWORD'
targetEmail = 'YOUR_TARGET_EMAIL'
# Input wanted size AND the shoe link
targetSize = '14'
url = "https://www.nike.com/ca/t/air-force-1-07-shoe-rWtqPn/CW2288-001"

# while True:
# check if size is available twice a day
#   time.sleep(30)
check_shoe_size(url, targetSize, myEmail, myPassword, targetEmail)
