def word_count(book):
    wordcount=len(book.split())
    return wordcount

def char_count(book):
    chars = set(book)
    chardict = {}
    for char in chars:
        chardict[char] = 0
    for char in book:
        if char.lower() in chardict:
            chardict[char.lower()] = chardict[char.lower()] + 1
    return chardict

def sort_on(items):
    return items["num"]

def countsort(chardict):
    sortlist = []
    badchars = ['“','”','’','—','™','‘','•']
    for x in chardict:
        if ord(x) >=97 and chardict[x] != 0 and not x in badchars:
            sortlist.append({"char":x, "num":chardict[x]})
    sortlist.sort(reverse=True, key=sort_on)
    return sortlist
    