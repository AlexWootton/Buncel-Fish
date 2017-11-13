import csv

class Dictionary(list):
    """A list of dictionaries containing words/phrases in several languages.

    Each dictionary contains one word or phrase in several languages as read
    from a provided .csv file.
    The key is the language and the value is the word in that language.
    """

    def __init__(self, file='default_dict.csv', *args, **kwargs):
        if not isinstance(file, str):
            raise ValueError("File must be a string")
        super().__init__()
        try:
            self.file = open(file, "r")
        except:
            self.file = open("default_dict.csv", "r")
        if file[-4:] == ".csv":
            reader = csv.DictReader(self.file)
            for line in reader:
                self.append(line)
        else:
            raise ValueError("Must be a .csv file")
            # for line in self.file:
                # key, value = line.split(",")
                # self[key] = value
        self.file.close()

    @property
    def languages(self):
        lang_list = []
        for key in self[0]:
            lang_list.append(key)
        return lang_list

    def translate(self, word=None, origin=None, destination=None):
        possible_matches = []
        if not word:
            raise ValueError("You must provide a word to translate")
        if not origin:
            # search all dictionaries for word and try to translate to destination
            for dictionary in self:
                for key in dictionary:
                    if word.lower() == dictionary[key].lower():
                        return dictionary[destination]
                    elif word.lower() in dictionary[key].lower():
                        possible_matches.append(dictionary[key])
            raise ValueError("'{}' could not be found in any dictionary".format(word))
            return None
        if not destination:
            # return all available translations for word as dictionary
            for dictionary in self:
                if word.lower() in dictionary[origin].lower():
                    translations = {}
                    for key in dictionary:
                        translations[key] = dictionary[key]
                    return translations
        for dictionary in self:
            if word.lower() == dictionary[origin].lower():
                return dictionary[destination]
            elif word.lower() in dictionary[origin].lower():
                #import pdb; pdb.set_trace()
                possible_matches.append("'{}' meaning '{}'".format(dictionary[origin], dictionary[destination]))
        if possible_matches:
            return possible_matches
        else:
            raise ValueError("'{}' is not in the {} dictionary".format(word, origin.capitalize()))
            return None
