import urllib2
import logging
import csv
import datetime

def downloadData(url):
    content = urllib2.uropen('https://s3.amazonaws.com/cuny-is211-spring2015/birthdays100.csv')
    info =  content.read()

def processData(info):
    csv_file = csv.reader(info)
    my_dict = {}
    date_format = datetime.strptime('%d/%m/%y %0:%0')
    assignment2 = 'logging_example.out'
    logging.basicConfig(filename=assignment2, level=logging.error,)
    logging.debug('Error processing line')

def displayPerson(id = int(), persondata=[]):
    pass