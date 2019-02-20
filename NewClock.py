from Tkinter import *
import time
# Random phrases for the day to choice from in String form
#phrase_of_day = "Today will be great!", "Never Give Up!", "Success Is Key!", "Hello World Day", "Stay Motivated!!", "Speak In Confidence"
def newTime():
    global time1
    # get the current local time and date from the PC
    time2 = time.strftime('%A\n %B %d, %Y \n%I:%M:%S %p' + "\n" + '"' + word_of_day() + '"')
    # if time string has changed, update it
    if time2 != time1:
        time1 = time2
    clock.config(text=time2)
    # calls itself every 200 milliseconds
    # to update the time display as needed
    # could use >200 ms, but display gets jerky
    clock.after(200, newTime)

def word_of_day():
    #while not (time.strftime('%A') == "Saturday" or time.strftime('%A') == "Sunday"):
    if time.strftime('%A') == "Monday":
        the_day = "Africa Power!!"
        (the_day)
    elif time.strftime('%A') == "Tuesday":
        the_day = "Wakada Forever!!"
        (the_day)
    elif time.strftime('%A') == "Wednesday":
        the_day = "Bike Life Wednesday"
        (the_day)
    elif time.strftime('%A') == "Thursday":
        the_day = "Make Moves!!"
        (the_day)
    elif time.strftime('%A') == "Friday":
        the_day = "Can't Stop Won't Stop"
        (the_day)
    else:
        the_day = "The Weekend Baby!!"
        (the_day)
    return the_day
#    # uses the Random function to pick the phrase for the day.
#    speak_success = '' #Empty string
#    if speak_success == '':
#        print("\n" + "What Will Inspirer You Today")
#        speak_success = raw_input()
#    return speak_success

#word_of_day()
#choose_words = word_of_day()
root = Tk()
time1 = ''
root.title('Dell Clock')
clock = Label(root, font=('times', 40, 'bold'), bg='black', fg='green')
clock.pack(fill=BOTH, expand=1)
#image = Image.open(TestImage.jpg)
#image.show()
#image = ImageTk.PhotoImage(file = "C:\TestImage.jpg")
#clock.create_image(10, 10, image = image, anchor = NW)
newTime()
root.mainloop()
