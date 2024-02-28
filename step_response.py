"""! @file step_response.py
Program that creates a step response and records the voltage values at set time intervals using a timer interrupt
"""
import cqueue
import utime

def timer_int(tim_num):
    """!
    Timer Interrupt that places the values of pin B0 into a queue for the main function to read
    """
    if volt_queue.full() == False:
        
        volt_queue.put(pinB0.read()) # add voltage values to queue
        
    else:
        pass

def step_response (voltage):
    """!
    Runs the step response and initializes the timer interrupt
    """
    pinC0.value(voltage) # set pin
    timeint.callback (timer_int) # intialize timer interrupt
    utime.sleep(2) # wait to allow interrupt to collect data
        


if __name__ == "__main__":
    pinC0 = pyb.Pin(pyb.Pin.board.PC0, pyb.Pin.OUT_PP) # Initialize pin C0
    pinB0 = pyb.ADC(pyb.Pin.board.PB0) # Initialize pin B0
    timeint = pyb.Timer (1, freq = 100) # create timer interrupt
    QUEUE_SIZE = 200 # define queue size
    volt_queue = cqueue.IntQueue(QUEUE_SIZE) # create queue with chosen size
    voltage = 1 # value to set C0 to, corresponds to 3.3v
    time = 0 # set up a time variable that tracks the elapsed time
    pinC0.value(0) # clear any previous input to C0
    utime.sleep(2) # wait to allow pin to return to 0 voltage
    step_response(voltage) # run step response
    while volt_queue.any(): # pull items from queue and print to shell
        print(f'{time},{volt_queue.get()/1000}') 
        time += 10 # track elapsed time
        if time == 2000:
            break
    print("end") # end of program
    