import sys

from stats import count_chars, count_words, sort_chars_by_count


def get_book_text(path):
    with open(path, "r") as f:
        return f.read()


def main():
    args = sys.argv
    if len(args) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    path = args[1]
    text = get_book_text(path)
    word_count = count_words(text)
    char_count = count_chars(text)
    sorted_counts = sort_chars_by_count(char_count)
    print(
        f"""============ BOOKBOT ============
Analyzing book found at {path}...
----------- Word Count ----------
Found {word_count} total words
--------- Character Count -------"""
    )
    for count in sorted_counts:
        char = count["char"]
        count = count["count"]
        if char.isalpha():
            print(f"{char}: {count}")
    print("============= END ===============")


main()
