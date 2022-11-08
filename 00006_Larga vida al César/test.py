class Test(unittest.TestCase):

  def test_3_lugares_con_una_A_debería_ser_una_D(self):
    self.assertEquals(desplazar_hacia_adelante('A',3), 'D')

  def test_1_lugares_con_una_Z_debería_ser_una_A(self):
    self.assertEquals(desplazar_hacia_adelante('Z',1), 'A')
