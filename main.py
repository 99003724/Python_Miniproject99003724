'''

Author : Archita Modi
PS No : 99003724
Contact : archita.modi@ltts.com
Date of creation : 26.02.2021
Description: To find 5 words from the input text file.

'''


import re   # import regular expression


class SearchInputWord:
    # Constructor created

    def __init__(self, search_word):
        # open and read the text file.
        self.file_in = open(".txt", "r").read()
        self.search_word = search_word

    def search_word_inf(self):
        count = 0
        # Finding input word from the input text file.
        num_out = re.findall(self.search_word, self.file_in, re.M | re.I)
        # new output file created for the input word given for search.
        new_file = self.search_word + ".word_found.txt"
        new_out_file = open(new_file, "w+")
        new_out_file.write("count of word: ")
        new_out_file.write(str(len(num_out)))
        new_out_file.write(str("\n"))
        sp_t = self.file_in.split()   # Split input text file.
        # Using loop to find the words before and after the input word.
        for i in range(len(sp_t)):
            match = re.match(self.search_word, sp_t[i], re.M | re.I)
            if match:
                count += 1
                s_f = (sp_t[i-1] + " " + sp_t[i] + " " + sp_t[i+1] + "\n")
                # printing the line where the input word occurs.
                new_out_file.writelines(str(s_f))
        new_out_file.close()

# Main Function of the program.


if __name__ == "__main__":
    # loop to find 5 words from the text file.
    print("--------5 words to search from the text file--------")
    for x in range(5):
        word_search = input("Enter the word to search : ")
        sw = SearchInputWord(word_search)
        sw.search_word_inf()
        print("\n")
