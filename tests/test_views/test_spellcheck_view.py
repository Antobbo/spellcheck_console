import builtins
import sys
import unittest
from io import StringIO
from unittest.mock import patch

from app.controllers.spellcheck_controller import SpellcheckController
from app.models.spellcheck_model import SpellcheckModel
from app.views.spellcheck_view import SpellcheckView

class TestSpellcheckView(unittest.TestCase):

    def setUp(self):
        model = SpellcheckModel("","","","")
        self.spellcheck_view = SpellcheckView()

    #given
    @patch('builtins.input', side_effect = ['C:\\Users\\user\\dictionary.txt', 'C:\\Users\\user\\report.txt', '1', 'txt,pdf,doc'])
    def test_should_user_input_returned_be_as_expected(self, mock_input):
        #when
        results = self.spellcheck_view.get_user_input()
        #then
        self.assertEqual(results, ('C:\\Users\\user\\dictionary.txt', 'C:\\Users\\user\\report.txt', '1', 'txt,pdf,doc'), "They're not equal")

    # given
    @patch('builtins.input', side_effect=['C:\\Users\\user\\dictionary.txt', 'C:\\Users\\user\\report.txt', '2'])
    def test_should_user_input_returned_be_as_expected_when_webpages_selected(self, mock_input):
        # when
        results = self.spellcheck_view.get_user_input()
        # then
        self.assertEqual(results, ('C:\\Users\\user\\dictionary.txt', 'C:\\Users\\user\\report.txt', '2', ''), "They're not equal")

    # given
    @patch('builtins.input', side_effect=['C:\\Users\\user\\dictionary.txt', 'C:\\Users\\user\\report.txt', '1', ''])
    def test_should_user_input_returned_be_as_expected_when_file_types_empty_if_file_selected(self, mock_input):
        # when
        results = self.spellcheck_view.get_user_input()
        # then
        self.assertEqual(results, ('C:\\Users\\user\\dictionary.txt', 'C:\\Users\\user\\report.txt', '1', ''), "They're not equal")

    def test_should_error_messaged_contain_right_info(self):
        #given
        expected_output = (
            "\nThe following errors occurred:\n"
            "- The value of Dictionary File cannot be empty.\n"
            "- The value of Report File cannot be empty.\n"
            "- The value of Scan Mode cannot be empty.\n"
        )
        captured_output = StringIO()
        # redirect stdout
        sys.stdout = captured_output
        #when
        self.spellcheck_view.display_errors(self.get_errors())
        self.assertEqual(captured_output.getvalue(), expected_output)

    def get_errors(self):
        errors = [
            SpellcheckController.VALUE_CANNOT_BE_EMPTY_ERROR_MESSAGE.format(element=SpellcheckModel.DICTIONARY_FILE_STRING),
            SpellcheckController.VALUE_CANNOT_BE_EMPTY_ERROR_MESSAGE.format(element=SpellcheckModel.REPORT_FILE_STRING),
            SpellcheckController.VALUE_CANNOT_BE_EMPTY_ERROR_MESSAGE.format(element=SpellcheckModel.SCAN_MODE_STRING)
        ]
        return errors

    if __name__ == '__main__':
        unittest.main()



