import random
import datetime
from customer import Customer

#Fungsi menu
def menu_saldo():
    print('Saldo anda saat ini Rp. ' + str(atm.checkBalance()))

def menu_debet():
    nominal = float(input('Jumlah saldo yang akan diambil: '))
    verify_withdraw = input('Konfirmasi : Anda akan melakukan debet sebesar ? y/n Rp. ' + str(nominal))
    if verify_withdraw == "y":
        print("saldo awal anda adalah Rp. " + str(atm.checkBalance()))
    else:
        print('Transaksi dibatalkan')
        exit()

    if nominal < atm.checkBalance():
        atm.withdrawBalance(nominal)
        print("Transaksi berhasil")
        print("Saldo anda sekarang sebesar Rp. " + str(atm.checkBalance()))    
    else:
        print("Maaf saldo anda kurang untuk melakukan debet")

def menu_tabung():
    nominal = float(input('Jumlah saldo yang akan dimasukkan: '))
    verify_deposit = input('Konfirmasi : Anda akan melakukan deposit sebesar ? y/n Rp. ' + str(nominal))
    if verify_deposit == "y":
        atm.depositBalance(nominal)
        print("Saldo anda sekarang adalah Rp. " + str(atm.checkBalance()))
    else:
        print('Transaksi dibatalkan')
        exit()

def menu_gantiPin():
    pin_lama = int(input('Masukkan pin anda yang lama : '))
    if pin_lama != atm.checkPin():
        print('Pin lama yang anda masukkan salah')
    else:
        pin_baru = int(input('Masukkan pin baru anda : '))
        if pin_baru == atm.checkPin():
            print('Harap ganti dengan pin yang belum pernah anda gunakan')
        else:
            atm.pin = pin_baru
            verify_pin = int(input('Verifikasi pin baru anda : '))
            if verify_pin == atm.checkPin():
                print('Anda berhasil terverifikasi')
            else:
                print('Verifikasi gagal')
                exit()

def menu_keluar():
    print('======== Resi Transaksi ======== ')
    print('No Record : ' + str(random.randrange(100000, 1000000)))
    print('Tanggal & jam: ' + str(datetime.datetime.now()))
    print('Saldo anda saat ini sebesar Rp. ' + str(atm.checkBalance()))
    print('Terimakasih telah menggunakan ATM ini')

atm = Customer(id)

while True:
    id = int(input('Masukkan pin anda: '))    
    trial = 0
    while (id != atm.checkPin() and trial < 3):
        id = int(input('Masukkan pin anda #' + str(trial+1) + ': '))
        trial += 1
        if (trial == 3):
            print('Error 3x salah pin...') 
            exit()
    while True:
        print("Selamat datang")
        print("1. Cek Saldo")
        print("2. Debet")
        print("3. Tabung")
        print("4. Ganti Pin")
        print("5. Keluar")

        select_menu = int(input('Pilih Menu: '))

        if select_menu == 1:
            menu_saldo()
        elif select_menu == 2:
            menu_debet()
        elif select_menu == 3:
            menu_tabung()
        elif select_menu == 4:
            menu_gantiPin()
        elif select_menu == 5:
            menu_keluar()
            exit()
        else:
            print('Maaf menu yang dipilih tidak tersedia')


