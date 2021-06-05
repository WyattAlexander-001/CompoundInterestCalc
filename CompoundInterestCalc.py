'''
Compound Interest Calc
'''

def main():
    years = int(input('Enter the amount of years you want to invest: '))
    principal = float(input('Enter money in account currently: $'))
    monthly_cont = float(input('Enter monthly contribution: $'))
    yearly_cont = monthly_cont * 12
    interest = 1 + int(input('Enter interest: %'))/100
    
    i = 0
    
    while i < years:
        principal = (principal + yearly_cont) * interest
        i = i + 1
        print(f'Total on year:{i}, is ${round(principal,2)}')
    
    x = input('Try again? Type yes or no').lower()
    if x == 'yes':
        main()
    else:
        print('Done')

main()