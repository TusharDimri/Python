import webbrowser

ser = input("Enter your query")
query = f"https://google.com/search?q={ser}"
webbrowser.open(query)