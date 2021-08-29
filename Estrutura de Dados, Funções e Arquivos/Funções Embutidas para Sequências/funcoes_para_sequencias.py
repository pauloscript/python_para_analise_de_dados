#####################################################################
########## ESTRUTURA DE DADOS, FUNÇÕES E ARQUIVOS EM PYTHON #########
#####################################################################

################# FUNÇÕES EMBUTIDAS PARA SEQUÊNCIAS #################

##enumerate -> Converte sequências iteraveis em objetos enumerados.
##sorted -> Retorna uma lista com os elementos ordenados.
##zip -> Pareia os elementos de duas ou mais sequências.
##reversed -> Retorna um iterador inverso de uma sequência.

##O enumerate(iterable[], start), funciona básicamente com quaçquer conjunto de dados
##que possa ser iterado, como listas, tuplas, sequências em geral. Para cada elemento
##presente em uma lista o enumerate vai atribuir um valor, que por padrão começa em 0.
##É semelhante ao map() de algumas outras linguagem que usam (chave, valor), e pode ser
##muito útil para quando estiver indexando dados, como no exemplo a seguir, que cria um 
##dict como resultado.

#chamada = ['Alice', 'Antonio', 'Bruna', 'Carla', 'Diego', 'Eleonor']

#dict_chamada = {}

##Se nenhum valor for passado como segundo parâmetro para o enumerate ele assume 0
##como valor padrão, que não é o caso do exemplo a seguir.

#for i, v, in enumerate(chamada, 1): ##Observe que i é o iterador (count) e v é o valor
#dict_chamada[v] = i ##Para vada valor (v) o enumerate cria um índice (i)

#print(dict_chamada)

##Enquanto sort apenas ordena os elementos de uma lista (e retorna None), o seu colega
##sorted, retorna uma lista com os elementos ordenados.

#desordenado = [5, 8, 9, 2, 3, 1, 10]
#ordenado = desordenado.sort()
#print(ordenado)##A saída é um None.

#ordenado = sorted(desordenado)##A lista é ordenada e materializada
#print(ordenado)

##zip(iterable1, iterable2...) parea os elementos de duas ou mais sequências, retornando
##uma lista de tuplas. E se uma sequência for menor que a outra, o número de
##elementos retornados é determinado pela sequência mais curta.

#seq1 = ['a', 'b', 'c']
#seq2 = [1, 2, 3]

#pareados = list(zip(seq1, seq2))##Pareia os elementos e retorna uma lista de tuplas

#print(pareados)

##O reversed vai iterar pelos elementos de uma sequência qualquer em ordem inversa.

#revertendo = [1, 2, 3, 4, 5]

#revertendo = reversed(revertendo)##Observe que a lista inversa não é materializada, apenas um referência
#print(list(revertendo))##A partir do momento que a lista é iterada (com for, list etc) a lista é então materializada na ordem inversa