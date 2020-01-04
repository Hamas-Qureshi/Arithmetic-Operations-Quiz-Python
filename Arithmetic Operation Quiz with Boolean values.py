import random

def doTest(operation): 
    correctCounts = 0
    if(operation == 0):
        print("Performing Addition")
        for i in range(0, 10):
            num1 = random.randint(1,10)
            num2 = random.randint(1,10)
            ans = int(input((str(num1)+" + "+str(num2)+" = ")))
            if(ans == num1+num2):
                print("Correct Answer")
                return True
            else:
                print("Wrong Answer")
                print("The correct answer is: "+str(num1+num2))
                return False
    elif(operation == 1):
        print("Performing Multiplication")
        for i in range(0, 10):
            num1 = random.randint(1,10)
            num2 = random.randint(1,10)
            ans = int(input((str(num1)+" x "+str(num2)+" = ")))
            if(ans == num1*num2):
                print("Correct Answer")
                return True
            else:
                print("Wrong Answer")
                print("The correct answer is: "+str(num1*num2))
                return False
    
responsesCorrect = 0
print("The software will process a test with 10 questions …… ")
for compteur in range (10):
    operation = random.randint(0,1)
    if doTest(operation) == True:
         responsesCorrect += 1
print(responsesCorrect, "Correct responses")         
if responsesCorrect  <= 6 :
  print("Ask some help from your instructor.")
else:
  print("Congratulations!")
