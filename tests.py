import unittest
from encoder import Encoder
from decoder import Decoder


class EncoderDecoderTestCase(unittest.TestCase):
    def test_encode_decode(self):
        raw_content = 'Hello, world! Kappa'
        encoder = Encoder(raw_content)
        encoded_content, reversed_mappings = encoder.encode()
        decoder = Decoder(encoded_content, reversed_mappings)
        decoded_content = decoder.decode()
        self.assertEqual(raw_content, decoded_content)


if __name__ == '__main__':
    unittest.main()
