class Test(unittest.TestCase):

  def test_palabra_misteriosa_debería_ser_correcta(self):
    self.assertEquals(descifrar_cesar('ARTUV',2), 'YPRST')
