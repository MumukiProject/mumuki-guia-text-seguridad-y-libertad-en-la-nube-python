class Test(unittest.TestCase):

  def test_palabra_en_emojis_debería_ser_correcto(self):
    self.assertEquals(cifrar_mensaje_con_emojis('FRT'), '👻🤖🎹')
