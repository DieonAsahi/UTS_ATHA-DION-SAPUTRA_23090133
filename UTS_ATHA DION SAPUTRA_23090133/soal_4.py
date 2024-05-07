def hitung_bmi(Nilai_BMI,berat_badan,tinggi_badan):
    Nilai_BMI = berat_badan / tinggi_badan
    return Nilai_BMI

def main():
    if Nilai_BMI <= 18.5:
        kategori = "berat badan kurang"
    elif 18.5 <= Nilai_BMI < 24.9 :
        kategori = "berat badan normal"
    elif 25 <= Nilai_BMI < 29.9 :
        kategori = "kelebihan berat badan"
    else :
        kategori = "obesitas"

    berat_badan = float(input("masukan berat badan = "))
    tinggi_badan = float(input("masukan tinggi badan = "))

    
    BMI = hitung_bmi(Nilai_BMI,berat_badan,tinggoi_badan)
    print("berat badan = ",berat_badan)
    print("tinggi badan = ",tinggi_badan)
    print("nilai BMI anda = ",Nilai_BMI)
    print("kategori BMI = ",kategori)

if __name__ == "__main__":
    main()
