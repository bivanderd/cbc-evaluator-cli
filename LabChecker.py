print("Gunakan (.) untuk memisahkan ribuan")
Hb = float(input("Masukkan nilai Hb: "))
WBC = float(input("Masukkan nilai Leukosit: "))
Platelet = float(input("Masukkan nilai Trombosit: "))

if Hb < 13.5:
    print("Anemia Ringan")
elif Hb > 16.6 :
    print ("Hb Tinggi")

else:
    print ("Normal")

if WBC < 4.500:
    print("Leukopenia")
elif WBC > 11.000 :
    print ("Leukositosis")
else:
    print ("Normal")

if Platelet < 150.000:
    print("Trombositopenia")
elif Platelet > 450.000 :
    print ("Trombositosis")
else:
    print ("Normal")