def busca_primos(n):
    lista_p = []
    for num in range(2, 550):
        es_primo = True  
        for i in range (2,num): 
            if num % i == 0: 
                 es_primo = False
    
