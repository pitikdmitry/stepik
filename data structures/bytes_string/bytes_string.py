class BytesString(str):
    def __init__(self, text: str):
        super(BytesString, self).__init__()
        self._text = text
        self._index = 2

    def __iter__(self):
        return self

    def __next__(self) -> str:
        current_text = ""
        while self._index < len(self._text):
            if self._text[self._index] == "#":
                return current_text[:-1]
            elif self._text[self._index] == "b":
                self._index += 1
                return current_text[:-1]
            else:
                current_text += self._text[self._index]
            self._index += 1

        if not self._index < len(self._text):
            raise StopIteration
