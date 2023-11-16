import random
#1.) 2.) 3.)Create lists for programming lanuages and difficulty levels
programming_languages = ["Python","Javascript","C++","Ruby","Java"]
difficulty_levels =[2,3,4,2,5]

#4.)combine the two lists into another list
quiz_data = list(zip(programming_languages, difficulty_levels))

#5.)shuffle the order of the quiz data around
random.shuffle(quiz_data)

#player score variable 
score = 0


for language, difficulty in quiz_data:
    guess = input(f"""What is the difficulty of {language}?
                  Enter a number from 1-5: """)
    if guess.isdigit():
        guess = int(guess)
        if guess == difficulty:
            print("Correct!")
            score = score + 1
        else:
            print(f"Oops! The correct difficulty of {language} is {difficulty}")
    else:
        print("Invalid entry. PLease enter a number")

else:
    print("Quiz over! You end with a score of",score)
    if score == 5:
        print("Amazing! You got a perfect score!")
    else:
        print("you got",score,"out of 5 questions correct")
        print("Play again sometime! Try for that pefect score!")