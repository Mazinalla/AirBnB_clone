import unittest
from models.city import City

class TestCity(unittest.TestCase):

    def test_attributes(self):
        city = City()
        self.assertEqual(city.state_id, "")
        self.assertEqual(city.name, "")

    def test_to_dict(self):
        city = City()
        city_dict = city.to_dict()

        expected_keys = ['id', 'created_at', 'updated_at', 'state_id', 'name', '__class__']
        self.assertEqual(set(city_dict.keys()), set(expected_keys))
        self.assertEqual(city_dict['__class__'], 'City')

    def test_initialization_with_parameters(self):
        city = City(state_id="state123", name="City Name")
        self.assertEqual(city.state_id, "state123")
        self.assertEqual(city.name, "City Name")

    def test_str_representation(self):
        city = City(state_id="state123", name="City Name")
        str_repr = str(city)
        self.assertIn("[City]", str_repr)
        self.assertIn("'state_id': 'state123'", str_repr)
        self.assertIn("'name': 'City Name'", str_repr)

    def test_update_attributes(self):
        city = City(state_id="state123", name="City Name")
        city.update({'name': 'Updated Name'})
        self.assertEqual(city.name, 'Updated Name')

    def test_update_attributes_invalid(self):
        city = City(state_id="state123", name="City Name")
        city.update({'invalid_attribute': 'Invalid Value'})
        self.assertNotIn('invalid_attribute', city.__dict__)

if __name__ == '__main__':
    unittest.main()
