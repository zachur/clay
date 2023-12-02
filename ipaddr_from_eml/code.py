import re

file_path = r'dummy.eml'

with open(file_path, 'r') as file:
    file_lines = file.readlines()

ip_pattern = re.compile(r'\b(?:\d{1,3}\.){3}\d{1,3}\b')

ip_addresses = []

for line in file_lines:
    matches = ip_pattern.findall(line)
    ip_addresses.extend(matches)

for ip in ip_addresses:
    print(ip)

output_file_path = 'ipaddr_out.txt'
with open(output_file_path, 'w') as out_file:
    for ip in ip_addresses:
        out_file.write(str(ip) + '\n')
