import re
RE_WORD = re.compile('\w+')
class SentenceV4():
    def __init__(self, text) -> None:
        self.text = text
        self.wordIterator = RE_WORD.finditer(self.text)

    def __iter__(self):
        for mached in self.wordIterator:
            yield mached.group()

    