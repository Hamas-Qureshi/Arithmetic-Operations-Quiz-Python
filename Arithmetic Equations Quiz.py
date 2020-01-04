import random

def performTest(operation):
    correctCounts = 0
    if(operation == 0):
        print("Performing Addition")
        for i in range(0, 10):
            num1 = random.randint(1,10)
            num2 = random.randint(1,10)
            ans = int(input((str(num1)+" + "+str(num2)+" = ")))
            if(ans == num1+num2): 
                correctCounts = correctCounts + 1
                print("Correct Answer")
            else:
                print("Wrong Answer")
                print("The correct answer is: "+str(num1+num2))
    elif(operation == 1):
        print("Performing Multiplication")
        for i in range(0, 10):
            num1 = random.randint(1,10)
            num2 = random.randint(1,10)
            ans = int(input((str(num1)+" x "+str(num2)+" = ")))
            if(ans == num1*num2): 
                correctCounts = correctCounts + 1
                print("Correct Answer")
            else:
                print("Wrong Answer")
                print("The correct answer is: "+str(num1*num2))


    print("You have "+str(correctCounts)+" correct answers")
    return correctCounts
    
print("This software tests you with 10 questions …… ");
operation = int(input("0) Addition \n1) Multiplication\nPlease make a selection (0 or 1): "))
      
correctCounts = performTest(operation)
        
if correctCounts <= 6 :
  print("Please ask your teacher for help.")
else:
  print("Congratulations!")

