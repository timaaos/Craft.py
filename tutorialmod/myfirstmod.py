import api as mc
import gen_noise
import pyglet
import sys, os
import math
pathname = os.path.dirname(sys.argv[0])
texture = pathname + "\modtexture.png"
mc.TEXTURE_PATH = texture
WILBER_BLOCK = mc.tex_coords((2,2),(2,2),(2,2))
window = mc.Window(width=800, height=600, caption='CraftPy', resizable=True)
window.addToInventory(WILBER_BLOCK,"Wilber",5)
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
