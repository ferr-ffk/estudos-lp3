print('se isso aparecer é pq funciona kakakaka')

# como importar funções e variáveis de outro arquivo (módulo)

# importa tudo separado
# from matematica import *

# importa uma função ou mais funções em específico (nesse caso somar)
# from matematica import somar, PI

# importa tudo como membros de um objeto matematica
# import matematica

from matematica import *

soma_de_dois_numeros = somar(12, 14)

# named import
# from matematica import PI as PI_MAT

# importar módulos em pacotes
from estatistica.descritiva import media
# from [pacote].[modulo] import [função]

print(media([1, 2, 3, 4]))

# para importar modulos do diretorio atual
# from .[modulo] import *
# (o ponto é opcional)

# para importar modeulos de um diretorio superior
# from ..[modulo] import *