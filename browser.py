from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtWebEngineWidgets import *
import sys

class Browser(QMainWindow):
    def __init__(self):
        super(Browser, self).__init__()
        self.browser = QWebEngineView()
        self.browser.setUrl(QUrl('http://google.com'))
        self.setCentralWidget(self.browser)
        self.showMaximized()

        # navigation bar
        navigation = QToolBar()
        self.addToolBar(navigation)

        back = QAction('Back', self)
        back.triggered.connect(self.browser.back)
        navigation.addAction(back)

        forward = QAction('Forward', self)
        forward.triggered.connect(self.browser.forward)
        navigation.addAction(forward)

        home = QAction('Home', self)
        home.triggered.connect(self.navigatetohome)
        navigation.addAction(home)

        reload1 = QAction(' Refresh ', self)
        reload1.triggered.connect(self.browser.reload)
        navigation.addAction(reload1)

        self.urlbar = QLineEdit()
        self.urlbar.returnPressed.connect(self.gotourl)
        navigation.addWidget(self.urlbar)

        self.browser.urlChanged.connect(self.updatetourl)

    def gotourl(self):
        url = self.urlbar.text()
        self.browser.setUrl(QUrl(url))

    def navigatetohome(self):
        self.browser.setUrl(QUrl('https://google.com'))

    def updatetourl(self, q):
        self.urlbar.setText(q.toString())


B = QApplication(sys.argv)
QApplication.setApplicationName('Browser')
window = Browser()
B.exec_()