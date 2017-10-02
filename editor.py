#!/usr/bin/env python3
# coding=utf-8

import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QPushButton, QVBoxLayout, QFileDialog, QScrollArea, QFrame
from PyQt5.QtGui import QImage, QPixmap


class Editor(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
    
    def initUI(self):
        self.frame = QFrame(self)
        
        self.img = QLabel(self)
        
        self.scroll = QScrollArea(self)
        
        self.openbtn = QPushButton("open", self)
        self.openbtn.clicked.connect(self.openbtnclicked)
        
        self.scroll.setWidget(self.frame)
        self.scroll.setAutoFillBackground(True)
        self.scroll.setWidgetResizable(True)
        
        print("output -> ", self.scroll.width())
        
        vbox = QVBoxLayout()
        vbox.addWidget(self.scroll)
        vbox.addWidget(self.openbtn)
        self.setLayout(vbox)
        
        self.setGeometry(100, 100, 800, 600)
        self.setMinimumSize(800,600)
        self.show()
        
        
    def openbtnclicked(self):
        self.filename = QFileDialog.getOpenFileName(self, "Open Picture", ".")[0]
        if len(self.filename):
            image = QImage(self.filename)
            #self.
            self.img.setPixmap(QPixmap.fromImage(image))
            
            
if __name__ == "__main__":
    app = QApplication(sys.argv)
    e = Editor()
    sys.exit(app.exec_())