import api as mc
import pyglet
import sys, os
pathname = os.path.dirname(sys.argv[0])
texture = pathname + "\modtexture.png"
mc.TEXTURE_PATH = texture
window = mc.Window(width=800, height=600, caption='CraftPy', resizable=True)
model = mc.Model()
model._initialize()
window.model = model
mc.setup()
pyglet.app.run()
