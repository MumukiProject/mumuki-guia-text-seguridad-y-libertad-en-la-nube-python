¡Muy bien! Aunque `hash_mumuki` es una función muy rudimentaria y no la usaríamos en la vida real por no ser [segura en términos criptográficos](https://es.wikipedia.org/wiki/Funci%C3%B3n_hash_criptogr%C3%A1fica), nos da una buena idea de cómo se realizan estos cálculos.

¿Y cuándo nos puede servir? Por ejemplo, cuando hay que guardar información sensible. La mayoría de las páginas que almacenan contraseñas guardan su hash; y, al intentar iniciar sesión, se verifica que el hash guardado sea igual al hash de la contraseña ingresada.

```python
if hash_de_la_contrasena_guardada == hash_mumuki(contrasena_ingresada):
  iniciar_sesion()
```

De esta forma si una persona no autorizada accede a esa información no podrá utilizarla. :sunglasses:
