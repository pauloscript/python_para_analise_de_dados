#####################################################################
########## ESTRUTURA DE DADOS, FUNÇÕES E ARQUIVOS EM PYTHON #########
#####################################################################

############################### TUPLA ###############################

##A tupla é uma sequência imutável, de tamanho fixo, de objetos.
##Entendemos que ao definir uma tupla, os seus elementos e tamanho não podem ser alterados na execução,
##se ela for definida com cinco elementos, sempre tera os cinco elementos.  

#tup = 26, 35, 25, 19, 20

#print(type(tup)) ##A saída será um <class 'tuple'> indicando que a variável é uma tupla.

##Os elementos da tupla podem ser acessados a partir do seu índice, como acontece em outras linguagens (C, Java etc).

#print(tup[3]) ##Lembrando que o índice começa em 0.

##Qualquer sequência pode ser convertida em uma tupla, para isso passamos a sequência como parâmetro para tuple.

#palavra = 'Python'
#sequencia = [2, 5, 8, 6]

#tup_palavra = tuple(palavra)
#tup_sequencia = tuple(sequencia)

#print(type(tup_palavra))
#print(tup_palavra)
#print(tup_palavra[4])

##O objeto de uma tupla não pode ser substituído, mas ele pode ser alterado, o objeto em si é mutável.
##Para ficar mais claro, segue alguns exemplos.

##Criamos uma tupla de tuplas para armazenar todos os elementos
#imutavel = ('Oi!', ['01010110', '01101111', '01100011'], 2112)

##Em seguida tentamos alterar a tupla, inserindo outro elemento na "segunda posição".
#imutavel[1] = ['Você']

##Um erro será exibido <TypeError: 'tuple' object does not support item assignment>, pois como já referido não
##é possível substituir um elemento da tupla (são imutáveis e de tamanho fixo).

##Entretanto, objetos mutáveis, como uma Lista, podem ser modificados.
#imutavel[1].append('11101010')
#print(imutavel[1])

#print(imutavel)

##As tuplas também podem ser concatenadas ou multiplicadas por um inteiro.
##Para concatenar as tuplas é necessário usar o operador de soma '+'. Quando elas são concatenadas, formam
##uma única tupla. 

#tup1 = 'Data', 'Structures'
#tup2 = 'Foo', 'Bar'
#concat = tup1 + tup2

#print(type(concat)) ##O tipo continua sendo uma tupla <class 'tuple'>.
#print(concat) ##As tuplas concatenas formam uma única tupla ('Data', 'Structures', 'Foo', 'Bar').

##Ao multiplicar a tupla por um inteiro, a sua referencia é copiada.
#tup_multiplicada = tup1 * 2

#print(tup_multiplicada) ##É copiado a referência para os objetos, gerando ('Data', 'Structures', 'Data', 'Structures').

##As tuplas também podem ser "desestruturadas", como em JavaScript

#tup_idades = 25, 38, 59

#ana, carla, roberto = tup_idades

#print(f'Ana tem {ana} anos, Carla tem {carla} anos e Roberto tem {roberto} anos')

##A sintaxe '*nome_variavel' (por convenção, em Python, é usado *_ para essas variáveis) permite que alguns 
##elementos possam ser armazenados em variáveis x, y, z e o que sobrar fica em outra variável 
##que guarda os valores restantes.

#ana, *anos = tup_idades
#print(f'Ana tem {ana} anos e as outras pessoas tem {anos} anos respectivamente')