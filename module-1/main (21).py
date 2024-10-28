#Colton Kohler
#Module 1.3 Assignment
#10/27/2024
#This programm recreates the popular bar song "99 Bottles of Beer" and asks the user how many bottles of beer are on the wall."

# Function to count down bottles of beer on the wall

def countdown(bottles):
    while bottles > 0:
        if bottles > 1:
            print(f"{bottles} bottles of beer on the wall, {bottles} bottles of beer.")
            print(f"Take one down, pass it around, {bottles - 1} bottles of beer on the wall.\n")
        else:
            print("1 bottle of beer on the wall, 1 bottle of beer.")
            print("Take it down, pass it around, no more bottles of beer on the wall.\n")
        bottles -= 1  # reduce the bottle count each time

# Main program with input validation loop
while True:
    try:
        bottles = int(input("How many bottles of beer are on the wall? "))
        if bottles > 0:
            countdown(bottles)
            print("Time to buy more beer!")
            break  # Exit loop after valid input and countdown completion
        else:
            print("Please enter a positive integer.")
    except ValueError:
        print("Invalid input. Please enter a whole number.")

