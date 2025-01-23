'''Write a function that checks if a given string is a palindrome. A palindrome is a word, phrase, number, or other sequence of characters that reads the same forward and backward (ignoring spaces, punctuation, and capitalization). The function should return True if the input string is a palindrome and False otherwise.'''

def is_palindrome(s: str) -> bool:
    # Remove non-alphanumeric characters and convert to lowercase
    cleaned_str = ''.join(char.lower() for char in s if char.isalnum())
    # Check if the cleaned string is equal to its reverse
    return cleaned_str == cleaned_str[::-1]

# Example usage:
print(is_palindrome("A man, a plan, a canal, Panama"))  # Output: True
print(is_palindrome("race a car"))  # Output: False