import random

def lanzar_dado(probabilidad=0.16):
    numero = random.random()  # Genera un número aleatorio entre 0 y 1
    if numero < probabilidad:
        # La probabilidad de que caiga un número es probabilidad
        # Simulamos 6 caras del dado
        return random.randint(1, 6)
    else:
        # La probabilidad de que no caiga un número es (1 - probabilidad)
        # En este caso, devolvemos None para indicar un lanzamiento no válido
        return

def lanzar_dos_dados():
    dado1 = lanzar_dado()
    dado2 = lanzar_dado()
    # Verificar si alguno de los dados es None (es decir, no válido)
    if dado1 is None or dado2 is None:
        # Si uno de los dados es None, volvemos a lanzar ambos dados
        return lanzar_dos_dados()
    else:
        # Si ambos dados son válidos, devolvemos los resultados
        return dado1, dado2
    
def lanzar_dado_trucado(probabilidades_trucadas):
    numero = random.random()  # Genera un número aleatorio entre 0 y 1
    acumulado = 0
    for i, probabilidad in enumerate(probabilidades_trucadas):
        acumulado += probabilidad
        if numero < acumulado:
            return i + 1  # Sumamos 1 porque los índices comienzan desde 0
    return

def lanzar_dos_dados_trucados(probabilidades_dado1_trucado, probabilidades_dado2_trucado):
    dado1 = lanzar_dado_trucado(probabilidades_dado1_trucado)
    dado2 = lanzar_dado_trucado(probabilidades_dado2_trucado)
    return dado1, dado2

def main():
    probabilidades_dado1_trucado = [0.06, 0.06, 0.7, 0.06, 0.06, 0.06]  # Probabilidades modificadas para el primer dado
    probabilidades_dado2_trucado = [0.06, 0.06, 0.06, 0.7, 0.06, 0.06]  # Probabilidades modificadas para el segundo dado

    print("Dados normales")
    for i in range(10):  # Repetir el proceso 10 veces
        dado1, dado2 = lanzar_dos_dados()
        suma = dado1 + dado2
        print(f"Tirada {i+1}: |Dado 1 = {dado1}| |Dado 2 = {dado2}| |Suma = {suma}|")

    print('')
    print("Tirada de dados trucados")
    for i in range(10):  # Repetir el proceso 10 veces
        dado1_trucado, dado2_trucado = lanzar_dos_dados_trucados(probabilidades_dado1_trucado, probabilidades_dado2_trucado)
        suma_trucada = dado1_trucado + dado2_trucado
        print(f"Tirada {i+1}: |Dado 1 = {dado1_trucado}| |Dado 2 = {dado2_trucado}| |Suma = {suma_trucada}|")

if __name__ == "__main__":
    main()
