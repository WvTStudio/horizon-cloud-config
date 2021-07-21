import os
import json
import re

originurl = 'https://gitlab.com/zhekasmirnov/horizon-cloud-config/raw/master/'
afterurl = 'https://cdn.jsdelivr.net/gh/WvTStudio/horizon-cloud-config@master/'

packjsonfile = open(os.path.join('tmp', 'packs.json'))
origin = packjsonfile.read()
packjsonfile.close()
origin = re.sub(originurl, afterurl, origin)
# print(origin)
origin = json.loads(origin)

import sys,os

def split(fromfile,todir,chunksize):
    partnum = 0
    partmap = {}
    inputfile = open(fromfile,'rb')#open the fromfile
    while True:
        chunk = inputfile.read(chunksize)
        if not chunk:             #check the chunk is empty
            break
        partnum += 1
        filename = os.path.join(todir,('part%04d'%partnum))
        partmap['part%04d'%partnum]=afterurl+todir+('/part%04d'%partnum)
        fileobj = open(filename,'wb')#make partfile
        fileobj.write(chunk)         #write data into partfile
        fileobj.close()
    return partmap

packs = []
for i in origin['packs']:
    print(i['uuid'])
    filename = re.search('(?<=master/).+',i['package']).group()
    filedir = re.search('(?<=master/).+?(?=/)',i['package']).group()
    packjson = split(filename,filedir,1024*1024*10)
    i['package'] = packjson
    packs.append(i)
    os.remove(filename)

origin['packs'] = packs
print(json.dumps(origin, sort_keys=True, indent=4))
packjsonfile = open(os.path.join('.', 'packs.json'),'w')
packjsonfile.write(json.dumps(origin, sort_keys=True, indent=4))
