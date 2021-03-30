import time

start_time = time.time()

def main():
    timer = True
    while(timer):
        if((time.time() - start_time) >= 2):
            print("Timer Is Up!!")
            timer = False

main()
