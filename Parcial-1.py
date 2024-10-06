def busca_primos(n):

    lista_p = [] # Creamos la lista, vacía, después le vamos a agregar cosas
    for num in range(2, 550): # Empezar en 2 porque 0 y 1 no son primos. vamos desde el 2 hasta el numero que pusimos (550). Pusimos que corte en 550 de forma adrede, para establecer un corte.
        es_primo = True  
        for i in range (2,num): 
            if num % i == 0: 
                 es_primo = False
        if es_primo:
             lista_p.append(num)
    print (lista_p [n-1])
    busca_primos (1)


