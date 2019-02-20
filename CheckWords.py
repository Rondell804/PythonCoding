import urllib
def check_words():
    open_file = open("C:\movie_quotes.txt")
    read_file = open_file.read()
    print (read_file)
    check_profanity(read_file)
    open_file.close()
def check_profanity(text_to_check):
    #urllib Helps to open a connection to a website on the internet
    connection = urllib.urlopen("http://www.wdyl.com/profanity?q=" + text_to_check)
    output = connection.read()
    #print (output)

    if "true" in output:
        print ("Profanity Alert")
    elif "false" in output:
        print ("The Document contain no curse words")
    else:
        print ("The input was incorrect")
    connection.close()

check_words()
