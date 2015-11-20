__autor__ = "meirinaldo júnior";

#Defs
def verificapais(codigo):
        if codigo >= 2 and codigo <= 139:
            print ("EUA")
        elif 300 <= codigo <= 379:
            print ("França")
        elif codigo == 380:
            print ("Bulgaria")
        elif codigo == 383:
            print ("Eslovênia")
        elif codigo == 385:
            print ("Croácia")
        elif codigo == 387:
            print ("Bósnia e Herzegovina")
        elif 400 <= codigo <= 440:
            print ("Alemanhã")
        elif 450 <= codigo <= 459:
            print ("Japão")
        elif 490 <= codigo <= 499:
            print ("Japão")
        elif 460 <= codigo <= 469:
            print ("Rússia")
        elif codigo == 470:
            print ("Quirguistão")
        elif codigo == 471:
            print ("Ilha de Taiwan")
        elif codigo == 474:
            print ("Estônia")
        elif codigo == 475:
            print ("Letônia")
        elif codigo == 476:
            print ("Azerbaijão")
        elif codigo == 477:
            print ("Lituânia")
        elif codigo == 478:
            print ("Usbequistão")
        elif codigo == 479:
            print ("Sri Lanka")
        elif codigo == 480:
            print ("Filipinas")
        elif codigo == 481:
            print ("Bielorrússia")
        elif codigo == 482:
            print ("Ucrânia")
        elif codigo == 484:
            print ("Moldávia")
        elif codigo == 485:
            print ("Armênia")
        elif codigo == 486:
            print ("Géorgia")
        elif codigo == 487:
            print ("Cazaquistão")
        elif codigo == 489:
            print ("Hong Kong")
        elif 500 <= codigo <= 509:
            print ("Reino Unido")
        elif codigo == 520:
            print ("Grécia")
        elif codigo == 528:
            print ("Líbano")
        elif codigo == 529:
            print ("Chipre")
        elif codigo == 530:
            print ("Albânia")
        elif codigo == 531:
            print ("República da Macêdonia")
        elif codigo == 535:
            print ("Malta")
        elif codigo == 539:
            print ("República da Irlanda")
        elif 540 <= codigo <= 549:
            print ("Bélgica")
        elif codigo == 560:
            print ("Portugal")
        elif codigo == 569:
            print ("Islândia")
        elif 570 <= codigo <= 579:
            print ("Dinamarca")
        elif codigo == 590:
            print ("Polónia")
        elif codigo == 594:
            print ("Romênia")
        elif codigo == 599:
            print ("Hungria")
        elif 600 <= codigo <= 601:
            print ("África do Sul")
        elif codigo == 603:
            print ("Gana")
        elif codigo == 608:
            print ("Bahrein")
        elif codigo == 609:
            print ("Ilhas Maurício")
        elif codigo == 611:
            print ("Marrocos")
        elif codigo == 613:
            print ("Argélia")
        elif codigo == 616:
            print ("Quênia")
        elif codigo == 618:
            print ("Costa do Marfim")
        elif codigo == 619:
            print ("Tunísia")
        elif codigo == 621:
            print ("Síria")
        elif codigo == 622:
            print ("Egito")
        elif codigo == 624:
            print ("Líbia")
        elif codigo == 625:
            print ("Jordânia")
        elif codigo == 626:
            print ("Irã")
        elif codigo == 627:
            print ("Kuwait")
        elif codigo == 628:
            print ("Arábia Saudita")
        elif codigo == 629:
            print ("Emirados Árabes")
        elif 640 <= codigo <= 649:
            print ("Finlândia")
        elif 690 <= codigo <= 699:
            print ("China")
        elif 700 <= codigo <= 709:
            print ("Noruega")
        elif codigo == 729:
            print ("Israel")
        elif 730 <= codigo <= 739:
            print ("Suécia")
        elif codigo == 740:
            print ("Guatemala")
        elif codigo == 741:
            print ("El Salvador")
        elif codigo == 742:
            print ("Honduras")
        elif codigo == 743:
            print ("Nicarágua")
        elif codigo == 744:
            print ("Costa Rica")
        elif codigo == 745:
            print ("Panamá")
        elif codigo == 746:
            print ("República Dominicana")
        elif codigo == 750:
            print ("México")
        elif 754 <= codigo <= 755:
            print ("Canadá")
        elif codigo == 759:
            print ("Venezuela")
        elif 760 <= codigo <= 769:
            print ("Suiça")
        elif codigo == 770:
            print ("Colômbia")
        elif codigo == 773:
            print ("Uruguai")
        elif codigo == 775:
            print ("Peru")
        elif codigo == 777:
            print ("Bolívia")
        elif codigo == 779:
            print ("Argentina")
        elif codigo == 780:
            print ("Chile")
        elif codigo == 784:
            print ("Paraguai")
        elif codigo == 786:
            print ("Equador")
        elif 789 <= codigo <= 790:
            print ("Brasil")
        elif 800 <= codigo <= 839:
            print ("Itália")
        elif 840 <= codigo <= 849:
            print ("Espanha")
        elif codigo == 850:
            print ("Cuba")
        elif codigo == 858:
            print ("Eslováquia")
        elif codigo == 859:
            print ("Républica Checa")
        elif codigo == 860:
            print ("Sérvia")
        elif codigo == 865:
            print ("Mongólia")
        elif codigo == 867:
            print ("Coréia do Norte")
        elif codigo == 869:
            print ("Turquia")
        elif 870 <= codigo <= 879:
            print ("Holanda")
        elif codigo == 880:
            print ("Coréia do Sul")
        elif codigo == 884:
            print ("Cambdoja")
        elif codigo == 885:
            print ("Tailândia")
        elif codigo == 888:
            print ("Singapura")
        elif codigo == 890:
            print ("Índia")
        elif codigo == 893:
            print ("Vietnam")
        elif codigo == 899:
            print ("Indonésia")
        elif 900 <= codigo <= 919:
            print ("Áustria")
        elif 930 <= codigo <= 939:
            print ("Austrália")
        elif codigo == 955:
            print ("Malásia")
        elif codigo == 958:
            print ("Macau")
        else:
            print ("Código de país não encontrado ou não cadastradado")
    
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
        #codigo = codigo.strip()
        somaremultiplicar(codigo)
        digito = codigo[12]
        comparar_verificador(somaremultiplicar, digito)
        print("País de origem do código: ")
        #Verificar País
        if codigo[0:1] == "0":
            codigo_absoluto = "0"
        elif codigo[0:2] == "0":
            codigo_absoluto = codigo[1:2]
        else:
            codigo_absoluto = codigo[0:3]
            
        verificapais(int(codigo_absoluto))           


    if (opcao != 1 and opcao != 2 and opcao != 0):
        print("Numero inserido inválido!")
