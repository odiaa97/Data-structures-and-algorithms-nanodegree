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


def get_diff_nums(csv_list):
    diff_tel_nums = []
    for record in csv_list:
        if record[0] not in diff_tel_nums:
            diff_tel_nums.append(record[0])
        if record[1] not in diff_tel_nums:
            diff_tel_nums.append(record[1])
    return len(diff_tel_nums)


texts_diff_nums = get_diff_nums(texts)
calls_diff_nums = get_diff_nums(texts)

print(f"There are {texts_diff_nums + calls_diff_nums} different telephone numbers in the records.")

"""
TASK 1:
How many different telephone numbers are there in the records? 
Print a message:
"There are <count> different telephone numbers in the records."
"""
