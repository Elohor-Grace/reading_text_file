# Read text from a file, and count the occurence of words in that text
# Example:
# count_words("The cake is done. It is a big cake!") 
# --> {"cake":2, "big":1, "is":2, "the":1, "a":1, "it"
def read_file_content(filename):
    # [assignment] Add your code here 
    open_file = open("./story.txt", "r")
    read_file = open_file.read()
    return read_file
    #print("this file is true")
    #print (read_file)
   

def count_words():
    text = read_file_content("./story.txt")
    # [assignment] Add your code here
    split_text_content =text.split()
    #print(split_text_content)
    count = {}
    for i in split_text_content:
        if i in count:
            count[i] += 1
        else:
            count[i] =1
    return count

print(count_words())
    #return {"as": 10, "would": 20}