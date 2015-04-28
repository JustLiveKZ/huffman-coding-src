import json
from minheap import MinHeap


class Encoder(object):
    BYTE_SIZE = 8

    def __init__(self, input_filename, output_filename, mappings_filename):
        self.input_filename = input_filename
        self.output_filename = output_filename
        self.mappings_filename = mappings_filename
        self.content = ''
        self.encoded_content = ''
        self.meta_info = None
        self.mappings = {}

    def encode(self):
        self._read_content()
        occurrences = self._count_occurrences()
        heap = MinHeap.build_from_dict(occurrences)
        root = heap.merge_to_single_element()
        root.generate_mappings(self.mappings)
        self._replace_with_mappings()
        self._create_meta_info()

    def _read_content(self):
        self.content = open(self.input_filename, 'r').read()

    def _count_occurrences(self):
        occurrences = {}
        for char in self.content:
            if char in occurrences:
                occurrences[char] += 1
            else:
                occurrences[char] = 1
        return occurrences

    def _create_meta_info(self):
        self.meta_info = len(self.encoded_content) % self.BYTE_SIZE

    def _replace_with_mappings(self):
        encoded_list = []
        for char in self.content:
            encoded_list.append(self.mappings[char])
        self.encoded_content = ''.join(encoded_list)

    def write_encoded_content(self):
        with open(self.output_filename, 'wb') as f:
            f.write(self._get_iso_8859_1_char('{0:08b}'.format(self.meta_info)))
            remainder = len(self.encoded_content) % self.BYTE_SIZE
            if remainder:
                f.write(self._get_iso_8859_1_char(self.encoded_content[0:remainder]))
            current_pos = remainder
            while current_pos < len(self.encoded_content):
                f.write(self._get_iso_8859_1_char(self.encoded_content[current_pos:current_pos + self.BYTE_SIZE]))
                current_pos += self.BYTE_SIZE

    def _get_iso_8859_1_char(self, string_in_binary):
        return chr(int(string_in_binary, 2)).encode('iso-8859-1')

    def write_reversed_mappings(self):
        reversed_mappings = self._get_reversed_mappings()
        json_content = json.dumps(reversed_mappings)
        with open(self.mappings_filename, 'w') as f:
            f.write(json_content)

    def _get_reversed_mappings(self):
        return {v: k for k, v in self.mappings.items()}