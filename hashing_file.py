import csv
import hashlib
import json

# This is creating a csv file and writing the header to it.
create_csv = 'files/filename_output.csv'
f = open(create_csv, 'w')
writer = csv.writer(f)
# Reading the csv file and skipping the first row.
with open('hng1.csv', 'r') as csv_file:
    read_csv = csv.reader(csv_file, delimiter=',')
    next(read_csv)
    data = [a for a in read_csv] 

   # Creating a json file for each row in the csv file.
    for row in data:
        if row[1] and row[2]:
            
            series_number = row[0]
            file_name = row[1]
            name= row[2]
            description= row[3]
            gender = row[4]
            attributes = row[5]
            uuid = row[6]
           # This is creating a dictionary with the keys and values as directed by the given json schema
            json_file = {
                'format' : 'CHIP-0007',
                'name' : file_name.replace('-', ' ').title(),
                'description' : '',
                'minting_tool' : '',
                'series_number' : series_number,
                'sensitive_content' : False,
                'series_total' : data[-1][0],
                 "attributes": [
                    {
                        "trait_type": "gender",
                        "value": gender
                    }
                ],
                "collection": {
                    "name": "Zuri NFT tickets for free lunch",
                    "id": uuid,
                    "attributes": [
                        {
                            "type": "description",
                            "value": "Rewards for accomplishments during HNGi9"
                        }
                    ]
                },
            }

            # Creating a json file for each row in the csv file.
            jsonObject = json.dumps(json_file, indent=4) # Converting the json file to a string.
            with open(f'json/{file_name}.json', 'w') as output:
                output.write(jsonObject)
            output.close()

           # Creating a hash of the json file and appending it to the csv file.
            hashString = hashlib.sha256(jsonObject.encode()).hexdigest()
           # Appending the file name to the csv file.
            row.append(hashString)
            writer.writerow(row)

# Closing the file.
f.close()
        