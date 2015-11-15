__autor__ = "meirinaldo júnior";

#Defs
def somaremultiplicar(codigo):
    #menor que 12 caracteres
    if len(codigo) <= 11 or len(codigo) >= 14 :
        print("O código deve conter pelo 12 caracteres se estiver procurando o verificador, e 13 se estiver verificando se o código é válido.")
    else: 
        #Passando Valores para variáveis - Pares
        soma_multi_pares = (int(codigo[1]) + int(codigo[3]) + int(codigo[5]) + int(codigo[7]) + int(codigo[9]) + int(codigo[11]))*3
        #passando Valores para variaveis - ímpares
        soma_impares = int(codigo[0]) + int(codigo[2]) + int(codigo[4]) + int(codigo[6]) + int(codigo[8]) + int(codigo[10])
        #soma das multiplicações        
        soma_multiplicacoes = soma_multi_pares + soma_impares
        
        return (soma_multiplicacoes)

def mostrar_verificador(valor):
    for x in range(9):
        if x >= 1:
            if ((somaremultiplicar(codigo)+x) % 10 == 0):
                print ("O código verificador deste código é: ")
                print (x) #múltiplo
                break                 

def comparar_verificador(valor, digito_verificador):
    for x in range(9):
        if x >= 1:
            if ((somaremultiplicar(codigo)+x) % 10 == 0):
                if (int(digito_verificador) == x):                 
                    print ("O código verificador é válido!") #múltiplo
                else:
                    print("O código verificado é inválido")
                break                 

#Variaveis Globais
soma_multi_pares = int
soma_impares = int
soma_multiplicacoes = int
codigo = int
opcao = int
encontrado = bool
while opcao != 0:
    print("============================================================================")
    opcao = input("Digite '1' para encontrar o verificador, '2' para verificar código, ou '0' para sair ")
    opcao = int(opcao)

    if opcao == 1:     
        codigo = input("Digite o código de Barras sem o verificador: ")
        codigo = codigo.strip()
        somaremultiplicar(codigo)
        mostrar_verificador(somaremultiplicar)

    if opcao == 2:     
        codigo = input("Digite o código de Barras com o verificador: ")
        codigo = codigo.strip()
        somaremultiplicar(codigo)
        digito = codigo[12]
        comparar_verificador(somaremultiplicar, digito)
        print("País de origem do código: ")
        #Verificar País
        
        if(codigo[0]+codigo[1]+codigo[2] == "789"):
            print("Brasil")
            encontrado = True
        if(codigo[0]+codigo[1]+codigo[2] == "790"):
            print("Brasil")
            encontrado = True
        if(codigo[0]+codigo[1]+codigo[2] == "002"):
            print("E. U. A.")
            encontrado = True
        if(codigo[0]+codigo[1]+codigo[2] == "003"):
            print("E. U. A.")
            encontrado = True
        if(codigo[0]+codigo[1]+codigo[2] == "004"):
            print("E. U. A.")
            encontrado = True
        if(codigo[0]+codigo[1]+codigo[2] == "005"):
            print("E. U. A.")
            encontrado = True
        if(codigo[0]+codigo[1]+codigo[2] == "006"):
            print("E. U. A.")
            encontrado = True
        if(codigo[0]+codigo[1]+codigo[2] == "007"):
            print("E. U. A.")
            encontrado = True
        if(codigo[0]+codigo[1]+codigo[2] == "008"):
            print("E. U. A.")
            encontrado = True
        if(codigo[0]+codigo[1]+codigo[2] == "009"):
            print("Brasil")
            encontrado = True
        if(codigo[0]+codigo[1]+codigo[2] == "010"):
            print("E. U. A.")
            encontrado = True
        if(codigo[0]+codigo[1]+codigo[2] == "011"):
            print("E. U. A.")
            encontrado = True
        if(codigo[0]+codigo[1]+codigo[2] == "012"):
            print("E. U. A.")
            encontrado = True
        if(codigo[0]+codigo[1]+codigo[2] == "013"):
            print("E. U. A.")
            encontrado = True
        if(codigo[0]+codigo[1]+codigo[2] == "014"):
            print("E. U. A.")
            encontrado = True
        if(codigo[0]+codigo[1]+codigo[2] == "015"):
            print("E. U. A.")
            encontrado = True
        if(codigo[0]+codigo[1]+codigo[2] == "016"):
            print("E. U. A.")
            encontrado = True
        if(codigo[0]+codigo[1]+codigo[2] == "017"):
            print("E. U. A.")
            encontrado = True
        if(codigo[0]+codigo[1]+codigo[2] == "018"):
            print("E. U. A.")
            encontrado = True
        if(codigo[0]+codigo[1]+codigo[2] == "019"):
            print("E. U. A.")
            encontrado = True
        if(codigo[0]+codigo[1]+codigo[2] == "004"):
            print("E. U. A.")
            encontrado = True
        if(codigo[0]+codigo[1]+codigo[2] == "005"):
            print("E. U. A.")
            encontrado = True
        if(codigo[0]+codigo[1]+codigo[2] == "006"):
            print("E. U. A.")
            encontrado = True
        if(codigo[0]+codigo[1]+codigo[2] == "007"):
            print("E. U. A.")
            encontrado = True
        if(codigo[0]+codigo[1]+codigo[2] == "008"):
            print("E. U. A.")
            encontrado = True
        else:
            if (encontrado != True):
                print ("Código de país não encontrado ou não cadastradado")
        
            
    if (opcao != 1 and opcao != 2 and opcao != 0):
        print("Numero inserido inválido!")
