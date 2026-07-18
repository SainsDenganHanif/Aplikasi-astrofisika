import math as ma
import Modul_Global

#region Kecerahan

def Perkiraan_kecerahan_sederhana(M):
    """
    Menghitung perkiraan sederhana Kecerahan bintang dalam Lsol dari massanya dalam Msol
    INPUT : 
    M : float(0.08<M<200)

    Output
    L : float

    Berdasarkan https://worldbuildingpasta.blogspot.com/2019/06/an-apple-pie-f
    rom-scratch-part-ii-stars.html#simpleapproximations
    """

    if Modul_Global.Pengecek_error(M,0.08,200) == False:
        return

    if 0.08 <= M < 0.43:
        return 0.23*M**2.3
    elif 0.43 <= M < 2:
        return M**4
    elif 2 <= M < 55:
        return 1.4*M**3.5
    elif 55 <= M:
        return 32000*M

def Perkiraan_kecerahan_Eker2018(M):
    """
    Menghitung perkiraan sederhana Kecerahan bintang dalam Lsol dari massanya dalam Msol
    INPUT : 
    M : float(0.179<M<31)

    Output
    L : float

    Berdasarkan https://academic.oup.com/mnras/article/479/4/5491/5056185
    """
    if Modul_Global.Pengecek_error(M,0.179,31) == False:
        return
        
    if 0.179 < M <= 0.45:
        return 10**(2.028*ma.log10(M)-0.976)
    if 0.45 < M <= 0.72:
        return 10**(4.572*ma.log10(M)-0.102)
    if 0.72 < M <= 1.05:
        return 10**(5.743*ma.log10(M)-0.007)
    if 1.05 < M <= 2.4:
        return 10**(4.329*ma.log10(M)+0.010)
    if 2.4 < M <= 7:
        return 10**(3.967*ma.log10(M)+0.093)
    if 7 < M <= 31:
        return 10**(2.865*ma.log10(M)+1.105)

def Perkiraan_kecerahan_Manfred2018(M):
    """
    Menghitung perkiraan sederhana Kecerahan bintang dalam Lsol dari massanya dalam Msol
    INPUT : 
    M : float (0.2<M<0.85)

    Output
    L : float

    Berdasarkan https://iopscience.iop.org/article/10.3847/2515-5172/aaaa67
    """
    if Modul_Global.Pengecek_error(M,0.2,0.85) == False:
        return
    
    return M ** (-141.7*M**4 + 232.4*M**3 - 129.1*M**2 + 33.29*M + 0.215)

#endregion

#region radius

def Perkiraan_Radius_Eker2018(M):
    """
    Menghitung perkiraan sederhana Radius bintang dalam Rsol dari massanya dalam Msol
    INPUT : 
    M : float (0.179<M<1.5)

    Output
    R : float

    Berdasarkan https://academic.oup.com/mnras/article/479/4/5491/5056185
    """
    if Modul_Global.Pengecek_error(M,0.179,1.5) == False:
        return
    
    return 0.438*M**2 + 0.479*M + 0.075

def Perkiraan_Radius_Demircan1990(M):
    """
    Menghitung perkiraan sederhana Radius bintang dalam Rsol dari massanya dalam Msol
    INPUT : 
    M : float (0.08<M<200)

    Output
    R : float

    Berdasarkan https://ui.adsabs.harvard.edu/scan/manifest/1991Ap&SS.181..313D
    """

    if Modul_Global.Pengecek_error(M,0.08,200) == False:
        return

    if M < 1.66:
        return 10**(0.026+0.945*ma.log10(M))

    if M >= 1.66:
        return 10**(0.124+0.555*ma.log10(M))
#endregion

#region suhu

def Perkiraan_Suhu_Eker2018(M):
    """
    Menghitung perkiraan sederhana suhu efektif bintang dalam kelvin dari massanya dalam Msol
    INPUT : 
    M : float (1.5<M<31)

    Output
    R : float

    Berdasarkan https://academic.oup.com/mnras/article/479/4/5491/5056185
    """
    if Modul_Global.Pengecek_error(M,1.5,31) == False:
        return
    
    return 10**(-0.170 * ma.log10(M)**2 + 0.888*ma.log10(M) + 3.671)

#endregion

def Model_gabungan(M):
    """
    Menghitung Kecerahan, Radius dan suhu dari massa bintang

    INPUT : 
    M : float (0.08<M<200)

    Output
    {   "L" : Kecerahan,
        "R" : Jari-jari,
        "T" : Suhu}

    Model yang digunakan
    Kecerhanan : 
        Untuk 0.2 < M < 0.85 (Manfred)
        https://iopscience.iop.org/article/10.3847/2515-5172/aaaa67

        Untuk 0.179 < M < 31 (Eker)
        https://academic.oup.com/mnras/article/479/4/5491/5056185

        Untuk 0.08 < M < 200 (Sederhana)
        https://worldbuildingpasta.blogspot.com/2019/06/an-apple-pie-from-scratch-part-ii-stars.html#simpleapproximations

    Radius : 
        Untuk 1.5 < M < 31 Dari aturan stefan boltzmann

        Untuk 0.179 < M < 1.5 Dari rumus Eker
        https://academic.oup.com/mnras/article/479/4/5491/5056185

        Untuk 0.08 < M < 200 Demircan
        https://ui.adsabs.harvard.edu/scan/manifest/1991Ap&SS.181..313D

    Temperatur : 
        Untuk 1.5 < M < 31 Dari rumus Eker

        Untuk 0.179 < M < 1.5 Dari aturan steffan boltzmann

        Untuk 0.08 < M < 200 Demircan        
    """

    if Modul_Global.Pengecek_error(M,1.5,31) == False:
        return
    
    #Menghitung Kecerahan
    if 0.2 < M < 0.85:
        L = Perkiraan_kecerahan_Manfred2018(M)
    elif 0.179 < M < 31:
        L = Perkiraan_kecerahan_Eker2018(M)
    elif 0.08 <= M < 200:
        L = Perkiraan_kecerahan_sederhana(M)

    if 0.179 < M < 31:
        if M >= 1.5:
            T = Perkiraan_Suhu_Eker2018(M)
            R = Modul_Global.R_dari_L_dan_T(L,T)
        elif M < 1.5:
            R = Perkiraan_Radius_Eker2018(M)
            T = Modul_Global.T_dari_L_dan_R(L,R)
    elif 0.08 <= M < 200:
        R = Perkiraan_Radius_Demircan1990(M)
        T = Modul_Global.T_dari_L_dan_R(L,R)

    return {
        "L" : L,
        "R" : R,
        "T" : T
    }

print(Model_gabungan("abc"))