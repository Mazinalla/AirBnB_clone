import unittest
from models.review import Review

class TestReview(unittest.TestCase):

    def test_attributes(self):
        review = Review()
        self.assertEqual(review.place_id, "")
        self.assertEqual(review.user_id, "")
        self.assertEqual(review.text, "")

    def test_to_dict(self):
        review = Review()
        review_dict = review.to_dict()

        expected_keys = ['id', 'created_at', 'updated_at', 'place_id', 'user_id', 'text', '__class__']
        self.assertEqual(set(review_dict.keys()), set(expected_keys))
        self.assertEqual(review_dict['__class__'], 'Review')

    def test_initialization_with_parameters(self):
        review = Review(place_id="place123", user_id="user123", text="Great experience")
        self.assertEqual(review.place_id, "place123")
        self.assertEqual(review.user_id, "user123")
        self.assertEqual(review.text, "Great experience")

    def test_str_representation(self):
        review = Review(place_id="place123", user_id="user123", text="Great experience")
        str_repr = str(review)
        self.assertIn("[Review]", str_repr)
        self.assertIn("'place_id': 'place123'", str_repr)
        self.assertIn("'user_id': 'user123'", str_repr)
        self.assertIn("'text': 'Great experience'", str_repr)

    def test_update_attributes(self):
        review = Review(place_id="place123", user_id="user123", text="Great experience")
        review.update({'text': 'Updated review'})
        self.assertEqual(review.text, 'Updated review')

    def test_update_attributes_invalid(self):
        review = Review(place_id="place123", user_id="user123", text="Great experience")
        review.update({'invalid_attribute': 'Invalid Value'})
        self.assertNotIn('invalid_attribute', review.__dict__)

if __name__ == '__main__':
    unittest.main()
