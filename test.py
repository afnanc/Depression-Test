# Starting statment and general information about program.
print "                         DEPRESSION TEST "
print
print "Hello "
print "I am here to ask you a few questions relating to your mental health "
print "First and foremost, I need to ask for some general information from you "
print

# variables used for general information (If age is eleven or younger you can not write the test and if your a number that no human lived longer then you are to old)
name = input("What is your name? ")
age = int(input("How old are you? "))
if age <= 11 or age > 90:
    print "your are to young or old to write the test, you must be 12 or older "
    
else:
# Explains how to answer the questions
    print "\nFrom a scale of 0-3, determine your feelings towards each question \nin the past two weeks:"
    print "0 = not at all , 1 = several days , 2 = more than half the days , \n3 = nearly everyday.\n"
    
# Questions asked to the user answer of (0-3) can only be outputed or else code is invalid
    question_1 = int(input("1. little interest or pleasure in doing things? (0-3):"))
    if question_1 >= 4 or question_1 < 0:
        print "Invalid numbers, please reread and try again."

    question_2 = int(input("2. Feeling down, Depressed or Hopeless? (0-3):"))
    if question_2 >= 4 or question_2 < 0:
        print "Invalid numbers, please reread and try again."
        
    question_3 = int(input("3. Trouble falling or staying asleep, or sleeping too much?\n (0-3):"))
    if question_3 >= 4 or question_3 < 0:
        print "Invalid numbers, please reread and try again."
        
    question_4 = int(input("4. Feeling tired or having little energy? (0-3):"))
    if question_4 >= 4 or question_4 < 0:
        print "Invalid numbers, please reread and try again."
        
    question_5 = int(input("5. Poor appetite or overeating? (0-3):"))
    if question_5 >= 4 or question_5 < 0:
        print "Invalid numbers, please reread and try again."
    
    question_6 = int(input("6. Feeling bad about yourself - or that you are a failure \n or have let yourself or your family down? (0-3):"))
    if question_6 >= 4 or question_6 < 0:
        print "Invalid numbers, please reread and try again."
    question_7 = int(input("7. Trouble concentrating on things such as reading the newspaper \n or watching television? (0-3):"))
    if question_7 >= 4 or question_7 < 0:
        print "Invalid numbers, please reread and try again."
        
    question_8 = int(input("8. Moving or speaking so slowly that other people could have \nnoticed? (0-3):")) 
    if question_8 >= 4 or question_8 < 0:
        print "Invalid numbers, please reread and try again."
    
    question_9 = int(input("9. Thoughts that you would be better off dead, or of hurting \n yourself in some way? (0-3):"))
    if question_9 >= 4 or question_9 < 0:
        print "Invalid numbers, please reread and try again."

# a variable that adds up all the values of the questions
    depression_scale = question_1 + question_2 + question_3 + question_4 + question_5 + question_6 + question_7 + question_8 + question_9

# prints your final result of the survey
    print "\nresults = " + str(depression_scale) + "/27"
    print

# prints level of depression if your total is between 0-4
    if depression_scale >= 0 and depression_scale <= 4:
        print str(name)
        print "You have no depression."
    
# prints level of depression if your total is between 5-9
    if depression_scale >=5 and depression_scale <= 9:
        print str(name)
        print "You have mild depression."
    
# prints level of depression if your total is between 10-14
    if depression_scale >= 10 and depression_scale <= 14:
        print str(name)
        print "You have moderate depression."
    
# prints level of depression if your total is between 15-19
    if depression_scale >= 15 and depression_scale <= 19:
        print str(name)
        print "You have moderate to severe depression."
    
# prints level of depression if your total is between 20-27
    if depression_scale >= 20 and depression_scale <= 27:
        print str(name)
        print "You have severe depression."
    
# prints invalid when numbers are wrong (under 0 and over 27)
    if depression_scale >= 28 or depression_scale < 0:
        print str(name) 
        print "Invalid numbers, please reread and try again."
