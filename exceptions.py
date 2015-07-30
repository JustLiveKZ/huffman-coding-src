class HeapEmptyError(Exception):
    pass


class InvalidDigitSequence(Exception):
    def __init__(self, digit_sequence):
        self.digit_sequence = digit_sequence

    def __str__(self):
        return 'Invalid digit sequence: {}'.format(self.digit_sequence)

    @property
    def message(self):
        return str(self)
