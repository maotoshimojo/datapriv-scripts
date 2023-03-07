from collections import Counter
import csv

old_request_urls, new_request_urls = Counter(), Counter()

with open('data/http_redirects.csv') as f:
    reader = csv.reader(f, dialect='unix')
    next(reader)
    for row in reader:
        old, new = row[4], row[6]
        old, new = old.split('://')[1], new.split('://')[1]
        old, new = old.split('/')[0], new.split('/')[0]
        old_request_urls.update({old: 1})
        new_request_urls.update({new: 1})

print('old request urls:', old_request_urls.most_common(50))
print('new request urls:', new_request_urls.most_common(50))