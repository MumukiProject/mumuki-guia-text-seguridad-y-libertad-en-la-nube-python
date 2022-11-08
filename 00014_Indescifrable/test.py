class Test(unittest.TestCase):

  def test_debería_transformar_la_palabra_en_el_numero_correcto(self):
    self.assertEquals(hash_mumuki('me van a hashear'), 2635041755969520934347140)
