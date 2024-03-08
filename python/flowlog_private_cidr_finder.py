# The following script runs with a single argument after the script name. For example: python3 flowlog_private_cidr_finder.py SRE-6957_vpc-7362a615/4c383926-f410-4a7b-aaf5-2e9da3242f5f.csv

# This argument (SRE-6957_vpc-7362a615/4c383926-f410-4a7b-aaf5-2e9da3242f5f.csv) is the full location of the file that has the results for the athena query we ran previuosly. The Athena query we ran previously was: 

"""
SELECT DISTINCT "sourceaddress" FROM <table name> WHERE NOT regexp_like(sourceaddres, '^10\.192.*' 
"""

import sys

filename = str(sys.argv[1])

file = open(filename, 'r')

for line in file:
    temp_line = line.replace('"', '')
    line = temp_line.strip()
    splitted_line = line.split('.')
    if splitted_line[0] == '10':
        print(line)
    elif splitted_line[0] == '172' and int(splitted_line[1]) > 16 and int(splitted_line[1]) <= 31:
        print(line)
    elif splitted_line[0] == '192' and int(splitted_line[1]) == '168':
        print(line)
