import numpy as np
import adi
import time
import sys
import commpy

try:
    import matplotlib.pyplot as plt
    do_plots = True
except:
    print("To view plots install matplotlib")
    do_plots = False

#User config    
sample_rate = 720e3 # Hz
center_freq = 900e6+15.5e3 # Hz

try:
    sdr = adi.Pluto("ip:192.168.2.1")
except:
    print("No device found")
    sys.exit(0)
    
sdr.sample_rate = int(sample_rate)

# Config Tx
sdr.tx_rf_bandwidth = int(sample_rate) # filter cutoff, just set it to the same as sample rate
sdr.tx_lo = int(center_freq)
sdr.tx_hardwaregain_chan0 = 0 # Increase to increase tx power, valid range is -90 to 0 dB

#load file
samples_r = []
samples_i = []
try:
    with open("real.txt") as f, open("imag.txt") as h:
        s = 1
        while s:
            s2 = h.readline()
            s = f.readline()
            s.strip()
            s2.strip()
            s.replace("\n", "")
            s2.replace("\n", "")
            try:
                samples_r.append(float(s))
                samples_i.append(float(s2))
            except ValueError:
                print("End has been read")
except:
    print("file not found")
    sys.exit(0)

#normolize
samples_r = np.array(samples_r)
samples_i = np.array(samples_i)
compl = samples_r+samples_i*1j
samples_norm = abs(compl.max())
samples_ADC = (compl/samples_norm) *2**14

# Start the transmitter
sdr.tx_cyclic_buffer = True # Enable cyclic buffers
sdr.tx(samples_ADC) # start transmitting

input("press Enter to stop")

sys.exit()

