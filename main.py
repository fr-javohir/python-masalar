'''
1. Foydalanuvchi a sonini kiritsin. Siz u sonni 3 ning biron darajasimi yo’qmi aniqlang.
Masalan: 81
Natija: “Kiritilgan son 3 ning darajasi”
'''
shart=True
a=int(input('a = '))
son=a
while shart and a !=0:
    if a == 1:
        print(f'{son} 3 ning darajasi')
        shart=False
    elif a % 3 == 0:
        a//=3
    elif a % 3 !=0:
        print(f'{son} 3 ning darajasi emas')
        shart=False 
'''
3. Foydalanuvchidan butun son input oling. Son 0 dan kattaligi davomida sonni ekranga chiqaring (0 dan katta bo’lsa yana input olaversin), 0 dan kichkina  son kiritilganda while loop to’xtasin.
'''
shart2=True
while shart2:    
    a2=int(input('a = '))
    if a2<0:
        shart2=False

