import wave


def infowav(filename):
    w = wave.open(filename, 'rb')
    info = w.getparams()
    # print(info)

    nchannels, sampwidth, framerate, nframes = info[:4]
    time = nframes//framerate
    print("[XMeng] ----- "+filename+" -----")
    print("[XMeng] 通道数："+str(nchannels))    # 通道数
    print("[XMeng] 总时间："+str(time))    # 时间
    print("[XMeng] 每帧字节数："+str(sampwidth))  # 比特宽度 每一帧的字节数
    print("[XMeng] 帧率："+str(framerate))    # 帧率  每秒有多少帧
    print("[XMeng] 总帧数："+str(nframes))      # 总帧数
    print("[XMeng] ----- end -----")
    w.close()
