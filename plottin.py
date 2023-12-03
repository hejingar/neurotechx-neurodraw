import pandas as pd
from matplotlib import pyplot as plt
from scipy import signal
import numpy as np


#=============================================================================
def butter_bandpass_filter(data, lowcut, highcut, fs, order=2):
    nyq = 0.5 * fs
    low = lowcut /nyq
    high = highcut/nyq
    b, a = butter(order, [low, high], btype='band')
    #print(b,a)
    y = lfilter(b, a, data)
    return y
#=============================================================================

def compute_frequencies_percentage(path):
    plt.rcParams["figure.figsize"] = [7.00, 3.50]
    plt.rcParams["figure.autolayout"] = True
    columns = ["timestamp", "ch1"]
    df = pd.read_csv(path, usecols=columns)
    #cleaning the first and last seconds
    df.drop(df.head(2000).index, inplace=True)
    df.drop(df.tail(2500).index, inplace=True)

    notch_freq = 50 # set to 50 in Europe, 60 in North America
    numerator, denominator = signal.iirnotch(notch_freq, 20, 250)
    filtered_notch_data = signal.filtfilt(b=numerator, a=denominator, x=df.ch1, padtype=None)

    high_pass_freq = 1
    low_pass_freq = 35
    denom, nom = signal.iirfilter(int(3), [1, 35], btype="bandpass", ftype="butter", fs=float(250), output="ba")
    filtered_bp_data = signal.filtfilt(b=denom, a=nom, x=filtered_notch_data, padtype=None)


    fs = 512                                # Sampling rate (512 Hz)
    data = filtered_bp_data

    # Get real amplitudes of FFT (only in postive frequencies)
    fft_vals = np.absolute(np.fft.rfft(data))

    # Get frequencies for amplitudes in Hz
    fft_freq = np.fft.rfftfreq(len(data), 1.0/fs)

    # Define EEG bands
    eeg_bands = {'Delta': (0, 4),
                'Theta': (4, 8),
                'Alpha': (8, 12),
                'Beta': (12, 30),
                'Gamma': (30, 45)}

    # mean of the fft amplitude for each EEG band
    eeg_band_fft = dict()
    for band in eeg_bands:  
        freq_ix = np.where((fft_freq >= eeg_bands[band][0]) & 
                        (fft_freq <= eeg_bands[band][1]))[0]
        eeg_band_fft[band] = np.mean(fft_vals[freq_ix])

    # total mean amplitude
    total_mean_amplitude = sum(eeg_band_fft.values())

    # percentage for each band
    eeg_band_fft_percent = {band: (mean_amplitude / total_mean_amplitude) * 100 for band, mean_amplitude in eeg_band_fft.items()}
    data = [eeg_band_fft_percent[band] for band in eeg_bands]
    return data

# Now eeg_band_fft_percent contains the percentage of each EEG band

# df = pd.DataFrame(columns=['band', 'val'])
# df['band'] = eeg_bands.keys()
# # df['val'] = [eeg_band_fft[band] for band in eeg_bands]
# df['val'] = [eeg_band_fft_percent[band] for band in eeg_bands]
# ax = df.plot.bar(x='band', y='val', legend=False)
# ax.set_xlabel("EEG band")
# ax.set_ylabel("Mean band Amplitude")
# plt.show()


# print("Contents in csv file: ", df)
# plt.xlabel('timestamp', fontsize=10)
# plt.ylabel('EEG', fontsize=10)
# plt.plot(df.timestamp, filtered_bp_data)

# plt.show()