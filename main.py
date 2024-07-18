import sounddevice
from scipy.io.wavfile import write
fs= 44100
second =  int(input("Enter time duration in seconds: "))
print("Recording.....\n")
record_voice = sounddevice.rec( int ( second * fs ) , samplerate = fs , channels = 2 )
sounddevice.wait()
write("out.wav",fs,record_voice)
print("Finished.....\nPlease check your output file")

#codes are taken from https://www.analyticsvidhya.com/blog/2021/10/build-a-voice-recorder-using-python/