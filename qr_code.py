import qrcode
import time

def makeQr(input): 
    img = qrcode.make(input)
    print('Qr Code Generating!!')
    time.sleep(2)
    img.save('qrcode.jpg')
    print('Qr Code has been Successfully Generated!!')
    print('Run the Code Again to Generate Again')

user_input = input('Provide a Link: ')
check = input('Are you Sure you want to make a Qr Code for Link: ' + user_input + '?? y or n: ')


if(check == 'y'): 
    makeQr(user_input)

elif(check == 'n'): 
    print('Alright!!')
    time.sleep(5)
else: 
    print('Something Went Wrong pls try again!!')



