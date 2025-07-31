import random

batu = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

kertas = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

gunting = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

print("Selamat Datang digame Batu, Kertas, Gunting")
print('Pilih angka ini untuk main')
print('0 = Batu')
print('1 = Kertas')
print('2 = Gunting')

number = int(input('Masukan angka yang inginkan: '))

r_com = random.randint(0,2)

pilihan = [batu, kertas, gunting]

print('\nKamu Pilih')
print(pilihan[number])
print('\nKomputer Pilih')
print(pilihan[r_com])

if number == r_com:
    print('Seri apakah mau lanjut')
elif number == 0 and r_com == 2:
    print('Hasil: kamu menang')
elif number == 1 and r_com == 0:
    print('Hasil: kamu menang')
elif number == 2 and r_com == 1:
    print('Hasil: kamu menang')
else:
    print("Hasil: Anda Kalah!")

