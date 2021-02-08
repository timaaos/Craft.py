import api as mc
import pyglet
window = mc.Window(width=800, height=600, caption='CraftPy', resizable=True)
model = mc.Model()
model._initialize()
window.model = model
mc.setup()
pyglet.app.run()
