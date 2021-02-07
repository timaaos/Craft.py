import api as mc
import pyglet
def main():
    window = mc.Window(width=800, height=600, caption='CraftPy', resizable=True)




    mc.setup()
    window.MIN_Y = 0
    pyglet.app.run()
if __name__ == '__main__':
    main()
