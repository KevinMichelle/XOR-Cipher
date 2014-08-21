import sys
import random
import codecs
		
def generador(numero, longitud):
    numero = int(numero)
    longitud = int(longitud)
    llaves = []
    i = 0
    while i < numero:
        llave = []
        j = 0
        while j < longitud:
            temp = random.randrange(33, 126)
            caracter = unichr(temp)
            llave.append(caracter)
            j = j + 1
        llaves.append(''.join(llave))
        i = i + 1
    archivo = codecs.open('alice.key', 'w', 'utf-8')
    otro = codecs.open('bob.key', 'w', 'utf-8')
    salto = unichr(ord('\n'))
    for i, k in enumerate(llaves):
        archivo.write(k + salto)
        otro.write(k + salto)
    archivo.close()
    otro.close()
	
 
if len(sys.argv) != 3:
    print 'El número de argumentos es inválido'
else:
    if sys.argv[1].isdigit() and sys.argv[2].isdigit():
	    if sys.argv[1] > 1 and sys.argv[2] > 1:
		    generador(sys.argv[1], sys.argv[2])
        #else:
		 #   print 'Los números deben ser mayores que 0'
    else:
	    print 'Todos los argumentos deben ser numeros'
