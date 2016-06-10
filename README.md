# Assignment
Note: Here is a summary of the assignment. The three tasks are separately completed. The python code for: task-1 is presented in exercise1.py; task-2 is presented in exercise2.py; task-3 is presented in exercise3.py. The comments are inserted in each file to make is understandable for the reader. In the following lines some comments are added with the given task. These comments provide an overview of the completed and unattempted tasks 

First exercise: count the number of lines in Python for each file. 
    Comments: Task is completed. The output prints number of lines in each file

Second exercise: top 10 arrival airports in the world in 2013 (using the bookings file)

Arrival airport is the column arr_port. It is the IATA code for the airport

To get the total number of passengers for an airport, you can sum the column pax, grouping by arr_port. Note that there is negative pax. That corresponds to cancelations. So to get the total number of passengers that have actually booked, you should sum including the negatives (that will remove the canceled bookings).

Print the top 10 arrival airports in the standard output, including the number of passengers.

Bonus point: Get the name of the city or airport corresponding to that airport (programatically, we suggest to have a look at GeoBases in Github)

Bonus point: Solve this problem using pandas (instead of any other approach) 

    Comments: The task (with bonus tasks) is completed using pandas. The program takes an input to print the number of top records. As required in the bonus task, the city name is also printed in each output record. 

Third exercise: plot the monthly number of searches for flights arriving at Málaga, Madrid or Barcelona

For the arriving airport, you can use the Destination column in the searches file. Plot a curve for Málaga, another one for Madrid, and another one for Barcelona, in the same figure. Bonus point: Solving this problem using pandas (instead of any other approach) 

Bonus exercise: match searches with bookings

For every search in the searches file, find out whether the search ended up in a booking or not (using the info in the bookings file). For instance, search and booking origin and destination should match. For the bookings file, origin and destination are the columns dep_port and arr_port, respectively. Generate a CSV file with the search data, and an additional field, containing 1 if the search ended up in a booking, and 0 otherwise. 

Bonus exercise: write a Web Service

Wrap the output of the second exercise in a web service that returns the data in JSON format (instead of printing to the standard output). The web service should accept a parameter n>0. For the top 10 airports, n is 10. For the X top airports, n is X.

    comments: The primary task is completed. However, two bonus exercises are not attempted: match searches with bookings, and write a Web Service. The plot shows monthly number of searches for each destination: Málaga, Madrid or Barcelona. 