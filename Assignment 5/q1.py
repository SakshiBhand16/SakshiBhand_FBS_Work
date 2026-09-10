userid = 'admin'
password = '1234'
for i in range(1,4):
    uid = input('enter the userid:')
    passw = input('enter pass:')

    if(userid==uid and password==passw):
        print('login succesfully')
        break

    else:
        print('incorrect userid and password')

else:
    print('3 attempt complete')