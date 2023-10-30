def main():
    path = "./Books/frankenstein.txt"
    content = get_content(path)
    word_count = count_words(content)
    char_dict = get_dict(content)
    sorted_chars = sort_chars_by_value(char_dict)

    print(f"======== Assessing content of file: {path} ========")
    print(f"The document is {word_count} words loneg.")
    print()

    for item in sorted_chars:
        if not item["char"].isalpha():
            continue
        print(f"'{item['char']}' appears in the text {item['num']} times.")
    print()
    print(f"======== End of report ========")

def count_words(content):
    words = content.split()
    return(len(words))

def get_dict(text):
    chars = {}
    for word in text:
        lower_word = word.lower()
        if lower_word in chars:
            chars[lower_word] += 1
        else: chars[lower_word] = 1
    return chars

def sort_chars_by_value(dict):
    sorted_list = []
    for ch in dict:
        sorted_list.append({"char": ch, "num": dict[ch]})
    sorted_list.sort(reverse=True, key=sort_on)
    return sorted_list

def sort_on(dict):
    return dict["num"]

def get_content(path):
    with open(path) as f:
        return f.read()

main()
