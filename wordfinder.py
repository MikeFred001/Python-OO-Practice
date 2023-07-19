from random import choice

class WordFinder:
    """Word Finder: finds random words from a dictionary."""

    def __init__(self, path):
        '''creates word-finder functionality using given file path'''

        self.path = path
        # create an attribute with the list of words
        self.words = self.clean_file(self.path)
        # print out the number of words read, "[num] words read"
        print(f"{len(self.words)} words read")


    def clean_file(self, path):
        '''Accepts a file path and removes "\n" from them'''

        # read the file from the path
        file = open(path, "r")
        # extract all lines from the path (including empty lines)
        file_lines = file.readlines() # returns a list
        # remove new line chars and return
        return [line.replace("\n", "") for line in file_lines]
    #line.strip

    def random(self):
        """Returns random word from list of words"""
        return choice(self.words)


class SpecialWordFinder(WordFinder):
    """Extends functionality of WordFinder class to ignore empty lines and
    comments in files.
    """

    def clean_file(self, path):
        """Takes a file path and removes line breaks, empty lines and
        comment lines. Returns list.
        """

        return [
            line
            for line in super().clean_file(path)
            if not line.startswith("#") and line != ""
            ]
