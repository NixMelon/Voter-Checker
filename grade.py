# score/mark from the user
# name

score = input("Enter your score: ")
if score.isalnum() == True:
    print("Invalid input, Please try again!")
    exit()

    
score = float(score)
# __________________logic of the program_________________
if 80 <= score  and score <= 100:
    print("Your Grade is A:")

elif 75 <= score  and score < 80:
    print("Your Grade is B+: ") 
    
elif 70 <= score  and score < 75:
    print("Your Grade is B: ")

elif 65 <= score  and score < 70:
    print("Your Grade is C+: ")

elif 60 <= score  and score < 65:
    print("Your Grade is C: ")

elif 55 <= score  and score < 60:
    print("Your Grade is D+: ")

elif 50 <= score  and score < 55:
    print("Your Grade is D: ")

elif 0 <= score  and score < 50:
    print("Your Grade is F: ")
else:
    print("Your score is out of range.Please Check it again.")