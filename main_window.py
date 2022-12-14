import os
import sys
from iterator import Iterator
from copy_random import copy_to_random
from copy_dataset import copy_to_another
from annotation import annotation
from PyQt5 import QtWidgets
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *


class Window(QMainWindow):
    def __init__(self):

        super().__init__()
        self.init_ui()
        self.path_csv = ""

    def init_ui(self):

        self.setGeometry(100, 100, 1100, 600)
        self.setWindowTitle('Animals')
        self.setWindowIcon(QIcon('D:/icon.jpg'))

        menubar = self.menuBar()

        first = menubar.addMenu("Create annotation dataset")
        action1 = QAction("Create", self)
        action1.triggered.connect(self.click_dataset)
        first.addAction(action1)

        second = menubar.addMenu("Create copy dataset")
        action2 = QAction("Create", self)
        action2.triggered.connect(self.click_copy_dataset)
        second.addAction(action2)

        third = menubar.addMenu("Create random dataset")
        action3 = QAction("Create", self)
        action3.triggered.connect(self.click_random)
        third.addAction(action3)

        fourth = menubar.addMenu("Show tiger")
        action4 = QAction("Show", self)
        action4.triggered.connect(self.click_show_tiger)
        fourth.addAction(action4)

        fifth = menubar.addMenu("Show leopard")
        action5 = QAction("Show", self)
        action5.triggered.connect(self.click_show_leopard)
        fifth.addAction(action5)

        self.show()

    def click_dataset(self) -> None:
        """
        Creates a dataset creation event
        """
        dataset_path = QtWidgets.QFileDialog.getExistingDirectory(self, "Select Folder")
        if os.path.exists(dataset_path + "/tiger") and os.path.exists(
                dataset_path + "/leopard"
        ):
            path_csv = QtWidgets.QFileDialog.getExistingDirectory(
                self, "Select folder to save csvfile"
            )
            self.path_csv = annotation(dataset_path, path_csv)
            msg = QMessageBox()
            msg.setWindowTitle("Message")
            msg.setText("Annotation creation is complete!")
            msg.exec_()
            print(self.path_csv)

    def click_copy_dataset(self) -> None:
        """
        Creates a copy dataset event
        """
        dataset_path = QtWidgets.QFileDialog.getExistingDirectory(self, "Select Folder")
        if os.path.exists(dataset_path + "/tiger") and os.path.exists(
                dataset_path + "/leopard"
        ):
            path_another_dataset = QtWidgets.QFileDialog.getExistingDirectory(
                self, "Select folder to save another directory"
            )
            self.path_csv = copy_to_another(path_another_dataset, dataset_path)
            msg = QMessageBox()
            msg.setWindowTitle("Message")
            msg.setText("Copy dataset creation is complete!")
            msg.exec_()
            print(self.path_csv)

    def click_random(self) -> None:
        """
        Creates a random dataset event
        """
        dataset_path = QtWidgets.QFileDialog.getExistingDirectory(self, "Select Folder")
        if os.path.exists(dataset_path + "/tiger") and os.path.exists(
                dataset_path + "/leopard"
        ):
            path_random_dataset = QtWidgets.QFileDialog.getExistingDirectory(
                self, "Select folder to save random directory"
            )
            self.path_csv = copy_to_random(dataset_path, path_random_dataset)
            msg = QMessageBox()
            msg.setWindowTitle("Message")
            msg.setText("Random dataset creation is complete!")
            msg.exec_()
            print(self.path_csv)

    def click_show_tiger(self) -> None:
        """
        Switching event between images
        """
        if self.path_csv == "":
            msg = QMessageBox()
            msg.setWindowTitle("Message")
            msg.setText("There is no created annotation file yet")
            msg.exec_()
        else:
            iterator = Iterator("tiger", self.path_csv)
            while True:
                dialog = QMessageBox()
                dialog.setGeometry(100, 600, 100, 100)
                dialog.addButton("Next", QMessageBox.AcceptRole)
                dialog.addButton("Stop", QMessageBox.RejectRole)
                dialog.setWindowTitle("Buttons")
                dialog.setText("Next picture")
                dialog.setWindowIcon(QIcon('D:/icon.jpg'))
                dialog.exec()

                if dialog.clickedButton().text() == "Next":
                    image = iterator.__next__()
                    pix = QPixmap(image)
                    item = QGraphicsPixmapItem(pix)
                    scene = QGraphicsScene(self)
                    scene.addItem(item)
                    view = QGraphicsView(scene)
                    self.setCentralWidget(view)

                if dialog.clickedButton().text() == "Stop":
                    break

    def click_show_leopard(self) -> None:
        """
        Switching event between images
        """
        if self.path_csv == "":
            msg = QMessageBox()
            msg.setWindowTitle("Message")
            msg.setText("There is no created annotation file yet")
            msg.exec_()
        else:
            iterator = Iterator("leopard", self.path_csv)
            while True:
                dialog = QMessageBox()
                dialog.setGeometry(100, 600, 100, 100)
                dialog.addButton("Next", QMessageBox.AcceptRole)
                dialog.addButton("Stop", QMessageBox.RejectRole)
                dialog.setWindowTitle("Buttons")
                dialog.setWindowIcon(QIcon('D:/icon.jpg'))
                dialog.setText("Next picture")
                dialog.exec()

                if dialog.clickedButton().text() == "Next":
                    image = iterator.__next__()
                    pix = QPixmap(image)
                    item = QGraphicsPixmapItem(pix)
                    scene = QGraphicsScene(self)
                    scene.addItem(item)
                    view = QGraphicsView(scene)
                    self.setCentralWidget(view)

                if dialog.clickedButton().text() == "Stop":
                    break


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Window()
    sys.exit(app.exec_())