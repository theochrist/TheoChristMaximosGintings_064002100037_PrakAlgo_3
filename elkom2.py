x = int(input("masukkan total belanjaan = "))
y = int(input("masukkan jumlah uang = "))
kembalian = (y-x)
print ("uang kembalian = ", "Rp", kembalian)
uang_pecahan = [100000, 50000, 20000, 10000, 5000, 2000, 1000]
jumlah_pecahan = {}
sisa = kembalian
for pecahan in uang_pecahan:
    if sisa < pecahan : 
        continue
    banyak_pecahan = int(sisa / pecahan)
    sisa = sisa - (pecahan *  banyak_pecahan)
    print ('uang {} sebanyak: {} lembar' .format (pecahan, banyak_pecahan))
    
    