def isAnagram(s, t):
    if len(s) != len(t):
        return False
    else:
        return "They like each other"

s = input("Enter the first string: ")
t = input("Enter the second string: ")

print(isAnagram(s, t))