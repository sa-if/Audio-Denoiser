from pydub import AudioSegment
import noisereduce as nr
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.style as style

style.use('ggplot')

# Load audio file
audio = AudioSegment.from_file("input.mp3")

# Convert audio to numpy array
samples = np.array(audio.get_array_of_samples())

# Reduce noise
reduced_noise = nr.reduce_noise(samples, sr=audio.frame_rate)

# Plot original and reduced noise signals
fig, ax = plt.subplots(2, 1, figsize=(15,8))
ax[0].set_title("Original signal")
ax[0].plot(samples)
ax[1].set_title("Reduced noise signal")
ax[1].plot(reduced_noise)
plt.show()

# Convert reduced noise signal back to audio
reduced_audio = AudioSegment(
    reduced_noise.tobytes(), 
    frame_rate=audio.frame_rate, 
    sample_width=audio.sample_width, 
    channels=audio.channels
)

# Save reduced audio to file
reduced_audio.export("output.mp3", format="mp3")
