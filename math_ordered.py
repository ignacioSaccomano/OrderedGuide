'''
    Ignacio Saccomano 2020

    This program program´s main function is to sort the exercises from lowest to highest, and if the student´s guide is incomplete, the program also 
    tells how many are yet to be done and which (if so, of course).

    Then, the program asks the user how many exercises are needed to hand in, if so, and calculates accurately (to two decimals) how likely you are 
    to be asked for an exercise you couldn´t do.
'''


exercises = []     # Create list of user´s done exercises.
total = []         # List of total exercises to do in the guide.


many = int(input("How many exercises do you have to do? "))   # Total exercises to do.

def bad_luck(n):
    num = len(exercises)
    div = many
    stat = num / div

    if stat == 0:
        return "100"
    else:
        for i in range(n - 1):
            stat *= (num - 1) / (div - 1)
    return str(round(100 - stat * 100))

while True:
    try:
        data = int(input("Exercise: "))        # The user puts the number of the exercise done. If not, or if it ended, hits enter without putting any value.
    except:
        break
    exercises.append(data) # Adds each excercise to done list.

    # TODO: Fix empty value taken as one.

exercises = list(dict.fromkeys(exercises)) # Delete duplicates if any.

print("This are the exercises you did (ordered): " + str(sorted(exercises)))  # Shows sorted exercises.

if len(exercises) == many:     # Verifies if user is done.
    print("Congratulations, you finished ;) \nNow enjoy!")
else:
    for i in range(many):
        total.append(i + 1)    # Creates a list composed of all exercises from the guide to compare after.

    missing = many - len(exercises)

    remain = list(set(total) - set(exercises))  # List of excercises missing.

    done = (len(exercises)/many) * 100   # Percentage of the total guide done.

    print("There are " + str(missing) + " exercises missing.")
    print("\nThose are: " + str(sorted(remain)))
    print("You did " + str(int(done)) + "% of the guide.")

    luck = int(input("How many exercises do you need to hand in? "))
    
    print("The probabilities you will be asked to hand in something you didn´t do are " + bad_luck(luck) + "%")
    

