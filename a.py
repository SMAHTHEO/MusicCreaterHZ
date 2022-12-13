

import wave, struct

f = wave.open("file.wav","wb")

# 设置声道数
f.setnchannels(1)
# 设置采样位数，单位字节
f.setsampwidth(2)
# 设置采样频率
f.setframerate(44100)
# 设置总帧数为n，若之后写入数据的总帧数不一致，会更新此数
f.setnframes(88200)
# 设置压缩格式。目前只支持 NONE 即无压缩格式，一般没用
# f.setcomptype(type, name)
# 设置各项参数，形式同前面getparams()返回的tuple
# f.setparams(tuple)
data = struct.pack('<h', 400)
for i in range(88200):
    f.writeframesraw( data )
f.close()




