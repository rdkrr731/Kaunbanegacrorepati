#Kaun banega crorpati
#greeeting
print("Welcome to Kaun Banega Crorepati\n")
name = input("Enter your name: ")  #taking name as input
print(name, "You can win 1million if you answer all the questions correctly\n"
      )  #printing name and rules
print("If you answer any question wrong you will lose the game\n")
print("You will be given 4 options to choose from\n")
print("If you choose the correct option you will win the amount of money\n")
# print("If you choose the wrong option you will lose the game")

#questionaire
Question1 = [
    "What country has the highest life expectancy?",
    "Where would you be if you were standing on the Spanish Steps?",
    "Which language has the more native speakers?",
    "What is the most common surname in the United States?",
    "What disease commonly spread on pirate ships?",
    "Who was the Ancient Greek God of the Sun?",
    "What was the name of the crime boss who was head of the feared Chicago Outfit?",
    "What year was the United Nations established?",
    "Who has won the most total Academy Awards?",
    "What artist has the most streams on Spotify?"
]

#Options
options = [
    "HongKong", "Rome", "India", "Smith", "Scurvy", "Apollo", "Al Capone",
    "1945", "Walt Disney", "Drake"
]

#answers
Answers1 = [
    "hongkong", "rome", "india", "smith", "scurvy", "apollo", "al capone",
    "1945", "walt disney", "drake"
]

Level = [1000, 2000, 3000, 5000, 10000, 20000, 40000, 80000, 160000, 320000]

for i in range(0, len(Question1)):
    print(Question1[i])
    print("\nOptions are: \n")
    print("1.", options[i % len(options)])
    print("2.", options[(i + 1) % len(options)])
    print("3.", options[(i + 2) % len(options)])
    print("4.", options[(i + 3) % len(options)])
    a = input("\nEnter your answer: ").lower()
    if a == Answers1[i]:
        print("\nCorrect answer!!\n")
        print(f"You have won Rs.{Level[i]}\n")
    else:
        print("Wrong answer")

        break
