class Test(unittest.TestCase):

  def test_palabra_misteriosa_debería_ser_correcta(self):
    self.assertEquals(cifrar_con_cesar('ABCDEZ', 2), 'CDEFGB')
