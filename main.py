from PIL import Image
import matplotlib.pyplot as plt
import numpy as np
#matplotlib inline

image=Image.open("/Users/aliah/Desktop/python/S2A_tile.png")
image.show()
plt.imshow(image)
print(image.size)
print(image.format)
print(image.mode)

with Image.open("/Users/aliah/Desktop/python/S2A_tile.png") as im:
    im= im.rotate(90)
    im.show()
    im = im.convert('L')
    im.show()


image_array =np.array(image)
spectrum = np.fft.fft2(image_array)
spectrum_shifted= np.fft.fftshift(spectrum)
magnitude = np.abs(spectrum_shifted)
phase = np.angle(spectrum_shifted)
plt.imshow(magnitude, cmap='gray')
plt.title('magnitude of spectrum')
plt.show()
plt.imshow(phase, cmap='gray')
plt.title('phase of spectrum')
plt.show()
fx,fy = np.meshgrid(np.fft.fftfreq(image_array.shape[1]),np.fft.fftfreq(image_array.shape[0]))

plt.plot(fx,magnitude)
plt.xlabel('Frequency(Hz)')
plt.ylabel('Magnitude')
plt.title('Magnitude of spectrum')
plt.show()

plt.plot(fx, phase)
plt.xlabel('Frequency(Hz)')
plt.ylabel('Phase (radians)')
plt.title('Phase of spectrum')
plt.show()