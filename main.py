from stats import word_count, char_count, sort_on, countsort
import sys

def get_book_text(bookpath):
    with open(bookpath,'rt') as bp:
        book = bp.read()
    return book

def main(bookpath):
    # book = get_book_text("workspace/github.com/JCB-CT/bookbot/books/frankenstein.txt")
    book = get_book_text(bookpath)
    # print(book)
    print('============ BOOKBOT ============')
    print(f"Analyzing book found at {bookpath}...")
    print("----------- Word Count ----------")
    print(f"Found {word_count(book)} total words")
    charcount=char_count(book)
    charsort = countsort(charcount)
    print("--------- Character Count -------")
    for char in charsort:
        print(f"{char["char"]}: {char["num"]}")
    print("============= END ===============")

if __name__=="__main__":
    if len(sys.argv) <  2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    else:
        main(sys.argv[1])