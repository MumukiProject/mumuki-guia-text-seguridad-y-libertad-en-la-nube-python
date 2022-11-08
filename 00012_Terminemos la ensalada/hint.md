Recordá que para aplicar el algoritmo de los emojis a cada letra hicimos lo siguiente:

```python
def cifrar_mensaje_con_emojis(mensaje):
  return ''.join([transformar_letra(letra) for letra in mensaje])
```
