def multiply(x, y):     # Function is defined by def
                    # Parameters go within the functions parantheses.
    result = x * y
    # print(result) # Use print when you only want to show data to a human
    return result # return will print the result within a function
                # Using return will send a value from one point within your code to another
                # Leave two balnk lines before and after the functions
def palindrome(string): # Palindrome a word reads itself backwards and forwards the same. racecar
    # backwards = string[::-1]
    # return backwards == string
    return string[::-1].casefold() == string.casefold() # return string[::-1] == string

def palindrome_sentence(sentence):
    string = ""
    for char in sentence:
        if char.isalpha():
            string += char
    print(string)
    # return string[::-1].casefold() == string.casefold()
    return palindrome(string)


word = input("Please enter a word/sentence that is a palindrome: ")
if palindrome_sentence(word):
    print("'{}' is a palindrome!".format(word))
else:
    print("'{}' is not a palindrome.".format(word))

# answer = multiply(10.5, 4)
# print(answer)
#
# forty_two = multiply(6, 7)
# print(forty_two)

# for value in range(1, 5):
#     two_times = multiply(2, value)
#     print(two_times)
