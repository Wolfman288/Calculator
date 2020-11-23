def calculate():
    operation = input('''
Skriv in den Matte operatör du vill använda:
+ för addition
- för subtraction
* för multiplication
/ för division
''')

    number_1 = int(input('Skriv in första numret: '))
    number_2 = int(input('Skriv in andra numret: '))

    if operation == '+':
        print('{} + {} = '.format(number_1, number_2))
        print(number_1 + number_2)

    elif operation == '-':
        print('{} - {} = '.format(number_1, number_2))
        print(number_1 - number_2)

    elif operation == '*':
        print('{} * {} = '.format(number_1, number_2))
        print(number_1 * number_2)

    elif operation == '/':
        print('{} / {} = '.format(number_1, number_2))
        print(number_1 / number_2)

    else:
        print('Du har inte skrivit in rätt operatör, Kör programmet igen för att försöka igen.')

    
    again()

def again():
    calc_again = input('''
Vill du använda mig igen?
Skriv J för JA eller N för NEJ.
''')

    if calc_again.upper() == 'J':
        calculate()
    elif calc_again.upper() == 'N':
        print('Ses någon annan gång! :D')
    else:
        again()

calculate()