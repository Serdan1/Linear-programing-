from Unidades import Espadachin, Arquero, Jinete

def verificar_comida(swordsmen, bowmen, horsemen):
    """Verifica si la combinación de unidades cumple la restricción de comida."""
    espadachin = Espadachin()
    arquero = Arquero()
    jinete = Jinete()
    total_comida = (swordsmen * espadachin.comida +
                    bowmen * arquero.comida +
                    horsemen * jinete.comida)
    return total_comida <= 1200

