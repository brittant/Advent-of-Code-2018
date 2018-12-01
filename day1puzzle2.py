'''
Code Puzzle 2 Day 1
'''

total = 0           # Keeps track of the current frequencies
frequencies = []    # A list of all the frequencies
unique = True       # Track if we have seen a duplicate or not

with open('xmasinput.txt') as f:
    lines = [line.rstrip('\n') for line in open('xmasinput.txt')]

    while unique:                           # Continue looping through lines until we see a duplicate
        print("Searching...")
        for x in lines:
            total = total + int(x)          # Update current frequency
            if total in frequencies:
                print('STOP::: ', total)    # Print the duplicate to console
                unique = False              # Update variable to break the while loop
                break                       # break out of for loop
            frequencies.append(total)       # Update frequencies list after checking the current frequency
