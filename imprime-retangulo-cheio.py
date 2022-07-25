# Escreva um programa que recebe como entradas (utilize a função input) dois números inteiros correspondentes à largura e à altura de um retângulo, respectivamente. O programa deve imprimir, usando repetições encaixadas (laços aninhados), uma cadeia de caracteres que represente o retângulo informado com caracteres '#' na saída.
largura=int(input('Digite a largura da área: '))
altura=int(input('Digite a altura da área: '))
while(altura>0):
    print(largura*'#')
    altura=altura-1
# O resultado dos testes com seu programa foi:
# Parabéns! Todos os testes tiveram sucesso!