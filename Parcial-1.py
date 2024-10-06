def busca_primos(n):

    lista_p = [] # Creamos la lista, vacía, después le vamos a agregar cosas
    for num in range(2, 550): # Empezar en 2 porque 0 y 1 no son primos. vamos desde el 2 hasta el numero que pusimos (550). Pusimos que corte en 550 de forma adrede, para establecer un corte.
        es_primo = True  # Arrancamos estableciendo que todos los números son verdaderos para después poner que los números cuyo módulo es 0 los tome como falsos
        for i in range(2,num): 
            if num % i == 0: #Definimos el false (los números que no son primos)
                 es_primo = False 
        if es_primo:
             lista_p.append(num) #Le pedimos que sume el número primo True a la lista
    print (lista_p [n-1])  #Imprime el argumento, o sea  el numero con el que acompañamos la función
    
    busca_primos (100) #Aca llamamos la función y entre paréntesis ponemos el num que queremos


