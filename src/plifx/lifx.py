import sys
import os
import lifxUtil

from PyQt5.QtWidgets    import QApplication, QMainWindow, QLabel, QPushButton, QDial, QGridLayout, QWidget, QSlider
from PyQt5.QtGui        import QIcon

#Global Section
btoken = ''

class MyWindow(QWidget):
    def __init__(self):
        super(MyWindow, self).__init__()
        self.x = 0
        self.y = 0
        self.width = 500
        self.height = 500
        self.initUI()

    def initUI(self):
        self.setWindowTitle("Lifx GUI")
        self.setGeometry(self.x, self.y, self.width, self.height)

        self.layout = QGridLayout()

        self.color_dial = QDial(self)
        self.color_dial.setMinimum(0)
        self.color_dial.setMaximum(359)
        self.color_dial.valueChanged.connect(self.print_dial_value)
        self.color_label = QLabel(self)
        self.color_label.setText(str(self.color_dial.value()))

        self.brightness_slider = QSlider(self)
        self.brightness_label = QLabel(self)
        self.brightness_label.setText(str(self.brightness_slider.value()+1))
        self.brightness_slider.valueChanged.connect(self.print_slider_value)

        self.hue_slider = QSlider(self)
        self.hue_label = QLabel(self)
        self.hue_label.setText(str(self.hue_slider.value()+1))
        self.hue_slider.valueChanged.connect(self.print_hue_slider_value)



        self.toggle_btn = QPushButton(self)
        self.toggle_btn.setText("on/off")
        self.toggle_btn.clicked.connect(lambda: lifxUtil.toggle(btoken))

        self.apply_btn = QPushButton(self)
        self.apply_btn.setText("apply")
        self.apply_btn.clicked.connect(lambda: lifxUtil.setColor(btoken, self.color_dial.value(), self.hue_slider.value()+1, self.brightness_slider.value()+1))

        self.layout.addWidget(self.color_dial, 0, 0)
        self.layout.addWidget(self.brightness_slider, 0, 2)
        self.layout.addWidget(self.hue_slider, 0, 1)
        self.layout.addWidget(self.hue_label, 1, 1)
        self.layout.addWidget(self.color_label, 1, 0)
        self.layout.addWidget(self.brightness_label, 1, 2)
        self.layout.addWidget(self.toggle_btn, 2, 2)
        self.layout.addWidget(self.apply_btn, 2, 1)

        self.setLayout(self.layout)

    def print_dial_value(self):
        self.color_label.setText(str(self.color_dial.value()))
    def print_slider_value(self):
        self.brightness_label.setText(str(self.brightness_slider.value()+1))
    def print_hue_slider_value(self):
        self.hue_label.setText(str(self.hue_slider.value()+1))



if __name__ == '__main__':
    app = QApplication(sys.argv)
    win = MyWindow()
    if os.path.exists('token'):
        with open("token", "r") as f:
            f.seek(0)
            btoken = f.read()
        win.show()
    sys.exit(app.exec_())
