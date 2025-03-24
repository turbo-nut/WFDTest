import unittest
from partA import Vehicle, Motorbike


class VehicleTestCase(unittest.TestCase):
    def testIfInstance(self):
        toyota = Vehicle('prius', 2004, 170, 50750, 'red')
        self.assertTrue(isinstance(toyota, Vehicle),
                        'Object is not an instance of Vehicle.')

    def testIfNotInstance(self):
        harley = "real motorbike"
        self.assertFalse(isinstance(harley, Vehicle),
                         'Object is an instance of vehicle')

    def twinTests(self):
        car1 = Vehicle('prius', 2004, 170, 50750, 'red')
        car2 = Vehicle('prius', 2004, 170, 50750, 'blue')
        self.assertFalse(car1 == car2, 'Objects are not equal')

    def checkUpdatedName(self):
        toyota = Vehicle('prius', 2004, 170, 50750, 'red')
        toyota.setName('carolla')
        self.assertTrue(toyota.name == 'carolla', 'Update method not working')

    def checkUpdatedInsurance(self):
        harley = Motorbike('Cruiser', 1995, 250, 10500,
                           'black', 'John Doe', True)
        harley.setInsurance(False)
        self.assertTrue(harley.isInsured is False, 'Update method not working')


if __name__ == "__main__":
    unittest.main()
