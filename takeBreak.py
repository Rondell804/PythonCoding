import webbrowser
import time
def openBrowser():
    #wait = time.sleep(3)
    takeBreak = 3
    goHome = 0
    while takeBreak > goHome:
        time.sleep(10)
        webbrowser.open("https://www.youtube.com/watch?v=Z-ZV61eDLXI")
        takeBreak = takeBreak - 1
openBrowser()
