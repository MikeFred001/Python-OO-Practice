class WordFinder:
    """Word Finder: finds random words from a dictionary."""

    def __init__(self, path):
        '''creates word-finder functionality using given file path'''

        self.path = path
        # create an attribute with the list of words
        self.words = self.remove_newline(self.path)
        # print out the number of words read, "[num] words read"
        print(f"{len(self.words)} words read")


    def remove_newline(self, path):
        '''Accepts a list of lines from a file remove "\n" from them '''

        # read the file from the path
        file = open(path, "r")
        # extract all lines from the path (including empty lines)
        file_lines = file.readlines() # returns a list
        # remove new line chars and return
        return [line.replace("\n", "") for line in file_lines]
