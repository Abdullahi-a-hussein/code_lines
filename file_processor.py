

class FileProcessor:
    """ This file is for processing text files to fetch information from the file. """

    def __init__(self, file_path) -> None:
        """initialize the class attributes"""
        self.wordcount = {}
        with open(file_path, 'r') as File:
            content = [word.strip().lower() for word in File.read().split(" ") if len(word) > 1]
        for word in content:
            if word not in self.wordcount:
                self.wordcount[word] = 1
            else:
                self.wordcount[word] += 1

    def word_count(self) -> int:
        """
        return the number of words in this file
        caution: in this code a word has at least two letters.
        """
        return len(self.wordcount)

    def most_used_word(self) -> str:
        """return the most used word in this text file and the number of times it's been used"""
        most_used = max(self.wordcount, key=self.wordcount.get)
        return "the most used word is: " + most_used + ", \n it's been used " + \
               str(self.wordcount[most_used]) + " times"


if __name__ == "__main__":
    file = "secod.text"
    word_processor = FileProcessor(file)
    print("number of words in this file: ", word_processor.word_count())
    print(word_processor.most_used_word())
