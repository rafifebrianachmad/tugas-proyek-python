def menu():
	import os
	os.system("CLS")
	print("|||||| |||||| ||  || |||||| ||||||")
	print("  ||   ||     || ||  ||         ||")
	print("  ||   |||||| ||||   |||||     ||")
	print("  ||   ||     || ||      ||   ||")
	print("  ||   |||||| ||  || |||||   ||")  
	print("================================")
	print("|        SELAMAT DATANG        |")
	print("|   GERBANG TOL SENTUL BARAT   |")
	print("================================")
	print("|*********Daftar Menu**********|")
	print("=================================")
	print("|1. Melihat riwayat kendaraan---|")
	print("|2. Menambah data kendaraan-----|")
	print("|3. Informasi tarif-------------|")
	print("|4. Membuka gerbang tol---------|")
	print("|5. Mencari data antrian gerbang|")
	print("|6. Keluar dari program---------|")
	print("=================================") 
	pil= int(input("Masukan no menu yang dipilih:"))
	pilihmenu(pil)
#----------------------------------------------------
def pilihmenu(p):
	if p==1:
		lihatdata()
	elif p==2:
		tambahdata()
	elif p==3:
		informasibiaya()
	elif p==4:
		membukagerbang()
	elif p==5:
		caridata()
	elif p==6:
		print("Keluar dari program")
		print("Terimakasih")
#---------------------------------------------------
def lihatdata():
	print("=====================================================")
	print("|Anda berada pada menu menampilkan riwayat kendaraan|")
	print("=====================================================")
	f = open("datakendaraan.txt","r")
	isi = f.readlines()
	isi.sort()
	if len(isi)==0:
		print("Data masih kosong")
	else:
		i = 1
		for x in isi:
			pecah= x.split(",")
			print("========================================")
			print("|"+str(i)+". ", end="")
			print("|Nomor Kendaraan\t\t:"+pecah[0]+"\n"+"|   |Jenis Kendaraan\t\t:"+pecah[1]+"\n"+"|   |Golongan Kendaraan\t\t:"+pecah[2]+"\n"+"|   |Waktu registrasi\t\t:"+pecah[3],end="")
			i += 1
	print("========================================")
	print("\ntekan [enter] untuk kembali ke menu")
	f.close()
	input()
	menu()
#---------------------------------------------------
def tambahdata():
	print("==========================================")
	print("|Anda sedang berada pada menu tambah data|")
	print("==========================================")
	print("Silahkan masukan data sesuai format yang ditentukan")
	kendaraan=Queue()
	gerbang=[]
	
	no= input("Nomor Kendaraan: ")
	j= input("Masukan Jenis Kendaraan: ")
	n= input("Masukan Golongan Kendaraan: ")
	tgl= input("Masukan Waktu Kendaraan masuk: ")
	gerbang.append(no)
	kendaraan.enqueue(gerbang)
	f=open("datakendaraan.txt","a")
	f.writelines([no+",",j+","+n+","+tgl+"\n"])
	f.close()
	print("======================================")
	print ("Ketik Y untuk menambah data kendaraan") 
	print ("Ketik N untuk kembali ke menu utama ") 
	print("======================================")
	c= input("Ingin menambah data kendaraan lagi? [Y/N]  ")
	if c == ("Y"):
		tambahdata()
	elif c == ("N"):
		menu()
#--------------------------------------------------
def informasibiaya():
    import os
    os.system("CLS")
    print("\nAnda Berada Pada Menu Golongan Tarif Tol")
    
    print("=============================================================== ")
    print("| Gol. Kendaraan  | Jenis Kendaraan          | Tarif Kendaraan |")
    print("=============================================================== ")
    print("| Golongan 1      | Sedan, Bus, Jip, Pick Up | Rp 14.000,-     |")
    print("| Golongan 2      | Truk 2 Gardan            | Rp 21.000,-     |")
    print("| Golongan 3      | Truk 3 Gardan            | Rp 21.000,-     |")
    print("| Golongan 4      | Truk 4 Gardan            | Rp 28.000,-     |")
    print("| Golongan 5      | Truk 5 Gardan            | Rp 28.000,-     |")
    print("===============================================================")
    print("\nTekan [ENTER] untuk registrasi!")
    input()
    datatarif()
#------------------------------------------------------------------------------
def datatarif() :
    import os
    os.system("CLS")
    print("Anda Berada Pada Menu Menambah Kendaraan")
    print("Masukkan Detail Kendaraan Anda!")
    bukadata = open("datakendaraan.txt","a")
    print("\nMasukkan Golongan Kendaraan Anda! [1,2,3,4,5]")
    golinput = input(" : ")
    if golinput == "1":
        print("\nGolongan 1 mempunyai tarif sebesar Rp 14.000,-")
    elif golinput == "2":
        print("\nGolongan 2 mempunyai tarif sebesar Rp 21.000,-")
    elif golinput == "3":
        print("\nGolongan 3 mempunyai tarif sebesar Rp 21.000,-")
    elif golinput == "4":
        print("\nGolongan 4 mempunyai tarif sebesar Rp 28.000,-")
    elif golinput == "5":
        print("\nGolongan 5 mempunyai tarif sebesar Rp 28.000,-")
    bukadata.close()

    print("\nTekan [ENTER] untuk kembali ke menu!")
    input()
    menu()
#------------------------------------------------------------------------------
def caridata():
	print("========================================")
	print("|Anda sedang berada pada menu cari data|")
	print("========================================")
	nama=input("\nMasukan Nomor kendaraan yang dicari:")
	f = open("datakendaraan.txt","r")
	cd=[]
	isi = f.readlines()
	if len(isi)==0: 
		print("Data masih kosong") 
	else:
		for x in isi:
			pecah = x.split(",")
			if nama==pecah[0]:
				cd=pecah
	if cd:
		print("Data yang anda cari adalah ")
		print("Nomor Kendaraan\t\t:"+cd[0]+"\nJenis Kendaraan\t\t:"+cd[1]+"\nGolongan Kendaraan\t\t:"+cd[2]+"\nWaktu Registrasi\t:"+cd[3])
	else:
		print("\nData tidak ditemukan\n")
	f.close()
	print("==================================")
	print ("Ketik Y untuk mencari data") 
	print ("Ketik N untuk kembali ke menu utama ")
	print("==================================") 
	c=input("Ingin mencari data kendaraan lagi? [Y/N]  ")
	if c == ("Y"):
		caridata()
	elif c == ("N"):
		menu()
#--------------------------------------------------
def membukagerbang():
	print("=======================================")
	print("|Anda berada pada menu membuka gerbang|")
	print("=======================================")
	membuka=input("Tekan [Enter] untuk membuka gerbang")
	f=open("datakendaraan.txt","r")
	kendaraan=Queue()
	isi=f.readlines()
	for x in isi:
		kendaraan.enqueue(x)
	if len(kendaraan.items)==1:
		print("Tidak ada kendaraan yang masuk")
	else:
		buka=kendaraan.dequeue()
		k=0
		for y in isi:
			if y==buka:
				y=membuka
				isi[k]=y
	f.close()
	q=len(kendaraan.items)-1
	buka=kendaraan.items[q]
	i = 1
	for a in kendaraan.items:
		masa= a.split(",")
		print("========================================")
		print("Kendaraan selanjutnya")
		print("|"+str(i)+". ", end="")
		print("|Nomor Kendaraan\t\t:"+masa[0]+"\n"+"|   |Jenis Kendaraan\t\t:"+masa[1]+"\n"+"|   |Golongan Kendaraan\t:"+masa[2]+"\n"+"|   |Waktu registrasi\t\t:"+masa[3],end="")
		i += 1
	f=open("datakendaraan.txt","w")
	isi=f.writelines(isi)
	f.close()

	print("=====================================")
	print("Ketik Y untuk membuka kembali gerbang") 
	print("Ketik N untuk kembali ke menu utama ") 
	print("=====================================")
	c= input("Ingin membuka kembali gerbang? [Y/N]  ")
	if c == ("Y"):
		membukagerbang()
	elif c == ("N"):
		menu()
#--------------------------------------------------
import random
import sys
import time
def mengetik(s):
    for c in s + '\n':
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(random.random() * 0.1)
mengetik('Hallo para pengguna jalan TOL\nSelamat Datang di menu Gerbang Tol Sentul Barat\n............LOADING............')
#--------------------------------------------------
class Queue:
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def enqueue(self, item):
        self.items.insert(0,item)

    def dequeue(self):
        return self.items.pop()

  
#--------------------------------------------------
menu()
