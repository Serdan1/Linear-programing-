from Recursos import verificar_comida, verificar_madera, verificar_oro
from Poder import calcular_poder

def main():
    max_poder = 0
    mejor_combinacion = (0, 0, 0)  # (swordsmen, bowmen, horsemen)

    # Iterar sobre combinaciones de unidades
    for swordsmen in range(21):  # Rango de 0 a 20
        for bowmen in range(21):
            for horsemen in range(21):
                # Verificar restricciones
                if (verificar_comida(swordsmen, bowmen, horsemen) and
                    verificar_madera(swordsmen, bowmen, horsemen) and
                    verificar_oro(swordsmen, bowmen, horsemen)):
                    # Calcular poder
                    poder = calcular_poder(swordsmen, bowmen, horsemen)
                    if poder > max_poder:
                        max_poder = poder
                        mejor_combinacion = (swordsmen, bowmen, horsemen)

    # Mostrar resultados
    print("================= Solución =================")
    print(f"Poder óptimo = {max_poder} 💪")
    print("Ejército:")
    print(f" - 🗡️ Espadachines = {mejor_combinacion[0]}")
    print(f" - 🏹 Arqueros = {mejor_combinacion[1]}")
    print(f" - 🐎 Jinetes = {mejor_combinacion[2]}")

if __name__ == "__main__":
    main()

    