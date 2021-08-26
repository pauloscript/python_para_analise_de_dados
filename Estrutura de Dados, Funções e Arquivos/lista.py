#####################################################################
########## ESTRUTURA DE DADOS, FUNÇÕES E ARQUIVOS EM PYTHON #########
#####################################################################

############################### LISTA ###############################

##Em oposição as tuplas, a lista é uma estrutura de dados dinâmica, isto é, ela têm tamanho variável e o seu
##conteúdo pode ser modificado.

#pessoas = ['Marco', 'Julia', 'Rafaela', 'Sofia']

#print(type(pessoas), f'{pessoas}') ##A saída será um tipo lista e a lista de pessoas, definida anteriormente.

##Sendo a lista uma das estruturas de dados mais básicas, podemos realizar algumas operações, como inserir
##em qualquer posição e remover elementos de qualquer posição. Observando que, a lista tem um custo muito alto
##para realizar esse tipo de operação, pois ela move os elementos uma posição a mais para poder inserir
##o novo valor na posição especificada.

##Alguns métodos e operadores disponíveis são:
##append(elemento) -> Inserir um novo elemento ao final da lista.
##insert(posicao, elemento) -> Iara inserir um elemento em uma posição específica da lista.
##pop(posicao) -> Remover um elemento de uma posição específica e retorna-lo.
##remove(elemento) -> Remove o elemento, quando informado o seu valor (não o indíce, como no insert() ou pop())
##in -> Verifica se um elemento pertence a lista e retorna True ou False ex: 'ABC' in lista_alfabeto.
##not in -> Verifica se um elemento não pertence a lista e retorna True ou False ex: 'ABC' not in numeros.
##+ -> O operador '+' pode ser usado para concatenar duas listas.
##sort -> A função sort permite ordenar os elementos de uma lista.
##bisect -> Módulo que implementa a busca binária.
##slice -> slice ou fatiameto é a possíbilidade de "dividir" uma lista em outras listas.

#pessoas.append('Rafael') ##Elemento sendo inserido depois de 'Sofia' que é a última pessoa da lista.
#pessoas.insert(2, 'Alec') ##Rafaela é movida uma posição (de 2 para 3, e assim por diante) e em seu lugar entra o Alec.
#quem_saiu = pessoas.pop(0)##Marco que está na primeira posição será removido da lista e retornado.
#pessoas.remove('Marco')##Podemos passar explicitamente qual elemento será removido.
#print(pessoas)

##Podemos verificar se uma lista contem ou não um valor usando 'in' e 'not in'
#print('Silvio' in pessoas)## Retorna False, pois Silvio não está na nossa lista de pessoas.
#print('Silvio' not in pessoas)## Nesse caso retorna True, pois é verdade que Silvio não está na lista de pessoas.

##Listas podem ser concatenadas usando o operador +
#concatenando = ['Concatenando', 2]
#listas = ['listas']

#concat_lista = concatenando + listas

#print(concat_lista) ##Será exibido uma única lista com os elementos das listas concatenadas.

##Os elementos de uma lista podem ser ordenados, sem a necessidade de criar outra, usando a função sort()
#desordenado = [5, 7, 2, 10, 14, 21, 18, 0, 3]

#desordenado.sort()

#print(desordenado)


##Para fazer a busca binária em uma lista, podemos usar um módulo de Python chamado bisect. Esse módulo implementa
##a busca binária e inserção de elementos em uma lista ordenada.

#import bisect

#ex_bisect = [5, 6, 8, 8, 12, 20]

##O bisect.bisect encontra a posição que um novo elemento deve ser inserido para que a lista continue ordenada.

#bisect.bisect(ex_bisect, 2) ##A posição que deve inserir esse elemento e para manter a lista ordenada é a 0.

##Em seguida usamos o bisect.insort para inserir um elemento nessa posição
#bisect.insort(ex_bisect, 2)

#print(ex_bisect) ##A lista agora começa com o elemento 2 estando na primeira posição (índice 0)

##Se as listas podem ser concatenadas, então elas também podem ser separadas. Esse é o caso do slice (fatiamento)
##que permite separar uma lista em outras listas com os valores desejados.
##Para isso usamos uma notação de start:stop (início:fim) que deve ser informada ao operador []

#lista = ['Maçã', 'Pera', 'Mamão', 'Melão', 2, 5, 8, 7]
#frutas = lista[0:4]
#numeros = lista[4:8]

#print(f'Frutas {frutas} e números {numeros}')

##Observe que a posição final (stop) não faz parte dos elementos, sendo o final - 1, Ex: 0:4 vai retornar
##os elementos do índice 0 até o índice 3. No 4:8 vai retornar os elementos do índice 4 até o índice 7.