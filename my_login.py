user = [
    {
        'username' : 'user01',
        'password' : 'abc123'
    }
]
batasU = 0
batasP = 0
status = False

print('', '{:-^85s}'.format('Selamat Datang'), sep='\n')
while batasU <= 3:
    a = input('Silahkan Masukkan Username Anda : ')
    for i in user:
        if a == i['username']:
            while batasP <= 2:
                b = input('Silahkan Memasukkan Password Anda : ')
                for j in i:
                    if b == i['password']:
                        print('{:-^85}'.format('Selamat Anda Telah Login'))
                        status = True
                        break
                    else:
                        print('{:-^85}'.format('Password Salah'))
                        batasP += 1
                        break
        else:
            print('{:-^85}'.format('Username Salah'))
            batasU += 1
    if batasP > 2:
        print('{:-^85}'.format('Anda Salah Memasukkan Password Sebanyak 3 Kali, Program Ditutup'))
        break
    elif status == True:
        break
    elif batasU > 2:
        print('{:-^85}'.format('Anda Salah Memasukkan Usename Sebanyak 3 Kali, Program Ditutup'))
