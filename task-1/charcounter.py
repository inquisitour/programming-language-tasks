class Charcounter:
    def __init__(self):
        self.wordnumber = 0
        self.digitnumber = 0
        self.letternumber = 0
        self.whitespacenumber = 0
        self.specialcharnumber = 0
        self.is_word_present = False
        self.is_word_counted = False

    def increase_wordnumber(self):
        self.wordnumber += 1
        self.is_word_present = True

    def increase_digitnumber(self):
        self.digitnumber += 1
        self.is_word_present = True

    def increase_letternumber(self):
        self.letternumber += 1
        self.is_word_present = True

    def increase_whitespacenumber(self):
        self.whitespacenumber += 1
        self.is_word_present = True

    def increase_specialcharnumber(self):
        self.specialcharnumber += 1
        self.is_word_present = True

    def check_char(self, char):
        if char.isdigit():
            self.increase_digitnumber()
        elif char in 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz':
            self.increase_letternumber()
        elif char == ' ':
            self.increase_whitespacenumber()
        else:
            self.increase_specialcharnumber()

    def check_word_presence(self):
        return self.is_word_present

    def print_charcounter(self):
        return "Number of words: " + str(self.wordnumber) + "\n"\
             + "Number of digits: " + str(self.digitnumber) + "\n"\
             + "Number of letters: " + str(self.letternumber) + "\n"\
             + "Number of whitespaces: " + str(self.whitespacenumber) + "\n"\
             + "Number of special characters: " + str(self.specialcharnumber) + "\n"

    def reset_all(self):
        self.wordnumber = 0
        self.digitnumber = 0
        self.letternumber = 0
        self.whitespacenumber = 0
        self.specialcharnumber = 0
        self.is_word_present = False
        self.is_word_counted = False
        self.new_input = True