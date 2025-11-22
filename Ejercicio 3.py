def aproximar_pi_leibniz(n_terms):
    """Aproxima pi usando la serie de Leibniz: pi/4 = ∑_{k=0}^∞ ((-1)^k)/(2k+1)"""
    suma = 0.0
    for k in range(n_terms):
        termino = ((-1)**k) / (2*k + 1)
        suma += termino
    return 4.0 * suma

n = int(input("Pon el número de términos para la aproximación: "))
aprox = aproximar_pi_leibniz(n)
print(f"Aproximación de pi con {n} términos: {aprox}")
