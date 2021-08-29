#####################################################################
########## ESTRUTURA DE DADOS, FUNÇÕES E ARQUIVOS EM PYTHON #########
#####################################################################

########################## Comprehensions ###########################

##list comprehension
##dict comprehension

##Comprehensions funcionam como um filtro que pode ser usado em sequências.
##Se você tiver, por exemplo, uma lista com valores, caracteres ou expressões
##indesejadas use uma comprehension para filtrar e criar uma nova lista com os
##dados desejados. 
 
##list comprehension em Python segue a seguinte sintaxe:
##new_list = [expression for value in collection if condition]

#marcas = ['CocaCola', 'Johnsons', 'uniLever', 'bunGE', 'sci', 'fi', 'tst']

#tratamento_marcas = [v.upper() for v in marcas if len(v) > 3]

#print(tratamento_marcas)

##dict comprehension se asemelha a uma list comprehension, sendo definida na
##sintaxe a seguir:
##new_dict = {key-expression : value-expression for value in collection if condition}

##Podemos usar a lista de marcas para criar um dicionário de marcas

#dict_marcas = {value : index for index, value in enumerate(tratamento_marcas)}

#print(dict_marcas)
