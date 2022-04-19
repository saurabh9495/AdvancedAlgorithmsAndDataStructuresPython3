class TrieNode:
    def __init__(self,char='') -> None:
        self.children = [None]
        self.is_end_word = False
        self.char = char