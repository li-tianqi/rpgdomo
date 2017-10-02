#!/usr/bin/env python3
# coding=utf-8

import sys
from PyQt5.QtWidgets import QLabel
from PyQt5.QtCore import pyqtSignal


class ImgLabel(QLabel):
    mouseRelease = pyqtSignal()
    keyPressed = pyqtSignal()
    mouseMoved = pyqtSignal()
    mousePressed = pyqtSignal()
    mouseDoubleClick = pyqtSignal()
    wheel = pyqtSignal()
    
    def mouseReleaseEvent(self, e):
        self.mouseRelease.emit()
        
    def keyPressedEvent(self, e):
        self.keyPressed.emit()
        
    def mouseMovedEvent(self, e):
        self.mouseMoved.emit()
        
    def mousePressed(self, e):
        self.mousePressed.emit()
        
    def mouseDoubleClickEvent(self, e):
        self.mouseDoubleClick.emit()
        
    def wheelEvent(self, e):
        self.wheel.emit()
        