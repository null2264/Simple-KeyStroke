#!/usr/bin/env python3

import sys
from PyQt5.QtCore import *
from PyQt5.QtGui import QPalette, QColor, QFont
from PyQt5.QtWidgets import *
import keyboard, mouse

# ---- ColorSchemes
# Human Readable ColorSchemes
# scheme_name = [background, foreground]
zi_dark = ["2F3640", "ffffff"] # normal
zi_darkP = ["37B0FF", "ffffff"] # pressed

# Readable Color by the codes
colorscheme = str("* {background:" + "#" + str(zi_dark[0]) + "; color: " + "#" + str(zi_dark[1]) + "}")
colorscheme_pressed = str("* {background:" + "#" + str(zi_darkP[0]) + "; color: " + "#" + str(zi_darkP[1]) + "}")

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(132, 132)
        Form.setStyleSheet(u"* {background: #44BD32}")
        font = QFont()
        font.setFamily(u"Google Sans")
        font.setBold(True)
        font.setWeight(75)
        self.lab_up = QLabel(Form)
        self.lab_up.setFont(font)
        self.lab_up.setGeometry(QRect(50, 15, 31, 31))
        self.lab_up.setStyleSheet(colorscheme)
        self.lab_up.setAlignment(Qt.AlignCenter)
        self.lab_up.setObjectName("lab_up")
        self.lab_left = QLabel(Form)
        self.lab_left.setFont(font)
        self.lab_left.setGeometry(QRect(15, 50, 31, 31))
        self.lab_left.setStyleSheet(colorscheme)
        self.lab_left.setAlignment(Qt.AlignCenter)
        self.lab_left.setObjectName("lab_left")
        self.lab_down = QLabel(Form)
        self.lab_down.setFont(font)
        self.lab_down.setGeometry(QRect(50, 50, 31, 31))
        self.lab_down.setStyleSheet(colorscheme)
        self.lab_down.setAlignment(Qt.AlignCenter)
        self.lab_down.setObjectName("lab_down")
        self.lab_right = QLabel(Form)
        self.lab_right.setFont(font)
        self.lab_right.setGeometry(QRect(85, 50, 31, 31))
        self.lab_right.setStyleSheet(colorscheme)
        self.lab_right.setAlignment(Qt.AlignCenter)
        self.lab_right.setObjectName("lab_right")
        self.lab_x = QLabel(Form)
        self.lab_x.setFont(font)
        self.lab_x.setObjectName(u"lab_x")
        self.lab_x.setGeometry(QRect(15, 85, 66, 31))
        self.lab_x.setStyleSheet(colorscheme)
        self.lab_x.setAlignment(Qt.AlignCenter)
        self.lab_c = QLabel(Form)
        self.lab_c.setFont(font)
        self.lab_c.setObjectName(u"lab_c")
        self.lab_c.setGeometry(QRect(85, 85, 31, 31))
        self.lab_c.setStyleSheet(colorscheme)
        self.lab_c.setAlignment(Qt.AlignCenter)

        self.retranslateUi(Form)
        QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QCoreApplication.translate
        Form.setWindowTitle(_translate("KeyStroke", "KeyStroke"))
        self.lab_up.setText(_translate("Form", "↑"))
        self.lab_left.setText(_translate("Form", "A"))
        self.lab_down.setText(_translate("Form", "↓"))
        self.lab_right.setText(_translate("Form", "D"))
        self.lab_x.setText(_translate("Form", "X"))
        self.lab_c.setText(_translate("Form", "C"))

def release_up(f): 
    ui.lab_up.setStyleSheet(str(colorscheme))
def pressed_up(f):
    ui.lab_up.setStyleSheet(str(colorscheme_pressed))
def release_down(f): 
    ui.lab_down.setStyleSheet(str(colorscheme))
def pressed_down(f):
    ui.lab_down.setStyleSheet(str(colorscheme_pressed))
def release_a(f): 
    ui.lab_left.setStyleSheet(str(colorscheme))
def pressed_a(f):
    ui.lab_left.setStyleSheet(str(colorscheme_pressed))
def release_d(f): 
    ui.lab_right.setStyleSheet(str(colorscheme))
def pressed_d(f):
    ui.lab_right.setStyleSheet(str(colorscheme_pressed))
def release_x(f): 
    ui.lab_x.setStyleSheet(str(colorscheme))
def pressed_x(f):
    ui.lab_x.setStyleSheet(str(colorscheme_pressed))
def release_c(f): 
    ui.lab_c.setStyleSheet(str(colorscheme))
def pressed_c(f):
    ui.lab_c.setStyleSheet(str(colorscheme_pressed))

# ---- Init
app = QApplication(sys.argv)
window = QWidget()
ui = Ui_Form()
ui.setupUi(window)

# ---- Hotkeys
# keyboard.add_hotkey('a', set_style_bgwhite) ---- This is a test
keyboard.on_press_key('up',pressed_up)
keyboard.on_release_key('up',release_up)
keyboard.on_press_key('down',pressed_down)
keyboard.on_release_key('down',release_down)
keyboard.on_press_key('a',pressed_a)
keyboard.on_release_key('a',release_a)
keyboard.on_press_key('d',pressed_d)
keyboard.on_release_key('d',release_d)
keyboard.on_press_key('c',pressed_c)
keyboard.on_release_key('c',release_c)
keyboard.on_press_key('x',pressed_x)
keyboard.on_release_key('x',release_x)

# ---- Launch Window
window.show()
sys.exit(app.exec_())
