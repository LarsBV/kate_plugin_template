# -*- coding: utf-8 -*-

from .my_plugin import *


@kate.init
def init():
  global plugin
  plugin = MyPlugin()
  
@kate.unload
def unload():
    global plugin
    if plugin:
        del plugin
        plugin = None
