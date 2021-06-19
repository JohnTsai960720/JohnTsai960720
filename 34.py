from random import randrange
from time import sleep
from mcpi.minecraft import Minecraft
mc=Minecraft.create()

r = randrange(1,16)
t=0
while True:
    hits=mc.events.pollBlockHits()
    if len(hits)>0:
        hit = hits[0]
        
        block=mc.getBlockWithData(hit.pos)
        data=block.data
        if data == r:
            mc.postToChat("恭喜找到我")
            mc.setBlock(hit.pos,57)
            break
        elif data < r:
            mc.postToChat("找錯了!試試更大的ID吧")
        elif data > r:
            mc.postToChat("找錯了!試試更小的ID吧")
        t=t+1
        if t>5:
            mc.postToChat("失敗")
            sleep(3)
            x,y,z = mc.player.getPos()
            mc.createExplosion(x,y,z)