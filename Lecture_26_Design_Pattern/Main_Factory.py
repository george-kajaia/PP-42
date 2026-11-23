class CSVParser:
    def __init__(self, file_name):
        self.file_name = file_name

    def parse(self):
        print(f'Parsing CSV file: {self.file_name}')

class JSONParser:
    def __init__(self, file_name):
        self.file_name = file_name

    def parse(self):
        print(f'Parsing JSON file: {self.file_name}')

class TXTParser:
    def __init__(self, file_name):
        self.file_name = file_name

    def parse(self):
        print(f'Parsing TXT file: {self.file_name}')


def parse_data(file_name, file_extension):
    file_extensions: dict[str, any] = {
        "csv": CSVParser,
        "json": JSONParser,
        "txt": TXTParser
    }

    parser_obj = file_extensions.get(file_extension)(file_name)
    parser_obj.parse()

file_name = 'data.csv'
file_extension = file_name.split('.')[-1]
parse_data(file_name, file_extension)
