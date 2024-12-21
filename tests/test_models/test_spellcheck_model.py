import sys
import unittest
from io import StringIO

from app.models.spellcheck_model import SpellcheckModel


class TestSpellcheckModel(unittest.TestCase):

    def test_print_well_formatted_model(self):

        model = SpellcheckModel("C:\\Users\\Documents\\python\\Spellcheck_various\\dictionary.txt", "C:\\Users\\Documents\\python\\Spellcheck_various", "1", "adoc, doc")
        expected_model_print = (
            f"{model.REPORT_FILE_STRING}: C:\\Users\\Documents\\python\\Spellcheck_various\\dictionary.txt.\n"
            f"{model.DICTIONARY_FILE_STRING}: C:\\Users\\Documents\\python\\Spellcheck_various.\n"
            f"{model.SCAN_MODE_STRING}: 1.\n"
            f"{model.FILE_EXTENSIONS_STRING}: adoc, doc.\n")
        self.assertEqual(str(model), expected_model_print)