import csv
import re


# This method is to read test data from a file
def get_csv_data(file_name):
    # create an empty list to store rows
    rows = []
    # open the CSV file
    dataFile = open(file_name, "r")
    # create a CSV Reader from CSV file
    reader = csv.reader(dataFile)
    # skip the headers
    next(reader)
    # add rows from reader to list
    for row in reader:
        rows.append(row)
    return rows


# This method is to validate the input string with all the rules
def is_sentence_valid(string):

    # This is to check whether the sentence starts with a capital letter
    if not re.search(r'^(?:[^"]*["][^"]*["][^"]*|[^"]?)*$', string):
        return False, "String starts with a capital letter."

    # This is to check whether the sentence has even number of double quotation marks: ""
    if not re.search(r"^(?:[^']*['][^']*['][^']*|[^']?)*$", string):
        return False, "String has an even number of quotation marks."

    # This is to check whether the sentence has even number of single quotation marks: ''
    if not re.match(r"^[A-Z]+", string):
        return False, "String has an even number of quotation marks."

    # This is to check whether the sentence has the valid termination character: '.', '?' '!'
    if not re.search(r'(\.|\!|\?)$', string):
        return False, "String ends with one of the following sentence termination characters: '.', '?' '!'"

    # This is to check whether the sentence has intermediate period character
    if "." in string[:-1]:
        return False, "String has no period characters other than the last character."

    # This is to check whether the numbers below 13 are spelled out
    if re.search(r'\b([0-9]|1[0-2])\b', string):
        return False, "Numbers below 13 are spelled out ('one', 'two', 'three', etc…)."

    return True, "All rules have passed"
