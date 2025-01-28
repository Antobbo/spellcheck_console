import os
import tempfile
import unittest
from contextlib import nullcontext

from app.controllers.spellcheck_controller import SpellcheckController
from app.models import spellcheck_model
from app.models.spellcheck_model import SpellcheckModel
from app.views.spellcheck_view import SpellcheckView


class TestSpellCheckController(unittest.TestCase):

    def setUp(self):
        model = SpellcheckModel("", "", "", "")
        view = SpellcheckView()
        self.controller = SpellcheckController(view, model)

    #INPUT VALIDATION
    def test_should_validate_inputs_have_no_errors(self):
        dictionary_file = self.get_file("dictionary.txt")
        report_file = "C:\\Users\\Documents\\python\\Spellcheck_various"
        scan_mode = "1"
        file_types = ""
        errors = self.controller.validate_inputs(dictionary_file, report_file, scan_mode, file_types)
        self.assertTrue(len(errors) == 0)
        self.delete_file(dictionary_file)

    def test_should_validate_inputs_have_one_empty_error_dictionary_file(self):
        dictionary_file = ""
        report_file = "C:\\Users\\Documents\\python\\Spellcheck_various"
        scan_mode = "1"
        file_types = ""
        errors = self.controller.validate_inputs(dictionary_file, report_file, scan_mode, file_types)
        self.assertTrue(len(errors) == 1)
        self.assertEqual(errors[0].__str__(), "The value of Dictionary File cannot be empty.")

    def test_should_validate_inputs_have_one_empty_error(self):
        dictionary_file = self.get_file("dictionary.txt")
        report_file = ""
        scan_mode = "1"
        file_types = ""
        errors = self.controller.validate_inputs(dictionary_file, report_file, scan_mode, file_types)
        self.assertTrue(len(errors) == 1)
        self.assertEqual(errors[0].__str__(), "The value of Report File cannot be empty.")
        self.delete_file(dictionary_file)

    def test_should_validate_inputs_have_two_empty_errors(self):
        dictionary_file = ""
        report_file = ""
        scan_mode = "1"
        file_types = ""
        errors = self.controller.validate_inputs(dictionary_file, report_file, scan_mode, file_types)
        self.assertTrue(len(errors) == 2)
        self.assertEqual(errors[0].__str__(), "The value of Dictionary File cannot be empty.")
        self.assertEqual(errors[1].__str__(), "The value of Report File cannot be empty.")

    def test_should_validate_inputs_have_three_empty_errors(self):
        dictionary_file = ""
        report_file = ""
        scan_mode = ""
        file_types = ""
        errors = self.controller.validate_inputs(dictionary_file, report_file, scan_mode, file_types)
        self.assertTrue(len(errors) == 3)
        self.assertEqual(errors[0].__str__(), "The value of Dictionary File cannot be empty.")
        self.assertEqual(errors[1].__str__(), "The value of Report File cannot be empty.")
        self.assertEqual(errors[2].__str__(), "The value of Scan Mode cannot be empty.")

    def test_should_validate_inputs_have_one_scan_mode_error(self):
        dictionary_file = self.get_file("dictionary.txt")
        report_file = "C:\\Users\\Documents\\python\\Spellcheck_various"
        scan_mode = "55"
        file_types = ""
        errors = self.controller.validate_inputs(dictionary_file, report_file, scan_mode, file_types)
        self.assertTrue(len(errors) == 1)
        self.assertEqual(errors[0].__str__(), "The range of the values should be between 1 and 2.")
        self.delete_file(dictionary_file)

    def test_should_validate_inputs_have_one_scan_mode_error_when_value_0(self):
        dictionary_file = self.get_file("dictionary.txt")
        report_file = "C:\\Users\\Documents\\python\\Spellcheck_various"
        scan_mode = "0"
        file_types = ""
        errors = self.controller.validate_inputs(dictionary_file, report_file, scan_mode, file_types)
        self.assertTrue(len(errors) == 1)
        self.assertEqual(errors[0].__str__(), "The range of the values should be between 1 and 2.")
        self.delete_file(dictionary_file)

    def test_should_validate_inputs_have_four_empty_errors(self):
        dictionary_file = ""
        report_file = ""
        scan_mode = "3"
        file_types = ""
        errors = self.controller.validate_inputs(dictionary_file, report_file, scan_mode, file_types)
        self.assertTrue(len(errors) == 3)
        self.assertEqual(errors[0].__str__(), "The value of Dictionary File cannot be empty.")
        self.assertEqual(errors[1].__str__(), "The value of Report File cannot be empty.")
        self.assertEqual(errors[2].__str__(), "The range of the values should be between 1 and 2.")

    def test_should_scan_mode_be_number_error_message(self):
        dictionary_file = self.get_file("dictionary.txt")
        report_file = "C:\\Users\\Documents\\python\\Spellcheck_various"
        scan_mode = "test"
        file_types = "doc, pdf"
        errors = self.controller.validate_inputs(dictionary_file, report_file, scan_mode, file_types)
        self.assertTrue(len(errors) == 1)
        self.assertEqual(errors[0].__str__(), "The value must be a number.")
        self.delete_file(dictionary_file)

    def test_should_non_existent_dictionary_file_generate_error(self):
        dictionary_file = "C:\\Users\\Documents\\python\\Spellcheck_various\\dictionary.txt"
        report_file = "C:\\Users\\Documents\\python\\Spellcheck_various"
        scan_mode = "1"
        file_types = "doc,pdf"
        errors = self.controller.validate_inputs(dictionary_file, report_file, scan_mode, file_types)
        self.assertTrue(len(errors) == 1)
        self.assertEqual(errors[0].__str__(), self.controller.DICTIONARY_FILE_DOES_NOT_EXIST)

    def test_should_existent_dictionary_file_not_generate_error(self):
        dictionary_file = self.get_file("dictionary.txt")
        report_file = "C:\\Users\\Documents\\python\\Spellcheck_various"
        scan_mode = "1"
        file_types = "doc,pdf"
        errors = self.controller.validate_inputs(dictionary_file, report_file, scan_mode, file_types)
        self.assertTrue(len(errors) == 0)
        self.delete_file(dictionary_file)

    def test_should_file_extensions_entered_not_generate_error(self):
        dictionary_file = self.get_file("dictionary.txt")
        report_file = "C:\\Users\\Documents\\python\\Spellcheck_various"
        scan_mode = "1"
        file_types = "doc,pdf"
        errors = self.controller.validate_inputs(dictionary_file, report_file, scan_mode, file_types)
        self.assertTrue(len(errors) == 0)
        self.delete_file(dictionary_file)

    def test_should_file_extensions_entered_be_in_model(self):
        dictionary_file = self.get_file("dictionary.txt")
        report_file = "C:\\Users\\Documents\\python\\Spellcheck_various"
        scan_mode = "1"
        file_types = "doc,xls,pdf,php"
        errors = self.controller.validate_inputs(dictionary_file, report_file, scan_mode, file_types)
        self.assertTrue(len(errors) == 0)
        file_ext = self.controller.spellcheck_model.ALL_ALLOWED_SCANNABLE_FILE_EXTENSIONS
        self.assertEqual(len(file_ext),4)
        self.delete_file(dictionary_file)

    @staticmethod
    def get_file(file_name):
        test_dir = tempfile.mkdtemp()
        f = open(os.path.join(test_dir, file_name), 'w')
        f.write('test string')
        f.close()
        return f.name

    @staticmethod
    def delete_file(file_path):
        os.remove(file_path)
