# ini merupakan hasil yang dikuti
print("Welcome to the rollercoaster!")
height = int(input("What is your height? "))
bill = 0 # ini memberikan variabel kosong yang nanti akan di isi seiring waktu

if height >= 160:
    print("Come In and wellcome")
    old = int(input("How old are you? "))
    if old < 12: # jika umur nya dibawah 12 maka eksekusi variabel dan print $5
        bill = 5
        print("$5")
    elif old <= 18: # jika umur nya 12 - 18 maka eksekusi variabel dan print $7
        bill = 7
        print("$7")
    else: # selain dari umur 12 dan 18 maka eksekusi variabel dan print $12
        bill = 12
        print("$12")
    photo = input("How many photos do you like? y/n")
    if photo == "y": # jika memilih y maka eksekusi
        bill += 3 # variabel bill di ambil dari umur berapa dan di beri biaya berapa lalu tambahkan dengan 3
    print("$" + str(bill))

    pay = int(input("How much do you pay? $")) # ubah input menjadi int
    if pay >= bill: # jika input int melebihi bill maka eksekusi
        pay -= bill # pembayaran input int di kurang dengan bill keseluruhan
    print(f"Here's your change ${pay}")
    print("Have fun playing")
else:
    print("See You later")
    
# merupakan sebuah program rollercoaster sederhana