def sorting(words, order):
    order_dict = {}
    reverse_dict = {}
    for i in range(0,len(order)):
        order_dict[order[i]] = i
        reverse_dict[i] = order[i]
        
    number_words = convert_to_numbers(words, order_dict)
    sorted_numbers = sorted(number_words)
    sorted_words = convert_to_letters(sorted_numbers, reverse_dict) 
    return sorted_words
    
    
def convert_to_numbers(words, order_dict):
    number_words = []
    for i in range(0, len(words)):
        new_word = ""
        original_word = words[i]
        for j in range(0, len(words[i])):
            new_word += str(order_dict[original_word[j]])
         
        number_words.append(new_word)
        
    return number_words


def convert_to_letters(sorted_numbers, reverse_dict):
    sorted_words = []
    for i in range(0, len(sorted_numbers)):
        letter_word = ""
        number_word = sorted_numbers[i]
        for j in range(0, len(sorted_numbers[i])):
            letter_word += str(reverse_dict[int(number_word[j])])
         
        sorted_words.append(letter_word)  
        
    return sorted_words
       