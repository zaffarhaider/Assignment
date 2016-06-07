import pandas as pd

#Exercise-2: top 10 arrival airports in the world in 2013 (using the bookings file)
def arr_arrivals():
    fields = ['arr_port','pax'] # select the required fields
    bookings = pd.read_csv('bookings.csv',sep='^',usecols=fields) # read the data from the selected coloumns
    #group cloumn: arr_ports and count value in 'pax', then sort values to get maximum number of arrivals
    result= bookings.groupby('arr_port')['pax'].count().sort_values(ascending=False) 
    print result[:10] #print to 10 recodrs of dataframe
    