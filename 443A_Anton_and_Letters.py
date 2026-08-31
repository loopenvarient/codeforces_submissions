s = input()
 
letters = set()
 
for char in s:
    if char.isalpha():
        letters.add(char)
 
print(len(letters))