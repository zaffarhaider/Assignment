import csv
import pandas as pd

#Exercise-2: top 10 arrival airports in the world in 2013 (using the bookings file)

def arrivals():
    fields = ['arr_port','pax'] # select the required fields
    bookings = pd.read_csv('bookings.csv',sep='^',usecols=fields) # read the data from the selected coloumns
    print('\n First 5 records')
    print bookings.head()