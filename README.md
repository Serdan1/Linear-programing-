# Linear Programming Project

Este proyecto resuelve un problema de optimización lineal para maximizar el poder de un ejército compuesto por espadachines, arqueros, y jinetes, sin usar bibliotecas externas. Se implementa en Python usando un enfoque de fuerza bruta.

## Problema
- **Objetivo**: Maximizar el poder: `70*swordsmen + 95*bowmen + 230*horsemen`.
- **Restricciones**:
  - Comida: `60*swordsmen + 80*bowmen + 140*horsemen <= 1200`
  - Madera: `20*swordsmen + 10*bowmen <= 800`
  - Oro: `40*bowmen + 100*horsemen <= 600`
  - Variables: `swordsmen`, `bowmen`, `horsemen` son enteros no negativos.
- **Solución óptima**: 6 espadachines, 0 arqueros, 6 jinetes, con poder = 1800.


## Codigo
Usa una estructura modular:
Unidades/: Clases Espadachin, Arquero, Jinete con atributos (comida, madera, oro, poder). Soldados.py es un placeholder vacío.

Recursos/: Funciones verificar_comida, verificar_madera, verificar_oro para validar restricciones. recursos.py es un placeholder vacío.

Poder.py: Función calcular_poder para calcular el poder total.

main.py: Fuerza bruta que itera sobre combinaciones y produce la solución esperada (6 espadachines, 0 arqueros, 6 jinetes, poder = 1800).

requirements.txt: Vacío o con un comentario indicando que no se usan bibliotecas.


## Estructura del proyecto
El proyecto está organizado en módulos para mantener la lógica clara y modular. **Por favor, copia el siguiente diagrama para incluirlo en la documentación**:

```mermaid
graph TD
    A[Linear-programing] --> B[Recursos]
    A --> C[Unidades]
    A --> D[Poder.py]
    A --> E[main.py]
    A --> F[README.md]
    A --> G[requirements.txt]

    B --> B1[Comida.py]
    B --> B2[Madera.py]
    B --> B3[Oro.py]
    B --> B4[__init__.py]
    B --> B5[recursos.py]

    C --> C1[Soldados.py]
    C --> C2[__init__.py]
    C --> C3[arqueros.py]
    C --> C4[espadachines.py]
    C --> C5[jinetes.py]

    B1 -->|Verifica comida| B
    B2 -->|Verifica madera| B
    B3 -->|Verifica oro| B
    B4 -->|Importa funciones| B
    B5 -->|Placeholder| B

    C1 -->|Placeholder| C
    C2 -->|Importa clases| C
    C3 -->|Clase Arquero| C
    C4 -->|Clase Espadachin| C
    C5 -->|Clase Jinete| C

    D -->|Calcula poder| A
    E -->|Lógica principal| A
    F -->|Documentación| A
    G -->|Sin bibliotecas| A
