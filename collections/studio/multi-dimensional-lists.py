food = "water bottles,meal packs,snacks,chocolate"
equipment = "space suits,jet packs,tool belts,thermal detonators"
pets = "parrots,cats,moose,alien eggs"
sleep_aids = "blankets,pillows,eyepatches,alarm clocks"

# a) Use split to convert the strings into four cabinet lists. Alphabetize the contents of each cabinet.

food_list = food.split(',')
food_list.sort()

equipment_list = equipment.split(',')
equipment_list.sort()

pets_list = pets.split(',')
pets_list.sort()

sleep_aids_list = sleep_aids.split(',')
sleep_aids_list.sort()

print(food_list, equipment_list, pets_list, sleep_aids_list)


# b) Initialize a cargo_hold list and add the cabinet lists to it. Print cargo_hold to verify its structure.

cargo_hold = [food_list, equipment_list, pets_list, sleep_aids_list]
print(cargo_hold)

# c) Query the user to select a cabinet (0 - 3) in the cargo_hold.

user_input = input('Select a cabinet (0-3):  ')

# d) Use bracket notation and format to display the contents of the selected cabinet. If the user entered an invalid number, print an error message.



# e) Modify the code to query the user for BOTH a cabinet in cargo_hold AND a particular item. Use the in method to check if the cabinet contains the selected item, then print “Cabinet ____ DOES/DOES NOT contain ____.”
