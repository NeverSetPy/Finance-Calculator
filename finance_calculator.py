# Asks user to choose from a menu. Outcome branches according to option selected.

import math 

print('\ninvestment - To calculate the amount of interest you\'ll earn on your investment' )
print('bond       - to calculate the amount you\'ll have to pay on a home loan\n')

print('Enter either \'investment\' or \'bond\' from the menu above to proceed:\n')

# User input is standardised to lowercase.
# Inputs assigned to variables to use in formula to calculate either type of interest.

input_1 = input('Enter your selection').lower()
if input_1 == 'investment':
    print('You have selected \'investment.\'')
    P = int(input('How much money do you want to deposit?:'))
    r = int(input('What is the interest?'))
    t = int(input('How many years do you want to invest?'))

# Ask user follow up questions only after initial data has been gathered and recorded.

    raw_interest = input('Do you want simple or compound interest rate?').lower()
    simple_int = A = (P * t * r)/100
    compound_int = A = P * math.pow((1 + r/100),t)

# Calculates one of two interest options.
# Additional error message for incorrect input.

    if raw_interest == 'simple':
        print('Here is your simple interest calculation:', simple_int)
    elif raw_interest == 'compound':
        print('Here is your compound interest calculation:', compound_int)  
    else:
        print('Please enter a valid selection.')

# Second branch for choosing 'bond.'
# Gathers data and puts into bond repayment formula.
# Additional error message for incorrect input.

elif input_1 == 'bond':
    print('You have selected \'bond.\'')
    P = int(input('Value of house:'))
    i = int(input('Interest rate:'))
    n = int(input('Over how many months do you plan to repay the bond?:'))
    repayment = (i/100/12 * P)/(1 - (1 + i/100/12)**(-n))
    print('You will have to repay the following each month:', repayment)
else:
    print('Oops! Please enter either investment or bond.')
    input_1 = input('Enter your selection').lower()