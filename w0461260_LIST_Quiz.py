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

#use the difficulty and laguages for the for loop of the quiz
for language, difficulty in quiz_data:
    #user guesses the difficulty of the prompted language
    guess = input(f"""What is the difficulty of {language}?
                  Enter a number from 1-5: """)
    #convert answer to int if it's a number
    if guess.isdigit():
        guess = int(guess)
        #if answer is correct. add a point to the score
        if guess == difficulty:
            print("Correct!")
            score = score + 1
        #result if answer is incorrect
        else:
            print(f"Oops! The correct difficulty of {language} is {difficulty}")
    #message if input is not a number
    else:
        print("Oops. You have to enter a number")

#once quiz is complete
else:
    
    print("Quiz over! You end with a score of",score)
#if the user got a 0 by answering with non int values the whole time
    if score == 0:
        print("Buddy... You gotta answer with numbers,What are you doing?")
    else:
        #if user got a perfect score on the quiz
        if score == 5:
            print("Amazing! You got a perfect score!")
        # if user did not get a perfet score. tell them how many they did get.
        #and encourage them to try again for a perfect score
        else:
            print("you got",score,"out of 5 questions correct")
            print("Play again sometime! Try for that pefect score!")