import re

with open('final_results_2023-07-04.csv', 'r') as file:
    # skip iter
    next(file)
    for index, row in enumerate(file):
        line = row.split(',')[:2]
        line[1] = ''.join(re.findall(r'\b(?:\d{1,3}\.){3}\d{1,3}\b', line[1]))
        #line.append(ip)
        #line = tuple(line)
        print(line)
