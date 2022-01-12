def banner(text=" ",screen_width=80): # 80 is the default value if I don't add it below
    if len(text) > screen_width - 4:
        raise ValueError("String '{0}' is larger than specific width "
                         "'{1}'".format(text, screen_width)) # Creates Crash rather than error message.
    if text == '*':
        print('*' * screen_width)
    else:
        centered_text = text.center(screen_width - 4)
        output_string = ('**{0}**'.format(centered_text))
        print(output_string)


banner('*')
banner('Hello there how are you doing?')
banner('We are moving through the text fields')
banner('And this will be the very very very very very very long one, you know it '
       'has to be long',99)
banner('Trying to get more than the screen width')
banner('Another long long long long message that will reach the barrier, we are'
       ' almost there',99)
banner('of 80 characters.',) # Always call a functions rather than print it
banner('*')                # If you try to print it, None will appear

# numbers = [4, 6, 9, 10, 29, 1, 2]
# print(numbers.sort()) # If performing an action, None will print.
# print(numbers)        # If performing a result, the result will appear
# sorted(numbers)       # Will print numbers because it sorted the numbers after being printed.
#                       # If you don't explicitly return a value. Python returns None