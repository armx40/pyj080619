from keras.models import Sequential
from keras.layers import Dense
import numpy as np
from superset import generate_candidates

RESISTANCE = np.array([
    100e3,
    95e3,
    105e3,
    110e3,
    115e3,
    90e3,
    120e3,
    125e3,
    130e3,
    135e3
])

watt = np.array([18+((240*240)/r) for r in RESISTANCE])

extra_watts = sum(watt) -18*10
extra_watt_cost = f"Month: 15\nYear: {15*12}"


# generate datasets
# sum all watt
powers = generate_candidates(watt)
sum_of_powers = [sum(i) for i in powers]


model = Sequential()
model.add(Dense(units=64, activation='relu', input_dim=100))
model.add(Dense(units=10, activation='softmax'))


#model.compile(loss='categorical_crossentropy',optimizer='sgd', metrics=['accuracy'])
