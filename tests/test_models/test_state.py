import unittest
from models.state import State

class TestState(unittest.TestCase):

    def test_attributes(self):
        state = State()
        self.assertEqual(state.name, "")

    def test_to_dict(self):
        state = State()
        state_dict = state.to_dict()

        expected_keys = ['id', 'created_at', 'updated_at', 'name', '__class__']
        self.assertEqual(set(state_dict.keys()), set(expected_keys))
        self.assertEqual(state_dict['__class__'], 'State')

    def test_initialization_with_parameters(self):
        state = State(name="California")
        self.assertEqual(state.name, "California")

    def test_str_representation(self):
        state = State(name="California")
        str_repr = str(state)
        self.assertIn("[State]", str_repr)
        self.assertIn("'name': 'California'", str_repr)

    def test_update_attributes(self):
        state = State(name="California")
        state.update({'name': 'Updated State'})
        self.assertEqual(state.name, 'Updated State')

    def test_update_attributes_invalid(self):
        state = State(name="California")
        state.update({'invalid_attribute': 'Invalid Value'})
        self.assertNotIn('invalid_attribute', state.__dict__)

if __name__ == '__main__':
    unittest.main()
