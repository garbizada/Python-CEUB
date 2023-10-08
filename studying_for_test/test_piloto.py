import unittest
from piloto import Piloto

class TestPilot(unittest.TestCase):
  def setUp(self):
    self.piloto1 = Piloto('Ayrton', 'Senna', 2000)
    self.piloto2 = Piloto('Alain', 'Prost', 2000)
    self.piloto3 = Piloto('Felipe', 'Massa', 500)


  def test_email(self):
    self.assertEqual(self.piloto1.email, 'Ayrton.Senna@email.com.br')
    self.assertEqual(self.piloto2.email, 'Alain.Prost@email.com.br')
    self.assertEqual(self.piloto3.email, 'Felipe.Massa@email.com.br')

    self.piloto3.nome = "Roberto"
    self.piloto3.sobrenome = "PupoMoreno"

    self.assertEqual(self.piloto3.email, "Roberto.PupoMoreno@email.com.br")

    def test_nome_completo(self):
      self.assertEqual(self.piloto1.nome_completo, 'Ayrton Senna')
      self.assertEqual(self.piloto2.nome_completo, 'Alain Prost')
      self.assertEqual(self.piloto3.nome_completo,'Felipe Massa')

    def test_aumentar_salario(self):
      self.piloto1.aumentar_salario()
      self.piloto2.aumentar_salario()
      self.piloto3.aumentar_salario()

      self.assertEqual(self.piloto1.salario, 2200)
      self.assertEqual(self.piloto2.salario, 2200)
      self.assertEqual(self.piloto3.salario, 1500)


if __name__ == '__main__':
  unittest.main()







