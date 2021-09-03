############################################################################################################
################################ NumPy: arrays e processamento vetorizado ##################################
############################################################################################################

##NumPy?
##ndarrays?
##Wtf é isso?

##Sem mais delongas, o que é o NumPy e esse tal de ndarray?

##Numerical Python ou simplesmente NumPy, é um pacote Python para processamento númerico em arrays. Alguns dos
##principais recursos do NumPy é o ndarray e as operações matemáticas que podem ser feitas nesse tipo de array.
##O ndarray, basicamente, é um array multidimensional (estilo Interestelar) no qual pode ser realizado diversas
##operações matemáticas de forma eficiente e sem a necessidade de criar laços e funções para percorrer o array.
##Essas ferramentas matemáticas são oferecidas pelo pacote NumPy, bem como as ferramentas de leitura e escrita
##de dados em array para trabalhar com arquivos em memória. Os recursos matemáticos são voltados para a álgebra
##linear, geração de números pseudoaleatórios e transformadas de Fourier.
##NumPy é uma biblioteca bem ampla e devido a isso, neste arquivo, será coberto apenas o basicão do NumPy.

##Criando ndarrays
##Tipos de dados para ndarrays
##Aritmética com arrays NumPy
##Indexação básica e fatiamento
##Indexando com fatias
##Indexação sofisticada
##Transposição de arrays e troca de eixos
##Funções universais
##Programação orientada a arrays
##Lógica condicional como operações de array
##Métodos matemáticos e estatísticos
##Métodos para arrays booleanos
##Ordenação
##Unicidade e lógica de conjuntos
##Entrada e saída de arquivos com arrays
##Álgebra linear
##Geração de números pseudoaleatórios

import numpy as np

##### Criando ndarrays #####

#data = np.random.randn(2, 3)

#print('Numeros pseudoaleatorios')
#print(data)

#print('Multiplicacao (por 10) dos numeros pseudoaleatorios')
#print(data * 10)

#print('Soma dos nomeros pseudoaleatorios')
#print(data + data)

##Observe que as operações são aplicadas a todo o conjunto de dados no ndarray
##É importante resaltar que o ndarray é (e deve ser) composto por dados homogeneos, apenas inteiros
##ou apenas reais etc.

##A seguir, é apresentado algumas funções para a criação de arrays com NumPy.

##array()
##A função array() converte os dados de uma sequência em um ndarray.

#sequencia = [7, 9, 15, 1, 32]

#array = np.array(sequencia)

#print(type(array), array) ##Com base na sequência de entrada o np.array() cria um novo ndarray, inferindo qual deve ser o tipo de dado para o novo ndarray

##zeros() ou ones()
##As funções zeros() ou ones() cria um ndarray de 0s ou 1s, sendo necessário informar como parâmeto o tamanho e formato (dimensões).

#zeros = np.zeros((3, 3))
#print(zeros)

#uns = np.ones((3, 3))
#xprint(uns)

##Tipos de dados para ndarrays
