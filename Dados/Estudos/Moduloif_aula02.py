meta = 0.05
taxa = 0.0
rendimento = 0.20

if rendimento > meta:
    if rendimento >= 0.20:
        taxa = 0.04
        print ('A taxa foi de {}'.format(taxa))
    else:
        taxa = 0.02
        print ('A taxa foi de {}'.format(taxa))
else:
    taxa = 0.00
    print('A taxa foi de {}'.format(taxa))


##########################
# if condicao_1:
#     'o que fazer se a condicäo 1 for verdadeira'
#     if condicao_2:
#         'o que fazer se a condicäo 1 e 2 for verdadeira'
#     else:
#         'o que fazer se a condicäo 2 for falsa (mas a condicao_1 for verdadeira)'
# else:
#     'o que fazer se a condicäo 1 for falsa'
##########################