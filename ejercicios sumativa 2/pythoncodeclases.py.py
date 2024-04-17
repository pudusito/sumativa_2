'''INICIO'''

#declaracion de variables
contador = 0
promedio = 0
suma = 0
cantidad_personas = 0
edad = 0
mayor_edad = 0
menor_edad = 0

print("A cuantas personas se le preguntara la edad:")#escribe un titulo
cantidad_personas=int(input()) #lee el numero de la cantidad de personas

while contador < cantidad_personas: #ciclo mientras
    contador=contador + 1 #contador y guarda en la variable contador
    print("edad" , contador) #escribe edad y muestra la variable contador
    edad=int(input()) #lee, pregunta la edad numerica y guarda en variable edad
    suma = suma + edad #operacion suma y guarda en variable suma
    if edad >= 18: #control de flujo SI
        mayor_edad=mayor_edad + 1 #contador de cuantos mayores de edad hay, guarda en variable mayor edad
    elif edad < 18: #control de flujo SINO
           menor_edad=menor_edad + 1 #contador de cuantos menores de edad hay,guarda en variable menor edad
    
promedio = suma / cantidad_personas #operacion matematica para sacar el promedio de edad, lo guarda en variable promedio
print("el promedio de edad es:", promedio) #escribe un titulo y muestra la variable promedio
print("los menores de edad son:", menor_edad)#escribe un titulo y muestra la variable menor de edad
print("los mayores de edad son:", mayor_edad)#escribe un titulo y muestra la variable mayor de edad
print("este algoritmo fue desarrolado por Benjamin Ivan Maldonado Barrales")#escribe creditos del autor
      

'''FINAL'''