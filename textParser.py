
class Dataset:
    def __init__(self, input_file):
        self.input_file = input_file
        self.n_sentences = []
        self.vocab = None
        self.words = {}


def read_file():
    n_sentences = []
    with open('datasetSentences.txt', 'r') as file:
        file.readline() # skip first row
        lines = file.readlines()
        for line in lines:
            n_sentences.append(line.lstrip('0123456789\t'))
    return