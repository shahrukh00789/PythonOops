def searcher():
    import time
    book = "This is a book on harry and code with haary and good"

    time.sleep(4)

    while True:
        text = (yield)
        if text in book:
            print("Your text is in book")
        else:
            print("Your text is not in book")


search = searcher()
next(search)
search.send("harry")
search.send("harry")
