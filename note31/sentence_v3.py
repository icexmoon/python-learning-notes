import re


class SentenceV3():
    RE_WORD = re.compile('\w+')

    def __init__(self, text) -> None:
        self.text = text
        self.words = SentenceV3.RE_WORD.findall(text)

    def __iter__(self):
        return iter(self.words)