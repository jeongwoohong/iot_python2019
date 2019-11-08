import sys

input_file = sys.argv[1] # mysql_server_error_log.txt
output_file=sys.argv[2] #output_files/3output.csv

messages = {}

notes = []
with open(input_file, 'r', newline='') as text_file:
    for row in text_file:
        if '[Note]' in row:
            row_list = row.split(' ', 4) # 두번째 인자는 MAX split 수 5번째이후는 split 하지는 않는다:
            day = row_list[0].strip()
            note = row_list[4].strip('\n').strip()
            if note not in notes:
                notes.append(note)
            if day not in messages:
                messages[day] = {}
            if note not in messages[day]:
                messages[day][note] = 1
            else:
                messages[day][note] += 1

filewriter = open(output_file, 'w', newline='')
header = ['Date']
header.extend(notes)
header = ','.join(map(str,header)) + '\n'
print(header)
filewriter.write(header)
for day, day_value in messages.items():
    row_of_output = []
    row_of_output.append(day)
    for index in rage(len(notes)) :
        if notes[index] in day_value.keys():
            row_of_output.append(day[notes[index]])
        else:
            row_of_output.append(0)
    output = ','.join(map(str,row_of_output)) + '\n'
    print(output)
    filewriter.write(output)
filewriter.close()
