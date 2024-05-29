#!/usr/bin/env python3

class MyString:
    def __init__(self, value=""):
        if not isinstance(value, str):
            print("The value must be a string.")
            self.value = ""
        else:
            self.value = value

    def is_sentence(self):
        return self.ends_with_period()

    def is_question(self):
        return self.ends_with_question_mark()

    def is_exclamation(self):
        return self.ends_with_exclamation_mark()

    def ends_with_period(self):
        return self.value.endswith('.')

    def ends_with_question_mark(self):
        return self.value.endswith('?')

    def ends_with_exclamation_mark(self):
        return self.value.endswith('!')

    def count_sentences(self):
        if not self.value:
            return 0
        sentences = self.value.split('. ')
        import re
        sentences = re.split(r'[.!?]+', self.value)
        sentences = [s for s in sentences if s.strip()]  
        return len(sentences)
