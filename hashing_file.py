import csv
import hashlib
import json

# This is creating a csv file and writing the header to it.
create_csv = 'filename_output.csv'
f = open(create_csv, 'w')
writer = csv.writer(f)

# Writing the header to the csv file.
writer.writerow(['S/N', 'Filename', 'UUID', 'Output File Name'])

# Reading the csv file and skipping the first row.
with open('name.csv', 'r') as csv_file:
    read_csv = csv.reader(csv_file, delimiter=',')
    next(read_csv)
    data = [a for a in read_csv] 

   # Creating a json file for each row in the csv file.
    for row in data:
        if row[1] and row[2]:
            sn, file_name, uuid = row[0], row[1], row[2]
            json_file = {
                'format' : 'CHIP-0007',
                'id' : uuid,
                'name' : file_name.replace('-', ' ').title(),
                'filename': file_name,
                'description' : '',
                'minting_tool' : '',
                'sensitive_content' : False,
                'series_number' : sn,
                'series_total' : data[-1][0],
                'collection' : {
                    'name' : 'viganem-the-drummer-girl',
                    'id' : '5a5a6f5c-39f3-4beb-ab74-60d3c7a90fd4'
                }
            }

            # Creating a json file for each row in the csv file.
            jsonObj = json.dumps(json_file, indent=4)
            with open(f'{file_name}.json', 'w') as output:
                output.write(jsonObj)
            output.close()

           # Creating a hash of the json file and appending it to the csv file.
            hashString = hashlib.sha256(jsonObj.encode()).hexdigest()
            row.append(f'{file_name}.csv')
            writer.writerow(row)

f.close()
        