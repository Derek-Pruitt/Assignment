
# AUTHOR:       Derek Pruitt

#PYTHON:        3.8.3

# For D&D use, eventualy make it a app whith more programs

import random

def use_dice():
    while True: # Will keep running until stopped with "break" statement
        d_in = input("Please select D100, D20, D12, D10, D8, D6, D4, D3...\n   >")
        result = None
        if d_in == 'D12':
            result = random.randrange(1,13)
        elif d_in == 'D20':
            result = random.randrange(1,21)
        elif MORE DICE:
            ## Do stuff
        else:
            print('You did not select a D100, D20, D12, D10, D8, D6, D4, D3\n')
            yes_or_no = input('Use again? Y/N\n')
            if yes_or_no != 'Y': # If anything but Y is given, end loop
                break ## The loop will stop if this line is reached
                ## Note no use of quit(), as we may want execution to be returned to us

        if result is not None:
            print('{}'.format(result))

    print('Goodbye') ## This will execute just before function exits
