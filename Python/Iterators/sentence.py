class Sentence:
    def __init__(self, text):
        self.text = text
        self.words = text.split()
        self.index = 0

    def __iter__(self):
        return self

    def __next__(self):
        try:
            word = self.words[self.index]
        except IndexError:
            raise StopIteration()
        self.index += 1
        return word


for word in Sentence("This is a     sentence"):
    print(word)


def sentence(text):
    for word in text.split():
        yield word


for word in sentence("Hello world for a generator"):
    print(word)
