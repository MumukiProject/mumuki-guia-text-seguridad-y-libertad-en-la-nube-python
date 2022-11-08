def convertir_a_numero(letra):
  return ord(letra) - 65


def convertir_a_letra(numero):
  return chr(numero % 26 + 65)
