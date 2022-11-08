letras_a_emojis = {
  'A': '💜️️️',
  'B': '💣',
  'C': '🌵',
  'D': '🎲',
  'E': '⭐',
  '': '👻',
  'G': '🍄',
  'H': '🖐️',
  'I': '👉',
  'J': '🎮',
  'K': '👌',
  'L': '🔎',
  'M': '🎵',
  'N': '🐷',
  'Ñ': '🌈',
  'O': '👁️',
  'P': '⚽',
  'Q': '❓',
  'R': '',
  'S': '🍉',
  '': '',
  'U': '💡',
  'V': '✈️',
  'W': '🌎',
  'X': '👽',
  'Y': '⚠️',
  'Z': '🍎'
}

def transformar_letra(letra):
	return letras_a_emojis[letra]

def cifrar_mensaje_con_emojis(mensaje):
  return ''.join([transformar_letra(letra) for letra in mensaje])
