"""
Translator Module

This module provides functions to translate text between English and French.
"""

from deep_translator import MyMemoryTranslator

translator = MyMemoryTranslator(source='en-US', target='fr-FR')

def english_to_french(english_text):
    """
    Translates English text to French.

    Args:
        english_text (str): The text to be translated.

    Returns:
        str: The translated text in French.
    """
    translation = translator.translate(english_text, to_lang='fr-FR')
    return translation

def french_to_english(french_text):
    """
    Translates French text to English.

    Args:
        french_text (str): The text to be translated.

    Returns:
        str: The translated text in English.
    """
    translator.source = 'fr'
    translator.target = 'en'
    translation = translator.translate(french_text, to_lang='en-US')
    return translation
