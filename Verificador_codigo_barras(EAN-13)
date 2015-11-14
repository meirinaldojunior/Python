__autor__ = "meirinaldo júnior";

#Variaveis Globais

soma_pares = int
soma_impares = int

mult_num_pares = int

soma_multiplicacoes = int

opcao = input("Digite '1' para encontrar o verificador, ou '2' para verificar código")
opcao = int(opcao)
if opcao == 1:   
    codigo = input("Digite o código de Barras sem o verificador: ")
    codigo = codigo.strip()
    #menor que 12 caracteres
    if len(codigo) < 11 or len(codigo) > 13 :
        print("O código deve conter pelo 12 caracteres")
    else: 
        #Passando Valores para variáveis - Pares
        soma_pares = int(codigo[1]) + int(codigo[3]) + int(codigo[5]) + int(codigo[7]) + int(codigo[9]) + int(codigo[11])
      
        mult_num_pares = soma_pares*3

        #passando Valores para variaveis - ímpares
        soma_impares = int(codigo[0]) + int(codigo[2]) + int(codigo[4]) + int(codigo[6]) + int(codigo[8]) + int(codigo[10])

        #soma das multiplicações
        
        soma_multiplicacoes = mult_num_pares + soma_impares

       
        #Encontrar multiplo de 10
        for x in range(9):
            if x >= 1:
                if ((soma_multiplicacoes+x) % 10 == 0):
                 print ("O código verificador deste código é: ")
                 print (x) #múltiplo
                 break                 
    
if opcao == 2:
    codigo = input("Digite o código de Barras com o verificador: ")
    codigo = codigo.strip()
 #menor que 12 caracteres
    if len(codigo) < 11:
        print("O código deve conter pelo 13 caracteres")
    else: 
           #Passando Valores para variáveis - Pares
        soma_pares = int(codigo[1]) + int(codigo[3]) + int(codigo[5]) + int(codigo[7]) + int(codigo[9]) + int(codigo[11])
      
        mult_num_pares = soma_pares*3

        #passando Valores para variaveis - ímpares
        soma_impares = int(codigo[0]) + int(codigo[2]) + int(codigo[4]) + int(codigo[6]) + int(codigo[8]) + int(codigo[10])

        #soma das multiplicações
        
        soma_multiplicacoes = mult_num_pares + soma_impares

       
        #Encontrar multiplo de 10
        for x in range(9):
            if x >= 1:
                if ((soma_multiplicacoes+x) % 10 == 0): #se o resto da divisão de n/x for 0 (múltiplo)
                    if int(codigo[12]) == x:
                        print ("Código Valido!")
                    else:
                        print ("Código inválido, o numero verificador é:")
                        print (x)
else:
    print("Opção inválida tente novamente")
