# -*- coding: utf-8 -*-

# Author: <Your name>
# License see LICENSE

from PyKDE4.kdecore import i18n
from PyKDE4.kdeui import KAction, KIcon

from PyQt4.QtCore import QObject
from PyQt4.QtGui import QMenu

from libkatepate.errors import showOk, showError

import kate

class MyPlugin(QObject):
  def __init__(self):
    QObject.__init__(self)

    self.window = kate.mainInterfaceWindow().window()
    
    showOk('MyPlugin inits!')
    
    # self.act = KAction(KIcon("reload"), i18n("Auto Reload"), self)
    # self.act.setObjectName("test")
        
    # self.window.actionCollection().addAction(self.act.objectName(), self.act)
    # self.window.findChild(QMenu, 'view').addAction(self.act)

    # if not self.act.objectName() in kate.configuration:
    #    kate.configuration[self.act.objectName()] = "alt+r"

    # self.act.setShortcut(kate.configuration[self.act.objectName()])

    # self.act.setCheckable(True)
    # self.act.setChecked(False)
    
    # self.act.changed.connect(self.onActionChange)
    # self.act.toggled.connect(self.toggle)
    
    # kate.mainInterfaceWindow().viewChanged.connect(self.onViewChanged)  

  def onActionChange(self):
      kate.configuration[self.sender().objectName()] =  self.sender().shortcut().toString()
      kate.configuration.save()
      print(self.sender().objectName() + ': Save ' + kate.configuration[self.sender().objectName()])
  
  