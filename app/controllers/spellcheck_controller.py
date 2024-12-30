import os.path


class SpellcheckController:

    VALUE_CANNOT_BE_EMPTY_ERROR_MESSAGE = "The value of {element} cannot be empty."
    SCAN_MODE_WRONG_RANGE_ERROR_MESSAGE = "The range of the values should be between {first_value} and {last_value}."
    VALUE_INVALID_TYPE_MUST_BE_NUMBER = "The value must be a number."
    DICTIONARY_FILE_DOES_NOT_EXIST = "A dictionary text file must exist."

    def __init__(self, spellcheck_view, spellcheck_model):
        self.spellcheck_view = spellcheck_view
        self.spellcheck_model = spellcheck_model

    def validate_inputs(self, dictionary_file, report_file, scan_mode, file_types):
        errors = []
        if dictionary_file == "":
            errors.append(self.VALUE_CANNOT_BE_EMPTY_ERROR_MESSAGE.format(element = self.spellcheck_model.DICTIONARY_FILE_STRING))
        if report_file == "":
            errors.append(self.VALUE_CANNOT_BE_EMPTY_ERROR_MESSAGE.format(element=self.spellcheck_model.REPORT_FILE_STRING))
        if scan_mode == "":
            errors.append(self.VALUE_CANNOT_BE_EMPTY_ERROR_MESSAGE.format(element=self.spellcheck_model.SCAN_MODE_STRING))
        if scan_mode != "":
            try:
               scan_mode_opt =  int(scan_mode)
               if scan_mode_opt <= 0 or int(scan_mode_opt) > len(self.spellcheck_model.SCAN_MODE):
                   errors.append(self.SCAN_MODE_WRONG_RANGE_ERROR_MESSAGE.format(
                       first_value=next(iter(self.spellcheck_model.SCAN_MODE)),
                       last_value=len(self.spellcheck_model.SCAN_MODE)))
            except ValueError:
                errors.append(self.VALUE_INVALID_TYPE_MUST_BE_NUMBER)
        if len(dictionary_file) != 0 and not os.path.exists(dictionary_file):
            errors.append(self.DICTIONARY_FILE_DOES_NOT_EXIST)
        return errors

    #todo: validate file extensions, file paths
    def update_spellcheck_model(self, dictionary_file, report_file, scan_mode, file_types):
        #todo update the model
        pass