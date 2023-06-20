import re
from collections import Counter 
class Dataset:
    def __init__(self, filename):
        self.filename = filename
        self.n_sentences = []
        self.vocab = []
        self.words = []
        self.n_words = 0


    def read_file(self):
        # n_sentences = []
        with open(self.filename, 'r') as file:
            file.readline() # skip first row
            lines = file.readlines()
            for line in lines:
                self.n_sentences.append(line.lstrip('0123456789\t').rstrip('\n').lower())
        return self.n_sentences
    
    def get_unique_words(self):
        for sentence in self.n_sentences:
            for word in sentence.split():
                # if word not in self.words:
                self.words.append(re.sub(r'\W+', '', word))
        self.vocab = list(set(self.words))
        self.n_words = len(self.vocab)
        return self.vocab, self.n_words

    def get_word_counts(self):
        word_counter = Counter()
        for sentence in self.n_sentences:
            words = re.findall(r'\w+', sentence)
            word_counter.update(words)
        for word, count in word_counter.most_common(10):
            print(word, count)
        return word_counter


file_handler = Dataset('datasetSentences.txt')
file_content = file_handler.read_file()
# print(len(file_content))
# print(file_content[100])
word_list, word_count = file_handler.get_unique_words()
# print(word_list[100])
# print(word_count)
count_dict = file_handler.get_word_counts()

print(type(count_dict))

