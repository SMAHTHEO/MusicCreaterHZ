
import wave
f = wave.open ('file.wav', 'rb' )
params = f.getparams ()
nchannels,sampuidth,framerate,nframes=params[:4]
print("元组：(声道数,量化位数(byte单位),,采样频率,采样点数,压缩类型,压缩类型)")
print (params)
channel=f.getnchannels()
print("通道数：",channel)
sampwidth = f.getsampwidth ( )
print("比特宽度每一帧的字节数：",sampwidth)
framerate=f.getframerate()
print("顿率每秒有多少帧：",framerate)
frames=f.getnframes()
print("顿数：",frames)
duration = frames/framerate
print("音频持续时间单位秒：",duration)
audio=f.readframes(frames)
print("按帧读音频,返回二进制数据：",audio)