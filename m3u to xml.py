import re,os,glob

for file in glob.glob("*.m3u"):
    f01 = open(file)
f01 = f01.read()
name = file.replace('.m3u','.xml')
XML = open(name,'w')
line1 = '<streamingInfos>\n'


XML.write(line1)



p = re.compile(ur'#EXTINF:.+?,(.+?)\n')
pp = re.compile(ur'\n(.+?).ts')
mm = re.findall(pp, f01)
m = re.findall(p, f01)
names = []
urls = []
for name in m:
    names.append(name)
for url in mm:
    urls.append(url)
i = 0
while len(names) > i:
    XML.write( '<item>'+'\n<title>'+names[i]+'</title>\n<link>plugin://plugin.video.f4mTester/?streamtype=TSDOWNLOADER&amp;url='+urls[i]+'.ts'+'</link>\n</item>')
    i += 1

XML.close()
