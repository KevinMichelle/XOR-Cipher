import sys
import codecs

def xorcipher(filename, fkeyone, fkeytwo):
    try:
        archivo = codecs.open(filename, 'r', 'utf-8')
        keyone = codecs.open(fkeyone, 'r', 'utf-8')
        keytwo = codecs.open(fkeytwo, 'r', 'utf-8')
    except IOError, e:
        print 'Error al abrir alguno de los archivos'
	print e
    else:
        plaintext = archivo.read()
        klone = keyone.read().splitlines()
        kltwo = keytwo.read().splitlines()
        llaveuno = klone[0]
        llavedos = kltwo[0]
	ciphertext = []
	#Encriptar el "plaintext"
    for i, caracter in enumerate(plaintext):
        cipher = ord(llaveuno[i % len(llaveuno)]) ^ ord(caracter)
        ciphertext.append(unichr(cipher))
	klone.pop(0)
	print 'CIPHERTEXT'
	print ''.join(ciphertext)
	mensaje = []
	#Desencriptar el "ciphertext"
	for i, caracter in enumerate(ciphertext):
	    car = ord(llavedos[i % len(llavedos)]) ^ ord(caracter)
	    mensaje.append(unichr(car))
	kltwo.pop(0)
	print 'PLAINTEXT'
	print ''.join(mensaje)
	archivo = codecs.open('alice.key', 'w', 'utf-8')
	otro = codecs.open('bob.key', 'w', 'utf-8')
	salto = unichr(ord('\n'))
	if len(klone) >= 1:
		for i, k in enumerate(klone):
		    archivo.write(k + salto)
		archivo.close()
		for i, k in enumerate(kltwo):
			otro.write(k + salto)
		otro.close()
	else:
		archivo.close()
		otro.close()


if len(sys.argv) == 4:
    filename = sys.argv[1]
    fkeyone = sys.argv[2]
    fkeytwo = sys.argv[3]
    xorcipher(filename, fkeyone, fkeytwo)
else:
    print 'Todos los argumentos deben ser numeros'
