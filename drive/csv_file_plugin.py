import requests
import csv
url="https://raw.githubusercontent.com/NavyaDeepika-Garakapati/python/main/drive/testfile_with%2Bpublic_permission.csv"
response = requests.get(url)
# print(response.text)
lines = response.text.split('\n')
# now iterate over those lines
ip_list = set()

for row in csv.DictReader(lines):
    ip = row['ip']
    if ip != '':
        ip_list.add(row['ip'])
print(ip_list)