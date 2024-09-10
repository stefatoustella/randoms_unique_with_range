import os
import random

first_number = int(input("First number: "))
last_number = int(input("Last number: "))

how_many = int(input("How many numbers do you want? "))

if how_many > ((last_number + 1) - first_number):
    # make a sound alert
    duration = 0.1  # seconds
    freq = 262  # Hz
    os.system("play -nq -t alsa synth {} sine {}".format(duration, freq))
    duration = 0.1  # seconds
    freq = 294  # Hz
    os.system("play -nq -t alsa synth {} sine {}".format(duration, freq))
    duration = 0.1  # seconds
    freq = 330  # Hz
    os.system("play -nq -t alsa synth {} sine {}".format(duration, freq))
    duration = 0.1  # seconds
    freq = 349  # Hz
    os.system("play -nq -t alsa synth {} sine {}".format(duration, freq))
    duration = 0.1  # seconds
    freq = 392  # Hz
    os.system("play -nq -t alsa synth {} sine {}".format(duration, freq))
    duration = 0.1  # seconds
    freq = 440  # Hz
    os.system("play -nq -t alsa synth {} sine {}".format(duration, freq))
    duration = 0.1  # seconds
    freq = 494  # Hz
    os.system("play -nq -t alsa synth {} sine {}".format(duration, freq))
    duration = 0.5  # seconds
    freq = 523  # Hz
    os.system("play -nq -t alsa synth {} sine {}".format(duration, freq))

    # speak!
    os.system(
        'spd-say "You made a mistake! Your program has modified your how_many variable"'
    )
    print("You have exceed the Max of your Last Number!!!")
    how_many = (last_number + 1) - first_number
    result = random.sample(range(first_number, last_number + 1), how_many)
    print(result)
else:
    result = random.sample(range(first_number, last_number + 1), how_many)
    print(result)
