import csv

             
    #Task-1: Count the number of lines in Python for each file 
def read_files():
    f1 = open('bookings.csv') # opens the booking.csv file
    f2 = open('searches.csv') # opens the searches.csv file
    try:
        reader1 = csv.reader(f1) # creates the reader object
        reader2 = csv.reader(f2) 
        
        for row_f1 in reader1:   # iterates the rows of the file in orders
            row_count_f1 = sum(1 for row_f1 in f1)   # count number of rows
        for row_f2 in reader2:
            row_count_f2 = sum(1 for row_f2 in f2)
    finally:
        print("Number of lines in booking.csv= ",row_count_f1)
        print("Number of lines in searches.csv= ",row_count_f2)