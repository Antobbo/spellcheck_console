class SpellcheckController:

    VALUE_CANNOT_BE_EMPTY_ERROR_MESSAGE = "The value of {element} cannot be empty."

    def __init__(self, spellcheck_view, spellcheck_model):
        self.spellcheck_view = spellcheck_view
        self.spellcheck_model = spellcheck_model

    def validate_inputs(self, dictionary_file, report_file, scan_mode, file_types):
        #todo: to finish with other errors
        errors = []
        if dictionary_file == "":
            errors.append(self.VALUE_CANNOT_BE_EMPTY_ERROR_MESSAGE.format(element = "Dictionary File"))
        if report_file == "":
            errors.append(self.VALUE_CANNOT_BE_EMPTY_ERROR_MESSAGE.format(element="Report File"))

        return errors

    def update_spellcheck_model(self, dictionary_file, report_file, scan_mode, file_types):
        #todo update the model
        pass