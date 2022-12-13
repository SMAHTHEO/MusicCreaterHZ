

import wave
import struct
import math
import random
sampleRate = 12800  # hertz
duration = 1.0  # seconds
frequency = 440.0  # hertz
obj = wave.open('001.wav', 'w')
obj.setnchannels(1)  # mono
obj.setsampwidth(2)
obj.setframerate(sampleRate)
for i in range(25600):  # 50
    value = 0
    if i % 512 == 0:
        value = 20000
    if i % 512 == 256:
        value = - 20000
    data = struct.pack('<h', value)
    obj.writeframesraw(data)
for i in range(25600):  # 100
    value = 0
    if i % 256 == 0:
        value = 20000
    if i % 256 == 128:
        value = - 20000
    data = struct.pack('<h', value)
    obj.writeframesraw(data)
for i in range(25600):  # 200
    value = 0
    if i % 128 == 0:
        value = 20000
    if i % 128 == 64:
        value = - 20000
    data = struct.pack('<h', value)
    obj.writeframesraw(data)
for i in range(25600):  # 400
    value = 0
    if i % 64 == 0:
        value = 20000
    if i % 64 == 32:
        value = - 20000
    data = struct.pack('<h', value)
    obj.writeframesraw(data)
for i in range(25600):  # 800
    value = 0
    if i % 32 == 0:
        value = 20000
    if i % 32 == 16:
        value = - 20000
    data = struct.pack('<h', value)
    obj.writeframesraw(data)
for i in range(25600):  # 1600
    value = 0
    if i % 16 == 0:
        value = 20000
    if i % 16 == 8:
        value = - 20000
    data = struct.pack('<h', value)
    obj.writeframesraw(data)
for i in range(25600):  # 3200
    value = 0
    if i % 8 == 0:
        value = 20000
    if i % 8 == 4:
        value = - 20000
    data = struct.pack('<h', value)
    obj.writeframesraw(data)
for i in range(25600):  # 6400
    value = 0
    if i % 4 == 0:
        value = 20000
    if i % 4 == 2:
        value = - 20000
    data = struct.pack('<h', value)
    obj.writeframesraw(data)






obj.close()
