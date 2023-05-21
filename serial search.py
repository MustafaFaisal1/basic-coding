data = [1,2,3,4,5]
guess = int(input("Enter a guess: "))
found = False
index = 0
while found == False and index < len(data):
    if guess == data[index]:
        found = True
    index += 1
if found:
    print ("your guess was correct")