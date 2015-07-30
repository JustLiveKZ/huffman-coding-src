from minheap import MinHeap


class Encoder(object):
    BYTE_SIZE = 8

    def __init__(self, raw_content):
        self.raw_content = raw_content
        self.encoded_digit_sequence = ''
        self.encoded_content = b''
        self.mappings = {}

    def encode(self):
        occurrences = self._count_occurrences()
        heap = MinHeap.build_from_dict(occurrences)
        root = heap.merge_to_single_element()
        self.mappings = self._generate_mappings(root)
        self.encoded_digit_sequence = self._replace_with_mappings()
        self.encoded_content = self._encode()
        return self.encoded_content, self.reversed_mappings

    def _count_occurrences(self):
        occurrences = {}
        for char in self.raw_content:
            if char in occurrences:
                occurrences[char] += 1
            else:
                occurrences[char] = 1
        return occurrences

    def _generate_mappings(self, node):
        mappings = {}
        node.generate_mappings(mappings)
        return mappings

    def _replace_with_mappings(self):
        encoded_list = []
        for char in self.raw_content:
            encoded_list.append(self.mappings[char])
        return ''.join(encoded_list)

    def _encode(self):
        remainder = len(self.encoded_digit_sequence) % self.BYTE_SIZE
        encoded_content_list = [self._get_iso_8859_1_char('{0:08b}'.format(remainder))]
        if remainder:
            encoded_content_list.append(self._get_iso_8859_1_char(self.encoded_digit_sequence[0:remainder]))
        current_pos = remainder
        while current_pos < len(self.encoded_digit_sequence):
            encoded_content_list.append(self._get_iso_8859_1_char(self.encoded_digit_sequence[current_pos:current_pos + self.BYTE_SIZE]))
            current_pos += self.BYTE_SIZE
        return b''.join(encoded_content_list)

    def _get_iso_8859_1_char(self, string_in_binary):
        return chr(int(string_in_binary, 2)).encode('iso-8859-1')

    @property
    def reversed_mappings(self):
        return {v: k for k, v in self.mappings.items()}
