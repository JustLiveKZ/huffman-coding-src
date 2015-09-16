# Huffman coding
Realization of Huffman coding for information zipping

## Usage
### Encode
    python3 main.py encode --input=<input_file> --output=<output_file> --mappings=<mappings_file>

For example if you have your raw text you want to encode in `raw.txt` and you want to write encoded text into `encoded.txt` and mappings into `mappings.txt` you should use command as follow:

    python3 main.py encode --input="raw.txt" --output="encoded.txt" --mappings="mappings.txt"

### Decode
    python3 main.py decode --input=<input_file> --output=<output_file> --mappings=<mappings_file>

For example if you have your encoded text you want to decode in `encoded.txt` and mappings in `mappings.txt` and you want to write decoded text into `raw.txt` you should use command as follow:

    python3 main.py decode --input="encoded.txt" --output="raw.txt" --mappings="mappings.txt"

## Tests
    python3 tests.py

There is actually a single test case which encodes raw text then decodes it back and checks if original text equals to decoded text. But this single test case gives about 90% coverage of code.
