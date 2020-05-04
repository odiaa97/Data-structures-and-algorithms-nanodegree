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


def get_area_codes(csv_list):
    all_codes = set()
    calls_from_bangalore = 0
    calls_to_bangalore = 0
    for record in csv_list:
        if record[0].startswith("(080"):
            calls_from_bangalore += 1
            if record[1].startswith("(080)"):
                calls_to_bangalore += 1
            if record[1].startswith("(0"):
                tel_code = record[1].split(")")
                tel_code[0] += ")"
                all_codes.add(tel_code[0])
            elif record[1].startswith("6") or record[1].startswith("7") or record[1].startswith("8"):
                all_codes.add(record[1][0:4])
            elif record[1].startswith("140"):
                all_codes.add(record[1][0:3])
    codes_list = list(all_codes)
    codes_list.sort(key=len)
    print("The numbers called by people in Bangalore have codes:\n" + "\n".join(codes_list))
    percentage = calls_from_bangalore / calls_to_bangalore
    print(f"{percentage:.2f} percent of calls from fixed lines in Bangalore are calls to other fixed lines in Bangalore.")


get_area_codes(calls)

"""
TASK 3:
(080) is the area code for fixed line telephones in Bangalore.
Fixed line numbers include parentheses, so Bangalore numbers
have the form (080)xxxxxxx.)

Part A: Find all of the area codes and mobile prefixes called by people
in Bangalore.
 - Fixed lines start with an area code enclosed in brackets. The area
   codes vary in length but always begin with 0.
 - Mobile numbers have no parentheses, but have a space in the middle
   of the number to help readability. The prefix of a mobile number
   is its first four digits, and they always start with 7, 8 or 9.
 - Telemarketers' numbers have no parentheses or space, but they start
   with the area code 140.

Print the answer as part of a message:
"The numbers called by people in Bangalore have codes:"
 <list of codes>
The list of codes should be print out one per line in lexicographic order with no duplicates.

Part B: What percentage of calls from fixed lines in Bangalore are made
to fixed lines also in Bangalore? In other words, of all the calls made
from a number starting with "(080)", what percentage of these calls
were made to a number also starting with "(080)"?

Print the answer as a part of a message:
"<percentage> percent of calls from fixed lines in Bangalore are calls
to other fixed lines in Bangalore."
The percentage should have 2 decimal digits
"""
