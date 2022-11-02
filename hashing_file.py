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
with open('path/You csv file', 'r') as csv_file:
    read_csv = csv.reader(csv_file, delimiter=',')
    next(read_csv)
    data = [a for a in read_csv] 

   # Creating a json file for each row in the csv file.
    for row in data:
        if row[1] and row[2]:
            sn, file_name, uuid = row[0], row[1], row[2]
           # This is creating a dictionary with the keys and values as directed by the given json schema
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
                    'name' : '',
                    'id' : ''
                }
            }

            # Creating a json file for each row in the csv file.
            jsonObject = json.dumps(json_file, indent=4) # Converting the json file to a string.
            with open(f'{file_name}.json', 'w', encoding='utf-8') as output:
                output.write(jsonObject)
            output.close()

           # Creating a hash of the json file and appending it to the csv file.
            hashString = hashlib.sha256(jsonObject.encode()).hexdigest()
           # Appending the file name to the csv file.
            row.append(f'{file_name}.csv')
            writer.writerow(row)

# Closing the file.
f.close()
        