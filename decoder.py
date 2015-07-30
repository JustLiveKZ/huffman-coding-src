from exceptions import InvalidDigitSequence


class Decoder(object):
    def __init__(self, encoded_content, mappings):
        self.encoded_content = encoded_content
        self.encoded_digit_sequence = ''
        self.mappings = mappings
        self.raw_content = ''

    def decode(self):
        self.encoded_digit_sequence = self._get_encoded_digit_sequence()
        self.raw_content = self._replace_with_mappings()
        return self.raw_content

    def _get_encoded_digit_sequence(self):
        remainder = self.encoded_content[0]
        encoded_content = self.encoded_content[1:]
        digit_sequence_list = []
        try:
            remainder_chars = encoded_content[0]
            digit_sequence_list.append('{0:0{1}b}'.format(remainder_chars, remainder))
            for char in encoded_content[1:]:
                digit_sequence_list.append('{0:08b}'.format(char))
        except IndexError:
            pass
        return ''.join(digit_sequence_list)

    def _replace_with_mappings(self):
        raw_content_list = []
        code = ''
        for char in self.encoded_digit_sequence:
            code += char
            if code in self.mappings:
                raw_content_list.append(self.mappings[code])
                code = ''
            else:
                keys_with_same_prefix = [key for key in self.mappings.keys() if key.startswith(code)]
                if not keys_with_same_prefix:
                    raise InvalidDigitSequence(code)
        return ''.join(raw_content_list)
