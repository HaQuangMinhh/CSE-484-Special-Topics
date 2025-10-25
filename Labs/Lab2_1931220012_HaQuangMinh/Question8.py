file_name = "personal_page.html"

name = input("Enter your name: ")
description = input("Describe yourself: ")


html_content = f"""<html>
<head>
</head>
<body>
   <center>
      <h1>{name}</h1>
   </center>
   <hr />
   {description}
   <hr />
</body>
</html>"""


try:
    with open(file_name, "w", encoding="utf-8") as file:
        file.write(html_content)
    print(f"Personal web page has been created as '{file_name}'.")
except Exception as e:
    print(f"An error occurred: {e}")
