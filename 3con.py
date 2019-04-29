"""
Created on Fri Apr 26 22:04:22 2019

@author: ## Numeros saltitatntes by Dagoberto@panassol.com
"""
global ncomuns
ncomuns = 0
global nsalt
nsalt,ntotal = 0,100

#Função que verifica tipo de numero e incrementa  as vars controladoras ntotal,ncomuns e nsalt.
def verify(num):
    global ncomuns,nsalt
    menor,maior = 0,0
    tamStr=len(str(num-1))
    digits=list(str(num))
    x=0
    while x+1 < tamStr:                
        #print("Posicao: "+str(digits[int(x)])+str( int(digits[x+1])) )
        #compara os caracteres em sequencia para classificar o numero como CRES ou DECRES
        if (int(digits[x]) > int(digits[x+1]) ):
            #print("DECRES !" )
            menor = 1
        elif (int(digits[x]) < int(digits[x+1]) ):
            #print("CRESCENTE !" )
            maior = 1        
        #print("Comparação: "+str(digits[x])+"-"+str(digits[y(x+1)])  )
        x=x+1 ## while
    if (menor ==1 and maior ==1 ):
        nsalt = nsalt+1
    else:
        ncomuns = ncomuns+1
    return 

NumeroMeta = int(0.5 * ntotal)
while nsalt < NumeroMeta:  
    NumeroMeta = (0.5 * ntotal) 
    print ("% Atual de Numeros Saltitentes"+str(nsalt / ntotal))
    verify(ntotal)
    if (nsalt == NumeroMeta):
        print ("Alcançada Meta de 50% - Numeros Saltitantes: "+str(nsalt)+" Total de Numeros: "+str(ntotal)  )
        break
    ntotal = ntotal + 1
      
#Zerando variaveis e buscar os 99%
ncomuns = 0
nsalt = 0
ntotal = 100
NumeroMeta = (0.99 * ntotal)
print ("Calculando a Meta de 99% - aguarde...")
while nsalt < NumeroMeta:  
    NumeroMeta = (0.99 * ntotal) 
    verify(ntotal)
    if(nsalt == NumeroMeta):
        print ("Alcançada Meta de 99% - Numeros Saltitantes: "+str(nsalt)+" Total de Numeros: "+str(ntotal) )
        break
    ntotal = ntotal + 1   
