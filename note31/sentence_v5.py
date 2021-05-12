import re
RE_WORD = re.compile('\w+')
class SentenceV5():
    def __init__(self, text) -> None:
        self.text = text
        self.wordIterator = RE_WORD.finditer(self.text)

    def __iter__(self):
        return (mached.group() for mached in self.wordIterator)

    