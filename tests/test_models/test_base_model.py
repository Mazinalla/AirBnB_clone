import unittest
import datetime
from models.base_model import BaseModel

class TestBaseModel(unittest.TestCase):

    def test_init(self):
        # Test the initialization of BaseModel
        base_model_instance = BaseModel()
        self.assertTrue(hasattr(base_model_instance, 'id'))
        self.assertTrue(hasattr(base_model_instance, 'created_at'))
        self.assertIsNone(base_model_instance.updated_at)
        self.assertFalse(base_model_instance.soft_deleted)

    def test_init_with_kwargs(self):
        # Test initialization with kwargs
        data = {
            'id': '123',
            'created_at': '2022-03-09T12:34:56.789',
            'updated_at': '2022-03-10T08:45:30.123',
            'soft_deleted': True,
            'custom_attribute': 'custom_value'
        }
        base_model_instance = BaseModel(**data)

        self.assertEqual(base_model_instance.id, '123')
        self.assertTrue(hasattr(base_model_instance, 'custom_attribute'))
        self.assertEqual(base_model_instance.custom_attribute, 'custom_value')
        self.assertTrue(base_model_instance.soft_deleted)
        self.assertIsInstance(base_model_instance.created_at, datetime.datetime)
        self.assertIsInstance(base_model_instance.updated_at, datetime.datetime)

    def test_str_representation(self):
        # Test the string representation of BaseModel
        base_model_instance = BaseModel()
        str_representation = str(base_model_instance)
        self.assertIn('BaseModel', str_representation)
        self.assertIn(base_model_instance.id, str_representation)

    def test_save_method(self):
        # Test the save method and updated_at timestamp
        base_model_instance = BaseModel()
        initial_updated_at = base_model_instance.updated_at
        base_model_instance.save()
        self.assertNotEqual(initial_updated_at, base_model_instance.updated_at)

    def test_save_method_without_timestamp_update(self):
        # Test the save method without updating the timestamp
        base_model_instance = BaseModel()
        initial_updated_at = base_model_instance.updated_at
        base_model_instance.save(update_timestamp=False)
        self.assertEqual(initial_updated_at, base_model_instance.updated_at)

    def test_soft_delete_method(self):
        # Test the soft_delete method
        base_model_instance = BaseModel()
        base_model_instance.soft_deleted()
        self.assertTrue(base_model_instance.soft_deleted)
        self.assertIsNotNone(base_model_instance.updated_at)

    def test_to_dict_method(self):
        # Test the to_dict method
        data = {
            'id': '123',
            'created_at': '2022-03-09T12:34:56.789',
            'updated_at': '2022-03-10T08:45:30.123',
            'soft_deleted': True,
            'custom_attribute': 'custom_value'
        }
        base_model_instance = BaseModel(**data)
        obj_dict = base_model_instance.to_dict()

        self.assertEqual(obj_dict['id'], '123')
        self.assertEqual(obj_dict['custom_attribute'], 'custom_value')
        self.assertTrue(obj_dict['soft_deleted'])
        self.assertIn('created_at', obj_dict)
        self.assertIn('updated_at', obj_dict)

if __name__ == '__main__':
    unittest.main()
