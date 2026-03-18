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
def view_flights(flightlist, flight, source, destination, flightnum, seats, price):
  """Reads flightlist data to print all flight information in a fairly celan"""
  import os
  flightlist = os.open("Flightlist.xlsx", mode = "r")
  print(f"------------------------------------------\nDeparting    Arriving   Flight Number   Seats Available   Price------------------------------------------\n------------------------------------------\n")
  for flight in flightlist():
    if flight != type(int):
      pass
    source = flightlist[0]
    destination = flightlist[1]
    flightnum = flightlist[2]
    seats = flightlist[3]
    price = flightlist[4]
    print(f"{source}   {destination}   {flightnum}   {seats}   {price}")
  print("------------------------------------------")
view_flights()