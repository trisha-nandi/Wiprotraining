
from MyPackage.spring_op import reverse_string,to_uppercase,string_length
from MyPackage.str_validate import is_alpha,is_palindrome

text = "Trishaa"

print("Original:" ,text)
print("Reversed:",reverse_string(text))
print("Uppercase:", to_uppercase(text))
print("Length:",string_length(text))

print("Is Plindrome:", is_palindrome(text))
print("Is Alphabet Only:",is_alpha(text))