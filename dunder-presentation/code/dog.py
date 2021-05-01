class TT:
    """Tibetan Terrier fun facts."""
    coat = '2 layers of hair'
    mortal_enemy = "cat"

    def __init__(self, name: str, vocab: list, toy: str, sex: str):
        self.name = name
        self.vocab = vocab
        self.favorite_toy = toy
        self.sex = sex

    def __repr__(self):
        indent = "  "
        r = str()
        for key, value in self.__dict__.items():
            r += indent + key + ": " + repr(value) + "\n"
        return r

    def __str__(self):
        return self.name


harley = TT(
    "Harley",
    ["sit", "come", "down", "drop it", "no bite", "heel", 'paw'],
    "heart toy",
    sex="female",
)

def deep(object):
    attrs = dir(object)
    class_attrs = []
    for attr in attrs:
        if fullmatch('\_\_.+\_\_', attr) is not None:
            class_attrs.append(attr)
