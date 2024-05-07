def new_game():
    guesses =[]
    correct_guess =0
    question_num =1

    for key in questions:
        print("--------------------------------------")
        print(key)
        for i in answers[question_num-1]:
            print(i)
        guess =input("Enter A  (or)  B (or)    C (or)    D ?" ).upper()
        guess =guess.upper()
        guesses.append(guess)

        correct_guess+= check_ans(questions.get(key),guess)
        question_num+=1  

    display_score(correct_guess,guess)




def check_ans(answers,guess):
    if answers== guess:
        print(" Correct !")
        return 1 
    else :
        print("Wrong !")
        return 0       
    
def display_score(correct_guess, guesses):
    
    score =int(correct_guess/len(questions)*100)
    print()
    print("--------------------------------------")
    print("Your Score is   "+str(score)+"%" )
    
    if score>=90:
        print("Good Job. You are Very Smart")
    elif 60>=score>=40:
        print("Your are score is Average")
    elif score==100:
        print("You are Extremely Brilliant !!!")
    elif score<=40:
        print("You need to try more !")    
    print("--------------------------------------")            





questions ={"1. The Value Of Pi ?  :   ":"D",
            
            "2. What is the average of first 50 natural numbers ?  :   ":"C",
            "3. What is the next number 1,2,3,5,8,13,--- ?:   ":"D",
            "4. The Value of Cos 360 ? :   ":"A",
            "5. What is the name of Number System with Base 2 ?:   ":"B",
            "6. How many Zero in One Trillion ?  :    ":"A",
            "7. Solve 3+6 *(5+4)/3-7 ?  :  ":"C",
            "8. Counting Numbers are Kept under __ Number ?  :    ":"A",
            "9. The value of e=2.71828 is known as ?   :   ":"B",
            "10. What is the Next Number 1,4,13,40,121,__  ?  :   ":"C",
            "11. What is the 544,509,474,439,__  ? :    ":"A",
            "12. What is the sum of 130+125+191 ?  :    ":"C",
            "13. 144,__,206,240 ?  :    ":"D",
            "14. If tan(α) = 3/4, what is the value of cos(α)?":"B",
            "15.If all Blooms are Flowers, and some Flowers are Roses, can we conclude that some Blooms are Roses?":"A"
            
         }

answers =[["A. 3.14179, B. 3.24259,  C. 3.14195,   D. 3.14159"],#1
          ["A. 5.50",  "B. 20.5",  "C. 25.5", "D. 15.5"],#2
          ["A. 16", "B. 17", "C. 18", "D. 21" ],#3
          ["A. 1 ",  "B. 0 ", "C. 2 ", "D. None"],#4
          ["A. Decimal ",  "B. Binary ",  "C. Octal", "D.Hexadecimal"],#5
          ["A. 12",  "B. 9",  "C.10",  "D.6"],#6
          ["A. 10", "B. 12",  "C. 14",  "D. 16"],#7
          ["A. Natural ",  "B. Whole", "C. Rational", "D. Irrational"],#8
          ["A. Avogadro",  "B. Euler",  "C. Archimedes",  "D.Fermat"],#9
          ["A. 144 ",  "B. 243",  "C. 364", "D. 462"],#10
          ["A. 404", "B. 444", "C.397", "D. 304"],#11
          ["A. 436",  "B. 336", "C.446",  "D.346"],#12
          ["A. 184",  "B. 176", "C. 182", "D.174"],#13
          ["A. 5/4",  "B. 4/5", "C. 0", "D. 0.5"],#14
           ["A. Yes",  "B. No", "C. Not Sure", "D. I Dont Know"]#15


          ]
new_game()

