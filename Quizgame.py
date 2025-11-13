print("Hello Dhruv Welxome bacl ")

print("Welcome to Dhruv's quiz game ")

playing =input("Do you want to play Dhruv's quiz game ? ")
if playing.lower() !="yes" :
    quit()

print("Okay! thats great. Let's play the game. ")
score=0
answer1=input("What is the full form of cpu ? ")
if answer1.lower()=="central processing unit":
    print("Thats correct! ")
    score += 1 
else:
    print("Thats incorrect")

answer2=input("What does gpu stand for ? ")
if answer2.lower()=="graphics processing unit":
    print("Thats correct! ")
    score += 1
else:
    print("Thats incorrect")

answer3=input("What does RAM stand for ? ")
if answer3.lower()=="random access memory":
    print("Thats correct! ")
    score += 1
else:
    print("Thats incorrect")

answer4=input("what does PSU stand for ? ")
if answer4.lower()=="power supply":
    print("Thats correct! ")
    score += 1
else:
    print("Thats incorrect")


print("You scored " + str(score)+" in the quiz game. ")
print("You scored " + str(int((score/4)*100))+"%"+" in the quiz game. ")




