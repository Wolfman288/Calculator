###Emanuel Näslun###

def calculate():
    operation = input('''
Skriv in den Matte operatör du vill använda:
+ för addition
- för subtraction
* för multiplication
/ för division
''')

    #Dem 2 nummer du vill använda
    number_1 = int(input('Skriv in första numret: '))
    number_2 = int(input('Skriv in andra numret: '))

    #Addition
    if operation == '+':
        print('{} + {} = '.format(number_1, number_2))
        print(number_1 + number_2)

    #Subtraction
    elif operation == '-':
        print('{} - {} = '.format(number_1, number_2))
        print(number_1 - number_2)

    #Multiplication
    elif operation == '*':
        print('{} * {} = '.format(number_1, number_2))
        print(number_1 * number_2)

    #Division
    elif operation == '/':
        print('{} / {} = '.format(number_1, number_2))
        print(number_1 / number_2)

    else:
        print('Du har inte skrivit in rätt operatör, Kör programmet igen för att försöka igen.')

    
    again()
#Om du vill göra igen
def again():
    calc_again = input('''
Vill du använda mig igen?
Skriv J för JA eller N för NEJ.
''')
#Ja eller Nej
    if calc_again.upper() == 'J':
        calculate()
    elif calc_again.upper() == 'N':
        print('Ses någon annan gång! :D')
    else:
        again()

calculate()