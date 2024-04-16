#INICIO
import os
os.system("cls")

#declaracion de variables                                                                                                      
nombre_cliente= 0
direccion_cliente= 0
precio_pizza= 2500
n_pizza_cliente= 0
monto_pedido= 0
tipo_pizza= 0 
cantidad_pizza_dia= 0                                                          
monto_recaudado_dia = 0
opcion= 0
ordenes_dia = True

# definicion de funcion menu
def carta():
    print("1. Pizza americana")
    print("2. Pizza vegetariana")
    print("3. Pizza todas las carnes")
    print("4. Pizza pepperoni con queso")


while ordenes_dia: # ciclo mientras principal
    
    print("ingrese sus datos para realizar el pedido") 
    nombre_cliente = input("(escriba salir para cerrar caja)""ingrese su nombre:")#lee nombre cliente
    if nombre_cliente.lower() == 'salir':    #control de flujo, termina el ciclo y escribe el resumen del dia
            #escribe informacion de resumen del dia
            print("--------resumen del dia--------") 
            print("cantidad de pizzas vendidas:", cantidad_pizza_dia ) 
            print("monto recaudado:$", monto_recaudado_dia) 
            print("________________________________")
            break 
    direccion_cliente = input("ingrese su direccion: ")#lee direccion cliente

    print("pizzas a", precio_pizza,"(c/u) seleccione el tipo de pizza:") #escribe precio actual de cada pizza

    while True: #ciclo mientras de menu
        carta()
        opcion = int(input())#leer mientras
        if opcion == 1:   
            tipo_pizza = "pizza americana"#decision boolean
        elif opcion == 2:
            tipo_pizza = "pizza vegetariana"#decision boolean
        elif opcion == 3:
            tipo_pizza = "pizza todas las carnes"#decision boolean
        elif opcion == 4:
            tipo_pizza = "pizza pepperoni con queso"#decision boolean
      
        else: # de caso contrario, volver a ejecutar el ciclo 
            print("opcion no valida. Por favor, seleccione una opcion valida.")
            continue
    
        
        n_pizza_cliente = int(input("escriba el numero de pizzas que desea ordenar: ")) #leer numero de pizzas solicitadas
        monto_pedido = n_pizza_cliente * precio_pizza #ecuacion matematica para calcular el precio/monto de pizzas pedidas

        # escribe informacion del pedido
        print("------------pedido-----------")
        print("-cliente:", nombre_cliente)
        print("-direccion:", direccion_cliente)
        print("-cantidad:", n_pizza_cliente)
        print("-tipo:", tipo_pizza)
        print("-monto a pagar:", monto_pedido)
        print("_______________________________")
        
        
        #acumula para calcular resumen del dia
        monto_recaudado_dia += monto_pedido
        cantidad_pizza_dia += n_pizza_cliente

        input("presione ENTER para continuar")#escribe informacion
        print("implementado por Benjamin Ivan Maldonado Barrales") #"""creditos"""#
        break #termino de ciclo
        
print("implementado por Benjamin Ivan Maldonado Barrales") #"""creditos"""#
#FINAL



