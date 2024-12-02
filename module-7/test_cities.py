#Colton Kohler
#Module7.2 Assignment
#12/1/2024
import unittest
from city_functions import city_country

class TestCityCountry(unittest.TestCase):
    """Tests for the function city_country."""

    def test_city_country(self):
        """Test for city_country with two arguments."""
        formatted = city_country("sapporo", "japan")
        self.assertEqual(formatted, "Sapporo, Japan")

    def test_city_country_population(self):
        """Test for city_country with optional population."""
        formatted = city_country("cape town", "south africa", 4773000)
        self.assertEqual(formatted, "Cape Town, South Africa - population 4773000")

    def test_city_country_language(self):
        """Test for city_country with optional language."""
        formatted = city_country("london", "england", 8866000, "english")
        self.assertEqual(formatted, "London, England - population 8866000, English")

if __name__ == "__main__":
    unittest.main()
