def is_palindrome(s):
    # Remove spaces and convert to lowercase
    cleaned_s = s.replace(" ", "").lower()
    # Check if the cleaned string is equal to its reverse
    if cleaned_s == cleaned_s[::-1]:
        return True
    else:
        return False

s = input("Enter a string: ")
print(is_palindrome(s))