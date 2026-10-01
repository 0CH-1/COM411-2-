#Display messages to the screen
print("Welcome to COM411!")
print ("In week 1  we will learn...")
print ("...How to use Git and GitHub")
print ("...How to output to the screen")
print ("...How to get user input")
print ("I hope you're enjoying the lesson thus far!")

# Display escape characters
print("\n Displays a new line")
print("\t Displays a tab space")
print("\\ Displays a back slash")
print("\" Displays a double quote")
print("\' Displays a single quote")

print("I am programming!")

# Display a box
print("##########")
print("#        #")
print("#        #")
print("##########")

# Ask user to enter their name
print("What is your name?")
name = input()
print(f"It is nice to meet you {name}")

# Display a box
print("##########")
print("#  o  o  #")
print("#  ----  #")
print("##########")

#BMI calculator
name=input("What's your name?")
age=int(input("What's your age? (in years)"))
height=float(input("What's your height? (in metres)"))
weight=int(input("What's your weight? (in kilogram)"))
BMI=weight/(height*height)
print(f"Your BMI is {BMI}")


#Checking state in game
Lives=int(input("How many lives do you have?"))
energy=int(input("How many energy do you have?"))
shield=int(input("How many shield do you have?"))
print(f"Lives: {'♥'*Lives}")
print(f"Energy: {'♦'*energy}")
print(f"Shield: {'♦'*shield}")