#!/usr/bin/env python3
from pyglet.gl import *
from pyglet.window import NoSuchConfigException

from rubiks import CubeController, CubeView


if __name__ == '__main__':
    controller = CubeController()

    platform = pyglet.window.get_platform()
    display = platform.get_default_display()
    screen = display.get_default_screen()
    try:
        template = pyglet.gl.Config(depth_size=24, sample_buffers=1, samples=4)
        config = screen.get_best_config(template)
    except NoSuchConfigException:
        config = screen.get_best_config()

    window = pyglet.window.Window(width=1024, height=768, caption="The Rubik's Cube", resizable=True, config=config)
    window.push_handlers(controller.on_key_press)
    view = CubeView(controller, window)

    pyglet.app.run()
