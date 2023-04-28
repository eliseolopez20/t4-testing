
from src.clock_factory import *
from unittest import TestCase

"""
 Este archivo contiene un test demo que la unica funcion es ejecutar metodos
 del ClockFactory para probar la libreria de coverage.
 Tienen que remplazar o eliminar este test cuando desarrollen su tarea.
"""

from src.clock_factory import ClockFactory

class TestClockFactory(TestCase):

    def test_create(self):
        new_clock = ClockFactory()
        clock = new_clock.create("hh:mm:ss:mmmm")
        clock.increment()
        self.assertEqual(clock.str(), "00:00:00:01")



        # Test str method
        clock.numbers[0].value = 23
        clock.numbers[1].value = 59
        clock.numbers[2].value = 59
        clock.numbers[3].value = 999
        self.assertEqual(clock.str(), "23:59:59:999")

        # Test clone method
        clock_clone = clock.clone()
        self.assertEqual(clock_clone.str(), "23:59:59:999")
        clock_clone.increment()
        self.assertEqual(clock_clone.str(), "00:00:00:00")
        self.assertEqual(clock.str(), "23:59:59:999")

        

    def test_reset(self):
        new_clock = ClockFactory()
        clock = new_clock.create("hh:mm:ss:mmmm")
        clock.numbers[0].value = 10
        clock.numbers[1].value = 10
        clock.numbers[2].value = 10
        clock.numbers[3].value = 10
        clock_clone = clock.clone()
        clock_clone.numbers[0].reset()
        clock_clone.numbers[1].reset()
        clock_clone.numbers[2].reset()
        clock_clone.numbers[3].reset()
        self.assertEqual(clock_clone.str(), "00:00:00:00")
    
    def test_invariant(self):
        new_clock = ClockFactory()
        clock = new_clock.create("hh:mm")
        self.assertEqual(True, clock.invariant())
        clock.numbers[0].value = 25
        self.assertFalse(clock.invariant())

    """ def test_invalid_change_of_operation(self):
        new_clock = ClockFactory()
        clock = new_clock.create("hh:mm:ss")
        clock.numbers[0] = 15
        clock.numbers[1] = 55
        clock.numbers[2] = 59
        clock_clone = clock.clone()
        clock_clone.increment()
        self.assertEqual(clock_clone.str(), "15:56:00")
        print(clock_clone.str())
        print("LOOOOOOOL") """
       
    def test_less_than_or_equal(self):
        new_clock = ClockFactory()
        clock = new_clock.create("hh:mm:ss")
        clock_clone = clock.clone()
        clock_clone.numbers[1].value = 10
        clock_clone.str()
        self.assertEqual(clock_clone.str(), "00:10:00")

    def test_invariant_less_than_or_equal(self):
        new_clock = ClockFactory()
        clock = new_clock.create("hh:mm:ss")
        clock_clone = clock.clone()
        clock_clone.numbers[2].value = 60
        self.assertFalse(clock_clone.invariant())




        


