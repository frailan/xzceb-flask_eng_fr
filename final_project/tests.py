"""
Unit tests for translator module
"""
import unittest
from machinetranslation.translator import english_to_french, french_to_english

class TestsTranslation(unittest.TestCase):
    """
    Test cases for translation functions.
    """

    def test_english_to_french(self):
        """
        Test the translation from English to French.
        """
        translation = english_to_french("Hello")
        self.assertEqual(translation, "Bonjour")
        self.assertNotEqual(translation, "Hola")
        
    def test_french_to_english(self):
        """
        Test the translation from French to English. 
        """
        translation = french_to_english("Bonjour")
        self.assertEqual(translation, "Hello")
        self.assertNotEqual(translation, "Hola")

if __name__ == '__main__':
    unittest.main()
