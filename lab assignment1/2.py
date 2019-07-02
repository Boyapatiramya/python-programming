stringinput = input('Please enter a string:')
# Two lists are needed. One will be a list of characters that make up the current string that is being analyzed
# The other list is a list of all strings found while running the program.
current = []
strings = []
# Look at each character in the Input String
for char in stringinput:
    # Check to see if character is in current string list
    if char in current:
        # Use the join function on the current to create a string with nothing in between the characters. Then use
        # append to add the new string to the list of strings found
        strings.append(''.join(current))

        nextstring = current.index(char)+1
        current = current[nextstring:]
    # Add current character to current string list after checking to see if it is already in the list.
    current.append(char)

strings.append(''.join(current))
# Use the max function to grab the longest string from the strings list
long = max(strings, key = len)

print('The longest string of characters without repeating is', long,'with a length of', len(long))