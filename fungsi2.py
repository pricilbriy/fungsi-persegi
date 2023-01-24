#MEMBUAT VARIABEL GLOBAL
nama = "python"
versi = "1.0.0"

def hel():
    #variabellokal
    nama = "c#"
    versi = "1.0.2"
    #akses variabel lokal
    print("nama : %s" % nama)
    print("versi : %s" % versi)

#akses variabel global
print("nama : %s" % nama)
print("versi : %s" % versi)

#memanggil fungsi help()
help()