#!/usr/bin/env python3
# coding=utf-8

import sys
from PyQt5.QtWidgets import QWidget, QApplication, QLabel
from PyQt5.QtGui import QPixmap, QPainter, QImage, QColor
from PyQt5.QtCore import QTimer, Qt

class RpgFrame(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()


    def initUI(self):
        self.dt_img = QImage()
        self.dt_img.load("dt04.png")

        self.dt_cover_img = QImage()
        self.dt_cover_img.load("dt04_2.png")

        self.dt_collision_img = QImage()
        self.dt_collision_img.load("dt04_3.png")
        #painter = QPainter()
        #painter.begin(self)
        #painter.drawImage(0,0,image)
        #painter.end()
        self.rw_img = QImage()
        self.rw_img.load("rw0201.png")

        a = self.dt_collision_img.pixel(5,5)
        b = QColor(a).getRgb()
        c = QColor(a) == QColor(0,0,0)
        print(b)
        print(c)



        #self.step = 0
        self.rw_img_x = 0
        self.rw_img_y = 0
        self.rw_x = 176
        self.rw_y = 166


        self.dt_img_x = 850
        self.dt_img_y =580


        self.dir = 'E'



        self.timer = QTimer(self)
        self.timer.timeout.connect(self.gostep)
        #self.timer.start(160)
        self.timer.setInterval(160)
        self.flag_D = False
        self.flag_A = False
        self.flag_S = False
        self.flag_W = False

        self.setGeometry(200, 200, 400, 400)
        self.show()

    def gostep(self):
        if self.dir == 'E':
            step = self.collision()
            if self.dt_img_x + 400 + 15 >= 1568:
                self.dt_img_x = 1568 - 400
                if self.rw_x + 48 + 15 >= 400:
                    self.rw_x = 400 - 48
                else:
                    self.rw_x = self.rw_x + step
            else:
                if self.rw_x > 186 or self.rw_x < 166:
                    self.rw_x = self.rw_x + step
                else:
                    self.dt_img_x = self.dt_img_x + step
            self.rw_img_y = 300
            print(step)

        elif self.dir == 'W':
            step = self.collision()
            if self.dt_img_x -15 <= 0:
                self.dt_img_x = 0
                if self.rw_x - 15 <= 0:
                    self.rw_x = 0
                else:
                    self.rw_x = self.rw_x - step
            else:
                if self.rw_x > 186 or self.rw_x < 166:
                    self.rw_x = self.rw_x - step
                else:
                    self.dt_img_x = self.dt_img_x - step
            self.rw_img_y = 150

        elif self.dir == 'S':
            step = self.collision()
            if self.dt_img_y + 400 + 15 >= 1024:
                self.dt_img_y = 1024 - 400
                if self.rw_y + 68 + 15 >= 400:
                    self.rw_y = 400 - 68
                else:
                    self.rw_y = self.rw_y + step
            else:
                if self.rw_y > 176 or self.rw_y < 156:
                    self.rw_y = self.rw_y + step
                else:
                    self.dt_img_y = self.dt_img_y + step
            self.rw_img_y = 0

        else:
            step = self.collision()
            if self.dt_img_y - 15 <= 0:
                self.dt_img_y = 0
                if self.rw_y -15 <= 0:
                    self.rw_y = 0
                else:
                    self.rw_y = self.rw_y - step
            else:
                if self.rw_y > 176 or self.rw_y < 156:
                    self.rw_y = self.rw_y - step
                else:
                    self.dt_img_y = self.dt_img_y - step
            self.rw_img_y = 450


        if self.rw_img_x == 840:
            self.rw_img_x = 0
        else:
            self.rw_img_x = self.rw_img_x + 120

        self.update()


    def collision(self):
        a = self.dt_img_x + self.rw_x
        b = self.dt_img_y + self.rw_y
        if self.dir == 'E':
            range_j = range(b+10, b+58)
            for i in range(15):
                for j in range_j:
                    if QColor(self.dt_collision_img.pixel(a + 30 + 1 + i, j)) == QColor(0,0,0):
                        return i
            return 15
        elif self.dir == 'W':
            range_j = range(b+10, b+58)
            for i in range(15):
                for j in range_j:
                    if QColor(self.dt_collision_img.pixel(a+18 - 1 - i, j)) == QColor(0,0,0):
                        return i
            return 15
        elif self.dir == 'S':
            range_j = range(a+18, a+30)
            for i in range(15):
                for j in range_j:
                    if QColor(self.dt_collision_img.pixel(j, b + 58 + 1 + i)) == QColor(0,0,0):
                        return i
            return 15
        else:
            range_j = range(a+18, a+30)
            for i in range(15):
                for j in range_j:
                    if QColor(self.dt_collision_img.pixel(j, b+10 - 1 - i)) == QColor(0,0,0):
                        return i
            return 15




    def paintEvent(self, event):
        painter = QPainter(self)
        painter.begin(self)
        painter.drawImage(0, 0, self.dt_img, self.dt_img_x, self.dt_img_y, 400, 400)
        painter.drawImage(0,0, self.dt_collision_img, self.dt_img_x, self.dt_img_y, 400, 400)
        painter.drawImage(self.rw_x, self.rw_y, self.rw_img, self.rw_img_x + 36, self.rw_img_y + 41, 48, 68)
        #painter.drawImage(0, 0, self.dt_cover_img, self.dt_img_x, self.dt_img_y, 400, 400)
        painter.end()


    def keyPressEvent(self, e):
        if e.key() == Qt.Key_D and not e.isAutoRepeat():
            self.dir = 'E'
            if not self.flag_D:
                self.long_D = -1
                self.timer.start()
            self.flag_D = True
        #print("1")
        #print(e.isAutoRepeat())
        if e.key() == Qt.Key_A and not e.isAutoRepeat():
            self.dir = 'W'
            if not self.flag_A:
                self.long_A = -1
                self.timer.start()
            self.flag_A = True
        if e.key() == Qt.Key_S and not e.isAutoRepeat():
            self.dir = 'S'
            if not self.flag_S:
                self.long_S = -1
                self.timer.start()
            self.flag_S = True
        if e.key() == Qt.Key_W and not e.isAutoRepeat():
            self.dir = 'N'
            if not self.flag_W:
                self.long_W = -1
                self.timer.start()
            self.flag_W = True

    def keyReleaseEvent(self, e):
        if e.key() == Qt.Key_D and not e.isAutoRepeat() and self.long_D == -1:
            if self.flag_D:
                self.long_D = 0
                self.timer.stop()
                self.rw_img_x = 0
                self.update()
            self.flag_D = False
        #print("2")
        #print(e.isAutoRepeat())
        if e.key() == Qt.Key_A and not e.isAutoRepeat() and self.long_A == -1:
            if self.flag_A:
                self.long_A = 0
                self.timer.stop()
                self.rw_img_x = 0
                self.update()
            self.flag_A = False
        if e.key() == Qt.Key_S and not e.isAutoRepeat() and self.long_S == -1:
            if self.flag_S:
                self.long_S = 0
                self.timer.stop()
                self.rw_img_x = 0
                self.update()
            self.flag_S = False
        if e.key() == Qt.Key_W and not e.isAutoRepeat() and self.long_W == -1:
            if self.flag_W:
                self.long_W = 0
                self.timer.stop()
                self.rw_img_x = 0
                self.update()
            self.flag_W = False





if __name__ == "__main__":
    app = QApplication(sys.argv)
    a = RpgFrame()
    sys.exit(app.exec_())

