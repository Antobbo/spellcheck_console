import sys
import unittest
from io import StringIO

from app.models.spellcheck_model import SpellcheckModel


class TestSpellcheckModel(unittest.TestCase):

    def test_print_well_formatted_model(self):
        expected_model_print = ("Report file: C:\\Users\\Documents\\python\\Spellcheck_various\\dictionary.txt.\n"
                                "Dictionary file: C:\\Users\\Documents\\python\\Spellcheck_various.\n"
                                "Scan mode: 1.\n"
                                "File extensions: adoc, doc.\n")
        model = SpellcheckModel("C:\\Users\\Documents\\python\\Spellcheck_various\\dictionary.txt", "C:\\Users\\Documents\\python\\Spellcheck_various", "1", "adoc, doc")
        self.assertEqual(str(model), expected_model_print)