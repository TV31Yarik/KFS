import unittest
from kfs.lab2 import energy_counter, DETEK, tarif_day, tarif_night

class TestEnergyCounter(unittest.TestCase):
    
    def setUp(self):
        self.counter = energy_counter(1, "2025-03-30", 500, 300)
    
    def test_update_existing_counter(self):
        self.counter.change_inf("2025-03-31", 550, 320)
        self.assertEqual(self.counter.day_inf, 550)
        self.assertEqual(self.counter.night_inf, 320)
    
    def test_add_new_counter(self):
        manager = DETEK()
        manager.counters = []
        manager.add_or_update_counter(3, "2025-03-30", 400, 250)
        self.assertEqual(len(manager.counters), 1)
        self.assertEqual(manager.counters[0].number, 3)
    
    def test_lowered_night_reading(self):
        self.counter.change_inf("2025-03-31", 550, 290) 
        self.assertEqual(self.counter.night_inf, 290 + 80)
    
    def test_lowered_day_reading(self):
        self.counter.change_inf("2025-03-31", 480, 320) 
        self.assertEqual(self.counter.day_inf, 480 + 100)
    
    def test_lowered_both_readings(self):
        self.counter.change_inf("2025-03-31", 480, 290)  
        self.assertEqual(self.counter.day_inf, 480 + 100)
        self.assertEqual(self.counter.night_inf, 290 + 80)

if __name__ == "__main__":
    unittest.main()

