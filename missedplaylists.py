import feedparser
import csv

purl = "https://gdata.youtube.com/feeds/api/playlists/"

f = open('youtube_failed.csv','a')
w = csv.writer(f)
playlistid = raw_input("Enter the playlist id : ")
prss = feedparser.parse(purl+str(playlistid))
for i in range(prss.entries.__len__()):
    try:
        vrss = feedparser.parse(str(prss.entries[i].id))
    except:
        print(prss.entries[i].id,' not parsed')

    #out = str.join(str(plid,vrss.entries[0].title,vrss.entries[0].description))
    try:
        #print(playlist[plid],vrss.entries[0].title,vrss.entries[0].description)
        w.writerow([prss.feed.title.encode('utf-8'),vrss.entries[0].title.encode('utf-8'),vrss.entries[0].link.encode('utf-8'),vrss.entries[0].description.encode('utf-8')])
    except:
        print("Error detected")
f.close()       
