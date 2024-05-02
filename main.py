from calculadora import Calculadora
from comodo import Comodo

calc = Calculadora()


comodo = Comodo(
    input('qual a largura do comodo? '),
    input('qual a profundidade do comodo?')
)

#calc.area_paredes: float = 2 * (largura + profundidade) * altura

print( "a area das paredes é:",
      calc.calcular_area_paredes(
          comodo)
      )

#calc.area_teto: float = largura * profundidade

print(
    'A área do teto é:', calc.calcular_area_teto(
        comodo)
)

print(
    ' litragem de tinta necessaria é:',
    calc.calcular_litragem_necessaria()
)