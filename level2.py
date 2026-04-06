text = input("enter a string: ")
vowels="aeiouAEIOU"
count=0
for char in text:
    if char in vowels:
        count+=1
print("number of voweles: ", count)