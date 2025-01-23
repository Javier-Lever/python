'''Write a Python program to display the current date and time.
Sample Output :
Current date and time :
2014-07-05 14:34:14'''

# from datetime import datetime

# date_string = "2025-01-23 17:35:00"
# parsed_date = datetime.strptime(date_string, "%Y-%m-%d %H:%M:%S")
# print("Parsed Date and Time:", parsed_date)

import datetime
now = datetime.datetime.now()

print("Current date and time : ")

print(now.strftime("%Y-%m-%d %H:%M:%S"))