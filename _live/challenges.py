"""
Write a function called `getLastChar()` that takes a string as an argument
and returns the last character of that string.
  - Input: `'twister'`
  - Output: `'r'`
"""
def get_last_char(word):
    return word[-1]


print(get_last_char('twister') == 'r')


"""
Write a function called `repeater()` that takes a string and an integer
as arguments, and returns the string repeated that many number of times.
  - Input: `3, 'blah'`
  - Output: `blahblahblah`
"""
def repeater(word, num):
    output = ''
    for _ in range(0, num):
        output += word
    return output


print(repeater('apple', 4) == 'appleappleappleapple')
