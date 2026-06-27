#PROYECTO LÓGICA: KATAS DE PYTHON
#Autor: Miguel Encinas Gimenez

# 1. Escribe una función que reciba una cadena de texto como parámetro y devuelva un diccionario con las frecuencias
# de cada letra en la cadena. Los espacios no deben ser considerados.
def diccionario_de_frecuencias(string):
    """
    Función que calcula la frecuencia de aparición de cada letra en una cadena de texto,
    ignorando los espacios y unificando las letras en minúsculas.

    Args:
    string (str): Cadena de texto sobre la que se quiere calcular la frecuencia de letras.

    Returns:
    dict: Diccionario donde cada clave es una letra y cada valor es el número de veces que aparece.
    """
    string_sin_espacios = string.replace(" ","").lower()
    # Usamos este comando para eliminar los espacios de la cadena de texto, # y para obtener todo el texto en minúsculas,
    # ya que es más correcto a la hora de contar frecuencia de letras.
    frecuencias = {} #Creamos nuestro diccionario vacío
    for letra in string_sin_espacios: #Recorremos las letras de nuestra string sin espacios
        if frecuencias.get(letra) == None:
            frecuencias[letra] = 1 #Si nuestra letra aun no está en el dict, la añadimos (como key) con un value = 1
        else:
            frecuencias[letra] += 1 #Si nuestra letra ya es una key del dict (es decir, no es la 1era vez que aparece), a su value le sumamos 1
    return frecuencias
prueba_ej1 = diccionario_de_frecuencias("Tres tristes tigres comen trigo en un trigal")
print(prueba_ej1)

# 2. Dada una lista de números, obtén una nueva lista con el doble de cada valor. Usa la función map()
def valores_dobles(lista):
    """
    Función que devuelve una nueva lista con el doble de cada número de la lista original.

    Args:
    lista (list): Lista de números sobre la que se aplicará la operación.

    Returns:
    list: Lista con cada valor numérico multiplicado por 2.
    """
    lista_2 = list(map(lambda x: x*2, lista))
    # Usamos map para definir una función lambda que nos duplica nuestra variable (argumento:x / expresión: x*2)
    # Ese lambda lo aplicamos sobre el argumento de nuestra función (lista) y, como map sólo nos devuelve un objeto con los resultados, le pedimos a Python
    # que nos lo devuelve a modo de lista con list().
    return lista_2
prueba_ej2 = valores_dobles([1, 2, 3, 4, 5, 6, 7])
print(prueba_ej2)

# 3. Escribe una función que tome una lista de palabras y una palabra objetivo como parámetros. La función debe
# devolver una lista con todas las palabras de la lista original que contengan la palabra objetivo.
def encontrar_palabra (lista, palabra): #Definimos nuestra función con los dos argumentos
    """
    Función que busca palabras dentro de una lista que contengan una palabra o fragmento objetivo.

    Args:
    lista (list): Lista de palabras en la que se realizará la búsqueda.
    palabra (str): Palabra o fragmento de texto que se quiere encontrar dentro de cada elemento.

    Returns:
    list: Lista con las palabras que contienen la palabra o fragmento buscado.
    """
    coincidencias = [] #Creamos nuestra lista vacía para llenarlas con las palabras coincidente
    # Creamos un bucle for de manera que, cuando iteremos en la lista, si nuestra palabra está dentro del elemento,
    # #añade dicho elemento a la lista.
    for elemento in lista:
        if palabra in elemento:
            coincidencias.append(elemento)
    return coincidencias
texto = "Tres tristes tigres comen trigo en un trigal"
# En este caso he hecho el ejemplo con un texto, que he convertido a lista con el método split(), pero se podría pasar
# directamente una lista de palabras.
prueba_ej3 = encontrar_palabra(texto.split(), "tr")
print(prueba_ej3)

# 4. Genera una función que calcule la diferencia entre los valores de dos listas. Usa la función map()
def diferencia_listas_1(lista_1, lista_2): #Definimos la función para calcular la diferencia entre listas (función 1)
    """
    Función que calcula la diferencia entre los elementos correspondientes de dos listas numéricas.

    Args:
    lista_1 (list): Primera lista de números.
    lista_2 (list): Segunda lista de números.

    Returns:
    list: Lista con el resultado de restar a cada elemento de lista_1 el elemento correspondiente de lista_2.
    """
    def resta_valores(a, b): #Dentro de ellas, definimos una función para una resta entre dos valores individuales (función 2)
        """
        Función interna que resta dos valores numéricos.

        Args:
        a (int, float): Primer valor numérico.
        b (int, float): Segundo valor numérico.

        Returns:
        int, float: Resultado de restar a - b.
        """
        resta = a - b
        return resta #Concluimos la función 2
    #Volvemos a función 1. Usamos map() para aplicar la función 2 con los argumentos que hemos definido para la función 1
    lista_resta = list(map(resta_valores, lista_1, lista_2))
    return lista_resta
# Definimos las listas y aplicamos la función 1, que usa map() para generar una lista con la diferencia de los valores de las
# dos listas dadas a partir de la resta definida en la función 2
lista_prueba_1 = [1,2,3,4,5,6]
lista_prueba_2 = [6,5,4,3,2,1]
prueba_ej4_1 = diferencia_listas_1(lista_prueba_1, lista_prueba_2)
print(prueba_ej4_1)

# Como solución alternativa, se me ha ocurrido esta función que se me hace más sencilla, ya que no implica definir función dentro
# de función, aunque no sería válida ya que no usa la función map(). Usamos el método zip() para pasar las dos listas a la vez
# por el bucle for, y vamos iterando para hacer la resta elemento por elemento; después, añadimos el elemento resultante a nuestra lista
def diferencia_listas_2(lista_1, lista_2):
    """
    Función que calcula la diferencia entre los elementos correspondientes de dos listas usando zip().

    Args:
    lista_1 (list): Primera lista de números.
    lista_2 (list): Segunda lista de números.

    Returns:
    list: Lista con las diferencias, elemento por elemento, entre ambas listas.
    """
    lista_resta = []
    for numero_1, numero_2 in zip(lista_1, lista_2):
        valor_resta = numero_1 - numero_2
        lista_resta.append(valor_resta)
    return lista_resta
prueba_ej4_2 = diferencia_listas_2(lista_prueba_1,lista_prueba_2)
print(prueba_ej4_2)

# 5. Ecribe una función que tome una lista de números como parámetro y un valor opcional nota_aprobado, que por 
# defecto es 5. La función debe calcular la media de los números en la lista y determinar si la media es mayor o igual 
# que nota aprobado. Si es así, el estado será "aprobado", de lo contrario, será "suspenso". La función debe devolver 
# una tupla que contenga la media y el estado.
def nota_final(lista_numeros, nota_aprobado = 5): #Definimos la función con nuestros 2 parámetros: la lista de números y el parámetro fijo 'nota_aprobado'
    """
    Función que calcula la media de una lista de notas y determina si el resultado es aprobado o suspenso.

    Args:
    lista_numeros (list): Lista de notas numéricas.
    nota_aprobado (int | float, optional): Nota mínima necesaria para aprobar, y que por defecto es 5.

    Returns:
    tuple: Tupla formada por la media calculada y el estado final, que será "aprobado" o "suspenso".
    """
    suma_numeros = 0 #Establecemos un valor inicial en 0
    for numero in lista_numeros:
        suma_numeros += numero #Vamos sumando los elementos en la variable suma_numeros
    numero_datos = len(lista_numeros)
    promedio = suma_numeros/numero_datos #Dividimos la suma de los elementos entre el número de datos (promedio)
    if promedio >= nota_aprobado: #Condición 1: Si el promedio es mayor o igual que 'nota_aprobado', devolvemos una tupla con el promedio y el string 'aprobado'
        tupla1 = (promedio, "aprobado")
        return tupla1
    else: #Condición 1: Si el promedio es menor que 'nota_aprobado', devolvemos una tupla con el promedio y el string 'suspenso'
        tupla2 = (promedio, "suspenso")
        return tupla2
#Vamos a pasar dos listas de ejemplo para observar ambas posibilidades, así como imprimir su tipo y confirmar que obtenemos tuplas como resultado.
lista_notas1 = [5,4.5, 6.25, 3.25, 3.25, 5, 2.75]
lista_notas2 = [7, 5.5, 8.5, 5, 4.5, 9.5, 4.75]
prueba_ej5_1 = nota_final(lista_notas1)
prueba_ej5_2 = nota_final(lista_notas2)
print(prueba_ej5_1)
print(type(prueba_ej5_1))
print(prueba_ej5_2)
print(type(prueba_ej5_2))

# 6. Escribe una función que calcule el factorial de un número de manera recursiva.
def factorial(numero):
    """
    Función que calcula el factorial de un número mediante recursividad.

    Args:
    numero (int): Número entero del que se quiere calcular el factorial.

    Returns:
    int, str: Factorial del número indicado; si el número es 0, devuelve un mensaje indicando que su factorial es 1.
    """
    if numero == 1:
        return 1
    elif numero == 0:
        return 'El factorial de 0 es 1'
    #Matemáticamente, el factorial de 0 está definido como 1 (en un conjunto de 0 elementos, solo hay 1 forma de ordenar
    #dichos elementos). Tenemos por tanto que especificar este caso en nuestro condicional if para evitar tener un error
    else:
        return numero * factorial(numero-1)
# Con esta llamada recursiva, estamos diciendo a la función que, al pedirle el factorial de nuestro número, nos devuelva
# nuestro número multiplicado por el factorial del número-1 (esta es la manera de descomponer el factorial de un número).
# La función va aplicando el return hasta que llega a numero = 1. En ese momento, entiende que factorial(1) = 1, y por tanto,
# puede ir 'escalando hacia atrás' para calcular que los factoriales. Por ejemplo, según la función: factorial(2) = 2 * factorial(1),
# como factorial(1) = 1, la función sabrá que factorial(2) = 2 * 1 = 2, y así sucesivamente hasta volver a nuestro número.
prueba_ej6 = factorial(6)
print(prueba_ej6)

# 7. Genera una función que convierta una lista de tuplas a una lista de strings. Usa la función map()
def tupla_string_1(lista_tuplas):
    # Para este primer método, he usado una simple función map dentro de list() para convertir en string los métodos de la lista de tuplas.
    # Como se puede ver en los print, para una lista de tuplas, al aplicar la función, seguimos teniendo una lista, pero las tuplas se han
    # convertido tal cual estaban en strings. Por eso, el elemento [0] es (7,8,9), y es un string como tal.
    """
    Función que convierte cada tupla de una lista en una cadena de texto.

    Args:
    lista_tuplas (list): Lista formada por tuplas.

    Returns:
    list: Lista con las tuplas convertidas a strings.
    """
    lista_strings = list(map(str, lista_tuplas))
    return(lista_strings)

lista = [(7,8,9), (1,2,3), (4,5,6)]
prueba_ej7_1 = tupla_string_1(lista)
print(prueba_ej7_1)
print(type(prueba_ej7_1))
print(prueba_ej7_1[0])
print(type(prueba_ej7_1[0]))

# Este segundo método lo he desarrollado porque creo que se puede entender el ejercicio de dos formas. En este caso, partiendo igualmente
# de una lista de tuplas dada, definimos en primer lugar una nueva lista vacía (lista_strings). Tras esto, llegamos hasta los elementos
# individuales con bucles for: el primero se refiere a las tuplas de la lista, y el segundo a los números dentro de cada tupla. Transformamos
# cada elemento en un string, y con la función map, los vamos añadiendo a nuestra lista_strings. De esta manera, cuando hacemos los prints,
# podemos comprobar que, en este caso, hemos generado una lista de strings individuales; por ejemplo, el elemento [0] en este caso sería el 7,
# que sería de tipo string.
def tupla_string_2(lista_tuplas):
    """
    Función que recorre una lista de tuplas y convierte cada elemento individual de las tuplas en string.

    Args:
    lista_tuplas (list): Lista cuyos elementos son tuplas con valores individuales.

    Returns:
    list: Lista con todos los elementos internos de las tuplas convertidos a strings.
    """
    lista_strings = []
    for tupla in lista_tuplas:
        for numero in tupla:
            numero = str(numero)
            map(lista_strings.append(numero), lista_strings)
    return lista_strings
prueba_ej7_2 = tupla_string_2(lista)
print(prueba_ej7_2)
print(type(prueba_ej7_2))
print(prueba_ej7_2[0])
print(type(prueba_ej7_2[0]))

# 8. Escribe un programa que pida al usuario dos números e intente dividirlos. Si el usuario ingresa un valor no numérico o intenta
# dividir por cero, maneja esas excepciones de manera adecuada. Asegúrate de mostrar un mensaje indicando si la división fue exitosa o no.
try:
    # Comenzamos nuestro bloque 'try' con la petición de input por el usuario, solicitando dos números diferentes llamados num1 y num 2.
    # Tras esto, expresamos la operación que queremos realizar, basada en la división de uno entre otro.
    num1 = int(input("Ingrese el primer número: "))
    print(f'El primer número elegido por el usuario fue: {num1}')
    num2 = int(input("Ingrese el segundo número: "))
    print(f'El segundo número elegido por el usuario fue: {num2}')
    division = num1/num2
    # Una vez concluido el bloque 'try', incorporamos los bloques except para manejar las dos excepciones que contemplamos: recibir un valor
    # que no pueda transformarse en int (ValueError) o intentar realizar una división entre 0 (ZeroDivisionError). Estas excepciones van acompañadas
    # de mensajes indicando el error que ha ocurrido.
except ValueError:
    print('Operación fallida. Por favor, ingrese un número válido para poder realizar la operación')
except ZeroDivisionError:
    print('Operación fallida. El segundo número debe ser distinto de 0 para poder realizar la operación')
    'Por último, definimos nuestro bloque else, que nos permitirá definir lo que ocurre cuando no hayamos incurrido en los errores previamente definidos'
else:
    print(f'Operación exitosa. El resultado de la división es: {division}')

# 9. Escribe una función que tome una lista de nombres de mascotas como parámetro y devuelva una nueva lista
# excluyendo ciertas mascotas prohibidas en España. La lista de mascotas a excluir es ["Mapache", "Tigre",
# "Serpiente Pitón", "Cocodrilo", "Oso"].Usa la función filter()
def filtrado_mascotas(animal):
    """
    Función  para filtrar el nombre de mascotas prohibidas.

    Args:
    animal (str): Nombre de la mascota que se quiere comprobar.

    Returns:
    bool: True si el animal no está en la lista de mascotas prohibidas; False si sí lo está y debe excluirse.
    """
    '''Definimos la función con 'animal', ya que el método filter() va a pasar los elementos cada elemento del iterable como
    valores individuales a través de la función, no como una lista entera'''
    mascotas_prohibidas = ["Mapache", "Tigre", "Serpiente Pitón", "Cocodrilo", "Oso"] #Definimos la lista de animales prohibidos
    if animal in mascotas_prohibidas:
        return False #Condicional if para definir la condición de eliminación del elemento (es decir, cuándo un elemento devuelve False)
    return True #Cuando un elemento no cumple la condición para ser catalogado como False, entonces será True
mascotas_ejemplo = ["Conejo", "Perro", "Tigre", "León", "Cocodrilo", "Oso Panda", "Ratón", "Serpiente Pitón",
                    "Gato", "Iguana", "Mapache", "Rinoceronte", "Hámster", "Serpiente de Cascabel", "Oveja"]
prueba_ej9 = list(filter(filtrado_mascotas, mascotas_ejemplo))
# El método filter() requiere que la función devuelva valores booleanos con lo que filtrará los valores falsos y se quedará con los que devuelvan True
print(prueba_ej9)

# 10. Escribe una función que reciba una lista de números y calcule su promedio. Si la lista está vacía, lanza una
# excepción personalizada y maneja el error adecuadamente.
def calculo_promedio(lista_numeros):#Definimos nuestra función, y dentro de ella, nuestro bloque 'try', que se ejecutará si no aparece ningún error
    #que hayamos incluido en los bloques 'except
    """
    Función que calcula el promedio de una lista dada de números.

    Args:
    lista_numeros (list): Lista de valores numéricos.

    Returns:
    float, str: Promedio de los números de la lista o mensaje de error si la lista está vacía.
    """

    try:
        # En este bloque try, por tanto, hemos pedido que nos sume los números de la lista y lo divide entre el número
        # de elementos de la lista, dándonos así el promedio de los números de la lista.
        suma = 0
        for numero in lista_numeros:
            suma += numero
        promedio = suma/len(lista_numeros)
        return promedio
    except ZeroDivisionError:
        # En este bloque, definimos lo que ocurre si nos encontramos con el error en cuestión, que es el que aparece
        # cuando pasamos una lista vacía en la función
        return 'El número de elementos es 0. Al no poder dividir entre 0, esta operación no es posible'
lista_ejemplo1 = [5, 17, 93, 6, 32, 5, 23, 20, 33]
prueba_ej10_1 = calculo_promedio(lista_ejemplo1)
print(prueba_ej10_1) #Print del promedio de la primera lista de ejemplo, obteniendo el promedio de dicha lista
lista_ejemplo2 = []
prueba_ej10_2 = calculo_promedio(lista_ejemplo2)
print(prueba_ej10_2) # Print del promedio de la segunda lista, la cual estaba vacía, obteniendo el mensaje en respuesta al error

# 11. Escribe un programa que pida al usuario que introduzca su edad. Si el usuario ingresa un valor no numérico o un
# valor fuera del rango esperado (por ejemplo, menor que 0 o mayor que 120), maneja las excepciones adecuadamente.
try:
    # En primer lugar, definimos un bloque 'try' en el que solicitamos la edad al usuario.
    # Tras esto, expresamos la operación que queremos realizar, basada en la división de uno entre otro.
    edad = int(input("Ingrese su edad (número entre 0 y 120): "))
    if edad < 0 or edad > 120:
        print('Por favor, ingrese un número dentro del rango indicado')
    #Con este 'if statement', establecemos un control de flujo, mediante el cual le decimos al programa que, si el valor ingresado está fuera de rango,
    #nos devuelva un mensaje pidiéndonos un valor dentro del rango establecido.
    else:
        print(f'Gracias por confirmarnos que tiene {edad} años')
    # Tras definir el bloque 'try' y el 'if statement', definimos el bloque except para gestionar la otra excepción que contemplamos en este ejercicio:
    # recibir un valor que no pueda transformarse en int (ValueError).
except ValueError:
    print('Por favor, ingrese un número válido')

# 12. Genera una función que al recibir una frase devuelva una lista con la longitud de cada palabra. Usa la función map()

def longitud_palabras(frase): #Definimos nuestra función
    """
    Función que calcula la longitud de cada palabra de una frase.

    Args:
    frase (str): Cadena de texto formada por una o varias palabras.

    Returns:
    list: Lista de números enteros con la longitud de cada palabra.
    """
    lista_frase = frase.split() #Convertimos nuestra frase, es decir, nuestro conjunto de strings, en una lista de strings con split()
    lista_longitud = list(map(lambda elemento: len(elemento), lista_frase))
    #Iteramos a lo largo de nuestra lista de strings, pero no con un bucle for, sino con la función map(), que en esta ocasión he decidido combinarla con
    #una función lambda ya que vamos a aplicar una función sencilla. Con esto, le decimos a la función que itere a través de los elementos de la lista_frase,
    #y nos calcule la longitud de cada uno, para finalmente devolvernos el resultado en forma de lista
    return lista_longitud
frase1 = 'En un lugar de la Mancha de cuyo nombre no quiero acordarme' #Probamos nuestra función con una frase
prueba_ej12 = longitud_palabras(frase1)
print(prueba_ej12)

# 13. Genera una función la cual, para un conjunto de caracteres, devuelva una lista de tuplas con cada letra en
# mayúsculas y minúsculas. Las letras no pueden estar repetidas .Usa la función map()
def lista_tuplas(caracteres): #Definimos nuestra función
    """
    Función que genera una lista de tuplas con cada carácter único, en minúscula y mayúscula.

    Args:
    caracteres (str): Cadena de texto o conjunto de caracteres a procesar.

    Returns:
    list: Lista de tuplas donde cada tupla contiene un carácter en minúscula y su equivalente en mayúscula.
    """
    no_espacios = caracteres.replace(" ","") #En caso de que sea una frase, eliminamos los espacios para que no figuren en la lista final.
    #También aprovechamos a convertir el conjunto de letras a minúscula, para favorecer la homogeneidad
    lista_caracteres = [] #Lista temporal donde vamos a incluir nuestros caracteres
    for elemento1 in no_espacios:
        lista_caracteres.append(elemento1.lower()) #Introducimos los caracteres de nuestro conjunto en la lista, en formato minúsculas para
        #garantizar homogeneidad y no tener elementos duplicados en la lista, ya que minúscula y mayúscula se pueden considerar caracteres distintos.
    set_unicos = set(lista_caracteres) #En un set no puede haber valores duplicados, así que convertimos nuestra lista de caracteres a un set.
    lista_funcion = list(map(lambda x: tuple([x,x.upper()]),set_unicos))
    #En esta función, usamos map() para iterar los elementos de nuestro set_unicos. La función a realizar viene determinada por una lambda, que toma
    #el elemento del conjunto y crea un tupla con dicho elemento (ya viene en minúscula) y su equivalente en mayúscula.
    #Todo viene englobado por el método list(), que nos permite convertir el resultado de map() a una lista.
    return lista_funcion
caracteres1 = "En un lugar de la Mancha de cuyo nombre no quiero acordarme"
prueba_ej13 = lista_tuplas(caracteres1)
print(prueba_ej13)

# 14. Crea una función que retorne las palabras de una lista de palabras que comience con una letra en especifico. Usa la función filter()
def comprobar_letra(lista_palabras, letra):
    """
    Función que filtra las palabras de una lista que comienzan por una letra específica.

    Args:
    lista_palabras (list): Lista de palabras que se desea filtrar.
    letra (str): Letra inicial que deben tener las palabras seleccionadas.

    Returns:
    list: Lista con las palabras que empiezan por la letra indicada.
    """
    lista_filtrada = list(filter(lambda palabra: palabra[0].lower() == letra, lista_palabras))
    #Definimos la función y, para este caso concreto, vamos a seleccionar las palabras que empiecen por la letra 'M'.
    #Establecemos como condición falsa que el primer elemento del string sea diferente a 'm', aplicando un lower()
    #previamente para que reconozca la palbra tanto si está escrita en mayúscula como en minúscula.
    return lista_filtrada
lista_ejercicio = ['Mermelada', 'Bicicleta', 'paisaje', 'montaña', 'Paracaídas', 'COCHE',
                   'pelota', 'Metal', 'MACEDONIA', 'Puerta', 'Televisión', 'mÓVIL', 'Ordenador',
                   'baloncesto', 'AGUA', 'dátil', 'Eneldo', 'Frío', 'LLAVES']
letra_inicio = str(input("Indique una letra con la que realizar el ejercicio: ")).lower() #Aplicamos también la minúscula a la letra seleccionada
prueba_ej14 = comprobar_letra(lista_ejercicio, letra_inicio)
print(prueba_ej14)


# 15. Crea una función lambda que sume 3 a cada número de una lista dada.
sumar_tres = lambda lista: [elemento + 3 for elemento in lista]
# Como ya hemos visto a lo largo del módulo, la función lambda permite crear funciones sencillas de manera más simplificada,
# ahorrando en muchas ocasiones el uso de 'def'. En este ejercicio concreto, podemos combinar nuestra función lambda con una
# estructura de tipo 'list comprehension', lo que nos permite definir una función sencilla y aplicable a la lista que definamos.
# En este caso, he usado 'lista' en vez de 'x' para el argumento de lambda con el fin de que sea más intuitivo.
prueba_ej15 = [1,2,3,4,5,6,7,8,9,0]
print(f'El resultado de aplicar lambda a nuestra lista es {sumar_tres(prueba_ej15)}')


# 16. Escribe una función que tome una cadena de texto y un número entero n como parámetros y devuelva una lista de
# todas las palabras que sean más largas que n. Usa la función filter()
def longitud_palabras(cadena_texto, n): #Definimos la función con nuestros 2 parámetros: la cadena de texto y la longitud n
    """
    Función que devuelve las palabras de una cadena de texto cuya longitud es mayor que un valor dado.

    Args:
    cadena_texto (str): Frase o cadena de texto que se quiere analizar.
    n (int): Longitud mínima que deben superar las palabras para ser incluidas.

    Returns:
    list: Lista formada por las palabras con longitud superior a n.
    """
    lista_texto = cadena_texto.split() #Transformamos nuestra cadena de texto en una lista de palabras
    lista_filtrada = list(filter(lambda palabra: len(palabra) > n, lista_texto)) #Aplicamos nuestra función filter con ayuda de lambda,
    #lo que nos permite pasarle un único parámetro a filter(). Para cada palabra de lista_texto, buscamos si nuestra condición es True o False
    return lista_filtrada
cadena_usuario = str(input("Introduzca una frase o cadena de texto: ")) #Pedimos al usuario que indique una cadena de texto a analizar
longitud_usuario = int(input("Introduzca la longitud deseada: ")) #Pedimos al usuario que indique la longitud deseada
prueba_ej16_1 = longitud_palabras(cadena_usuario, longitud_usuario) #Aplicamos la función
print(prueba_ej16_1)

# Este ejercicio me resultó un quebradero de cabeza, y llegué a otro código que, aunque no cumple el hecho de definir una
#función que reciba los dos parámetros, creo que también es interesante y válido. A raíz de ella, llegué al código que muestro arriba.
cadena_texto = str(input("Introduzca una frase o cadena de texto: ")).split()
longitud = int(input("Introduzca la longitud deseada: "))
prueba_ej16_2 = list(filter(lambda palabra: len(palabra) > longitud, cadena_texto))
print(prueba_ej16_2)

# 17. Crea una función que tome una lista de dígitos y devuelva el número correspondiente. Por ejemplo, [5,7,2]
# corresponde al número quinientos setenta y dos (572). Usa la función reduce()
from functools import reduce #Importamos reduce de functools
numeros_22 = [2, 4, 8, 16] #Creamos nuestra lista de dígitos, que formarán nuestro número final
prueba_ej22 = int(reduce(lambda x, y: str(x) + str(y), numeros_22)) #Aplicamos el método reduce mediante una función lambda, que toma dos variables
#y realiza una suma entre ellas. Como vamos a transformar nuestros dígitos en strings en dicha función, lo que haremos será poner uno detás de otro.
# Tras la primera adición (número 1 * número 2), el resultado pasará a ser la x, y la y será el número 3, y así sucesivamente. Una vez se ha aplicado
#nuestra función a todos los elementos de la lista, transformamos nuestro número a integer, envolviendo toda la función con el método int()
print(prueba_ej22)
print(type(prueba_ej22))

# 18 . Escribe un programa en Python que cree una lista de diccionarios que contenga información de estudiantes (nombre, edad, calificación) 
#y use la función filter para extraer a los estudiantes con una calificación mayor o igual a 90. Usa la función filter()
def filtrado_calificacion(lista_dicts):
    #Definimos la función que nos va a devolver la lista de diccionarios filtrada. Para ello, usamos un lambda dentro de filter, estableciendo la
    #condición de que la clave calificación debe ser igual o mayor a 90 (si se cumple, es True); esto se aplica a nuestra lista de diccionarios,
    #todo envuelto en el método list(), para obtener una lista con los diccionarios que cumplan la condición
    """
    Función que filtra una lista de diccionarios de estudiantes según su calificación.

    Args:
    lista_dicts (list): Lista de diccionarios con información de los diferentes estudiantes.

    Returns:
    list: Lista de los diccionarios correspondientes a los estudiantes con calificación mayor o igual a 90.
    """
    nombres_filtrados = list(filter(lambda diccionario: diccionario['calificacion'] >= 90, lista_dicts))
    return nombres_filtrados
lista_diccionarios = [] #Para crear nuestra lista de diccionarios, comenzamos creando una lista vacía
for i in range(0,5):
    #Establecemos un contador con el bucle loop, de manera que nos pide 5 veces rellenar un diccionario (es decir, con input del usuario). Para cada
    #vez, el sistema nos pedirá un nombre, una edad y una calificación, y se irán creando y añadiendo los diccionarios a la lista
    diccionario = {'nombre': str(input('Ingrese un nombre (sin tildes): ')),
                   'edad': int(input('Ingrese una edad: ')),
                   'calificacion': int(input('Ingrese una calificacion: '))}
    lista_diccionarios.append(diccionario)

prueba_ej18 = filtrado_calificacion(lista_diccionarios) #Ejecutamos nuestra función en la lista de diccionarios que hemos creado
print(prueba_ej18)


# 19. Crea una función lambda que filtre los números impares de una lista dada.
filtro_impares = lambda lista: [elemento for elemento in lista if elemento%2 != 0]
# En este ejercicio, volvemos a combinar el uso de lambda con una estructura tipo 'list comprehension', de manera que, para los elementos
# de la lista, vamos iterando uno por uno y comprobando si el resto de su división entre 2 es distinto de 0. Si lo es, lo consideramos impar,
# y por lo tanto lo añadimos a nuestra lista.
prueba_ej19 = [1, 23, 53, 675, 34, 62, 3, 567, 254, 876, 54, 95]
print(f'Los números impares de nuestra lista son {filtro_impares(prueba_ej19)}')

# 20. Para una lista con elementos tipo integer y string obtén una nueva lista sólo con los valores int. Usa la función filter()
def obtencion_int(elemento):
    # En primer lugar, definimos nuestra función, que tomará como argumento cada elemento de la lista (recordemos que la función filter()
    # itera por si misma, por lo que no es necesario usar un bucle 'for' en nuestra función.
    """
    Función que toma una lista con componentes integers y strings, y se queda únicamente con los valores int.

    Args:
    elemento (int, str): Elemento individual de una lista de integers y strings.

    Returns:
    bool: False si el elemento es de tipo string, True en caso contrario.
    """
    if type(elemento) == str:
        return False
    return True
    # Nos han especificado que, de una lista con elementos tipo 'int' y 'str', obtengamos únicamente los elementos tipo 'int', de ahí
    # la decisión de utilizar ese condicional if. Si la lista tuviera elementos de otro tipo (p. ej., 'float'), podríamos adaptar el condicional
    # acorde a los tipos de elementos que tuviéramos
lista_combinada = [9, 'hola', 5, 73, 29, 'Python', 'thePower', 0, 'pandas', 'numpy', 'jupyter', 39]
prueba_ej20 = list(filter(obtencion_int, lista_combinada))
print(f'Los elementos tipo "int" de nuestra lista son {prueba_ej20}')

#21. Crea una función que calcule el cubo de un número dado mediante una función lambda
funcion_cubo = lambda x: x**3
# En este ejercicio concreto, al pedirnos simplemente que elevemos un número al cubo,
# podemos crear dicha función mediante el uso de lambda, definiendo el argumento 'x', y tras ello la expresión (x**3)
x = 5
print(f'El cubo de {x} es igual a {funcion_cubo(x)}')

# 22. Dada una lista numérica, obtén el producto total de los valores de dicha lista.Usa la función reduce()
from functools import reduce #Importamos reduce de functools
numeros_22 = [1, 2, 3, 4, 5, 6] #Creamos nuestra lista de números, con números del 1 al 6
prueba_ej22 = reduce(lambda x, y: x * y, numeros_22) #Aplicamos el método reduce mediante una función lambda, que toma dos variables
#y realiza una multiplicación entre ellas. Tras la primera multiplicación (número 1 * número 2), el producto pasará a ser la x, y
#la y será el número 3, y así sucesivamente
print(prueba_ej22)

# 23. Concatena una lista de palabras.Usa la función reduce() .
from functools import reduce #Importamos reduce de functools
palabras = ['Hola', 'yo','me', 'llamo', 'Miguel', 'y', 'tengo', '29', 'años'] #Creamos nuestra lista de palabras individuales
prueba_ej23 = reduce(lambda x, y: x + " " + y, palabras) #Aplicamos el método reduce mediante una función lambda, que toma dos variables
#y las une con un espacio entre medio. Tras la primera unión (palabra 1 + palabra 2), dicha unión de palabras pasará a ser la x, y
#la y será la palabra 3, y así sucesivamente
print(prueba_ej23)

# 24. Calcula la diferencia total en los valores de una lista. Usa la función reduce() .
from functools import reduce #Importamos reduce de functools
numeros_23 = [1, 2, 3, 4, 5, 6] #Creamos nuestra lista de números, con números del 1 al 6
prueba_ej24 = reduce(lambda x, y: x - y, numeros_23) #Aplicamos el método reduce mediante una función lambda, que toma dos variables
#y realiza una resta entre ellas. Tras la primera resta (número 1 - número 2), el resultado pasará a ser la x, y la y será el número 3,
#y así sucesivamente
print(prueba_ej24)

# 25. Crea una función que cuente el número de caracteres en una cadena de texto dada.
def conteo_caracteres(cadena_texto):
    """
    Función que cuenta el número de caracteres de una cadena de texto (excluyendo los espacios).

    Args:
    cadena_texto (str): Cadena de texto cuyos caracteres se quieren contar.

    Returns:
    int: Número total de caracteres en la cadena de texto.
    """
    #Definimos nuestra función, en la que recibimos una cadena de texto. En este caso, he considerado quitar los espacios para
    #no contarlos como caracteres útiles, aunque se podrían mantener también. Tras esto, usamos len() para contar el númoero de caracteres
    no_espacios = cadena_texto.replace(" ","")
    num_caracteres = len(no_espacios)
    return num_caracteres
cadena_usuario = str(input('Por favor, introduzca aquí su cadena de texto: ')) #Le solicitamos al usuario que introduzca una cadena de texto
prueba_ej25 = conteo_caracteres(cadena_usuario)
print(f'El número de caracteres totales es: {prueba_ej25}')

# 26. Crea una función lambda que calcule el resto de la división entre dos números dados.
resto_division = lambda x,y: x%y
#Creamos una función lambda sencilla con dos parámetros (x, y) para que calcule el resto de su división
num1 = 5
num2 = 2
#Definimos dos variables, num1 y num2, cuyo valor podemos sustituir por el número que se desee, y las pasamos por nuestra función lambda.
print(f'El resto de esta división es {resto_division(num1,num2)}')

# 27. Crea una función que calcule el promedio de una lista de números.
def promedio(lista_numeros): #Definimos nuestra función
    """
    Función que calcula el promedio de una lista de números.

    Args:
    lista_numeros (list): Lista de numeros.

    Returns:
    float: Promedio de los números incluidos en la lista.
    """
    suma = 0 #Definimos una variable con un valor inicial 0, a la cual le iremos añadiendo la suma de los números de la lista
    for numero in lista_numeros:
        suma += numero #Iteramos a través de los números de la lista, y vamos sumando cada uno al resultado acumulado de la suma de los anteriores
    promedio = suma/len(lista_numeros) #Dividimos la suma de los números entre el número de datos que teníamos, para obtener el promedio
    return promedio
lista_numeros = [256, 945, 314, 220, 235, 813, 301, 710, 308, 641]
prueba_ej27 = calculo_promedio(lista_numeros) #Aplicamos la función a la lista que hemos puesto como ejemplo
print(prueba_ej27)

# 28. Crea una función que busque y devuelva el primer elemento duplicado en una lista dada.
def deteccion_duplicados(lista):
    """
    Función que detecta el primer elemento duplicado en una lista (se ignoran diferencias entre mayúsculas y minúsculas).

    Args:
    lista (list): Lista de elementos de texto a analizar.

    Returns:
    string: Mensaje indicando el primer duplicado encontrado, o bien que no existen duplicados.
    """

    lista_nueva = []
    for elemento in lista:
        if elemento.lower() in lista_nueva:
            mensaje1 = print(f'El elemento {elemento.lower()} ya estaba en la lista, por lo tanto, es el primer duplicado')
            return mensaje1
        else:
            lista_nueva.append(elemento.lower())
    mensaje2 = print('No había ningún elemento duplicando en la lista')
    return mensaje2
lista_ej28 = ['pollo', 'bacon', 'huevos', 'merluza','Pollo', 'perejil', 'pan', 'Huevos']
prueba_ej28 = deteccion_duplicados(lista_ej28)


# 29. Crea una función que convierta una variable en una cadena de texto y enmascare todos los caracteres con el
# carácter '#', excepto los últimos cuatro.
def codificacion(variable):
    """
    Función que convierte una variable en texto y enmascara todos sus caracteres, excepto los últimos cuatro.

    Args:
    variable (any): Valor que se quiere convertir a string y codificar.

    Returns:
    str: Cadena de texto enmascarada con '#',exceptuando los cuatro últimos caracteres.
    """
    #Definimos nuestra función, a la que le pasaremos nuestra variable. En primer lugar, vamos a convertir nuestra variable en str.
    #Tras ello, calculamos la longitud de dicha varirable, y creamos una lista vacía.
    variable_texto = str(variable)
    longitud = len(variable_texto)
    lista1 = []
    #En esta lista vacía, incluiremos el siguiente for loop, basado en la creación de una lista, con la longitud del string original, restándole 4.
    #Por cada carácter en el que iteramos, mediante el bucle for, añadimos un '#' a la lista. Finalmente, fuera del bucle for, convertimos la lista en un string.
    for i in range(0,longitud-4):
        lista1.append('#')
    string1 = "".join(lista1)
    lista2 = []
    #Seguimos un mecanismo similar, pero en este caso, hacemos un bucle for en las 4 últimas posiciones. En este bucle, cada caracter por el que iteramos
    #será añadido tal cual a nuestra lista2. Tras esto, convertimos la lista a string y, finalmente, unimos los dos strings, por lo que tenemos un string
    #que se compone de '#' excepto los 4 últimos caracteres de la palabra.
    for i in range(longitud-4, longitud):
        lista2.append(variable_texto[i])
    string2 = "".join(lista2)
    string_cod = string1 + string2
    return string_cod
variable_usuario = input('Introduzca aquí su variable: ')
prueba_ej29 = codificacion(variable_usuario)
print(f'La variable codificada es: {prueba_ej29}')

# 30. Crea una función que determine si dos palabras son anagramas, es decir, si están formadas por las mismas letras pero en diferente orden.
def anagramas(palabra1, palabra2):
    """
    Función que comprueba si dos palabras son anagramas, comparando para ello la frecuencia de sus letras.

    Args:
    palabra1 (str): Primera palabra a comparar.
    palabra2 (str): Segunda palabra a comparar.

    Returns:
    None: Imprime un mensaje indicando si las palabras son anagramas o no.
    """
    #Para este ejercicio, creo qu puede ser interesante reciclar parte de la función que hemos usado en el ejercicio 1, en el cual
    #elaboramos un diccionario que contuviera las frecuencias de las palabras
    palabra1 = palabra1.lower()
    palabra2 = palabra2.lower() #Ponemos las dos palabras en minúsculas para evitar resultados falsos entre mayúsculas y minúsculas
    frecuencias = {}  # Creamos nuestro diccionario vacío, que tendrá las frecuencias de los caracteres de una palabra
    if palabra1 == palabra2:
        #Primera condición: si pasamos dos palabras iguales, imprimimos este mensaje y gracias al return salimos de la función
        mensaje1 = print('¡No podemos comprobar si es un anagrama porque es la misma palabra!')
        return mensaje1
    else:
        #Dentro del else, establecemos el funcionamiento de nuestra función comparativa para detectar anagrama
        for letra in palabra1:  # Recorremos las letras de nuestra primera palabra
            if frecuencias.get(letra) == None:
                frecuencias[letra] = 1  # Si nuestra letra aun no está en el dict, la añadimos (como key) con un value = 1
            else:
                frecuencias[letra] += 1  # Si nuestra letra ya es una key del dict (es decir, no es la 1era vez que aparece), a su value le sumamos 1
        for letra in palabra2:  # Recorremos las letras de nuestra segunda palabra sin espacios
            if frecuencias.get(letra) == None:
                frecuencias[letra] = 1  # Si nuestra letra aun no estaba en el dict, la añadimos (como key) con un value = 1
            else:
                frecuencias[letra] -= 1  #Si nuestra letra ya esta una key del dict, vamos a restar 1 unidad al valor que habíamos obtenido a partir
                # de la primera palabra por cada vez que aparezca esta letra en la segunda palabra. De esta manera, si ambas palabras tienen una letra
                # repetida el mismo número de veces, el valor de esa letra en el dict será 0
        nuevo_diccionario = {}
        for clave,valor in frecuencias.items():
            if valor != 0:
                nuevo_diccionario.update({clave:valor}) #Hemos creado un nuevo diccionario vacío, y en el vamos a añadir los pares de clave:valor del
                #diccionario 'frecuencias' tras pasar los caracteres de ambas palabras; excepto cuando el valor sea 0, lo cual quiere decir que ambas
                #palabras presentaban el mismo número de esa letra
            else:
                pass
        if len(nuevo_diccionario) == 0:
            #Por tanto, si este nuevo diccionario se queda vacío, significa que ambas palabras presentaban la misma frecuencia de todos los caracteres,
            # y ninguna presentaba letras que la otra palabra no tuviese; por tanto, podemos concluir que en este caso, ambas palabras son un anagrama.
            mensaje2 = print('La palabra es un anagrama, tiene las mismas letras pero en distinto orden')
            return mensaje2
        else:
            #Si, por el contrario, el diccionario presenta algún valor, quiere decir que alguna letra entre las palabras no coincidía, o que está presente
            #en ambas pero con distinta frecuencia; por lo tanto, estas palabras no serán un anagrama.
            mensaje3 = print(f'La palabra no es un anagrama, se diferencian en las siguientes letras: {nuevo_diccionario.keys()}')
            return mensaje3
x = 'Cabello'
y= 'Cebolla'
prueba_ej30 = anagramas(x,y)

# 31. Crea una función que solicite al usuario ingresar una lista de nombres y luego solicite un nombre para buscar en esa lista. 
# Si el nombre está en la lista, se imprime un mensaje indicando que fue encontrado, de lo contrario, se lanza una excepción.
def buscar_nombre(): #Definimos nuestra función, en este caso será una función sin parámetros, ya que nos los pide dentro de la propia función
    """
    Función que solicita una lista de nombres al usuario,y luego busca un nombre concreto dentro de ella.

    Args:
    No hay argumentos

    Returns:
    None: Imprime un mensaje indicando si el nombre buscado se encuentra en la lista o no.
    """
    lista_nombres = [] #Creamos una lista vacía para ir añadiendo los nombres
    for i in range(7):
        #Le pedimos al usuario que nos propocione 7 nombres que se irán añadiendo a la lista (se puede variar este número según la necesidad)
        elemento = str(input(f'Escriba el elemento {i} de la lista: ')).lower() #Añadimos el nombre en formato string y en minúsculas, por homogeneidad
        lista_nombres.append(elemento)
    nombre = str(input('Seleccione ahora el nombre a buscar: ')).lower()
    #Ahora le pedimos al usuario que nos indique un nombre (el cual será transformado a minúsculas también) para buscarlo en la lista previa
    if nombre in lista_nombres:
        #Si el nombre está en la lista, imprimiremos el mensaje escrito en la línea de abajo
        mensaje1 = print(f'¡El nombre "{nombre}" está en la lista!')
        return mensaje1
    else:
        #Si por el contrario no está, imprimiremos el mensaje que hemos especificado en la línea siguiente
        mensaje2 = print(f'El nombre "{nombre}" no se encuentra en la lista proporcionada')
        return mensaje2
prueba_ej31 = buscar_nombre()

# 32. Crea una función que tome un nombre completo y una lista de empleados, busque el nombre completo en la lista y devuelve el puesto 
# del empleado si está en la lista, de lo contrario, devuelve un mensaje indicando que la persona no trabaja aquí.
def filtro_empleados(empleados, nombre): #Definimos la función con los dos parámetros que nos indican: la lista de empleados y el nombre a buscar
    """
    Función que busca un empleado por su nombre completo, y muestra su puesto si está registrado.

    Args:
    empleados (list): Lista de diccionarios con la información de los empleados.
    nombre (str): Nombre completo del empleado que se desea buscar.

    Returns:
    None: Imprime el puesto del empleado encontrado, o bien un mensaje indicando que no trabaja en la empresa.
    """
    for empleado in empleados: #Iteramos a través de los diccionarios que estarán dentro de la lista
        if empleado['nombre completo'] == nombre:
            #Si el nombre que hemos buscado coincide con el valor de la clave 'nombre completo' en alguno de nuestros diccionarios,
            #entonces nos devuelve el mensaje 1
            mensaje1 = print(f"El puesto del empleado {nombre.title()} es {empleado['puesto'].title()}")
            return mensaje1
    #Tras terminar de iterar, si no se ha cumplido la condición if que hemos establecido, entonces se aplicará el siguiente return
    mensaje2 = print(f"{nombre.title()} no trabaja aquí")
    return mensaje2
lista_empleados = [] #Definimos una lista vacía, que será rellenada con la información de nuestros trabajadores

for i in range(0, 5):
    # Establecemos un contador con el bucle loop, de manera que nos pide 5 veces rellenar un diccionario (es decir, con input del usuario). Para cada
    # vez, el sistema nos pedirá un nombre completo y un puesto de trabajo, y se irán creando y añadiendo los diccionarios a la lista
    diccionario = {'nombre completo': str(input('Ingrese un nombre y dos apellidos (sin tildes): ')).lower(),
                   'puesto': str(input('Ingrese el puesto de trabajo (sin tildes): ')).lower()}
    # Ahora, con input, le pedimos al usuario que nos indique un nombre completo para buscar en nuestro diccionario
    lista_empleados.append(diccionario)
nombre_empleado = str(input('Ahora ingrese un nombre y dos apellidos para buscar (sin tildes): ')).lower()
prueba_ej32 = filtro_empleados(lista_empleados, nombre_empleado) #Ejecutamos nuestra función con las variables definidas.

#33. Crea una función lambda que sume elementos correspondientes de dos listas dadas.
lista_ej1 = [1,2,3,4,5,6]
lista_ej2 = [6,5,4,3,2,1]
#Al estar usando una función lambda, es mejor que definamos nuestras dos variables (las listas) previamente

prueba_ej33 = list(map(lambda elemento1,elemento2: elemento1 + elemento2, lista_ej1, lista_ej2))
#Definimos el método map() que, como función, encierra a lambda, la cual define como variables los elementos individuales de ambas listas, y su función
#es sumarlos. Tras esto, completamos map() con los elementos iterables, que serán las propias listas previamente definidas. Todo esto queda encerrado en
#un list() que nos permitirá obtener el resultado en forma de lista.
print(f'El resultado de la suma de elementos es {prueba_ej33}')

# 34. Crea la clase Arbol , define un árbol genérico con un tronco y ramas como atributos. Los métodos disponibles son:
# crecer_tronco , nueva_rama , crecer_ramas , quitar_rama e info_arbol . El objetivo es implementar estos métodos para manipular la estructura del árbol.
# Código a seguir:
#  1. Inicializar un árbol con un tronco de longitud 1 y una lista vacía de ramas.
#  2. Implementar el método crecer_tronco para aumentar la longitud del tronco en una unidad.
#  3. Implementar el método nueva_rama para agregar una nueva rama de longitud 1 a la lista de ramas.
#  4. Implementar el método crecer_ramas para aumentar en una unidad la longitud de todas las ramas existentes.
#  5. Implementar el método quitar_rama para eliminar una rama en una posición específica.
#  6. Implementar el método info_arbol para devolver información sobre la longitud del tronco, el número de ramas y las longitudes de las mismas.
class Arbol: #Creamos nuestra clase: árbol
    def __init__(self): #Definimos los atributos de nuestra clase, en este caso: tronco (int) y ramas (lista)
        """
        Método constructor que inicia un objeto árbol con un tronco de longitud 1 y una lista vacía de ramas.

        Args:
        Ninguno

        Returns:
        Ninguno
        """
        self.tronco = 1 #Se nos pide un árbol con un tronco inicial de longitud 1
        self.ramas = [] #Se nos pide una variable 'ramas' como atributo
    def crecer_tronco(self): #Definimos la función crecer_tronco para añadir una unidad al tronco
        """
        Método que incrementa en una unidad la longitud del tronco del árbol.

        Args:
        Ninguno

        Returns:
        Ninguno
        """
        self.tronco += 1
    def nueva_rama(self): #Definimos la función nueva_rama para añadir una nueva rama a la lista
        """
        Método que añade una nueva rama de longitud 1 a la lista de ramas del árbol.

        Args:
        Ninguno

        Returns:
        Ninguno
        """
        self.ramas.append(1)
    def crecer_ramas(self): #Definimos la función crecer_ramas para añadir una unidad a cada de las ramas de la lista
        """
        Método que incrementa en una unidad la longitud de todas las ramas que posee el árbol en ese momento.

        Args:
        Ninguno

        Returns:
        Ninguno
        """
        for i in range(0, len(self.ramas)):
            self.ramas[i] += 1
    def quitar_rama(self, posicion): #Definimos la funcion quitar_rama (con un mecanismo defensivo) para eliminar una rama a elección
        """
        Método que elimina una rama situada en una posición específica de la lista de ramas.

        Args:
        posicion (int): Índice de la rama que se desea eliminar.

        Returns:
        Ninguno
        """
        if 0 <= posicion <= len(self.ramas)-1:
            self.ramas.pop(posicion)
        else:
            print("Elige una posición de 'rama' válida")
    def info_arbol(self): #Definimos la función info_arbol para obtener un diccionario con la información principal de nuestro árbol
        """
        Método que devuelve información general sobre el estado actual del árbol.

        Args:
        Ninguno

        Returns:
        dict: Diccionario con la longitud del tronco, el número de ramas y las longitudes de cada rama.
        """
        arbol = {'longitud_tronco': self.tronco,
                 'numero_ramas': len(self.ramas),
                 'longitud_ramas': tuple(self.ramas)}
        return arbol

# Caso de uso:
abeto = Arbol() #1. Crear un árbol.
abeto.crecer_tronco() #2. Hacer crecer el tronco del árbol una unidad.
abeto.nueva_rama() #3. Añadir una nueva rama al árbol.
abeto.crecer_ramas() #4. Hacer crecer todas las ramas del árbol una unidad.
abeto.nueva_rama() #5. Añadir dos nuevas ramas al árbol.
abeto.nueva_rama()
abeto.quitar_rama(2) #6. Retirar la rama situada en la posición 2.
print(abeto.info_arbol()) #7. Obtener información sobre el árbol.

# 36. Crea la clase UsuarioBanco ,representa a un usuario de un banco con su nombre, saldo y si tiene o no cuenta corriente. 
# Proporciona métodos para realizar operaciones como retirar dinero, transferir dinero desde otro usuario y agregar dinero al saldo.
# Código a seguir:
#  1. Inicializar un usuario con su nombre, saldo y si tiene o no cuenta corriente mediante True y False .
#  2. Implementar el método retirar_dinero para retirar dinero del saldo del usuario. Lanzará un error en caso de no poder hacerse.
#  3. Implementar el método transferir_dinero para realizar una transferencia desde otro usuario al usuario actual. Lanzará un error en caso de no poder hacerse.
#  4. Implementar el método agregar_dinero para agregar dinero al saldo del usuario.
# 36. Crea la clase UsuarioBanco ,representa a un usuario de un banco con su nombre, saldo y si tiene o no cuenta corriente.
# Proporciona métodos para realizar operaciones como retirar dinero, transferir dinero desde otro usuario y agregar dinero al saldo.
# Código a seguir:
#  1. Inicializar un usuario con su nombre, saldo y si tiene o no cuenta corriente mediante True y False .
#  2. Implementar el método retirar_dinero para retirar dinero del saldo del usuario. Lanzará un error en caso de no poder hacerse.
#  3. Implementar el método transferir_dinero para realizar una transferencia desde otro usuario al usuario actual. Lanzará un error en caso de no poder hacerse.
#  4. Implementar el método agregar_dinero para agregar dinero al saldo del usuario.
# Caso de uso:
#  1. Crear dos usuarios: "Alicia" con saldo inicial de 100 y "Bob" con saldo inicial de 50, ambos con cuenta corriente.
#  2. Agregar 20 unidades de saldo de "Bob".
#  3. Hacer una transferencia de 80 unidades desde "Bob" a "Alicia".
#  4. Retirar 50 unidades de saldo a "Alicia".
class UsuarioBanco: #Creamos nuestra clase: UsuarioBanco
    def __init__(self, nombre, saldo, cuenta_corriente): #Definimos los atributos de nuestra clase, en este caso: nombre, saldo y cuenta_corriente
        """
        Método constructor que inicia un usuario del banco con nombre, saldo y si tiene o no cuenta corriente.

        Args:
        nombre (str): Nombre del usuario bancario.
        saldo (int, float): Saldo inicial del usuario.
        cuenta_corriente (bool): Indica si el usuario dispone de cuenta corriente.

        Returns:
        Ninguno
        """
        self.nombre = nombre #Creamos las variables nombre, saldo y cuenta corriente
        self.saldo = saldo
        self.cuenta_corriente = cuenta_corriente
    def retirar_dinero(self, cantidad): #Definimos la primera función, retirar_dinero,  con el argumento 'cantidad'
        """
        Método que retira una cantidad del saldo del usuario si la operación es válida.

        Args:
        cantidad (int, float): Cantidad de dinero que se desea retirar.

        Returns:
        Ninguno
        """
        if cantidad > self.saldo: #Si la cantidad a retirar es mayor que el saldo disponible, recibimos un error
            print('Error: No dispones de saldo suficiente para realizar esta operación')
        elif cantidad <= 0: #Si la cantidad a retirar es menor o igual a 0, recibimos un error
            print('Por favor, introduzca un número válido')
        else: #Si se cumplen las condiciones, se retira dicha cantidad de la cuenta corriente
            self.saldo -= cantidad
    def transferir_dinero(self, emisor,cantidad): #Definimos la función transferir dinero, con los argumentos 'emisor' y 'cantidad'
        """
        Método que transfiere dinero desde otro usuario del banco al usuario actual.

        Args:
        emisor (UsuarioBanco): Usuario que envía el dinero.
        cantidad (int, float): Cantidad de dinero que se desea transferir.

        Returns:
        Ninguno
        """
        if cantidad <= 0: #Si la cantidad a transferir es menor o igual a 0, recibimos un error
            print('Error: Por favor, introduzca un número válido')
        elif cantidad > emisor.saldo: #Si la cantidad a transferir es mayor que el saldo del emsior, recibimos un error
            print('Error: El usuario emisor no tiene fondos suficientes para realizar esta operación')
        elif self.cuenta_corriente == False: #Si el receptor no dispone de cuenta corriente, recibimos un error
            print('Error: El usuario receptor no dispone de cuenta corriente')
        elif emisor.cuenta_corriente == False: #Si el emsior no dispone de cuenta corriente, recibimos un error
            print('Error: El usuario emisor no dispone de cuenta corriente')
        else: #Si se cumplen las condiciones, sustraemos la cantidad al emisor y se la añadimos al receptor
            emisor.saldo -= cantidad
            self.saldo += cantidad
    def agregar_dinero(self, cantidad): #Definimos la última función, agregar dinero, con el parámetro 'cantidad'
        """
        Método que añade una cantidad de dinero al saldo del usuario, si la cantidad es válida.

        Args:
        cantidad (int, float): Cantidad de dinero que se desea agregar al saldo.

        Returns:
        Ninguno
        """
        if cantidad <= 0: #Si la cantidad a agregar es menor o igual a 0, recibimos un error
            print('Error: Por favor, introduzca un número válido')
        else: #Si se cumplen las condiciones, se agrega la cantidad al usuario.
            self.saldo += cantidad

# Caso de uso:
alicia = UsuarioBanco('Alicia', 100, True)#1. Crear dos usuarios: "Alicia" con saldo inicial de 100
# y "Bob" con saldo inicial de 50, ambos con cuenta corriente.
bob = UsuarioBanco('Bob', 50, True)
bob.agregar_dinero(20) #2. Agregar 20 unidades de saldo de "Bob".
alicia.transferir_dinero(bob, 80) #3. Hacer una transferencia de 80 unidades desde "Bob" a "Alicia". Como podemos ver,
# nos da error porque el saldo de Bob es insuficiente
alicia.retirar_dinero(50) #4. Retirar 50 unidades de saldo a "Alicia".
print(alicia.__dict__) #Imprimimos la información de Alicia
print(bob.__dict__) #Imprimimos la información de Bob


#  37. Crea una función llamada procesar_texto que procesa un texto según la opción especificada: contar_palabras, reemplazar_palabras, eliminar_palabra. 
#  Estas opciones son otras funciones que tenemos que definir primero y llamar dentro de la función procesar_texto .
#  Código a seguir:
#  1. Crear una función contar_palabras para contar el número de veces que aparece cada palabra en el texto. Tiene que devolver un diccionario.
#  2. Crear una función reemplazar_palabras para remplazar una palabra_original del texto por una palabra_nueva . Tiene que devolver el texto con el remplazo de palabras.
#  3. Crear una función eliminar_palabra para eliminar una palabra del texto. Tiene que devolver el texto con la palabra eliminada.
#  4. Crear la función procesar_texto que tome un texto, una opción(entre "contar", "reemplazar", "eliminar") y un número de argumentos variable según la opción indicada.
# Caso de uso:
#  1. Comprueba el funcionamiento completo de la función procesar_texto
def contar_palabras(texto):  # Definimos la función de contar palabras. Como argumentos, tenemos únicamente el texto a analizar
    """
    Función que cuenta cuántas veces aparece cada palabra en un texto.

    Args:
    texto (str): Texto que se desea analizar.

    Returns:
    dict: Diccionario donde cada clave es una palabra, y cada valor correspondiente es su frecuencia de aparición.
    """
    texto_sin_simbolos = texto.replace(",", "").replace(";", "").replace(".", "").replace(":", "").replace("?","").replace("¿", "").replace("¡", "").replace("!", "").replace("-", "")
    # Modificamos el texto para eliminar todos los símbolos que puedan aparecer, ya que vamos a converitr nuestro texto en listas y separar los elementos
    # por los espacios, de manera que si permanecen los símbolos, podría contar alguna palabra como palabra+símbolo (ejemplo: 'y,' en vez de 'y').
    lista_palabras = texto_sin_simbolos.lower().split()  # Transformamos todo en minúsculas para no tener letras duplicadas, y hacemos la separación
    # en los espacios para generar nuestra lista
    frecuencia_palabras = {}  # Creamos nuestro diccionario vacío
    for palabra in lista_palabras:  # Recorremos las palabras del texto
        if frecuencia_palabras.get(palabra) == None:
            frecuencia_palabras[palabra] = 1  # Si nuestra palabra aun no está en el dict, la añadimos (como key) con un value = 1
        else:
            frecuencia_palabras[palabra] += 1  # Si nuestra palabra ya es una key del dict (es decir, no es la 1era vez que aparece), a su value le sumamos 1
    return frecuencia_palabras

def eliminar_palabras(texto, eliminacion): #Definimos la función de eliminar palabras. Como argumentos, tenemos el texto a analizar y la palabra a eliminar
    """
    Función que elimina una palabra concreta de un texto, y tras esto reconstruye el texto resultante (sin símbolos).

    Args:
    texto (str): Texto original que se desea modificar.
    eliminacion (str): Palabra que se quiere eliminar del texto.

    Returns:
    str: Texto reconstruido sin la palabra indicada.
    """
    texto_sin_simbolos = texto.replace(",", "").replace(";", "").replace(".", "").replace(":", "").replace("?", "").replace("¿", "").replace("¡", "").replace("!", "").replace("-", "")
    # Modificamos el texto para eliminar todos los símbolos que puedan aparecer, ya que vamos a converitr nuestro texto en listas y separar los elementos
    # por los espacios, de manera que si permanecen los símbolos, podría contar alguna palabra como palabra+símbolo (ejemplo: 'y,' en vez de 'y').
    lista_palabras = texto_sin_simbolos.lower().split()  # Transformamos todo en minúsculas para no tener letras duplicadas, y hacemos la separación
    nueva_lista = [] #Creamos una lista vacía para ir añadiendo las palabras nuevamente
    for palabra in lista_palabras:
        if palabra != eliminacion: #Si la palabra de nuestra lista es distinta a la que queremos eliminar, la añadimos a la nueva lista
            nueva_lista.append(palabra)
        else:
            pass #En caso contrario, pasamos, es decir, si la palabra de la lista es igual a la que queremos eliminar, no se añade
    texto_nuevo = " ".join(nueva_lista) #Rehacemos la frase usando el método .join en la nueva lista.
    #LIMITACIÓN IMPORTANTE: Con este método, generaremos de nuevo la frase, pero toda en minúsculas y sin los símbolos que hemos eliminado al principio. Sin embargo,
    #intentar generar nuevamente la frase tal cual estaba o aplicar la función de otra manera me parecía algo complejo para mis conocimientos actuales.
    return texto_nuevo

def reemplazar_palabras(texto, palabra_vieja, palabra_nueva): #Definimos la función de eliminar palabras. Como argumentos, tenemos el texto a analizar,
    #la palabra a sustituir y la nueva palabra.
    """
    Función que sustituye una palabra concreta de un texto por otra palabra nueva, y tras esto reconstruye el texto (sin símbolos).

    Args:
    texto (str): Texto original que se desea modificar.
    palabra_vieja (str): Palabra que se quiere reemplazar.
    palabra_nueva (str): Nueva palabra que sustituirá a la reemplazada.

    Returns:
    str: Texto reconstruido con la palabra reemplazada.
    """
    texto_sin_simbolos = texto.replace(",", "").replace(";", "").replace(".", "").replace(":", "").replace("?","").replace("¿", "").replace("¡", "").replace("!", "").replace("-", "")
    # Modificamos el texto para eliminar todos los símbolos que puedan aparecer, ya que vamos a converitr nuestro texto en listas y separar los elementos
    # por los espacios, de manera que si permanecen los símbolos, podría contar alguna palabra como palabra+símbolo (ejemplo: 'y,' en vez de 'y').
    lista_palabras = texto_sin_simbolos.lower().split()  # Transformamos todo en minúsculas para no tener letras duplicadas, y hacemos la separación
    nueva_lista = [] #Creamos la nueva lista, donde iremos añadiendo las palabras bajo ciertas condiciones
    for palabra in lista_palabras:
        if palabra != palabra_vieja: #Si la palabra no es igual que la palabra que queremos sustituir, la añadimos a la nueva lista.
            nueva_lista.append(palabra)
        else:
            nueva_lista.append(palabra_nueva) #Si la palabra es igual que la que queremos sustituir, añadimos la palabra nueva a la lista.
    texto_nuevo = " ".join(nueva_lista) #Generamos nuestra cadena de texto a partir de la lista que hemos creado
    #MISMA LIMITACIÓN QUE EN LA FUNCIÓN 'eliminar_palabras'
    return texto_nuevo

def procesar_texto(texto, opcion, *args): #Definimos nuestra 'función centralizada', que tendrá como argumentos el texto a analizar, la opción a escoger
    #entre las funciones previamente definidas, y el argumento *args, ya que cada función va a usar un número diferente de argumentos.
    """
    Función central que procesa un texto según la opción indicada: contar, eliminar o reemplazar.

    Args:
    texto (str): Texto sobre el que se realizará la operación.
    opcion (str): Operación que se desea aplicar. Puede ser "contar", "eliminar" o "reemplazar".
    *args: Argumentos adicionales, cuyo número varía en función de la opción seleccionada.

    Returns:
    dict / str / ninguno: Diccionario de frecuencias si la opción es "contar"; texto modificado si la opción es "eliminar" o "reemplazar";
    ninguno si la opción no es válida.
    """
    if opcion == 'contar': #Si nuestra opción es 'contar', usaremos la función contar_palabras con argumento texto
        contar = contar_palabras(texto)
        return contar
    elif opcion == 'eliminar':
        eliminar = eliminar_palabras(texto, args[0]) #Si nuestra opción es 'eliminar', usaremos la función eliminar_palabras con argumento texto, y el
        #argumento args[0] (en este caso, la palabra a eliminar
        return eliminar
    elif opcion == 'reemplazar':
        reemplazar = reemplazar_palabras(texto, args[0], args[1]) #Si nuestra opción es 'eliminar', usaremos la función eliminar_palabras con argumento texto, el
        #argumento args[0] (en este caso, la palabra a sustituir), y el argumento args[1] (en este caso, la palabra nueva)
        return reemplazar
    else:
        print('Esta opción no es válida')

extracto = ( #Nuestro texto, susituible por el texto que se desee
    "Esta mañana salí temprano a caminar por el parque. El parque estaba tranquilo, aunque algunas personas caminaban deprisa hacia el trabajo."
    " Me senté en un banco y observé cómo el sol iluminaba los árboles, los caminos y las hojas caídas. Mientras miraba las hojas, pensé en "
    "lo rápido que cambia todo: cambia el clima, cambia la ciudad y cambia también nuestra forma de ver las cosas. Después compré un café en una "
    "pequeña cafetería cercana. El café estaba caliente, tenía buen aroma y me ayudó a empezar el día con calma, con energía y con una sensación "
    "agradable de tranquilidad.")

punto_control = False #Punto de control, igual que en ejercicios anteriores
select_option = str(input("Seleccione el método a utilizar ('contar', 'reemplazar', 'eliminar'): ")).lower().strip()
#Input para que el usuario elija la opción que desee
if select_option in ['contar', 'reemplazar', 'eliminar']:
    punto_control = True #Si la opción seleccionada está entre las tres definidas, el punto de control se vuelve True
    if select_option == 'contar':
        contar = procesar_texto(extracto, select_option) #Si la opción es contar, pasamos la selección a la función central, con los argumentos
        #texto y opción
        print(contar)
    elif select_option == 'eliminar':
        palabra_eliminada = str(input('Introduzca la palabra a eliminar: ')).lower() #Si la opción es eliminar, pasamos la selección
        # a la función central, con los argumentos texto, opción y args[0], que será palabra_eliminada y será solicitada al usuario
        eliminar = procesar_texto(extracto, select_option, palabra_eliminada)
        print(eliminar)
    elif select_option == 'reemplazar':
        palabra_antigua = str(input('Introduzca la palabra que desea reemplazar: ')).lower()
        palabra_nueva = str(input('Introduzca la palabra a sustituir: ')).lower()#Si la opción es eliminar, pasamos la selección a la función central,
        # con los argumentos texto, opción, args[0] y args[0], que serán palabra_antigua y palabra_nueva, respectivamente. Ambas serán solicitadas al usuario
        reemplazar = procesar_texto(extracto, select_option, palabra_antigua, palabra_nueva)
        print(reemplazar)
if punto_control == False: #Si el punto de control ha permanecido False, significa que no hemos elegido una opción válida, y por lo tanto,
    # aparecerá el siguiente mensaje
    print(
        "El método seleccionado no está disponible. Por favor, escoja un método disponible: 'contar', 'reemplazar' o 'eliminar'")

# 38. Genera un programa que nos diga si es de noche, de día o tarde según la hora proporcionada por el usuario.
try: #Usamos el try para manejar la excepción que definiremos más adelante
    seleccion_hora = int(input("Seleccione el valor de la hora (0-23): ")) #Solicitamos la hora al usuario, y pasamos el valor a int
    seleccion_minutos = int(input("Seleccione el valor de los minutos (0-59): ")) #Solicitamos los minutos al usuario, y pasamos el valor a int
    seleccion_segundos = int(input("Seleccione el valor de los segundos (0-59): ")) #Solicitamos los segundos al usuario, y pasamos el valor a int
    comprobacion_hora = False #Nos marcamos tres banderas para los tres valores de hora, minutos y segundos. El fundamento de este recurso y cómo
    #llegué hasta él lo explico en el ejercicio siguiente. Lo he aplicado varias veces en estas katas ya que me parece muy útil
    comprobacion_minuto = False
    comprobacion_segundo = False
    if 0 <= seleccion_hora <= 23:
        comprobacion_hora = True #Si se cumple esta condición, el valor de comprobacion_hora pasa a ser True
    else:
        pass
    if 0 <= seleccion_minutos <= 59:
        comprobacion_minuto = True #Si se cumple esta condición, el valor de comprobacion_minuto pasa a ser True
    else:
        pass
    if 0 <= seleccion_segundos <= 59:
        comprobacion_segundo = True #Si se cumple esta condición, el valor de comprobacion_segundo pasa a ser True
    else:
        pass
    if comprobacion_hora == False or comprobacion_minuto == False or comprobacion_segundo == False:
        print('Alguno de los valores introducidos no está en el rango correcto. Por favor, introdúzcalos de nuevo')
        #Si alguno de los valores
    else:
        if 6 <= seleccion_hora <= 12:
            #Si la hora está en la franja horaria definida, unimos horas, minutos y segundos en un string y mandamos el mensaje de buenos días
            lista_hora = [str(seleccion_hora), str(seleccion_minutos), str(seleccion_segundos)]
            hora_usuario = ":".join(lista_hora)
            print(f'Son las {hora_usuario} y es de día. ¡Buenos días!')
        elif 13 <= seleccion_hora <= 20:
            # Si la hora está en la franja horaria definida, unimos horas, minutos y segundos en un string y mandamos el mensaje de buenas tardes
            lista_hora = [str(seleccion_hora), str(seleccion_minutos), str(seleccion_segundos)]
            hora_usuario = ":".join(lista_hora)
            print(f'Son las {hora_usuario} y es por la tarde. ¡Buenas tardes!')
        elif 0 <= seleccion_hora <= 5 or 21 <= seleccion_hora <= 23:
            # Si la hora está en la franja horaria definida, unimos horas, minutos y segundos en un string y mandamos el mensaje de buenas noches
            lista_hora = [str(seleccion_hora), str(seleccion_minutos), str(seleccion_segundos)]
            hora_usuario = ":".join(lista_hora)
            print(f'Son las {hora_usuario} y es de noche. ¡Buenas noches!')
except ValueError:
    #Una vez finalizado el bloque try, definimos el bloque except para manejar el ValueError. Si el usuario introduce un dato que no sea un número en
    #el campo de horas, minutos, o segundos, saltará nuestro 'except' y aparecerá el siguiente mensaje:
    print('Por favor, seleccione un número en todos los apartados')

# 39. Escribe un programa que determine qué calificación en texto tiene un alumno en base a su calificación numérica.
# Las reglas de calificación son:
#  - 0 - 69 insuficiente
#  - 70 - 79 bien
#  - 80 - 89 muy bien
#  - 90 - 100 excelente
lista_alumnos = [] #De manera similar a ejercicios anteriores, creamos una lista vacía, la cual llenaremos de diccionarios
for i in range(0, 5):
    #Igualmente, vamos a pedir al usuario que introduzca los datos de los alumnos con un bucle for repetido 5 veces. El usuario
    #tendrá que proporcionar nombre, apellido, ID del alumno y su calificación numérica.
    diccionario = {'nombre': str(input('Ingrese el nombre del alumno (sin tildes): ')).title(),
                   'apellido': str(input('Ingrese el apellido del alumno (sin tildes): ')).title(),
                   'ID': int(input('Ingrese el ID del alumno (código de dos dígitos): ')),
                   'calificacion': int(input('Ingrese la calificacion numérica del alumno (rango: 0-100): '))}
    lista_alumnos.append(diccionario) #Cada vez que se cree un diccionario, se añadirá a la lista creada previamente
ID_alumno = int(input('Ahora ingrese el ID del estudiante que quiera buscar (código de dos dígitos): '))
#Ahora, le pediremos al usuario que introduzca un ID para buscar la información del alumno correspondiente
encontrado = False
#En una consulta en internet, encontré este recurso que me parece muy útil para complementar lo aprendido. Básicamente, pongo una bandera
#o marca asociada la variable 'encontrado', que por defecto será False.
for alumno in lista_alumnos:
    if alumno['ID'] == ID_alumno:
        #El bucle indica que vamos a iterar por cada diccionario de la lista. Dentro de él, el condicional if indica lo que ocurre si encontramos
        #un alumno cuyo 'ID' sea igual al ID introducido por el usuario
        encontrado = True
        #Cuando esto ocurre, cambiamos nuestra variable a True, y la dejamos guardada de esa manera
        if alumno['calificacion'] >= 0 and alumno['calificacion'] <= 69:
            print(f"El alumno con ID {alumno['ID']}, llamado {alumno['nombre']+" "+alumno['apellido']} tiene una calificación de INSUFICIENTE")
        elif alumno['calificacion'] > 69 and alumno['calificacion'] <= 79:
            print(f"El alumno con ID {alumno['ID']}, llamado {alumno['nombre'] + " " + alumno['apellido']} tiene una calificación de BIEN")
        elif alumno['calificacion'] > 79 and alumno['calificacion'] <= 89:
            print(f"El alumno con ID {alumno['ID']}, llamado {alumno['nombre'] + " " + alumno['apellido']} tiene una calificación de MUY BIEN")
        elif alumno['calificacion'] > 89 and alumno['calificacion'] <= 100:
            print(f"El alumno con ID {alumno['ID']}, llamado {alumno['nombre']+" "+alumno['apellido']} tiene una calificación de EXCELENTE")
        #Este bloque es, en conjunto, lo que ocurre en función del alumno que encontremos. Explico el primero, y el resto son equivalentes. Si la
        #calificación del alumno está entre 0 y 69, imprimimos un f-string con una frase que contiene el ID del alumno, su nombre y apellidos, y su
        #calificación convertida a texto, en función de las condiciones establecidas en el enunciado (en este caso, insuficiente)
        break
        #Cuando hemos encontrado a un alumno con el ID coincidente, aplicamos break para parar la iteración y ahorrar recursos (en este caso da un poco
        #igual porque son 5 alumnos, pero es una buena práctica para conjuntos de datos más grandes). Esto lo hacemos porque en teoría no debería haber
        #dos alumnos diferentes con el mismo ID
if encontrado == False:
    #Aquí cobra sentido la bandera puesta anteriormente.Si la variable 'encontrado' se ha quedado como False, quiere decir que no ha encontrado ningún alumno
    #en el diccionario cuyo ID coincida con el introducido por el usuario. Por tanto, no hemos entrado en el primer condicional if, y la variable no ha sido
    #cambiada a True. Entonces, en este caso imprimiremos el mensaje de que el ID del alumno no existe.
    print('El ID de ese alumno no existe')


# 40. Escribe una función que tome dos parámetros: figura (una cadena que puede ser "rectangulo" , "circulo" o
# "triangulo" ) y datos (una tupla con los datos necesarios para calcular el área de la figura).
import math
# Necesitamos el módulo math para el cálculo de pi
def calculo_area(figura, datos): #Definimos la función con los parámetros figura (nombre de la figura) y datos (tupla con los datos)
    """
    Función que calcula el área de una figura geométrica a partir de una tupla de datos.

    Args:
    figura (str): Nombre de la figura. Puede ser "rectangulo", "triangulo" o "circulo".
    datos (tuple): Tupla con los datos necesarios para calcular el área. Para el rectángulo y el triángulo contiene la base y la altura;
    para el círculo, contiene el radio.

    Returns:
    float / ninguno: Área calculada de la figura, o ninguno si la figura indicada no es válida.
    """
    if figura == 'rectangulo': #Si la figura es 'rectangulo', usamos las posiciones de la tupla para calcular nuestro área
        area1 = datos[0] * datos[1]
        return area1 #Devolvemos el área calculada
    elif figura == 'triangulo':
        area2 = (datos[0] * datos[1]) / 2 #Mismo planteamiento que para el rectánculo
        return area2
    elif figura == 'circulo':
        area3 = datos[0]**2 * math.pi #Mismo planteamiento, aquí sólo tendremos un elemento en la tupla (el radio). Invocamos pi a través de math
        return area3
    else:
        print(f"{figura.title()} no es una figura válida, por lo que no se puede realizar la operación")
        #En caso de invocar la función con una figura inválida, tenemos un control flow interno para rechazar el input y exigir uno correcto

figura_valida = False #Mismo planteamiento que en el ejercicio anterior, lo usamos como 'bandera'
seleccion_figura = str(input("Seleccione 'rectangulo', 'triangulo', o 'circulo' (sin tildes): ")).lower().strip()
#Le pedimos al usuario un input del nombre de una figura, lo convertimos a minúscula y le quitamos espacios delante y detrás
if seleccion_figura == 'rectangulo':
    #Si la figura es rectangulo: marcamos nuestra bandera como True; pedimos la base y la altura; llamamos a la función con nuestra figura y
    #nuestra tupla de datos; imprimimos el valor del área
    figura_valida = True
    base_rectangulo = float(input('Seleccione la base del rectángulo (cm): '))
    altura_rectangulo = float(input('Seleccione la altura del rectángulo (cm):'))
    area_rectangulo = calculo_area('rectangulo', (base_rectangulo,altura_rectangulo))
    print(f'El área del rectángulo es {area_rectangulo} cm2')
elif seleccion_figura == 'triangulo':
    #Mismo planteamiento que con el rectángulo
    figura_valida = True
    base_triangulo = float(input('Seleccione la base del triángulo (cm): '))
    altura_triangulo = float(input('Seleccione la altura del triángulo (cm): '))
    area_triangulo = calculo_area('triangulo',(base_triangulo, altura_triangulo))
    print(f'El área del triángulo es {area_triangulo} cm2')
elif seleccion_figura == 'circulo':
    #Mismo planteamiento que con las figuras anteriores, pero esta vez sólo pedimos el radio
    figura_valida = True
    radio_circulo = float(input('Seleccione el radio del círculo (cm): '))
    area_circulo = calculo_area('circulo',(radio_circulo,))
    print(f'El área del círculo es {area_circulo} cm2')
if figura_valida == False:
    #Si nuestra 'bandera' no se marca como True, quiere decir que no se ha seleccionado un nombre de figura válido;
    #por lo tanto, ejecutamos un control flow para indicar que la operación no se puede realizar.
    print('Por favor, seleccione una figura válida para realizar la operación')

#Creo que también habría sido interesante resolver este ejercicio usando el recurso *args en vez de pasar una tupla de para los datos,
#ya que en función de la figura, tendremos que introducir un número diferente de argumentos:
import math
# Necesitamos el módulo math para el cálculo de pi
def calculo_area(figura, *args): #Definimos la función con los parámetros figura (nombre de la figura) y datos (*args)
    """
    Función que calcula el área de una figura geométrica, usando para ello un número variable de argumentos.

    Args:
    figura (str): Nombre de la figura. Puede ser "rectangulo", "triangulo" o "circulo".
    *args: Valores necesarios para calcular el área. Para el rectángulo y el triángulo se esperan base (args[0]) y altura a(args[1];
    para el círculo, se espera el radio.

    Returns:
    float / niguno: Área calculada de la figura, o ninguno si la figura indicada no es válida.
    """
    if figura == 'rectangulo': #Si la figura es 'rectangulo', usamos las posiciones de los *args para calcular nuestro área
        area1 = args[0] * args[1]
        return area1 #Devolvemos el área calculada
    elif figura == 'triangulo':
        area2 = (args[0] * args[1]) / 2 #Mismo planteamiento que para el rectánculo
        return area2
    elif figura == 'circulo':
        area3 = args[0]**2 * math.pi #Mismo planteamiento, aquí sólo tendremos un elemento en *args (el radio). Invocamos pi a través de math
        return area3
    else:
        print(f"{figura.title()} no es una figura válida, por lo que no se puede realizar la operación")
        #En caso de invocar la función con una figura inválida, tenemos un control flow interno para rechazar el input y exigir uno correcto

figura_valida = False #Mismo planteamiento que en el ejercicio anterior, lo usamos como 'bandera'
seleccion_figura = str(input("Seleccione 'rectangulo', 'triangulo', o 'circulo' (sin tildes): ")).lower().strip()
#Le pedimos al usuario un input del nombre de una figura, lo convertimos a minúscula y le quitamos espacios delante y detrás
if seleccion_figura == 'rectangulo':
    #Si la figura es rectangulo: marcamos nuestra bandera como True; pedimos la base y la altura; llamamos a la función con nuestra figura y
    #nuestros datos *args; imprimimos el valor del área
    figura_valida = True
    base_rectangulo = float(input('Seleccione la base del rectángulo (cm): '))
    altura_rectangulo = float(input('Seleccione la altura del rectángulo (cm):'))
    area_rectangulo = calculo_area('rectangulo', base_rectangulo,altura_rectangulo)
    print(f'El área del rectángulo es {area_rectangulo} cm2')
elif seleccion_figura == 'triangulo':
    #Mismo planteamiento que con el rectángulo
    figura_valida = True
    base_triangulo = float(input('Seleccione la base del triángulo (cm): '))
    altura_triangulo = float(input('Seleccione la altura del triángulo (cm): '))
    area_triangulo = calculo_area('triangulo',base_triangulo, altura_triangulo)
    print(f'El área del triángulo es {area_triangulo} cm2')
elif seleccion_figura == 'circulo':
    #Mismo planteamiento que con las figuras anteriores, pero esta vez sólo pedimos el radio
    figura_valida = True
    radio_circulo = float(input('Seleccione el radio del círculo (cm): '))
    area_circulo = calculo_area('circulo',radio_circulo)
    print(f'El área del círculo es {area_circulo} cm2')
if figura_valida == False:
    #Si nuestra 'bandera' no se marca como True, quiere decir que no se ha seleccionado un nombre de figura válido;
    #por lo tanto, ejecutamos un control flow para indicar que la operación no se puede realizar.
    print('Por favor, seleccione una figura válida para realizar la operación')

# 41. En este ejercicio, se te pedirá que escribas un programa en Python que utilice condicionales para determinar el
# monto final de una compra en una tienda en línea, después de aplicar un descuento. El programa debe hacer lo siguiente:
#  1. Solicita al usuario que ingrese el precio original de un artículo.
#  2. Pregunta al usuario si tiene un cupón de descuento (respuesta sí o no).
#  3. Si el usuario responde que sí, solicita que ingrese el valor del cupón de descuento.
#  4. Aplica el descuento al precio original del artículo, siempre y cuando el valor del cupón sea válido (es decir, mayor
#  a cero). Por ejemplo, descuento de 15€.
#  5. Muestra el precio final de la compra, teniendo en cuenta el descuento aplicado o sin él.
#  6. Recuerda utilizar estructuras de control de flujo como if, elif y else para llevar a cabo estas acciones en tu programa de Python.
# 41. En este ejercicio, se te pedirá que escribas un programa en Python que utilice condicionales para determinar el
# monto final de una compra en una tienda en línea, después de aplicar un descuento. El programa debe hacer lo siguiente:
#  1. Solicita al usuario que ingrese el precio original de un artículo.
#  2. Pregunta al usuario si tiene un cupón de descuento (respuesta sí o no).
#  3. Si el usuario responde que sí, solicita que ingrese el valor del cupón de descuento.
#  4. Aplica el descuento al precio original del artículo, siempre y cuando el valor del cupón sea válido (es decir, mayor
#  a cero). Por ejemplo, descuento de 15€.
#  5. Muestra el precio final de la compra, teniendo en cuenta el descuento aplicado o sin él.
#  6. Recuerda utilizar estructuras de control de flujo como if, elif y else para llevar a cabo estas acciones en tu programa de Python.

#He abordado dos estrategias diferentes en este ejercicio. En esta primera, he seguido enteramente las indicaciones del enunciado,
# y he trabajado con el supuesto de que los cupones descuentan un precio fijo del valor original
def calculo_precio1(): #Defino la función
    """
    Función que calcula el precio final de un producto aplicando, si procede, un cupón de descuento fijo en euros.

    Args:
    Ninguno

    Returns:
    float / ninguno: Precio final del producto si la operación es válida, o ninguno si no se puede calcular por una entrada incorrecta.
    """
    try: #Introduzco un primer bloque try, cuyo except salta en caso de ValueError, que se dará mayormente cuando en precio_original se
        #introduzca un valor diferente a un float.
        precio_original = float(input('Introduzca el precio original del artículo (€): '))
        if precio_original < 0:
            print('El precio original debe ser un número positivo')
        elif precio_original == 0:
            print('Si el precio de un producto es 0, no se puede aplicar ningún cupón de descuento')
        else:
            pregunta_cupon = str(input('Dispone de algún cupón de descuento (sí/no): ')).lower().strip()
            #Preguntamos si el usuario dispone de un cupón de descuento, pasando su respuestas por .lower() y. strip() para igualar formatos
            if pregunta_cupon == 'si' or pregunta_cupon == 'sí': #Valoramos que responda sí, tanto con tilde como sin tilde
                try: #Segundo bloque try, también manenjando la excepción de ValueError, que se dará si introducimos algo diferente de un float
                    #en la variable valor_cupon
                    valor_cupon = float(input('Introduzca el valor de su cupón de descuento en €: '))
                    if valor_cupon == 0: #Si el valor del cupón es 0, salta el mensaje diciendo que no se puede aplicar
                        print('El valor del cupón es 0, así que no se puede aplicar')
                        precio_final = precio_original
                        return precio_final
                    elif valor_cupon < 0:
                        print('Introduzca un número mayor que 0')
                    elif valor_cupon > precio_original:
                        print('El valor del cupón supera el del precio del producto, así que no se puede aplicar')
                    else:
                        precio_final = precio_original - valor_cupon
                        return precio_final
                except ValueError: #Bloque except correspondiente al bloque try más interno
                    print('Por favor, introduzca un valor numérico')
            elif pregunta_cupon == 'no':
                precio_final = precio_original
                return precio_final
            else:
                print('Por favor, introduzca una respuesta válida')
    except ValueError: #Bloque except correspondiente al bloque try más externo
        print('Por favor, introduzca un valor numérico')

precio1 = calculo_precio1() #Aplicamos la función y la guardamos en una variable
if precio1 == None:
    pass
else:
    print(f'El precio final de su producto es {precio1} €')

#En este segundo supuesto, por seguir practicando, he abordado un caso a mi parecer más realista, basado en tener cupones que
#aplican el descuento en forma de porcentaje. La estructura de código es la misma, pero he modificado algunos condicionales para
#que se adapten al formato porcentual de los cupones.
def calculo_precio2(): #Defino la función
    """
        Función que calcula el precio final de un producto aplicando, si procede, un cupón de descuento porcentual.

        Args:
        Ninguno

        Returns:
        float / ninguno: Precio final del producto si la operación es válida, o ninguno si no se puede calcular por una entrada incorrecta.
        """
    try: #Introduzco un primer bloque try, cuyo except salta en caso de ValueError, que se dará mayormente cuando en precio_original se
        #introduzca un valor diferente a un float.
        precio_original = float(input('Introduzca el precio original del artículo (€): '))
        if precio_original < 0:
            print('El precio original debe ser un número positivo')
        elif precio_original == 0:
            print('Si el precio de un producto es 0, no se puede aplicar ningún cupón de descuento')
        else:
            pregunta_cupon = str(input('Dispone de algún cupón de descuento (sí/no): ')).lower().strip()
            #Preguntamos si el usuario dispone de un cupón de descuento, pasando su respuestas por .lower() y. strip() para igualar formatos
            if pregunta_cupon == 'si' or pregunta_cupon == 'sí': #Valoramos que responda sí, tanto con tilde como sin tilde
                try:  # Bloque modificado para adaptarse a los cupones en forma de porcentaje.
                    valor_cupon = float(input('Introduzca el valor de su cupón de descuento en % (0-100): '))
                    if valor_cupon == 0:
                        print('El valor del cupón es 0, así que no se puede aplicar')
                        precio_final = precio_original
                        return precio_final
                    elif valor_cupon < 0:
                        print('Introduzca un número mayor que 0')
                    elif valor_cupon > 100:
                        print('Introduzca un número menor que 100')
                    else:
                        precio_final = precio_original - precio_original * (valor_cupon / 100)
                        return precio_final
                except ValueError: #Bloque except correspondiente al bloque try más interno
                    print('Por favor, introduzca un valor numérico')
            elif pregunta_cupon == 'no':
                precio_final = precio_original
                return precio_final
            else:
                print('Por favor, introduzca una respuesta válida')
    except ValueError: #Bloque except correspondiente al bloque try más externo
        print('Por favor, introduzca un valor numérico')

precio2 = calculo_precio2() #Aplicamos la función y la guardamos en una variable
if precio2 == None:
    pass
else:
    print(f'El precio final de su producto es {precio2} €')
