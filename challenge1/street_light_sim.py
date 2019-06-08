import numpy as np
import os 
import datetime
import matplotlib.pyplot as plt

def get_chance():
    for i in range(10000):
        r = np.random.normal(1)
        if r < -2.6:
            #print(r)
            #print("breaked")
            #print(i)
            return True


class street_light():
    def __init__(self):
        self.first_boot = datetime.datetime.now()
        self.datetime = datetime.datetime.now()
        self.power_usage = 0
        self.state = False
        self.voltage = 240
        self.reactive_power = 0
        self.inductive_power = 0
        self.current_usage = 0.072 
        
        self.mean_voltage = 240
        self.mean_current = 0.072

        self.FAULT = False
        self.fault_count = 100
        
        self.FAULT_time = 0

    def time_step(self):
        if self.FAULT == True:
            return
        
        one_time_later = datetime.timedelta(hours=1)
        self.datetime = self.datetime + one_time_later
        
        # change physical constants
        r=np.random.normal()
        self.voltage = self.mean_voltage + r
        
        r = r*np.random.normal(scale=self.current_usage/100)
        self.current_usage = self.mean_current + r

        self.power_usage = self.voltage * self.current_usage

        if get_chance():
            self.fault_count -=1

        if not self.FAULT:
            if self.fault_count == 0:
                self.FAULT = True
                self.FAULT_time = self.datetime
                return

    def __repr__(self):
        return f"<street_light/{os.urandom(8).hex()}>"




def routine():
    s = street_light()
    x=[]
    y=[]
    x_i = 0
    while(1):
        if s.FAULT == True:
            break
        x.append(x_i)
        x_i += 1
        s.time_step()
        y.append([s.current_usage,s.voltage,s.power_usage])

    for i in range(len(y[0])):
        plt.plot(x,y)
        plt.show(block=False)
