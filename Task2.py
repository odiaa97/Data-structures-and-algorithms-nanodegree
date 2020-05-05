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
    numbers_duration = dict()
    tel = ""
    for record in csv_list:
        # Adding durations of the calling numbers in the calls cumulatively
        if numbers_duration.get(record[0]) is not None:
            numbers_duration[record[0]] += int(record[3])
        else:
            numbers_duration[record[0]] = int(record[3])

        # Adding durations of the answering numbers cumulatively with the calling
        if numbers_duration.get(record[1]) is not None:
            numbers_duration[record[1]] += int(record[3])
        else:
            numbers_duration[record[1]] = int(record[3])

    # Finding the maximum length and the number that has the maximum duration
    max_number = max(numbers_duration, key=numbers_duration.get)
    max_length = max(numbers_duration.values())

    print(f"{max_number} spent the longest time {max_length} seconds, on the phone during september 2016.")


get_longest(calls)

"""
TASK 2: Which telephone number spent the longest time on the phone
during the period? Don't forget that time spent answering a call is
also time spent on the phone.
Print a message:
"<telephone number> spent the longest time, <total time> seconds, on the phone during 
September 2016.".
"""

