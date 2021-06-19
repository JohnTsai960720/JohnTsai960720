from random import randrange
from mcpi.minecraft import Minecraft
mc=Minecraft.create()

for i in range(100):
    x,y,z=mc.player.getTilePos()
    x=x+i

    for j in range(20):
        r=randrange(0,16)
        z=z+1
        mc.setBlock(x,y,z,35,r)
