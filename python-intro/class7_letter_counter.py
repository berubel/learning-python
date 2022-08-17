def letter_counter(words_list):
    counter = []
    for word in words_list:
        x = len(word)
        counter.append(x)
    return counter


if __name__ == '__main__':
    words = ['black', 'white', 'yellow', 'green']
    print(letter_counter(words))
