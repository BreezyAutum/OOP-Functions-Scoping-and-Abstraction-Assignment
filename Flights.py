# Autum's Code
"""
Assignment notes:
view_flights()
Display all available flights in a formatted table.
Loop through each flight in the flights list
Format and display the details of each flight.
The flight details should include flight number, source, destination, available seats, and price.
Parameter(s): list of flights
The function does not return any value including None.
"""
def view_flights(flightlist):
  """Reads flightlist data to print all flight information in a fairly celan"""
  import os
  li_flights = os.open("Flightlist.xlsx", mode = "r")
  print(f"------------------------------------------\nDeparting    Arriving   Flight Number   Seats Available   Price------------------------------------------\n------------------------------------------\n")
  for flight in li_flights():
    if flight != type(int):
      pass
    else:
      source = li_flights[0]
      destination = li_flights[1]
      flightnum = li_flights[2]
      seats = li_flights[3]
      price = li_flights[4]
      print(f"{source}   {destination}   {flightnum}   {seats}   {price}")
      flightlist.append(flight)
  print("------------------------------------------")
"""
It reads flights data from the flight file (i.e., file_name) 
The flight data is a comma separated values and includes flight number, source, destination, seats available, and price.
 It stores the flights data in a list (i.e., flights list) and returns it.
Parameter(s): flights’ file name.
It returns the flights list.
"""
def load_flights():
  """"""
view_flights()