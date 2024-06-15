import soundfile as sf
from matplotlib import pyplot as plt

signal,sample_rate=sf.read("/home/rguktrkvalley/computational lab/week7/sample-3s.wav")

'''duration=len(signal)/sample_rate'''

time=[i/sample_rate for i in range(len(signal))]

plt.figure(figsize=(10,4))
plt.plot(time,signal)
plt.title("audio signal")
plt.grid(True)
plt.show()
