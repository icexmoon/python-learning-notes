import re
import reprlib


class Sentence():
    RE_WORD = re.compile('\w+')

    def __init__(self, text) -> None:
        self.text = text
        self.words = Sentence.RE_WORD.findall(text)

    def __getitem__(self, index):
        return self.words[index]

    def __len__(self):
        return len(self.words)

    def __str__(self) -> str:
        return str(self.words)
