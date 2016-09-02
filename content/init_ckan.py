from ckanapi import RemoteCKAN
import csv
import sys

ua = 'ckanapiexample/1.0 (+http://example.com/my/website)'

claircity = RemoteCKAN('http://127.0.0.1', apikey=sys.argv[1], user_agent=ua)

with open('orglist.csv') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        claircity.action.organization_create(name=row['name'], title=row['title'], image_url=row['image_url'])

with open('grouplist.csv') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        claircity.action.group_create(name=row['name'], title=row['title'])
