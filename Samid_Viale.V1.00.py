while True:
    firstA=(input( " Mauro Viale: Usted viene a defender el/la/los: ""\n" 
    "A)Compre Argentino" "\n"
    "B) La convertibilidad"  "\n"
    "C)la libre exportación" "\n")).lower()
    if firstA != "a":
        print("Incorrecto! Mauro Viale no dijo esa frase. Cualquier apoyo por parte de B o C no tendría sentido para un empresario exportador como Alberto Samid.""\n"
        "No le convendría defender B porque los productos argentinos en el extranjero a un dolar alto(1-1) perderían competitividad; y si defendiera la libre exportación" "\n"
        "sus productos no podrían competir contra los precios de los productos extranjeros, mucho más baratos." )
    else: 
        print("Correcto, eso es lo que dijo Mauro Viale.A Alberto Samid le conviene tener una moneda devaluada, ya veremos sus motivos.")
        break
while True:
    firstB=(input("Si la moneda es fuerte, los productos nacionales van a encarecerse, pero eso beneficia al importador/exportador/ninguno:"))
    prefixes=("imp","Imp")
    
    if firstB.startswith(prefixes):
        print("Correcto,la Argentina practicó una política de puertas abiertas al comercio exterior durante los 90, beneficiando a los consumidores al tener productos baratos" "\n"
        "mientras pudiesen pagarlos, y a los importadores que los insertaban en el mercado interno, en desmedro de la industria nacional, por eso Samid responde:""\n"
        "Si tenemos una moneda menos fuerte, acá se van a empezar a abrir las fábricas." )
        break
    else:
        print("Incorrecto, una moneda más fuerte impediría que Samid pudiese competir, y no podría no beneficiar a ninguno, los tipos de cambio siempre benefician al" "\n"
        "importador/exportador")
        continue

while True:
    firstC=(input("Pague sus impuestos Alberto: ¿cuántos millones debe Alberto Samid?: " "\n"))
    secondC=int(firstC)
    if secondC <=65:
        print("Muy poco! debe más!")
    elif secondC >=75:print("Samid no debe tanto")
    else:
        print("Samid debe 70 millones! Muy bien, Samid fue condenado a prisión efectiva por evasión impositiva en el 2019. ")
    break

print("Digame como se llama")
import time
name = input("Dígame como se llama ")
print ("Si usted me dice como se llama yo le respondo lo que usted quiera.")
time.sleep(1)
print ("Vamos a adivinar mi nombre...")
time.sleep(0.5)
word = ("mauriciogoldfarb")
guesses = ''
turns = 10
while turns > 0:         

    failed = 0             

    for char in word:      

        if char in guesses:    
    
            print (char,end=""),    

        else:
    
            print ("_",end=""),     
       
            failed += 1    

    if failed == 0:        
        print ("Adivinaste mi nombre! Usted se tiene que arrepentir de lo que dijo,como va a decir semejante barbaridad,vamos a pelear!")
    
        break            
    guess = input("Adivina mi nombre:") 
    guesses += guess                    
    if guess not in word:  
 
        turns -= 1        
        print ("Mal!")  

        print ("Te quedan estos", + turns, 'Mas chances' )
 
        if turns == 0:           
    
        
            print ("Perdiste!"  )

import random

opciones=("insulto","golpe", "patadita")

player= None

computer=random.choice(opciones)

while player not in opciones:
     player=(input("Cual va a ser tu estrategia de ataque? insulto, golpe o patadita?"))
print(f"player{player}")
print(f"computer{computer}")

import random
opciones=("insulto","golpe", "patadita")
player= None
computer=random.choice(opciones)
while player not in opciones:
     player=(input("Cual va a ser tu estrategia de ataque? insulto, golpe o patadita?"))
print(f"Samid : {player}")
print(f"Viale: {computer}")

if player== computer:
     print("Es un empate! judio hijo de puta te voy a matá")
elif player== "insulto" and computer == "golpe":
     print("*Ruido de golpe sobre una quijada* el insulto no puede ganarle a un golpe!")
elif player=="insulto" and computer=="patadita":
     print("heriste mis sentimientos! un insulto  duele más que una simple patada!")
elif player=="golpe" and computer =="insulto":
     print("*Ruido de golpe sobre una quijada* el insulto no puede ganarle a un golpe!")
elif player=="golpe" and computer== "patadita":
     print("La patadita le gana a un golpe por ser más humillante.Ejemplificado por el viejito que le pega a Viale")
elif player=="patadita" and computer=="insulto":
     print("heriste mis sentimientos! un insulto  duele más que una simple patada!")
elif player== "patadita" and computer =="golpe":
     print("La patadita le gana a un golpe por ser más humillante.Ejemplificado por el viejito que le pega a Viale")
print("Al final, Mauro Viale se plantó contra alguien mucho más pesado, nunca revelandole su nombre, mientras que  Samid no dejó marchitar su honor. Salud a ambos guerreros! ")




