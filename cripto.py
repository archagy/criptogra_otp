import random
import string
from random import choice
startchar = ' ' #usar ascii desde 32
endchar ='~'	#hasta 126
modular= ord(endchar) - ord(startchar)+1 #variable modular sirve para calcular parte del encriptado y desencriptado

def keychar(cantidad):   #Genera llave segun la cantidad del mensaje
    key= ''.join(random.choice(string.letters) for i in range(cantidad))
    return key


	##encripta el mensaje tomando las llaves de el archivo personaA
def encriptar(mensaje):
	num=[]
	llave=[]
	res=""
	with open("personaA.txt","r+") as f:
		keys= f.readlines()
		keychar=keys[0].rstrip("\n")
	for i in range(len(mensaje)):
		messagechar = ord(mensaje[i]) - ord(startchar) 
		k =ord(keychar[i]) - ord(startchar) ##se aplica el filtro
		calculatedchar = int((messagechar) + k) % modular
		convertedchar = chr(calculatedchar + ord(startchar))
		res += convertedchar
	print res
	f.close()
	return res

	##Desencripta el mensaje tomando las llaves de el archivo personaB
def desencriptar(mensaje):
	num=[]
	llave=[]
	res=""
	with open("personaB.txt","r+") as f:
		keys= f.readlines()
		keychar=keys[0].rstrip("\n")
	for i in range(len(mensaje)):
		messagechar = ord(mensaje[i]) - ord(startchar)
		k=ord(keychar[i]) - ord(startchar)
		calculatedchar = int((messagechar) - k) % modular	
		convertedchar = chr(calculatedchar + ord(startchar))
		res += convertedchar

	print res
	f.close()
	return res		
#Generador de llaves...Genera llaves en un archvo
def generatorkeys(total_mensajes, cantidad):
	personaA=open("personaA.txt","w+")
	personaB=open("personaB.txt","w+")
	for i in range(total_mensajes):
		for j in range(cantidad):           
			valor = ord(keychar(cantidad)[i]) - ord(startchar)
			personaA.write(str(valor))
			personaB.write(str(valor))
		personaA.write("\n")
		personaB.write("\n")
	personaA.close()
	personaB.close()
    

				
		

def main():    
	total_mensajes = int(raw_input("Total de mensajes:"))#Cantidad de mensajes
	cantidad = int(raw_input("Longitud del mensaje:"))#longitud del mensaje
	generatorkeys(total_mensajes,cantidad)
	cond=True
	contador=1
	while cond:
		mensaje= raw_input("Introduce mensaje: ")
		if(total_mensajes==contador): ##Contador...al finalizar todos los mensajes se termina el programa
			
			print  "\t\tTerminaron los mensajes\n\n"
			cond= False
			
		else:
			
			contador+=1
		mensaje = mensaje.lower()
		print "Persona A envia mensaje: \n"
		encriptar(mensaje) #encripta mensaje
		print "Persona B desencripta: \n"
		desencriptar(encriptar(mensaje))#Desencripta mensaje
		
main()
