class SpellcheckModel:
    SCAN_CATEGORY = {
        1: "files",
        2: "webpages",
    }

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
        return (f"Report file: {self.report_file_path}.\n"
                f"Dictionary file: {self.dictionary_file_path}.\n"
                f"Scan mode: {self.scan_mode}.\n"
                f"File extensions: {self.file_extensions}.\n")