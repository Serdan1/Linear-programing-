from Unidades import Espadachin, Arquero, Jinete

def verificar_oro(swordsmen, bowmen, horsemen):
    """Verifica si la combinación de unidades cumple la restricción de oro."""
    espadachin = Espadachin()
    arquero = Arquero()
    jinete = Jinete()
    total_oro = (swordsmen * espadachin.oro +
                 bowmen * arquero.oro +
                 horsemen * jinete.oro)
    return total_oro <= 600

