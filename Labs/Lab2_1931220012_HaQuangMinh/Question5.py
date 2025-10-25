fileName = "scores.txt"

try: 
    with open(fileName, "r", encoding="utf-8") as file:
        maxScore = -1 
        maxName = ""
        recordCount = 0 

        for line in file:
            line = line.strip()
            if not line:
                continue

            parts = line.split() # tach name and score
            if len(parts) != 2:
                print(f"Skipping invalid {line}")
                continue

            name, score = parts
            try:
                score = int(score)
            except ValueError:
                print("Invalid score for {name}: {score}")
                continue

            recordCount += 1

            if score > maxScore:
                maxScore = score
                maxName = name

        if recordCount == 0:
            print("No valid records")
        else:
            print(f"Number of records: {recordCount}")
            print(f"Highest score: {maxScore} by {maxName}")

except FileNotFoundError:
    print(f"File '{fileName}' not found.")
except UnicodeDecodeError:
    print("Cannot read the file due to encoding issues.")
except Exception as e:
    print(f"An error occurred: {e}")
