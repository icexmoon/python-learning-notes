import requests
import time
startTime = time.time()
imgUrls = []
musicNames = ['前前前世「君の名は」 - 长泽陵川', '田中理恵 - 水の証', '雪の华 - 中島美嘉', 'Kyle Xian - 僕らの戦場（超时空要塞Δ 插曲）',
              'THIS ILLUSION(FGOW ver.) - FateGrand Order', 'Try Everything - Just Kids', 'YoRHa - Weight of the World／the End of YoRHa', 'トライアングラー／坂本真綾 - 动漫原声']
for i in range(1, 7):
    imgUrls.append("http://myweb.com/images/{}.jpg".format(i))
musicUrls = []
for i in musicNames:
    musicUrls.append("http://myweb.com/musics/{}.mp3".format(i))
webResources = []
webResources.extend(imgUrls)
webResources.extend(musicUrls)
for resurceUrl in webResources:
    resp = requests.get(resurceUrl, timeout=60)
    *_,fileName = resurceUrl.rpartition('/')
    with open(file='downloads/{}'.format(fileName),mode='wb') as fopen:
        fopen.write(resp.content)
endTime = time.time()
print("the time spends is {:.2f}s".format(endTime-startTime))
print('end')
# the time spends is 0.13s
# end
