import builtins
import unittest
from unittest.mock import patch

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

    if __name__ == '__main__':
        unittest.main()