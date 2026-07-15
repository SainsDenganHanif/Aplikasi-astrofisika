def Aproksimasi_Kecerahan_Sederhana(M):
    """
    Menghitung perkiraan sederhana Kecerahan bintang dalam Lsol dari massanya dalam Msol
    INPUT : 
    M : float(0.08<M<200)

    Output
    L : float
    """
    if 0.08 <= M < 0.43:
        L = 0.23*M**2.3
    elif 0.43 <= M < 2:
        L = M**4
    elif 2 <= M < 55:
        L = 1.4*M**3.5
    elif 55 <= M:
        L = 32000*M

    return L