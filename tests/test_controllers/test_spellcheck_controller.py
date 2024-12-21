import unittest
from contextlib import nullcontext

from app.controllers.spellcheck_controller import SpellcheckController
from app.models.spellcheck_model import SpellcheckModel
from app.views.spellcheck_view import SpellcheckView


class TestSpellCheckController(unittest.TestCase):



    def setUp(self):
        model = SpellcheckModel("", "", "", "")
        view = SpellcheckView()
        self.controller = SpellcheckController(view, model)

    def test_validate_inputs_has_no_errors(self):
        dictionary_file = "C:\\Users\\Documents\\python\\Spellcheck_various\\dictionary.txt"
        report_file = "C:\\Users\\Documents\\python\\Spellcheck_various"
        scan_mode = "1"
        file_types = ""
        errors = self.controller.validate_inputs(dictionary_file, report_file, scan_mode, file_types)
        self.assertTrue(len(errors) == 0)

    def test_validate_inputs_has_one_error_dictionary_file(self):
        dictionary_file = ""
        report_file = "C:\\Users\\Documents\\python\\Spellcheck_various"
        scan_mode = "1"
        file_types = ""
        errors = self.controller.validate_inputs(dictionary_file, report_file, scan_mode, file_types)
        self.assertTrue(len(errors) == 1)
        self.assertEqual(errors[0].__str__(), "The value of Dictionary File cannot be empty.")

    def test_validate_inputs_has_one_error_report_file(self):
        dictionary_file = "C:\\Users\\Documents\\python\\Spellcheck_various\\dictionary.txt"
        report_file = ""
        scan_mode = "1"
        file_types = ""
        errors = self.controller.validate_inputs(dictionary_file, report_file, scan_mode, file_types)
        self.assertTrue(len(errors) == 1)
        self.assertEqual(errors[0].__str__(), "The value of Report File cannot be empty.")

    def test_validate_inputs_has_two_errors_dictionary_file_and_report_file(self):
        dictionary_file = ""
        report_file = ""
        scan_mode = "1"
        file_types = ""
        errors = self.controller.validate_inputs(dictionary_file, report_file, scan_mode, file_types)
        self.assertTrue(len(errors) == 2)
        self.assertEqual(errors[0].__str__(), "The value of Dictionary File cannot be empty.")
        self.assertEqual(errors[1].__str__(), "The value of Report File cannot be empty.")
