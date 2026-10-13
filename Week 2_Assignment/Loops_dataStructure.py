 #Create a list and perform CRUD operations.

# Create a list
numbers = [10, 20, 30, 40]
print("Original list:", numbers)

# Read
print("First element:", numbers[0])

# Update
numbers[1] = 25
print("After updating:", numbers)

# Delete
numbers.remove(30)
print("After deleting:", numbers)

# Create (add a new element)
numbers.append(50)
print("After adding:", numbers)


 #Write a dictionary program to count word frequency.

sentence = "Python is a easy language."

words = sentence.split()
frequency = {}

for word in words:
    if word in frequency:
        frequency[word] += 1
    else:
        frequency[word] = 1

print("Word frequency:", frequency)

# Use nested loops to print a pattern.
for i in range(1,5):
    for j in range(1,i):
        print("*",end=" ")
    print()

 #Find largest and smallest number in a list.

list1=[10,55,68,97,40]
maximum=max(list1)
minimum=min(list1)
print("The maximum of the numbers in list is:",maximum)
print("The minimum of the numbers in the list is:",minimum)
    
 #Sort a list using sort() and lambda key
words=['Banana','Pear','Apple','Kiwi','Watermelon']
words.sort(key=lambda word: len(word))
print("Sorted by length:",words)


