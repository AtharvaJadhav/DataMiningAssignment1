import unittest
from temperature_converter import TemperatureConverter


class TestTemperatureConverter(unittest.TestCase):

    def test_to_fahrenheit(self):
        self.assertAlmostEqual(TemperatureConverter.to_fahrenheit(0), 32)
        self.assertAlmostEqual(TemperatureConverter.to_fahrenheit(100), 212)

    def test_to_celsius(self):
        self.assertAlmostEqual(TemperatureConverter.to_celsius(32), 0)
        self.assertAlmostEqual(TemperatureConverter.to_celsius(212), 100)

    def test_to_kelvin(self):
        self.assertAlmostEqual(TemperatureConverter.to_kelvin(0), 273.15)
        self.assertAlmostEqual(TemperatureConverter.to_kelvin(-273.15), 0)

    def test_kelvin_to_celsius(self):
        self.assertAlmostEqual(
            TemperatureConverter.kelvin_to_celsius(273.15), 0)
        self.assertAlmostEqual(
            TemperatureConverter.kelvin_to_celsius(373.15), 100)

    def test_fahrenheit_to_kelvin(self):
        self.assertAlmostEqual(
            TemperatureConverter.fahrenheit_to_kelvin(32), 273.15)
        self.assertAlmostEqual(
            TemperatureConverter.fahrenheit_to_kelvin(212), 373.15)

    def test_kelvin_to_fahrenheit(self):
        self.assertAlmostEqual(
            TemperatureConverter.kelvin_to_fahrenheit(273.15), 32)
        self.assertAlmostEqual(
            TemperatureConverter.kelvin_to_fahrenheit(373.15), 212)


# To run the tests:
if __name__ == "__main__":
    unittest.main()
