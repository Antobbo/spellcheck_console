class SpellcheckView:

    SCANNING_MESSAGE = "Scan in progress...please wait."
    SCAN_COMPLETE_MESSAGE = "The scan has completed successfully"
    FILE_LOCATION_MESSAGE = f"The report file has been saved here"

    def get_user_input(self):
        print(f"Welcome to the spell check app.")
        dictionary_file = input(f"Please enter file path and name of dictionary (empty for default)")
        report_file = input(f"Please enter file path and name of spell check report, empty for default")
        scan_mode = input(f"Please enter the scan mode, 1 for file/s and 2 for webpages")
        file_types = ""
        if int(scan_mode) == 1:
            file_types = input(f"Please enter a comma separated list of file extensions to scan (empty scans all)")
        return dictionary_file, report_file, scan_mode, file_types

    def display_scanning_message(self):
        return self.SCANNING_MESSAGE

    def display_can_complete_message(self):
        return self.SCAN_COMPLETE_MESSAGE

    def display_generated_report_file_path(self):
        file_location = "dummy_location" #TODO: to get it from model
        return self.FILE_LOCATION_MESSAGE + file_location
