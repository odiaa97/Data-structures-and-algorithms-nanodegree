"""
Read file into texts and calls.
It's ok if you don't understand how to read files
"""
import csv
with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)


def get_longest(csv_list):
    max_length = -1
    tel = ""
    for record in csv_list:
        if int(record[3]) >= max_length:
            max_length = int(record[3])
            tel = record[0]
    print(tel, "spent the longest time,", max_length, "seconds, on the phone during september 2016.")


get_longest(calls)

"""
TASK 2: Which telephone number spent the longest time on the phone
during the period? Don't forget that time spent answering a call is
also time spent on the phone.
Print a message:
"<telephone number> spent the longest time, <total time> seconds, on the phone during 
September 2016.".
"""

