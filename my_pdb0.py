""" my_pdb.py is a simple debugger 

    Usage: python3 my_pdb.py
"""

import sys
import string

# Grab the script from the user
script = input('What script would you like to debug? ')

# Grab the line on which to place the breakpoint (with error checking)
while True:
    try:
        breakpt = int(input('Line number on which to place the breakpoint? '))
        if breakpt < 0:
            print('The line number must be an integer greater than 0')
            continue
        break
    except ValueError:
        print('The line number must be an integer greater than 0')

# Read in and edit the original script
with open(script) as fin:
    # Read and remember the first lines of the script up to, but not
    # including, the line where we want to put a breakpoint
    edited_script = ''
    for i in range(breakpt - 1):
        the_line = fin.readline()
        assert the_line != '', "breakpt not in script"
        edited_script += the_line

    # Read the line where we're placing the breakpoint
    the_line = fin.readline()

    # Grab the whitespace so we get the right indentation
    my_whitespace = ''
    for c in the_line:
        if c in string.whitespace:
            my_whitespace += c
        else:
            break

    # Insert a raise statement as our breakpoint
    edited_script += my_whitespace + 'raise Exception("My breakpoint")\n'

    # Insert the line before which we break
    edited_script += the_line

    # Grab the rest of the lines in the script
    while True:
        the_line = fin.readline()
        
        if the_line == '':
            # We read the entire script
            break

        edited_script += the_line

# Write out the edited script
output_script = script.replace('.py', '-db.py')
with open(output_script, 'w') as fout:
    fout.write(edited_script)
print(f'Wrote {output_script}')
