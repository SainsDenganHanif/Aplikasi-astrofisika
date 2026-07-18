import math as ma
import Modul_Global

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

