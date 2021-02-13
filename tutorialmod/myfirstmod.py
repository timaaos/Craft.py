import api as mc
from Block import Block
import gen_noise
import pyglet
import sys, os
import math
pathname = os.path.dirname(sys.argv[0])
texture = pathname + "\modtexture.png"
mc.TEXTURE_PATH = texture
WILBER_BLOCK = Block()
WILBER_BLOCK.name = "Wilber"
WILBER_BLOCK.col = 5
window = mc.Window(width=800, height=600, caption='CraftPy', resizable=True)
window.inventory.append(WILBER_BLOCK)
model = mc.Model()
model._initialize()
window.model = model
window.transparentblocks.append(WILBER_BLOCK)
noise = gen_noise.noise(model.WORLDSIZE)
for noisearr in noise:
   for noisenum in noisearr:
      if(noisenum>0.2):
          pos = (noise.index(noisearr)-model.WORLDSIZE/2, math.floor(noisenum*15), noisearr.index(noisenum)-model.WORLDSIZE/2)
          if (not model.world.__contains__(pos)):
            model.add_block(pos,WILBER_BLOCK)
mc.setup()
pyglet.app.run()
