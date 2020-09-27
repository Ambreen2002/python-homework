# -*- coding: utf-8 -*-
"""Instructor Demo: CSV Reader.

This script will use the Pathlib library to set the file path,
use the csv library to read in the file, iterate over each
row of the file to capture employee salaries, calculate min,
max, avg metrics of employee salaries, and write the metrics
to a csv file.
"""

# Import the pathlib and csv library
from pathlib import Path
import csv

# Set the file path
csvpath = Path('./Resources/budget_data.csv')

# Initialize variable to hold salaries
greatest_increase = 0
greatest_decrease = 10000000000

# Initialize line_num variable
total_profit = 0
total_months = 0

# Open the input path as a file object
with open(csvpath, 'r') as csvfile:

    # Print the datatype of the file object
    print(type(csvfile))

    # Pass in the csv file to the csv.reader() function
    # (with ',' as the delmiter/separator) and return the csvreader object
    csvreader = csv.reader(csvfile, delimiter=',')
    # Print the datatype of the csvreader
    print(type(csvreader))

    # Go to the next row from the start of the file
    # (which is often the first row/header) and iterate line_num by 1
    header = next(csvreader)
    # Print the header
    print(f"{header} <---- HEADER")

    # Read each row of data after the header
    for row in csvreader:
        # Print the row
        total_months += 1
        row[1] = int(row[1])
        total_profit += row[1]
        if row[1]>greatest_increase:
            greatest_increase = row[1]
            greatest_increase_month = row[0]
        print(row)


print (f"Total Months: {total_months}")
print (f"Total Profit: {total_profit}")
print (f"greatest_increase: {greatest_increase} was on {greatest_increase_month}")
