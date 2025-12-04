import sys
from stats import get_word_count, get_char_count, sort_list, sort_on

if len(sys.argv) < 2:
    print(f"Usage: python3 main.py <path_to_book>")
    sys.exit(1)

file_name = sys.argv[1]

def get_book_text(file_name):

    with open(file_name) as f:
        data = f.read()

    return (data)


def main():
    num_words = get_word_count(get_book_text(file_name))
    char_count = get_char_count(get_book_text(file_name))
    report_dict = sort_list(char_count)
    print(f"============ BOOKBOT ============")
    print(f"Analyzing book found at {file_name}...")
    print(f"----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print(f"--------- Character Count -------")
    for each in report_dict:
        if each["char"].isalpha():
            print(f"{each["char"]}: {each["num"]}")
main()
