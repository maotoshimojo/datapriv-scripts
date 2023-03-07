from collections import Counter
import csv

hosts = Counter()

with open('data/javascript_cookies.csv') as f:
    reader = csv.reader(f, dialect='unix')
    next(reader)
    for row in reader:
        host = row[11]
        if host.startswith('www'):
            host = host[3:]
        if host.startswith('.'):
            host = host[1:]
        hosts.update({host: 1})

print('hosts:', hosts.most_common(50))