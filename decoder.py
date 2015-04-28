import json


class Decoder(object):
    BYTE_SIZE = 8

    def __init__(self, input_filename, output_filename, mappings_filename):
        self.input_filename = input_filename
        self.output_filename = output_filename
        self.mappings_filename = mappings_filename
        self.encoded_content = ''
        self.decoded_content = ''
        self.meta_info = None
        self.mappings = {}

    def decode(self):
        self._read_encoded_content()
        self._read_mappings()
        self._replace_with_mappings()

    def _read_encoded_content(self):
        with open(self.input_filename, 'rb') as f:
            self.meta_info = int.from_bytes(f.read(1), 'big')
            encoded_content = f.read()
            temp_list = []
            try:
                remainder = encoded_content[0]
                temp_list.append('{0:0{1}b}'.format(remainder, self.meta_info))
                for num in encoded_content[1:]:
                    temp_list.append('{0:08b}'.format(num))
                self.encoded_content = ''.join(temp_list)
            except IndexError:
                pass

    def _read_mappings(self):
        json_content = open(self.mappings_filename, 'r').read()
        self.mappings = json.loads(json_content)

    def _replace_with_mappings(self):
        temp_list = []
        code = ''
        for char in self.encoded_content:
            code += char
            if code in self.mappings:
                temp_list.append(self.mappings[code])
                code = ''
        self.decoded_content = ''.join(temp_list)

    def write_decoded_content(self):
        with open(self.output_filename, 'w') as f:
            f.write(self.decoded_content)