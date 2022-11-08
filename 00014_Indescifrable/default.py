def hash_mumuki(mensaje):
	tamanio_mensaje = 0 # completar

	return sum([
		ord(letra) * (31 ** (tamanio_mensaje - (posicion + 1)))
		for (posicion, letra)
		in enumerate(mensaje)
	])
