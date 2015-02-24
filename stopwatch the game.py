# template for "Stopwatch: The Game"
import simplegui

# define global variables
interval = 100
message = 0
points = 0
attempts = 0
isRunning = False

# define helper function format that converts time
# in tenths of seconds into formatted string A:BC.D
def format(t):
    D = t % 10
    C = ((t - D) / 10) % 10
    B = ((t - D) / 100) % 6
    A = (t / 10 / 60) % 10
    
    time = str(A) + ":" + str(B) + str(C) + "." + str(D)
    return time
    
    
def format_points():
    global points, attempts
    return str(points) + "/" + str(attempts)
    
# define event handlers for buttons; "Start", "Stop", "Reset"
def start():
    global isRunning
    timer.start()
    isRunning = True

def stop():
    global points, attempts, isRunning
    timer.stop()
    time = format(message)
    if (time[-1] == "0" and isRunning == True):
        points += 1
    if (isRunning == True):
        attempts += 1
    isRunning = False
    
def reset():
    global message, points, attempts
    timer.stop()
    message = 0
    points = 0
    attempts = 0
    
# define event handler for timer with 0.1 sec interval
def tick():
    global message
    message += 1

# define draw handler
def draw(canvas):
    canvas.draw_text(format(message),[100, 100], 24, "White")
    canvas.draw_text(format_points(),[200, 25], 24, "White")
    
# create frame
frame = simplegui.create_frame("Stopwatch: The Game", 300, 200)

# register event handlers
frame.set_draw_handler(draw)
timer = simplegui.create_timer(interval, tick)
frame.add_button("Start", start, 100)
frame.add_button("Stop", stop, 100)
frame.add_button("Reset", reset, 100)


# start frame
frame.start()

