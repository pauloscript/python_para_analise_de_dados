#####################################################################
########## ESTRUTURA DE DADOS, FUNÇÕES E ARQUIVOS EM PYTHON #########
#####################################################################


############################## FUNÇÕES ##############################

##Em Python as funções são declaradas usando a palavra def, e o retorno de valores é feito com a palavra return.
##Observe que o escopo da função é definido após os : e pela identação do código.

#def calc_imc(peso, altura):
#    imc = peso / pow(altura, 2)
#    return imc

#print(calc_imc(72, 1.68))

##Digamos que foi passado uma lista com as notas dos alunos de uma escola e querem fazer algumas análises
##estatísticas, mas antes disso observamos que por algum motivo as notas estão desorganizadas, como a seguir:

#notas_da_sec = ['10', '8a', '7.5', '7', '9#?', '6!!', ' 8.5 ']

##Para que essa lista de notas tenha algum valor, precisaremos realizar algumas operações de limpeza, como 
##remover os símbolos de pontuação e letras, remover espaços em branco e criar um padrão para fazer um uso adequado
##dessas notas.

#import re

#def limpar_notas(notas):
#    resultado = []
#    for nota in notas:
#        nota = nota.strip()
#        nota = re.sub('[a#?!]', '', nota)
#        nota = float(nota)
#        resultado.append(nota)
#    return resultado

#print(limpar_notas(notas_da_sec))

##Em Python também podemos definir funções lambda, semelhantes a arrow functions de JavaScript.
##Elas são contituídas de uma única instrução que tem como resultado o valor de retorno.

#result = lambda x: x + 5

#print(result(5))