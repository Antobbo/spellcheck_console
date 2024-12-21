class SpellcheckModel:
    SCAN_MODE = {
        1: "files",
        2: "webpages",
    }

    SCAN_MODE_STRING = "Scan Mode"
    REPORT_FILE_STRING = "Report File"
    DICTIONARY_FILE_STRING = "Dictionary File"
    FILE_EXTENSIONS_STRING = "File Extensions"


    def __init__(self, report_file_path, dictionary_file_path, scan_mode, file_extensions):
        self.report_file_path = report_file_path
        self.dictionary_file_path = dictionary_file_path
        self.scan_mode = scan_mode
        self.file_extensions = file_extensions

    def get_report_file_path(self):
        return self.report_file_path

    def get_dictionary_file_path(self):
        return self.dictionary_file_path

    def get_scan_mode(self):
        return self.scan_mode

    def get_file_extensions(self):
        return self.file_extensions

    def __str__(self):
        return (f"{self.REPORT_FILE_STRING}: {self.report_file_path}.\n"
                f"{self.DICTIONARY_FILE_STRING}: {self.dictionary_file_path}.\n"
                f"{self.SCAN_MODE_STRING}: {self.scan_mode}.\n"
                f"{self.FILE_EXTENSIONS_STRING}: {self.file_extensions}.\n")