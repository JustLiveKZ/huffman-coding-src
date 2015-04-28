import argparse
from decoder import Decoder
from encoder import Encoder


class Application(object):
    def __init__(self):
        self.args = None
        self.parser = argparse.ArgumentParser(prog='Huffman coding', description='Text zipping using Huffman coding')
        self.parser.add_argument('command', choices=['encode', 'decode'], help='command you want to perform, must be either encode or decode')
        self.parser.add_argument('-i', '--input', required=True, help='input filename')
        self.parser.add_argument('-o', '--output', required=True, help='output filename')
        self.parser.add_argument('-m', '--mappings', required=True, help='mappings filename')
        self.parser.add_argument('-v', '--version', action='version', version='%(prog)s 1.0')

    def run(self):
        self.args = self.parser.parse_args()
        getattr(self, self.args.command)()

    def encode(self):
        encoder = Encoder(self.args.input, self.args.output, self.args.mappings)
        encoder.encode()
        encoder.write_encoded_content()
        encoder.write_reversed_mappings()

    def decode(self):
        decoder = Decoder(self.args.input, self.args.output, self.args.mappings)
        decoder.decode()
        decoder.write_decoded_content()
