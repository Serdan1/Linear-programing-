# Linear-programing-

https://github.com/Serdan1/Linear-programing-.git

# Linear Programming Project (Rama main)

Este proyecto resuelve un problema de optimización lineal para maximizar el poder de un ejército compuesto por espadachines, arqueros, y jinetes, utilizando la biblioteca OR-Tools de Google. Se implementa en Python con el solver GLOP para programación lineal.

## Problema
- **Objetivo**: Maximizar el poder: `70*swordsmen + 95*bowmen + 230*horsemen`.
- **Restricciones**:
  - Comida: `60*swordsmen + 80*bowmen + 140*horsemen <= 1200`
  - Madera: `20*swordsmen + 10*bowmen <= 800`
  - Oro: `40*bowmen + 100*horsemen <= 600`
  - Variables: `swordsmen`, `bowmen`, `horsemen` son enteros no negativos.
- **Solución óptima**: Aproximadamente 6 espadachines, 0 arqueros, 6 jinetes, con poder = 1800 (puede mostrar valores fraccionarios debido al solver GLOP).

## Codigo
main.py: Implementa el problema con OR-Tools (pywraplp, solver GLOP). Produce la solución esperada (6 espadachines, 0 arqueros, 6 jinetes, poder = 1800), aunque con valores fraccionarios debido a GLOP (como 6.0000000000000036).

requirements.txt: Incluye ortools==9.11.4210, PuLP==2.9.0, Pyomo==6.8.0, SciPy==1.14.1, aunque 



## Estructura del proyecto
El proyecto utiliza una estructura simple, ya que OR-Tools maneja la optimización. **Por favor, copia el siguiente diagrama para incluirlo en la documentación**:

```mermaid
graph TD
    A[Linear-programing] --> B[main.py]
    A --> C[README.md]
    A --> D[requirements.txt]

    B -->|Lógica con OR-Tools| A
    C -->|Documentación| A
    D -->|Dependencias| A
