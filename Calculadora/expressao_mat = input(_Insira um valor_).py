operacao = input(" Digite a operação desejada (soma, subt, div, mult): ")
num_1 = input("Insira o primeiro número: ")
num_2 = input("Insira o segundo número: ")

if operacao == "soma":
    resultado = int(num_1) + int(num_2)
if operacao == "subt":
    resultado = int(num_1) - int(num_2)
if operacao == "div":
    resultado = int(num_1) / int(num_2)
if operacao == "mult":
     resultado = int(num_1) * int(num_2)
else:
    resultado = "Operação indisponível"

print("O resultado da operação é: " + str(resultado))



expressao_mat = input("Digite : ")
resultado = eval(expressao_mat)
print("O resultado é", resultado)