from Unidades import Espadachin, Arquero, Jinete

def verificar_madera(swordsmen, bowmen, horsemen):
    """Verifica si la combinación de unidades cumple la restricción de madera."""
    espadachin = Espadachin()
    arquero = Arquero()
    jinete = Jinete()
    total_madera = (swordsmen * espadachin.madera +
                    bowmen * arquero.madera +
                    horsemen * jinete.madera)
    return total_madera <= 800

    