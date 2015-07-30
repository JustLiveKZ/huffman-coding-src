import argparse
import json

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
        raw_content = open(self.args.input, 'r').read()
        encoder = Encoder(raw_content)
        encoded_content, reversed_mappings = encoder.encode()
        with open(self.args.output, 'wb') as f:
            f.write(encoded_content)
        with open(self.args.mappings, 'w') as f:
            json_mappings = json.dumps(reversed_mappings, separators=(',', ':'))
            f.write(json_mappings)

    def decode(self):
        encoded_content = open(self.args.input, 'rb').read()
        mappings = json.loads(open(self.args.mappings, 'r').read())
        decoder = Decoder(encoded_content, mappings)
        raw_content = decoder.decode()
        with open(self.args.output, 'w') as f:
            f.write(raw_content)
