# -*- coding: utf-8 -*-
"""Copyright: Arthur Milchior arthur@milchior.fr

"""

import cgi

from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

import anki.notes
from anki.hooks import addHook
from aqt import mw
from aqt.utils import askUser, showWarning, tooltip


def HTML(nids):
    """Show each field's content, and the note id. Click on cancel to stop seeing ids"""
    for nid in nids:
        note = mw.col.getNote(nid)
        text= "\n"
        for (name,value) in list(note.items()):
            text = text+ "\n"+ name + ":\n« "+ cgi.escape(value)+"\n<br/>--------------<br/>\n"
        text = text+ "\nnid: "+ str(note.id)
        if not askUser(text):
            return

def setupMenu(browser):
    a = QAction("Note's HTML", browser)
    a.setShortcut(QKeySequence("Ctrl+H")) # Shortcut for convenience. Added by Didi
    a.triggered.connect(lambda e: onHTML(browser))
    browser.form.menuEdit.addSeparator()
    browser.form.menuEdit.addAction(a)

def onHTML(browser):
    HTML(browser.selectedNotes())

addHook("browser.setupMenus", setupMenu)

