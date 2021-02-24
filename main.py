import re


class SearchInputWord:
    def __init__(self, search_word): 
        # open and read the text file.
        self.file_i = open(".txt", "r").read() 
        self.search_word = search_word

    def search_word_inf(self):
        count = 0        
        # Finding input word from the input text file.
        num_out = re.findall(self.search_word, self.file_i, re.M | re.I)
        # new output file created for the input word given to search
        new_file = self.search_word + ".word_found.txt"
        new_out_file = open(new_file, "w+")
        new_out_file.write("count of word: ")
        new_out_file.write(str(len(num_out)))
        new_out_file.write(str("\n"))
        split_text = self.file_i.split()
        # To find the words before and after the input word.s
        for i in range(len(split_text)):
            match = re.match(self.search_word, split_text[i], re.M | re.I)
            if match:
                count += 1
                y_f = (split_text[i-1] + " " + split_text[i] + " " + split_text[i+1] + "\n")
                # printing the line where the input word occurs.
                new_out_file.writelines(str(y_f)) 


# Main Function of the program.
if __name__ == "__main__":
    # loop to find 5 words from the text file.
    for x in range(5):     
        word_search = input("Enter the word: ")
        sw = SearchInputWord(word_search)
        sw.search_word_inf()
        print("\n")        