##Homework 6 problem 6.28##

languages = {"hello":"bonjour", "dog":"chien", "world":"monde"} #dictionary/translations

def translate(firstlang):
    firstlang = list(firstlang.split(" ")) #must put the user input into a list so we can check each word and translate
    for item in firstlang:#for loop runs through each word in list
        if item in languages:#each word in list is checked to see if in
        #dictionary, and then translated if it is. We met Walter for
        #online office hours and he recommended we use item.get(languages,"______") instead of the if statement but we couldn't get it to work for us.
            print(languages[item], end = " ")
        else:
            print("-----")
            
firstlang = str.lower(input("Enter a phrase: ")) #just incase user enters a word starting with a capital our program will still be able to properly search for the word.
translate(firstlang)







##Homework 6 problem 6.33##

import random
def diceproblem(dice_sum):
    num_sum_roll = 0 #counts number of rolls that equal the sum we are looking for
    total_roll = 0 #counts number of times we roll until 100 rolls of our sum is complete.
    while num_sum_roll <= 100: #while we have not rolled our sum 100 times
        roll = random.randrange(1,7)#chooses random dice number
        roll2 = random.randrange(1,7)
        roll_sum = roll + roll2 #adds die togeth 
        total_roll+=1 #counts the roll
        if roll_sum == dice_sum: #if the sum of the die is equal to the sum we are trying to roll, add 1
            num_sum_roll += 1
    print("It took", total_roll,"rolls to get 100 rolls of", dice_sum)
diceproblem(7) #calling the function


