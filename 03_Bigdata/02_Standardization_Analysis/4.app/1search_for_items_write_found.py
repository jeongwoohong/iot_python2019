import csv
import glob
import os
import sys
from datetime import date
from clrd import open_workbook, xldate_as_tuple

item_numbers_file = sys.argv[1] #item_numbers_to_find.csv
path_to_folder = sys.argv[2]
output_file = sys.argv[3]

item_numbers_to_find = []
with open(item_numbers_file, 'r', newline='') as item_numbers_csv_file:
    filereader = csv.reaer(item_numbers_csv_file)
    for row in filereader:
        item_numbers_to_find.append(row[0])
        I
    
    print(item_numbers_to_find)
