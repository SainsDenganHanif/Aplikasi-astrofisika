import math as ma

def  Validasi_Input(X,Rb,Ra):
    """
    Sebuah fungsi yang memberi batasan input dan memberi peringatan bila input diluar batasan dan/atau bukan sebuah float
    BENTUK : Pengecek_error(X,Rb,Ra)

    INPUT : 
    X   : Input yang ingin divalidasi
    Rb  : Rentang rendah input 
    Ra  : Rentang atas input

    OUTPUT : 
    True bila input sesuai keinginan
    False bila tidak
    """
    #cek Rb dan Ra
    try: #Error checker didalam error checker💀
        Rb = float(Rb) 
        Ra = float(Ra)  #Coba ubah Rentang jadi float
    except ValueError: #kalau gk bisa
        print("Input yang dimasukkan bukan sebuah angka, tolong masukkan sebuah angka")
        return False
    else: #kalau bisa...
        if Ra <= Rb: #Nah secara matematis bisa gk...
            print("Rentang atas harus lebih besar daripada rentang bawah")
            return False
        else:
            pass #GOOD BOY!

    #Nah baru cek X
    try: 
        X = float(X) #Coba ubah input jadi float
    except ValueError: #kalau gk bisa
        print(f"Input yang dimasukkan bukan sebuah angka, anda memasukkan {type(X)}. Tolong masukkan sebuah angka")
        return False
    else:
        if  Rb <= X <= Ra:  #Masuk gk...
            return True
        else: 
            print(f"Input yang dimasukkan diluar rentang, rentang yang diterima adalah {Rb} - {Ra}, anda memasukkan {X}")
            return False

def R_dari_L_dan_T(L,T):
    return ma.sqrt(L)/(T/5778)**2

def T_dari_L_dan_R(L,R):
    return 5778*ma.sqrt(ma.sqrt(L)/R)