import http.client
import os
import csv
import json
from pprint import pprint
tags = os.environ.get('DD_TAG')
conn = http.client.HTTPSConnection("api.datadoghq.com")
payload = ''
headers = {'Content-Type': 'application/json',"DD-API-KEY": os.environ.get('DD_API_KEY'),'DD-APPLICATION-KEY': os.environ.get('DD_APP_KEY')}
conn.request("GET", "/api/v1/monitor?group_states=all&name=&tags=&monitor_tags="+tags+"&with_downtimes=&id_offset=&page=&page_size=", body=payload,headers=headers)
res = conn.getresponse()
data = res.read()

json_to_dict = json.loads(data.decode("UTF-8"))

pprint(json_to_dict)
print("There are "+ str(len(json_to_dict)) +" monitors matching this search.")

# now we will open a file for writing
data_file = open('all_monitors_matching_query.csv', 'w')

# create the csv writer object
csv_writer = csv.writer(data_file)

# Counter variable used for writing
# headers to the CSV file
count = 0

#csv_writer.writerows(api_response)
for mon in json_to_dict:
    if count == 0:
        # Writing headers of CSV file
        header = mon.keys()
        #header = "123"
        csv_writer.writerow(header)
        count += 1

    # Writing data of CSV file
    csv_writer.writerow(mon.values())

data_file.close()
