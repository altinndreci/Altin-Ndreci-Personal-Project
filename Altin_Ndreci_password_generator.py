import string   #importing strings and randoms to begin coding process
import random

s1 = list(string.ascii_lowercase) #Lowercase Letters
s2 = list(string.ascii_uppercase) #Uppercase Letters
s3 = list(string.ascii_letters) #Mix of all letters
s4 = list(string.digits) #Numbers
s5 = list(string.punctuation) #Special Characters

#Asks for user input (I like having 10 characters or more as it is more likely to be a strong password)
user_preference = input("How many characters would you like your password to be (10 or more must be input): ")

#Putting input rules to make sure an affective password is made
while  True:
    try:
        character_input = int(user_preference)
        if character_input < 10:
            print("Nothing less than 10 characters please.")
            user_preference = input("Enter the amount of characters again: ")

        else:
            break
    except ValueError:
        print("Enter numbers only.")
        user_preference = input("How many characters would you like your password to be (10 or more must be input): ")

#Shuffling Characters
random.shuffle(s1)
random.shuffle(s2)
random.shuffle(s3)
random.shuffle(s4)
random.shuffle(s5)

#Calculates number of characters that were input to use
num_of_letter = min(character_input * 2 // 5, len(s1))
num_digits_punctuations = min(character_input // 5, len(s4), len(s5))

result = [] #Empty List

#Selecting random samples
result.extend(random.sample(s1, num_of_letter))
result.extend(random.sample(s2, num_of_letter))
result.extend(random.sample(s4, num_digits_punctuations))
result.extend(random.sample(s5, num_digits_punctuations))

#Fill remaining characters
remaining_characters = character_input - len(result)
if remaining_characters > 0:
    result.extend(random.choices(s3 + s4 + s5, k=remaining_characters))

random.shuffle(result)

#Final Password
password = "".join(result)
print("Your password is: ", password)