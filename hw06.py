import collections


class Word:
    def __init__(self, text, part_of_speech):
        self.text = text
        self.part_of_speech = part_of_speech


class Sentence:
    def __init__(self, content):
        self.content = content

    def __str__(self):
        return f"{self.show.capitalize()}."

    @property
    def show(self):
        show = " ".join([words[i].text for i in self.content])
        return show

    def show_parts(self):
        part = collections.Counter([words[i].part for i in self.content])
        return part.most_common(len(part))


class Noun(Word):
    def __init__(self, text):
        self.text = text
        self.__part_of_speech = "существительное"

    @property
    def part(self):
        return self.__part_of_speech


class Verd(Word):
    def __init__(self, text):
        self.text = text
        self.__part_of_speech = "глагол"

    @property
    def part(self):
        return self.__part_of_speech


class Adjective(Word):
    def __init__(self, text):
        self.text = text
        self.__part_of_speech = "прилагательное"

    @property
    def part(self):
        return self.__part_of_speech


words = [Noun("стол"),
         Noun("стул"),
         Adjective("деревянный"),
         Adjective("низкий"),
         Verd("помыли"),
         Verd("несте")]

contents = [Sentence([2, 0, 4]),
            Sentence([5, 3, 1])]

print(contents[0])
print(contents[0].show_parts())
print()
print(contents[1])
print(contents[1].show_parts())
