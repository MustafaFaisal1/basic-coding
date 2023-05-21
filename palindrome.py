word = str(input("Enter: "))
comp_word = ""
for n in range(len(word) - 1, - 1 , - 1):
    comp_word += word[n]
if comp_word == word:
    print ("The word is palindrome")
else:
    print ("The word is not a palindrome")