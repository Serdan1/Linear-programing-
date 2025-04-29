from Unidades import Espadachin, Arquero, Jinete

def calcular_poder(swordsmen, bowmen, horsemen):
    """Calcula el poder total de una combinación de unidades."""
    espadachin = Espadachin()
    arquero = Arquero()
    jinete = Jinete()
    total_poder = (swordsmen * espadachin.poder +
                   bowmen * arquero.poder +
                   horsemen * jinete.poder)
    return total_poder

