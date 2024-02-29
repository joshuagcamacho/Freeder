class Text:
    def __init__(self, body: str):
        self.raw_body = body
        self.lst_words = Text.get_words(body)

    def get_words(text: str, num_split: int) -> list[list[str]]:
        """
        Takes a block of text, and sections it into num_split.

        >>> get_words('hello my name is derrick and i like to eat food', 3)
        >>> [['hello my name'], ['is derrick and'], ['i like to'], ['eat food']]
        """
        raise NotImplementedError