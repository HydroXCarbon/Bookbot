
def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    num_words = get_num_words(text)
    char_dict = get_chars_dict(text)
    print_dict(char_dict,book_path,num_words)

def print_dict(char_dict,book_path,num_words):
    char_sort_list = list(char_dict.keys())
    char_sort_list.sort()
    print("--- Begin report of "+book_path+" ---\n")
    print(str(num_words)+" words found in the document")
    for item in char_sort_list:
        if item.isalpha():
            print("The '"+ item + "' character was found " + str(char_dict[item]) + " times")
    print("--- End report ---")

def get_chars_dict(text):
    chars = {}
    for c in text:
        lowered = c.lower()
        if lowered in chars:
            chars[lowered] += 1
        else:
            chars[lowered] = 1
    return chars

def get_num_words(text):
    words = text.split()
    return len(words)

def get_book_text(book_path):
    with open(book_path) as f:
        return f.read()
    
main()