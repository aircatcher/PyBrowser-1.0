import sys

from PySide2.QtWidgets import QApplication, QLabel, QLineEdit, QWidget
from PySide2.QtCore import QUrl
from PySide2.QtGui import *
from PySide2.QtWebEngineWidgets import QWebEngineView

app = QApplication(sys.argv)

view = QWebEngineView()
view.load(QUrl('https://www.youtube.com'))
view.show()

sys.exit(app.exec_())