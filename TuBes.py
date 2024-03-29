import streamlit as st
from streamlit_option_menu import option_menu
import numpy as np
import matplotlib.pyplot as plt

def generate_ask_signal(bits, bit_rate, carrier_freq, amplitude):
    time_per_bit = 1 / bit_rate
    t = np.linspace(0, len(bits) * time_per_bit, len(bits) * 1000)
    carrier_signal = amplitude * np.sin(2 * np.pi * carrier_freq * t)

    ask_signal = []
    for bit in bits:
        if bit == '1':
            ask_signal.extend(amplitude * np.sin(2 * np.pi * carrier_freq * t[t <= time_per_bit]))
        else:
            ask_signal.extend(np.zeros(len(t[t <= time_per_bit])))

    return t, ask_signal, carrier_signal

def plot_ask_signal_matplotlib(t, ask_signal, carrier_signal):
    plt.figure(figsize=(10, 6))
    plt.subplot(3, 1, 1)
    plt.plot(t, ask_signal, label='Sinyal ASK', color='blue')
    plt.title('Amplitude Shift Keying (ASK) Signal')
    plt.xlabel('Waktu')
    plt.ylabel('Amplitudo')
    plt.legend()

    plt.subplot(3, 1, 2)
    plt.plot(t, carrier_signal, label='Sinyal Pembawa', color='green')
    plt.title('Carrier Signal')
    plt.xlabel('Waktu')
    plt.ylabel('Amplitudo')
    plt.legend()

    plt.subplot(3, 1, 3)
    plt.plot(t, ask_signal, label='Sinyal ASK', color='blue')
    plt.plot(t, carrier_signal, label='Sinyal Pembawa', color='green')
    plt.title('Combined Signal')
    plt.xlabel('Waktu')
    plt.ylabel('Amplitudo')
    plt.legend()

    plt.tight_layout()
    plt.show()

# Input parameters
bits_input = input("Masukkan urutan bit (0 dan 1, tanpa spasi): ")
bits = list(bits_input)
bit_rate = float(input("Masukkan tingkat bit (bit per detik): "))
carrier_freq = float(input("Masukkan frekuensi pembawa: "))
amplitude = float(input("Masukkan amplitudo sinyal: "))

# Generate ASK signal
t, ask_signal, carrier_signal = generate_ask_signal(bits, bit_rate, carrier_freq, amplitude)

# Plot ASK signal menggunakan Matplotlib
plot_ask_signal_matplotlib(t, ask_signal, carrier_signal)
