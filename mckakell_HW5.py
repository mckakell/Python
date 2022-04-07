## Problem 5.39 Write function() that takes input a string and returns
## it with this modification: Every voewl is replace by four consecutive
## copies of itself and an exclamation mark(!) is added at the end.

def exclamation(string):
    vowels = 'aeiou'
    for vowel in vowels:#this runs through each index of variable vowels
        string = string.replace(vowel, vowel * 4)#this says vowel in string is replace by vowel letter x 4
    return string + '!'

string = "Hello"
string = string.lower()#I chose this method rather than making vowels ='aeiouAEIOU' but either works really
print(exclamation(string))#print function










## Problem 5.43 Implement function evenrow() that takes a
## two-dimensional list of integers and returns True if each row of the
## table sums up to an even number and False otherwise (i.e., if some
## row sums up to an odd number)

def evenrow(tdlist):
    row_sum = 0 #this acts as a counter
    for row in tdlist:
        #if statement says if there is no remainder count 1 for each index
        if sum(row) % 2 == 0:
            row_sum+= 1
        #if there is a remainder, subtract 1 for each row that is odd
        else:
            row_sum-=1
    #Since we counted 1 for each row that is even, if the counter is equal to the length of the list then we know its True.
    if row_sum == len(tdlist):
        return True
    else:
        return False

print(evenrow([[1,3],[2,4],[0,6]]))
print(evenrow([[1,3,2],[3,4,7],[0,5,2]]))
