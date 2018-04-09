class BytesString(str):
    def __init__(self, text: str):
        super(BytesString, self).__init__()
        self._text = text
        self._index = 0

    def __iter__(self):
        return self

    def __next__(self) -> str:
        current_text = ""
        if self._index < len(self._text):
            # read 0b

            current_text += self._text[self._index]
            self._index += 1
            current_text += self._text[self._index]
            self._index += 1

        while self._index < len(self._text):
            c = self._text[self._index]

            if c == "b":
                self._index -=1
                return current_text[:-1]

            current_text += c
            self._index += 1

        if current_text != "":
            return current_text

        if not self._index < len(self._text):
            raise StopIteration
