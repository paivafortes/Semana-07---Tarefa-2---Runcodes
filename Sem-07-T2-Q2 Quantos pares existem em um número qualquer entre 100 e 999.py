def quantos_numeros_pares(numero):
    quantidade_numeros_pares = 0
    posicao_zero = numero[0]
    posicao_um = numero[1]
    posicao_dois = numero[2]

    if(int(posicao_zero)%2==0): 
        quantidade_numeros_pares+=1
    if(int(posicao_um)%2==0): 
        quantidade_numeros_pares+=1
    if(int(posicao_dois)%2==0): 
        quantidade_numeros_pares+=1   
        
    return quantidade_numeros_pares

def main():
    numero_inteiro = input()
    
    if(len(numero_inteiro) == 3):
        print(quantos_numeros_pares(numero_inteiro))
    elif(True):
        print(0)

if __name__=='__main__':
    main()