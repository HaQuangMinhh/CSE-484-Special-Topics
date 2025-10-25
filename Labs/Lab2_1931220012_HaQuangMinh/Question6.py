fileName = "wordList.txt"

try:
    n = int(input("would you like to write to the file? "))
    if n <= 0:
        print("Number of words must be positive.")

    else:
        words = []
        for i in range(n):
            word = input(f"Enter word {i+1}: ")
            words.append(word)

        # Ghi vào file, mỗi từ 1 dòng
        with open(fileName, "w", encoding="utf-8") as file:
            for word in words:
                file.write(word + "\n")        

        print(f"{n} words have been written to '{fileName}'.")
except ValueError:
    print("Invalid input. Please enter an integer.")
except Exception as e:
    print(f"An error occurred: {e}")        