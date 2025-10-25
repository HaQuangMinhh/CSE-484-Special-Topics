fileName = input("Enter the file name: ")

try: 
    with open(fileName, "r", encoding="utf-8") as file:
        # Read all list
        lines = file.readlines()

        # Xac dinh so dong can in (5)
        linesToPrint = min(5, len(lines))

        for i in range(linesToPrint):
            print(lines[i], end="") # end để không tìm kiếm thêm dòng mới 

except FileNotFoundError:
    print(f"File: {fileName} not found")
except UnicodeDecodeError:
    print("Cannot read the file due to encoding issues")
