import pandas as pd

#Exercise-2: top 10 arrival airports in the world in 2013 (using the bookings file)
#This program prints airport city, air port code, and total number of passengers that have actually booked the flight
def arr_arrivals():
    fields = ['arr_city','arr_port','pax'] # select the required fields
    bookings = pd.read_csv('bookings.csv',sep='^',usecols=fields) # read the data from the selected coloumns
    #group cloumns: arr_city and arr_ports, counts value in 'pax', then sort values to get maximum number of arrivals
    result= bookings.groupby(['arr_city','arr_port'])['pax'].count().sort_values(ascending=False) 
    print result[:10] #print to 10 recodrs of dataframe
    