# This program will read in data from a text file containing food items
# and store the data within a list.
# The program will present the user with a set of menu options and will be
# able to sort the list, produce a report and query the list appropriately.

import csv

# Define the main function
def main():

    # Create a list to store the data from the file in
    food_items = []
    # Open a file named cw2file.txt
    with open('food_items.txt') as f:
        lines = f.read().splitlines()
        for line in lines:
            if line.strip()[0] == '#':
                continue

            food_items.append(line)

    dict = []
    with open('food_items.txt', newline='') as csvfile:
        reader = csv.DictReader(csvfile, skipinitialspace=True)
        for item in reader:
            dict.append(item)

    while True:
        print("\n\n------------------------------------------------------------")
        options = input("Menu:  Enter the number of the option you would like to select.\n"
                        "1. Output the number of meal records in the program.\n"
                        "2. Output a list of foods and details.\n"
                        "3. Output a report detailing the total calorie count of all foods.\n"
                        "4. Output all average serving weights.\n"
                        "5. Add a new food item.\n"
                        "6. Print a report of the number of items from each meal type.\n"
                        "7. Query the saturated fat threshold against food items.\n"
                        "8. Quit the program.\n"
                        "Enter option here: ")
        if options == '1':
            print("The number of meal records in the program is:", len(dict))
        elif options == '2':
            for item in dict:
                print("Time: {0}, Type: {1}, Description: {2}, Serving: {3}, Calories: {4}, Saturated Fat: {5}"\
                      .format(item["TIME"], item["MTYPE"], item["DESC"], item["SERVING"], item["KCAL"], item["SFATg"]))
        elif options == '3':
            calories = 0
            for item in dict:
                calories += int(item["KCAL"])
            print('Total calorie count of all foods: {0}'.format(calories))
        elif options == '4':
            servings = 0
            for item in dict:
                servings += int(item["SERVING"])
            print("Average serving weights for all food items: {0}".format(servings/len(dict)))
        elif options == '5':
            food_item = input("Add a new food item:")
            dict.append(food_item)
        elif options == '6':
            print("The number of items from each meal type:")
            for item in dict:
                input("Enter the meal type you would like to obtain a report for or enter 'all' to display a report"
                      "for all 3 meal types.")
                if input = 'Breakfast' or 'breakfast':
                    print("Breakfast: {0}.".format(item["MTYPE"] = 'Breakfast'))
        elif options == '7':
            print("The saturated fat threshold compared to food items:")
        elif options == '8':
            print("Thank you for using this program.")
            exit()
        else:
            print("Please enter an option from the menu.")

        input("\nPress return to continue")

# Call the main function
main()