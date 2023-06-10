def calculate_average_word_length(sentence):
    words = sentence.split()
    total_length = sum(len(word) for word in words)
    word_count = len(words)

    if word_count > 0:
        average_length = total_length / word_count
        return average_length
    else:
        return 0


# Example usage
input_sentence = input("Enter a sentence: ")
result = calculate_average_word_length(input_sentence)
print("Average word length:", result)