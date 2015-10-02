from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtMultimedia import *
import os
import threading

exitFlag=0

class myThread (threading.Thread):
    def __init__(self, threadID):
        threading.Thread.__init__(self)
        self.threadID = str(threadID)


    def run(self):
        print("Starting")

        os.system("python3 callThis.py")
        print("Exiting")
        exitFlag=1



class Form(QWidget):
    def __init__(self, parent=None):
        super(Form, self).__init__(parent)

        nameLabel = QLabel("Name:")
        self.nameLine = QLineEdit()
        self.submitButton = QPushButton("&amp;Submit")

        buttonLayout1 = QVBoxLayout()
        buttonLayout1.addWidget(nameLabel)
        buttonLayout1.addWidget(self.nameLine)
        buttonLayout1.addWidget(self.submitButton)

        self.submitButton.clicked.connect(self.submitContact)

        mainLayout = QGridLayout()
        # mainLayout.addWidget(nameLabel, 0, 0)
        mainLayout.addLayout(buttonLayout1, 0, 1)

        self.setLayout(mainLayout)
        self.setWindowTitle("Hello Qt")

    def submitContact(self):
        name = self.nameLine.text()
        newTask = myThread(1)
        newTask.start()
        print('Thread started')
        QMessageBox.information(self, "Success!",
            "Hello %s!" % name)

if __name__ == '__main__':
    import sys
    app = QApplication(sys.argv)

    screen = Form()
    screen.show()

    sys.exit(app.exec_())
