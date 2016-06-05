import csv
import pandas as pd

#Exercise-2: top 10 arrival airports in the world in 2013 (using the bookings file)

fields = ['arr_port', 'pax'] # select the required fields

df = pd.read_csv('bookings.csv',sep=',', usecols=fields) # read the data from the selected coloumns
