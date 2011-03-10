import urllib
import csv
import feedparser
from xml.dom import minidom
playlist = {}
url = "https://gdata.youtube.com/feeds/api/users/TedxTalks/playlists?v=2&max-results=50&start-index="

purl = "https://gdata.youtube.com/feeds/api/playlists/"
for i in range(10):
    rss = feedparser.parse(url+str(1+i*50))
    for i in range(rss.entries.__len__()):
        playlist[rss.entries[i].yt_playlistid] = rss.entries[i].title

#print(playlist)

f = open('youtube.csv','w')
w = csv.writer(f)
g = open('failure','w')

plcount = 0
missed = 0
vcount = 0
for plid in playlist:
    try:
        prss = feedparser.parse(purl+str(plid))
        plcount += 1
    except:
    	print(playlist[plid],' not parsed')
    for i in range(prss.entries.__len__()):
        try:
        	vrss = feedparser.parse(str(prss.entries[i].id))
        	vcount += 1
        except:
        	print(prss.entries[i].id, 'not parsed')
        try:
            #print(playlist[plid],vrss.entries[0].title,vrss.entries[0].description)
            w.writerow([playlist[plid].encode('utf-8'),vrss.entries[0].title.encode('utf-8'),vrss.entries[0].link.encode('utf-8'),vrss.entries[0].description.encode('utf-8')])
        except:
            print("Could not encode")
            g.write(str(plid))
            g.write('\n')
            print(plid)
            print(prss.entries[i].id, 'not encoded')
            missed = missed + 1
print(missed)
print("Playlists ",plcount)
print("Videos total ",vcount)
f.close()
g.close()
