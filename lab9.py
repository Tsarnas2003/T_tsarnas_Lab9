def encode(n):
    for i in range(len(n)):
        if int(n[i]) in range(0, 6):
            n = n[:i] + str(int(n[i]) + 3) + n[i+1:]
        elif int(n[i]) == 7:
            n = n[:i] + '0' + n[i+1:]
        elif int(n[i]) == 8:
            n = n[:i] + '1' + n[i+1:]
        elif int(n[i]) == 9:
            n = n[:i] + '2' + n[i+1:]
    return n


def decode(n):
    for i in range(len(n)):
        if int(n[i]) in range(3, 9):
            n = n[:i] + str(int(n[i]) - 3) + n[i + 1:]
        elif int(n[i]) == 0:
            n = n[:i] + '7' + n[i + 1:]
        elif int(n[i]) == 1:
            n = n[:i] + '8' + n[i + 1:]
        elif int(n[i]) == 2:
            n = n[:i] + '9' + n[i + 1:]
    return n


loop = True
while loop:
    print('\nMenu\n'
          '-------------\n'
          '1. Encode\n'
          '2. Decode\n'
          '3. Quit\n')
    menu = int(input('Please enter an option: '))
    if menu == 1:
        encoded_password = encode(str(input('Please enter your password to encode: ')))
        print('Your password has been encoded and stored!')
    elif menu == 2:
        try:
            print(f'The encoded password is {encoded_password}, '
                  f'and the original password is {decode(encoded_password)}.')
        except:
            print('You have not encoded a password yet.')
    elif menu == 3:
        loop = False
