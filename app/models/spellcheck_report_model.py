class SpellcheckReportModel:
    def __init__(self, total_number_files_found, total_number_files_checked, total_number_files_not_checked, total_number_of_typos, text_line_with_typo):
        self.total_number_files_found = total_number_files_found
        self.total_number_files_checked = total_number_files_checked
        self.total_number_files_not_checked = total_number_files_not_checked
        self.total_number_of_typos = total_number_of_typos
        self.text_line_with_typo = text_line_with_typo

    def get_total_number_files_found(self):
        return self.total_number_files_found

    def get_total_number_files_checked(self):
        return self.total_number_files_checked

    def get_total_number_files_not_checked(self):
        return self.total_number_files_not_checked

    def get_total_number_of_typos(self):
        return self.total_number_of_typos

    def get_text_line_with_typo(self):
        return self.text_line_with_typo