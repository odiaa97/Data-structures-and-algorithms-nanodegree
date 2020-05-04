"""
Read file into texts and calls.
It's ok if you don't understand how to read files.
"""
import csv

with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)


def expect_telemarketers(texts_csv, calls_csv):
    all_numbers = set()
    possible_numbers = set()
    for record in calls_csv:
        all_numbers.add(record[1])

    for record in texts_csv:
        all_numbers.add(record[0])
        all_numbers.add(record[1])

    for record in calls_csv:
        if record[0] not in all_numbers:
            possible_numbers.add(record[0])

    print("These numbers could be telemarketers:", "\n".join(list(possible_numbers)), sep="\n")


expect_telemarketers(texts, calls)

"""
TASK 4:
The telephone company want to identify numbers that might be doing
telephone marketing. Create a set of possible telemarketers:
these are numbers that make outgoing calls but never send texts,
receive texts or receive incoming calls.

Print a message:
"These numbers could be telemarketers: "
<list of numbers>
The list of numbers should be print out one per line in lexicographic order with no duplicates.
"""

