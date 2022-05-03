import random

# Dimensión  Claro de los sueños

# items
#Los items de tipo (sk)  "Especial" sirven para tener 2 turnos seguidos,es decir,que el rival se pierda su tuno por alguna razón
#Los items de tipo  (a) "Ataque" incrementan la fuerza
#Los items de tipo (s) "Sanacion" incrementan la vida
#Los items de tipo (p) "Precicison" incrementan la precision,obviamente
#Los items de tipo (vel) "Velocidad" incrementan la velocidad



objetos_sueños =         [
                                          #    bebe de la clase -> items(   )
                                          Items('Cohete Propulsor','a',random.randrange(1,4),"Con este cohete haras mucho daño",1),
                                          Items('Brebaje de lagrimas de Hada','s',random.randrange(10,20),"Esta bebida mejora la salud, se activa en el 2 turno",3),
                                          Items('Bote Hoodlum Red','a',random.randrange(10,20),"Con la tecnologia hoodlum podras golpear más fuerte",1)
                                          ]

#                                      Nombre, Vida, Ataque, Defensa, Precision, Velocidad 
villanos_sueños = [
                                        #    bebe de la clase -> Mob(   )
                       Mob('Hoodlum', 100, 20, 20, 10, 20),
                       Mob('Lum Oscuro', 120,10,5,20,20),
                       Mob('Rayma Oscuro',50,25,20,35,20)
   
                                  ]
rayman = Jugador('Rayman'150,45,50,50,25)

#Dimension Claro de los Sueños
dimension_sueños( 'Claro de los Sueños', [ [objetos_sueños[0], objetos_sueños[1], objetos_sueños[2] ], [ villanos_sueños[0], villanos_sueños[0], villanos_sueños[0] ] )


probabilidad = random.randrange(-2,4) #Esta es la probabilidad de encontrarte a leptys

boss = 'Leptys',200,50,5,10,5

#--Funciones--
def opciones():
   while True:
      
      print()
      print(' Atacar (a) ')
      print(' Defenderte (d) ' )
      print(' Huir (h) ')
      respuesta = input('Que quieres hacer? ')
      if respuesta in ['a','d','h']:
         break
         return respuesta
      else:
         print(' ',respuesta,' no es una opcion válida \n')
#--------------------
#---START BOSS BATTLE ---  
if probabilidad > 0:
                  print(' Te has encontrado con Leptys ')
                  print('\n Que vas ha hacer? ')
                  ronda = 1
                  while boss.vida > 0:
                     if perico.vida > 0:
                        break
                        
                     print(ronda,' con Leptys')
                     
                     recogida = opciones()
                     
                     
                     
                  
                     
                  
                  

