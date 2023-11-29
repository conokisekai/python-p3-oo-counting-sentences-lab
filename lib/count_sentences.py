#!/usr/bin/env python3


class MyString:
    def __init__(self, value=""):
        self._value = value
        
    def get_value(self):
     return self._value

    def set_value(self, stringVal):
     if (type(stringVal) == str):
      self._value = stringVal
     else:
      print("The value must be a string.")

    value = property(get_value, set_value)

    def is_sentence(self):
        return self.value.endswith(".")

    def is_question(self):
        return self.value.endswith("?")

    def is_exclamation(self):
        return self.value.endswith("!")

    def count_sentences(self):
        if not self.value:
            return 0
        sentences = filter(
            None, self.value.replace("?", ".").replace("!", ".").split(".")
        )
        return sum(1 for _ in sentences)
