file_name = "wordList.txt"

try:
    with open(file_name, "r", encoding="utf-8") as file:
        words = [line.strip() for line in file if line.strip()]  # loại bỏ dòng trống
    
    if not words:
        print("The file is empty.")
    else:
        num_words = len(words)
        longest_word = max(words, key=len)
        average_length = sum(len(word) for word in words) / num_words
        
        print(f"Number of words: {num_words}")
        print(f"Longest word: {longest_word}")
        print(f"Average word length: {average_length:.2f}")
        
except FileNotFoundError:
    print(f"File '{file_name}' not found.")
except UnicodeDecodeError:
    print("Cannot read the file due to encoding issues.")
except Exception as e:
    print(f"An error occurred: {e}")
