print(r'''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\ ` . "-._ /_______________|_______
|                   | |o ;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("selamat datang di penjajahan kapal bajaklaut.")
print("Your mission is to find the treasure.")
pilihan1 = input('Kita akan pergi kemana kapten? "kanan" atau "kiri"?\n').lower()


if pilihan1 == 'kanan':
    print("Mari kekanan aku melihat pulau disana")
    attack = input('kapten ada serangan mendadak!!. kita serang "meriam" atau "jajah"?\n').lower()
    if attack == "jajah":
        print('Hore kita menang kapten')
        door = input('Silahkan kapten pintu mana yang akan kapten buka? "tengkorak" , "topi" , "obor"?\n').lower()
        if door == "topi":
            print('Kamu kena tebas')
        elif door == "obor":
            print('Kamu mendapatkan harta karun')
        elif door == "tengkorak":
            print('Kamu kena tembak')
        else:
            print('tidak semuanya harus buka pintu satu-satu')
    else:
        print('Musuhnya terlalu kuat kapten, kita menyerah')
else:
    print('Kita kekiri untuk balik kedermaga, misi kita akan di lanjutkan besok hari')