# Made by Skj0nes-2
# Imports
import itertools
import re
charIn = input('All Characters: ') # Ask for characters to use
length = int(input('Combo Length: ')) # Ask for desired length of combos
print('Total Combos: '+str(len(charIn)**length)) # Print total number of combinations
chars = [char for char in charIn] # Seperate characters into list
result = []
for _ in range(length):
    result.append(chars) # Establish combo length
combos = list(itertools.product(*result)) # Generate combos
combosF = ''
for item in combos:
    pattern = "[" + re.escape("[]()', ") + "]" # List characters
    combo = re.sub(pattern, "", str(item)) # Remove list characters
    combosF=combosF+combo+'\n' # Add next combo to final combo list
with open('combos.txt', 'w') as file:
    file.write(combosF) # Write final combos list to file
print("Combos recorded at ' combos.txt '.") # Print exit msg
