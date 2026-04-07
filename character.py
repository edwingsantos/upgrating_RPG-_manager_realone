class Character:
    def __init__(self, name, char_class, level, stats):
        self.name = name
        self.char_class = char_class
        self.level = level
        self.stats = stats

    def to_dict(self):
        return {
            "Name": self.name,
            "Class": self.char_class,
            "Level": self.level,
            "Strength": self.stats["Strength"],
            "Speed": self.stats["Speed"],
            "Intelligence": self.stats["Intelligence"]
        }