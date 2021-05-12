import re


class SentenceV2():
    RE_WORD = re.compile('\w+')

    def __init__(self, text) -> None:
        self.text = text
        self.words = SentenceV2.RE_WORD.findall(text)

    def __iter__(self):
        return StenceIterator(self)


class StenceIterator():
    def __init__(self, sentence) -> None:
        self.sentence = sentence
        self.index = 0

    def __next__(self):
        try:
            result = self.sentence.words[self.index]
        except IndexError:
            raise StopIteration
        self.index += 1
        return result

    def __iter__(self):
        return self
