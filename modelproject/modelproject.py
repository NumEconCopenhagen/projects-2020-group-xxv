def Y_t(D,K,A,L,E,a,b,e):
    return D*(K**a)*((A*L)**b)*(E**e)
def D_t(R,R_0,phi):
    return (R/R_0)**phi
def A_t1(A,g):
    return A*(1+g)
def L_t1(L,n):
    return L*(1+n)
def K_t1(s,Y,d,K):
    return s*Y+(1-d)*K
def R_t1(R,E):
    return R-E
def E_t(sE,R):
    return sE*R    