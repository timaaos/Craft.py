import api as mc
import pyglet
import sys, os
pathname = os.path.dirname(sys.argv[0])
texture = pathname + "\modtexture.png"
mc.TEXTURE_PATH = texture
WILBER_BLOCK = mc.tex_coords((2,2),(2,2),(2,2))
window = mc.Window(width=800, height=600, caption='CraftPy', resizable=True)
window.addToInventory(WILBER_BLOCK,"Wilber",5)
model = mc.Model()
model._initialize()
window.model = model
mc.setup()
pyglet.app.run()
