def count_words(text):
    return len(text.split())


def count_chars(text):
    counts = {}
    for char in text.lower():
        if char in counts:
            counts[char] += 1
        else:
            counts[char] = 1
    return counts


def sort_chars_by_count(char_dict):
    output = [{"char": char, "count": count} for char, count in char_dict.items()]
    output.sort(key=lambda x: x["count"], reverse=True)
    return output
