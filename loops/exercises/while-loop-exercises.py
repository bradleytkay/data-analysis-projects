# Define three variables for the LaunchCode shuttle - one for the starting fuel level, another for the number of astronauts aboard, and the third for the altitude the shuttle reaches.

fuel_lvl = 10000
num_astronauts = 3
altitude_reached_km = 100

# Exercise #1: Construct while loops to do the following:
  # a. Query the user for the starting fuel level. Validate that the user enters a positive, integer value greater than 5000 but less than 30000. 

while num_choice > 5000 and num_choice < 30000:
    num_choice = input('Enter a number between 5001 and 29999')
    if num_choice < 5000 or num_choice > 30000:
        print('Invalid entry')

# b. Use a second loop to query the user for the number of astronauts (up to a maximum of 7). Validate the entry.
  
while num_astronauts > 0 and num_astronauts <= 7:
    num_astronauts = input('Enter a number between 1 and 7')
    if num_astronauts < 1 or num_astronauts > 7:
        print('Invalid entry')
  
# c. Use a final loop to monitor the fuel status and the altitude of the shuttle. Each iteration, decrease the fuel level by 100 units for each astronaut aboard. Also, increase the altitude by 50 kilometers.

while fuel_lvl > 0 and altitude_reached_km < 100000:
    fuel_lvl -= (100 * num_astronauts)
    altitude_reached_km += 50

# Exercise #2: Print the result with the phrase, The shuttle gained an altitude of ___ km and has ___ kg of fuel left. Fill in the blanks with the altitude and fuel level values.

print('The shuttle gained an altitude of ' + altitude_reached_km + ' and has ' + fuel_lvl + ' kg of fuel left.')

# If the altitude is 2000 km or higher, add “Orbit achieved!” Otherwise add, “Failed to reach orbit.”

if altitude_reached_km >= 2000:
    print('Orbit achieved!')
else:
    print('Failed to reach orbit.')