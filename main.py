def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    word_count = get_word_count(text)
    count = count_characters(text)
    listStuff = convert_to_list(count) #converts dictionary of count to list for printing
    listStuff.sort(reverse=True, key=sort_on)
    

   
    

    print ("--- Begin report of books/frankenstein.txt ---")
    print (f"{word_count} words were found in the document")
    print ()
    list_print(listStuff)
    print ("--- End of report ---")

def get_book_text(path):
    with open(path) as f: #opens file as identifier f
        return f.read() #returns text via read function

def get_word_count(text):
    words = text.split()
    return len(words)

def count_characters(input):
    chars = {}
    for c in input:
        lowered = c.lower()
        if lowered in chars:
            chars[lowered] += 1
        else:
            chars[lowered] = 1
    return chars

def sort_on(dict): #dependancy for sorting to be used in next func
    return dict["count"]

def convert_to_list(dict):
    converted_list = []
    for key, value in dict.items():
        new_dict = {}
        new_dict["character"] = key
        new_dict["count"] = value
        converted_list.append(new_dict)
    return converted_list

def list_print(list):
    for thing in list:
        if thing["character"].isalpha() == True:
            print (f"The '{thing["character"]}' character was found {thing["count"]} times")
    return






main()


""" 
def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    print(text)


def get_book_text(path):
    with open(path) as f:
        return f.read()


main()  
"""