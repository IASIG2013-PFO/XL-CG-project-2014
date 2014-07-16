# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_start_tab_menu.ui'
#
# Created: Tue Jul 15 16:55:32 2014
#      by: PyQt4 UI code generator 4.10.3
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_TabWidget(object):
    def setupUi(self, TabWidget):
        TabWidget.setObjectName(_fromUtf8("TabWidget"))
        TabWidget.resize(640, 494)
        self.tab_2 = QtGui.QWidget()
        self.tab_2.setObjectName(_fromUtf8("tab_2"))
        self.frame = QtGui.QFrame(self.tab_2)
        self.frame.setGeometry(QtCore.QRect(20, 10, 221, 431))
        self.frame.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtGui.QFrame.Raised)
        self.frame.setObjectName(_fromUtf8("frame"))
        self.splitter = QtGui.QSplitter(self.frame)
        self.splitter.setGeometry(QtCore.QRect(10, 10, 201, 161))
        self.splitter.setOrientation(QtCore.Qt.Vertical)
        self.splitter.setObjectName(_fromUtf8("splitter"))
        self.label = QtGui.QLabel(self.splitter)
        self.label.setObjectName(_fromUtf8("label"))
        self.editProjectName = QtGui.QLineEdit(self.splitter)
        self.editProjectName.setText(_fromUtf8(""))
        self.editProjectName.setObjectName(_fromUtf8("editProjectName"))
        self.label_2 = QtGui.QLabel(self.splitter)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.editDirName = QtGui.QLineEdit(self.splitter)
        self.editDirName.setObjectName(_fromUtf8("editDirName"))
        self.btnSelectPath = QtGui.QPushButton(self.splitter)
        self.btnSelectPath.setObjectName(_fromUtf8("btnSelectPath"))
        self.label_3 = QtGui.QLabel(self.frame)
        self.label_3.setGeometry(QtCore.QRect(10, 180, 201, 19))
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.comboBox = QtGui.QComboBox(self.frame)
        self.comboBox.setGeometry(QtCore.QRect(10, 200, 78, 25))
        self.comboBox.setObjectName(_fromUtf8("comboBox"))
        self.label_4 = QtGui.QLabel(self.frame)
        self.label_4.setGeometry(QtCore.QRect(10, 230, 201, 19))
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.btnExtraction = QtGui.QPushButton(self.frame)
        self.btnExtraction.setGeometry(QtCore.QRect(10, 250, 201, 35))
        self.btnExtraction.setObjectName(_fromUtf8("btnExtraction"))
        self.layoutWidget = QtGui.QWidget(self.frame)
        self.layoutWidget.setGeometry(QtCore.QRect(30, 340, 169, 29))
        self.layoutWidget.setObjectName(_fromUtf8("layoutWidget"))
        self.horizontalLayout = QtGui.QHBoxLayout(self.layoutWidget)
        self.horizontalLayout.setMargin(0)
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.checkBox = QtGui.QCheckBox(self.layoutWidget)
        self.checkBox.setObjectName(_fromUtf8("checkBox"))
        self.horizontalLayout.addWidget(self.checkBox)
        self.btnProjectValidation = QtGui.QPushButton(self.layoutWidget)
        self.btnProjectValidation.setObjectName(_fromUtf8("btnProjectValidation"))
        self.horizontalLayout.addWidget(self.btnProjectValidation)
        self.frame_3 = QtGui.QFrame(self.tab_2)
        self.frame_3.setGeometry(QtCore.QRect(270, 20, 351, 401))
        self.frame_3.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QtGui.QFrame.Raised)
        self.frame_3.setObjectName(_fromUtf8("frame_3"))
        self.gridLayoutWidget_2 = QtGui.QWidget(self.frame_3)
        self.gridLayoutWidget_2.setGeometry(QtCore.QRect(9, 29, 331, 251))
        self.gridLayoutWidget_2.setObjectName(_fromUtf8("gridLayoutWidget_2"))
        self.gridLayout_2 = QtGui.QGridLayout(self.gridLayoutWidget_2)
        self.gridLayout_2.setMargin(0)
        self.gridLayout_2.setObjectName(_fromUtf8("gridLayout_2"))
        TabWidget.addTab(self.tab_2, _fromUtf8(""))
        self.tab = QtGui.QWidget()
        self.tab.setObjectName(_fromUtf8("tab"))
        self.pushButton = QtGui.QPushButton(self.tab)
        self.pushButton.setGeometry(QtCore.QRect(200, 420, 87, 27))
        self.pushButton.setObjectName(_fromUtf8("pushButton"))
        self.frame_2 = QtGui.QFrame(self.tab)
        self.frame_2.setGeometry(QtCore.QRect(80, 20, 481, 401))
        self.frame_2.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtGui.QFrame.Raised)
        self.frame_2.setObjectName(_fromUtf8("frame_2"))
        self.gridLayoutWidget = QtGui.QWidget(self.frame_2)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(9, 29, 461, 361))
        self.gridLayoutWidget.setObjectName(_fromUtf8("gridLayoutWidget"))
        self.gridLayout = QtGui.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setMargin(0)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        TabWidget.addTab(self.tab, _fromUtf8(""))

        self.retranslateUi(TabWidget)
        TabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(TabWidget)

    def retranslateUi(self, TabWidget):
        TabWidget.setWindowTitle(_translate("TabWidget", "TabWidget", None))
        self.label.setText(_translate("TabWidget", "Selectionner Nom du Projet", None))
        self.label_2.setText(_translate("TabWidget", "Selectionner Répertoire Projet", None))
        self.editDirName.setText(_translate("TabWidget", "/home/pierre/Bureau", None))
        self.btnSelectPath.setText(_translate("TabWidget", "Selection Répertoire Projet", None))
        self.label_3.setText(_translate("TabWidget", "Selectionner Zone Cliente", None))
        self.label_4.setText(_translate("TabWidget", "Extraction", None))
        self.btnExtraction.setText(_translate("TabWidget", "Extraction", None))
        self.checkBox.setText(_translate("TabWidget", "check", None))
        self.btnProjectValidation.setText(_translate("TabWidget", "Valide Projet", None))
        TabWidget.setTabText(TabWidget.indexOf(self.tab_2), _translate("TabWidget", "NEW PROJECT", None))
        self.pushButton.setText(_translate("TabWidget", "PushButton", None))
        TabWidget.setTabText(TabWidget.indexOf(self.tab), _translate("TabWidget", "VIEW", None))

