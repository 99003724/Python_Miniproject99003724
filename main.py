import re

class text_processing:
#initializing the word to be searched
    def __init__(self,search_word):
        self.file_i = open("D:\\project.txt","r").read()
        self.search_word = search_word


    def search_word_inf(self):
        num_out = re.findall(self.search_word,self.file_i,re.MULTILINE | re.IGNORECASE)
        return num_out



#generating output file with searched keyword
def out_file(search_word,num_out):
        new_file = search_word + ".word_found.txt"
        new_out_file= open(new_file,"a")
        new_out_file.write("count of word: ")
        new_out_file.write(str(len(num_out)))
for             

#main function of the program
if __name__ == "__main__":
    word_search = input("Enter the word: ")
    find = text_processing(word_search)
    count = find.search_word_inf()
    out_file(word_search,count)