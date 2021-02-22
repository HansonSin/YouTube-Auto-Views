import time
import webbrowser

# parameters
link = "https://www.youtube.com/watch?v=dQw4w9WgXcQ" # change to the target youtube link
loopcount = 100 # how many times will the program loop
waittime = 5 # how long does the program wait every session in seconds

webbrowser.open(link)
for i in range(loopcount):
    print(i+1)
    webbrowser.open(link, new=0)
    time.sleep(waittime)
print("Quitting program...")
