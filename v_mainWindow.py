# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'v_mainWindow.ui'
##
## Created by: Qt User Interface Compiler version 6.8.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QComboBox, QDateEdit, QFrame,
    QGraphicsView, QGroupBox, QHBoxLayout, QHeaderView,
    QLabel, QLayout, QLineEdit, QMainWindow,
    QPlainTextEdit, QPushButton, QScrollArea, QSizePolicy,
    QSpacerItem, QSpinBox, QSplitter, QStatusBar,
    QTabWidget, QTableWidget, QTableWidgetItem, QTextBrowser,
    QTimeEdit, QToolBox, QVBoxLayout, QWidget)
import resources
import resources

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.setEnabled(True)
        MainWindow.resize(1213, 800)
        MainWindow.setMaximumSize(QSize(1280, 800))
        font = QFont()
        font.setFamilies([u"Noto Sans"])
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(False)
        MainWindow.setFont(font)
        icon = QIcon()
        icon.addFile(u":/icon/res/icon/icon.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setStyleSheet(u"font: 10pt \"Noto Sans\";\n"
"\n"
"\n"
"\n"
"")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setStyleSheet(u"#centralwidget{\n"
"background-color: white;\n"
"}")
        self.verticalLayout_2 = QVBoxLayout(self.centralwidget)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 5, 0, 5)
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setSpacing(10)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(-1, -1, -1, 0)
        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setSpacing(5)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(15, -1, 15, -1)
        self.label_logoLeft = QLabel(self.centralwidget)
        self.label_logoLeft.setObjectName(u"label_logoLeft")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(40)
        sizePolicy.setHeightForWidth(self.label_logoLeft.sizePolicy().hasHeightForWidth())
        self.label_logoLeft.setSizePolicy(sizePolicy)
        self.label_logoLeft.setMinimumSize(QSize(35, 35))
        self.label_logoLeft.setMaximumSize(QSize(35, 35))
        self.label_logoLeft.setPixmap(QPixmap(u":/icon/res/icon/clock.png"))
        self.label_logoLeft.setScaledContents(True)

        self.horizontalLayout_2.addWidget(self.label_logoLeft)

        self.label_dateTime = QLabel(self.centralwidget)
        self.label_dateTime.setObjectName(u"label_dateTime")
        self.label_dateTime.setFont(font)

        self.horizontalLayout_2.addWidget(self.label_dateTime)

        self.label_2 = QLabel(self.centralwidget)
        self.label_2.setObjectName(u"label_2")
        font1 = QFont()
        font1.setFamilies([u"Noto Sans"])
        font1.setPointSize(16)
        font1.setBold(False)
        font1.setItalic(False)
        self.label_2.setFont(font1)
        self.label_2.setStyleSheet(u"font: 16pt \"Noto Sans\";\n"
"color: #7f7f7f;\n"
"")
        self.label_2.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout_2.addWidget(self.label_2)

        self.label_30 = QLabel(self.centralwidget)
        self.label_30.setObjectName(u"label_30")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.label_30.sizePolicy().hasHeightForWidth())
        self.label_30.setSizePolicy(sizePolicy1)
        self.label_30.setMinimumSize(QSize(168, 0))
        self.label_30.setMaximumSize(QSize(168, 16777215))

        self.horizontalLayout_2.addWidget(self.label_30)

        self.label_logoRight = QLabel(self.centralwidget)
        self.label_logoRight.setObjectName(u"label_logoRight")
        self.label_logoRight.setMinimumSize(QSize(80, 40))
        self.label_logoRight.setMaximumSize(QSize(80, 40))
        self.label_logoRight.setPixmap(QPixmap(u":/logo/res/logo/semco.png"))
        self.label_logoRight.setScaledContents(True)
        self.label_logoRight.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.label_logoRight.setMargin(0)

        self.horizontalLayout_2.addWidget(self.label_logoRight)

        self.horizontalLayout_2.setStretch(2, 1)
        self.horizontalLayout_2.setStretch(4, 1)

        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.line = QFrame(self.centralwidget)
        self.line.setObjectName(u"line")
        self.line.setLineWidth(1)
        self.line.setMidLineWidth(0)
        self.line.setFrameShape(QFrame.Shape.HLine)
        self.line.setFrameShadow(QFrame.Shadow.Sunken)

        self.verticalLayout.addWidget(self.line)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setSizeConstraint(QLayout.SizeConstraint.SetDefaultConstraint)
        self.horizontalLayout.setContentsMargins(20, 0, 20, 10)
        self.splitter_mainWindow = QSplitter(self.centralwidget)
        self.splitter_mainWindow.setObjectName(u"splitter_mainWindow")
        self.splitter_mainWindow.setFont(font)
        self.splitter_mainWindow.setAutoFillBackground(False)
        self.splitter_mainWindow.setStyleSheet(u"#splitter_mainWindow::handle{\n"
"	background-color: white;\n"
"	image: url(:/icon/res/icon/dot_menu_more_vertical_icon.png)\n"
"}\n"
"#splitter_mainWindow::handle:pressed {\n"
"	\n"
"}")
        self.splitter_mainWindow.setFrameShape(QFrame.Shape.NoFrame)
        self.splitter_mainWindow.setLineWidth(1)
        self.splitter_mainWindow.setOrientation(Qt.Orientation.Horizontal)
        self.splitter_mainWindow.setOpaqueResize(True)
        self.splitter_mainWindow.setHandleWidth(15)
        self.splitter_mainWindow.setChildrenCollapsible(True)
        self.mainFrame_left = QFrame(self.splitter_mainWindow)
        self.mainFrame_left.setObjectName(u"mainFrame_left")
        self.mainFrame_left.setEnabled(True)
        self.mainFrame_left.setMinimumSize(QSize(0, 26))
        self.mainFrame_left.setFont(font)
        self.mainFrame_left.setStyleSheet(u"#mainFrame_left{\n"
"border-style: solid;\n"
"border-radius: 5px;\n"
"border-width: 1px;\n"
"border-color: LightGray;\n"
"}\n"
"#mainFrame_left:hover{\n"
"border-style: solid;\n"
"border-radius: 5px;\n"
"border-width: 2px;\n"
"border-color: gray;\n"
"}")
        self.mainFrame_left.setFrameShape(QFrame.Shape.Panel)
        self.mainFrame_left.setFrameShadow(QFrame.Shadow.Sunken)
        self.horizontalLayout_4 = QHBoxLayout(self.mainFrame_left)
        self.horizontalLayout_4.setSpacing(20)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(15, 5, 15, 15)
        self.frame_leftPort = QFrame(self.mainFrame_left)
        self.frame_leftPort.setObjectName(u"frame_leftPort")
        self.frame_leftPort.setEnabled(True)
        self.frame_leftPort.setStyleSheet(u"")
        self.verticalLayout_27 = QVBoxLayout(self.frame_leftPort)
        self.verticalLayout_27.setSpacing(20)
        self.verticalLayout_27.setObjectName(u"verticalLayout_27")
        self.verticalLayout_27.setContentsMargins(0, 5, 0, 0)
        self.lbl_equipmentId = QLabel(self.frame_leftPort)
        self.lbl_equipmentId.setObjectName(u"lbl_equipmentId")
        font2 = QFont()
        font2.setFamilies([u"Noto Sans"])
        font2.setPointSize(15)
        font2.setBold(False)
        font2.setItalic(False)
        self.lbl_equipmentId.setFont(font2)
        self.lbl_equipmentId.setStyleSheet(u"font: 15pt;")
        self.lbl_equipmentId.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_27.addWidget(self.lbl_equipmentId)

        self.verticalLayout_6 = QVBoxLayout()
        self.verticalLayout_6.setSpacing(10)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.verticalLayout_6.setContentsMargins(0, 0, -1, 0)
        self.verticalLayout_5 = QVBoxLayout()
        self.verticalLayout_5.setSpacing(5)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(-1, -1, -1, 0)
        self.horizontalLayout_13 = QHBoxLayout()
        self.horizontalLayout_13.setSpacing(20)
        self.horizontalLayout_13.setObjectName(u"horizontalLayout_13")
        self.horizontalLayout_13.setContentsMargins(-1, -1, 0, 0)
        self.label_15 = QLabel(self.frame_leftPort)
        self.label_15.setObjectName(u"label_15")

        self.horizontalLayout_13.addWidget(self.label_15)

        self.cb_customerName = QComboBox(self.frame_leftPort)
        self.cb_customerName.setObjectName(u"cb_customerName")
        self.cb_customerName.setMinimumSize(QSize(119, 26))
        self.cb_customerName.setStyleSheet(u"QComboBox {\n"
"    border: 1px solid gray;\n"
"    border-radius: 3px;\n"
"    padding: 1px 18px 1px 3px;\n"
"    min-width: 6em;\n"
"}\n"
"QComboBox::disabled {\n"
"    border: 1px solid gray;\n"
"    border-radius: 3px;\n"
"    padding: 1px 18px 1px 3px;\n"
"    min-width: 6em;\n"
"	background-color:white;\n"
"}\n"
"\n"
"\n"
"QComboBox::drop-down {\n"
"    subcontrol-origin: padding;\n"
"    subcontrol-position: top right;\n"
"    width: 25px;\n"
"\n"
"    border-left-width: 1px;\n"
"    border-left-color: darkgray;\n"
"    border-left-style: solid; /* just a single line */\n"
"    border-top-right-radius: 3px; /* same radius as the QComboBox */\n"
"    border-bottom-right-radius: 3px;\n"
"}\n"
"\n"
"QComboBox::down-arrow {\n"
"    image: url(:/icon/res/icon/down_b_arrow_icon.png)\n"
"}\n"
"\n"
"QComboBox::down-arrow:disabled {\n"
"    image: url(:/icon/res/icon/down_b_arrow_icon_gray.jpg)\n"
"}\n"
"\n"
"QComboBox::down-arrow:on { /* shift the arrow when popup is open */\n"
"    top: 1px;\n"
"    left: 1px;"
                        "\n"
"}")
        self.cb_customerName.setEditable(True)
        self.cb_customerName.setMinimumContentsLength(0)
        self.cb_customerName.setDuplicatesEnabled(False)
        self.cb_customerName.setFrame(True)

        self.horizontalLayout_13.addWidget(self.cb_customerName)


        self.verticalLayout_5.addLayout(self.horizontalLayout_13)

        self.horizontalLayout_10 = QHBoxLayout()
        self.horizontalLayout_10.setSpacing(20)
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.horizontalLayout_10.setContentsMargins(-1, -1, 0, 0)
        self.label_7 = QLabel(self.frame_leftPort)
        self.label_7.setObjectName(u"label_7")

        self.horizontalLayout_10.addWidget(self.label_7)

        self.cb_selectedModel = QComboBox(self.frame_leftPort)
        self.cb_selectedModel.setObjectName(u"cb_selectedModel")
        self.cb_selectedModel.setMinimumSize(QSize(119, 26))
        self.cb_selectedModel.setStyleSheet(u"QComboBox {\n"
"    border: 1px solid gray;\n"
"    border-radius: 3px;\n"
"    padding: 1px 18px 1px 3px;\n"
"    min-width: 6em;\n"
"}\n"
"QComboBox::disabled {\n"
"    border: 1px solid gray;\n"
"    border-radius: 3px;\n"
"    padding: 1px 18px 1px 3px;\n"
"    min-width: 6em;\n"
"	background-color:white;\n"
"}\n"
"\n"
"\n"
"QComboBox::drop-down {\n"
"    subcontrol-origin: padding;\n"
"    subcontrol-position: top right;\n"
"    width: 25px;\n"
"\n"
"    border-left-width: 1px;\n"
"    border-left-color: darkgray;\n"
"    border-left-style: solid; /* just a single line */\n"
"    border-top-right-radius: 3px; /* same radius as the QComboBox */\n"
"    border-bottom-right-radius: 3px;\n"
"}\n"
"\n"
"QComboBox::down-arrow {\n"
"    image: url(:/icon/res/icon/down_b_arrow_icon.png)\n"
"}\n"
"\n"
"QComboBox::down-arrow:disabled {\n"
"    image: url(:/icon/res/icon/down_b_arrow_icon_gray.jpg)\n"
"}\n"
"\n"
"QComboBox::down-arrow:on { /* shift the arrow when popup is open */\n"
"    top: 1px;\n"
"    left: 1px;"
                        "\n"
"}")
        self.cb_selectedModel.setEditable(True)
        self.cb_selectedModel.setMinimumContentsLength(0)
        self.cb_selectedModel.setDuplicatesEnabled(False)
        self.cb_selectedModel.setFrame(True)

        self.horizontalLayout_10.addWidget(self.cb_selectedModel)


        self.verticalLayout_5.addLayout(self.horizontalLayout_10)


        self.verticalLayout_6.addLayout(self.verticalLayout_5)


        self.verticalLayout_27.addLayout(self.verticalLayout_6)

        self.verticalLayout_31 = QVBoxLayout()
        self.verticalLayout_31.setSpacing(0)
        self.verticalLayout_31.setObjectName(u"verticalLayout_31")
        self.verticalLayout_31.setContentsMargins(10, 0, 10, 0)
        self.line_6 = QFrame(self.frame_leftPort)
        self.line_6.setObjectName(u"line_6")
        sizePolicy2 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Fixed)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.line_6.sizePolicy().hasHeightForWidth())
        self.line_6.setSizePolicy(sizePolicy2)
        self.line_6.setFrameShape(QFrame.Shape.HLine)
        self.line_6.setFrameShadow(QFrame.Shadow.Sunken)

        self.verticalLayout_31.addWidget(self.line_6)


        self.verticalLayout_27.addLayout(self.verticalLayout_31)

        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setSpacing(20)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(-1, -1, -1, 0)
        self.splitter_jobWindow = QSplitter(self.frame_leftPort)
        self.splitter_jobWindow.setObjectName(u"splitter_jobWindow")
        self.splitter_jobWindow.setStyleSheet(u"#splitter_jobWindow::handle{\n"
"	background-color: white;\n"
"	image: url(:/icon/res/icon/dot_menu_more_horizontal_icon.png)\n"
"}\n"
"#splitter_jobWindow::handle:pressed {\n"
"}")
        self.splitter_jobWindow.setOrientation(Qt.Orientation.Vertical)
        self.splitter_jobWindow.setHandleWidth(15)
        self.verticalLayoutWidget_5 = QWidget(self.splitter_jobWindow)
        self.verticalLayoutWidget_5.setObjectName(u"verticalLayoutWidget_5")
        self.verticalLayout_33 = QVBoxLayout(self.verticalLayoutWidget_5)
        self.verticalLayout_33.setObjectName(u"verticalLayout_33")
        self.verticalLayout_33.setContentsMargins(0, 0, 0, 0)
        self.frame = QFrame(self.verticalLayoutWidget_5)
        self.frame.setObjectName(u"frame")
        self.verticalLayout_58 = QVBoxLayout(self.frame)
        self.verticalLayout_58.setObjectName(u"verticalLayout_58")

        self.verticalLayout_33.addWidget(self.frame)

        self.splitter_jobWindow.addWidget(self.verticalLayoutWidget_5)
        self.verticalLayoutWidget_6 = QWidget(self.splitter_jobWindow)
        self.verticalLayoutWidget_6.setObjectName(u"verticalLayoutWidget_6")
        self.verticalLayout_59 = QVBoxLayout(self.verticalLayoutWidget_6)
        self.verticalLayout_59.setObjectName(u"verticalLayout_59")
        self.verticalLayout_59.setContentsMargins(0, 0, 0, 0)
        self.tabWidget = QTabWidget(self.verticalLayoutWidget_6)
        self.tabWidget.setObjectName(u"tabWidget")
        self.tabWidget.setContextMenuPolicy(Qt.ContextMenuPolicy.NoContextMenu)
        self.tabWidget.setDocumentMode(True)
        self.tab_5 = QWidget()
        self.tab_5.setObjectName(u"tab_5")
        self.tab_5.setContextMenuPolicy(Qt.ContextMenuPolicy.NoContextMenu)
        self.verticalLayout_70 = QVBoxLayout(self.tab_5)
        self.verticalLayout_70.setObjectName(u"verticalLayout_70")
        self.verticalLayout_70.setContentsMargins(-1, 20, -1, -1)
        self.horizontalLayout_50 = QHBoxLayout()
        self.horizontalLayout_50.setSpacing(20)
        self.horizontalLayout_50.setObjectName(u"horizontalLayout_50")
        self.horizontalLayout_50.setContentsMargins(-1, -1, 0, 0)
        self.label_21 = QLabel(self.tab_5)
        self.label_21.setObjectName(u"label_21")

        self.horizontalLayout_50.addWidget(self.label_21)

        self.spinBox_select_moduleNumber = QSpinBox(self.tab_5)
        self.spinBox_select_moduleNumber.setObjectName(u"spinBox_select_moduleNumber")
        self.spinBox_select_moduleNumber.setMinimum(1)
        self.spinBox_select_moduleNumber.setMaximum(32)

        self.horizontalLayout_50.addWidget(self.spinBox_select_moduleNumber)

        self.horizontalLayout_50.setStretch(0, 1)
        self.horizontalLayout_50.setStretch(1, 1)

        self.verticalLayout_70.addLayout(self.horizontalLayout_50)

        self.textBrowser_4 = QTextBrowser(self.tab_5)
        self.textBrowser_4.setObjectName(u"textBrowser_4")

        self.verticalLayout_70.addWidget(self.textBrowser_4)

        self.tabWidget.addTab(self.tab_5, "")
        self.tab_6 = QWidget()
        self.tab_6.setObjectName(u"tab_6")
        self.horizontalLayout_48 = QHBoxLayout(self.tab_6)
        self.horizontalLayout_48.setObjectName(u"horizontalLayout_48")
        self.horizontalLayout_48.setContentsMargins(-1, 20, -1, -1)
        self.textBrowser_5 = QTextBrowser(self.tab_6)
        self.textBrowser_5.setObjectName(u"textBrowser_5")

        self.horizontalLayout_48.addWidget(self.textBrowser_5)

        self.tabWidget.addTab(self.tab_6, "")

        self.verticalLayout_59.addWidget(self.tabWidget)

        self.splitter_jobWindow.addWidget(self.verticalLayoutWidget_6)

        self.verticalLayout_3.addWidget(self.splitter_jobWindow)


        self.verticalLayout_27.addLayout(self.verticalLayout_3)

        self.verticalLayout_27.setStretch(3, 20)

        self.horizontalLayout_4.addWidget(self.frame_leftPort)

        self.splitter_mainWindow.addWidget(self.mainFrame_left)
        self.mainFrame_right = QFrame(self.splitter_mainWindow)
        self.mainFrame_right.setObjectName(u"mainFrame_right")
        self.mainFrame_right.setEnabled(True)
        self.mainFrame_right.setStyleSheet(u"#mainFrame_right{\n"
"border-style: solid;\n"
"border-radius: 5px;\n"
"border-width: 1px;\n"
"border-color: LightGray;\n"
"}\n"
"#mainFrame_right:hover{\n"
"border-style: solid;\n"
"border-radius: 5px;\n"
"border-width: 2px;\n"
"border-color: gray;\n"
"}")
        self.mainFrame_right.setFrameShape(QFrame.Shape.StyledPanel)
        self.mainFrame_right.setFrameShadow(QFrame.Shadow.Plain)
        self.verticalLayout_7 = QVBoxLayout(self.mainFrame_right)
        self.verticalLayout_7.setSpacing(20)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.verticalLayout_7.setContentsMargins(15, 5, 15, 15)
        self.frame_right = QFrame(self.mainFrame_right)
        self.frame_right.setObjectName(u"frame_right")
        self.frame_right.setEnabled(True)
        self.frame_right.setStyleSheet(u"/*#portFrame1{\n"
"border-style: solid;\n"
"border-radius: 5px;\n"
"border-width: 1px;\n"
"border-color: LightGray;\n"
"}*/\n"
"#portFrame1:hover{\n"
"border-style: solid;\n"
"border-radius: 2px;\n"
"border-width: 1px;\n"
"border-color: lightgray;\n"
"}")
        self.verticalLayout_28 = QVBoxLayout(self.frame_right)
        self.verticalLayout_28.setSpacing(20)
        self.verticalLayout_28.setObjectName(u"verticalLayout_28")
        self.verticalLayout_28.setContentsMargins(0, 5, 0, 0)
        self.label_29 = QLabel(self.frame_right)
        self.label_29.setObjectName(u"label_29")
        self.label_29.setFont(font2)
        self.label_29.setStyleSheet(u"font: 15pt;\n"
"color: black;")
        self.label_29.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_28.addWidget(self.label_29)

        self.verticalLayout_16 = QVBoxLayout()
        self.verticalLayout_16.setSpacing(10)
        self.verticalLayout_16.setObjectName(u"verticalLayout_16")
        self.verticalLayout_16.setContentsMargins(0, -1, -1, 0)
        self.verticalLayout_8 = QVBoxLayout()
        self.verticalLayout_8.setSpacing(5)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.verticalLayout_8.setContentsMargins(-1, -1, -1, 0)
        self.horizontalLayout_9 = QHBoxLayout()
        self.horizontalLayout_9.setSpacing(20)
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.horizontalLayout_9.setContentsMargins(-1, -1, 0, 0)
        self.label = QLabel(self.frame_right)
        self.label.setObjectName(u"label")

        self.horizontalLayout_9.addWidget(self.label)

        self.cb_customerName_settings = QComboBox(self.frame_right)
        self.cb_customerName_settings.setObjectName(u"cb_customerName_settings")
        self.cb_customerName_settings.setEnabled(True)
        self.cb_customerName_settings.setMinimumSize(QSize(119, 26))
        self.cb_customerName_settings.setStyleSheet(u"QComboBox {\n"
"    border: 1px solid gray;\n"
"    border-radius: 3px;\n"
"    padding: 1px 18px 1px 3px;\n"
"    min-width: 6em;\n"
"}\n"
"QComboBox::disabled {\n"
"    border: 1px solid gray;\n"
"    border-radius: 3px;\n"
"    padding: 1px 18px 1px 3px;\n"
"    min-width: 6em;\n"
"	background-color:white;\n"
"}\n"
"\n"
"\n"
"QComboBox::drop-down {\n"
"    subcontrol-origin: padding;\n"
"    subcontrol-position: top right;\n"
"    width: 25px;\n"
"\n"
"    border-left-width: 1px;\n"
"    border-left-color: darkgray;\n"
"    border-left-style: solid; /* just a single line */\n"
"    border-top-right-radius: 3px; /* same radius as the QComboBox */\n"
"    border-bottom-right-radius: 3px;\n"
"}\n"
"\n"
"QComboBox::down-arrow {\n"
"    image: url(:/icon/res/icon/down_b_arrow_icon.png)\n"
"}\n"
"\n"
"QComboBox::down-arrow:disabled {\n"
"    image: url(:/icon/res/icon/down_b_arrow_icon_gray.jpg)\n"
"}\n"
"\n"
"QComboBox::down-arrow:on { /* shift the arrow when popup is open */\n"
"    top: 1px;\n"
"    left: 1px;"
                        "\n"
"}")
        self.cb_customerName_settings.setEditable(True)
        self.cb_customerName_settings.setMinimumContentsLength(0)
        self.cb_customerName_settings.setDuplicatesEnabled(False)
        self.cb_customerName_settings.setFrame(True)

        self.horizontalLayout_9.addWidget(self.cb_customerName_settings)

        self.horizontalLayout_9.setStretch(0, 1)
        self.horizontalLayout_9.setStretch(1, 1)

        self.verticalLayout_8.addLayout(self.horizontalLayout_9)

        self.horizontalLayout_23 = QHBoxLayout()
        self.horizontalLayout_23.setSpacing(20)
        self.horizontalLayout_23.setObjectName(u"horizontalLayout_23")
        self.horizontalLayout_23.setContentsMargins(-1, -1, 0, 0)
        self.label_20 = QLabel(self.frame_right)
        self.label_20.setObjectName(u"label_20")

        self.horizontalLayout_23.addWidget(self.label_20)

        self.cb_selectedModel_settings = QComboBox(self.frame_right)
        self.cb_selectedModel_settings.setObjectName(u"cb_selectedModel_settings")
        self.cb_selectedModel_settings.setEnabled(True)
        self.cb_selectedModel_settings.setMinimumSize(QSize(119, 26))
        self.cb_selectedModel_settings.setStyleSheet(u"QComboBox {\n"
"    border: 1px solid gray;\n"
"    border-radius: 3px;\n"
"    padding: 1px 18px 1px 3px;\n"
"    min-width: 6em;\n"
"}\n"
"QComboBox::disabled {\n"
"    border: 1px solid gray;\n"
"    border-radius: 3px;\n"
"    padding: 1px 18px 1px 3px;\n"
"    min-width: 6em;\n"
"	background-color:white;\n"
"}\n"
"\n"
"\n"
"QComboBox::drop-down {\n"
"    subcontrol-origin: padding;\n"
"    subcontrol-position: top right;\n"
"    width: 25px;\n"
"\n"
"    border-left-width: 1px;\n"
"    border-left-color: darkgray;\n"
"    border-left-style: solid; /* just a single line */\n"
"    border-top-right-radius: 3px; /* same radius as the QComboBox */\n"
"    border-bottom-right-radius: 3px;\n"
"}\n"
"\n"
"QComboBox::down-arrow {\n"
"    image: url(:/icon/res/icon/down_b_arrow_icon.png)\n"
"}\n"
"\n"
"QComboBox::down-arrow:disabled {\n"
"    image: url(:/icon/res/icon/down_b_arrow_icon_gray.jpg)\n"
"}\n"
"\n"
"QComboBox::down-arrow:on { /* shift the arrow when popup is open */\n"
"    top: 1px;\n"
"    left: 1px;"
                        "\n"
"}")
        self.cb_selectedModel_settings.setEditable(True)
        self.cb_selectedModel_settings.setMinimumContentsLength(0)
        self.cb_selectedModel_settings.setDuplicatesEnabled(False)
        self.cb_selectedModel_settings.setFrame(True)

        self.horizontalLayout_23.addWidget(self.cb_selectedModel_settings)

        self.horizontalLayout_23.setStretch(0, 1)
        self.horizontalLayout_23.setStretch(1, 1)

        self.verticalLayout_8.addLayout(self.horizontalLayout_23)


        self.verticalLayout_16.addLayout(self.verticalLayout_8)


        self.verticalLayout_28.addLayout(self.verticalLayout_16)

        self.verticalLayout_25 = QVBoxLayout()
        self.verticalLayout_25.setSpacing(0)
        self.verticalLayout_25.setObjectName(u"verticalLayout_25")
        self.verticalLayout_25.setContentsMargins(10, 0, 10, 0)
        self.line_7 = QFrame(self.frame_right)
        self.line_7.setObjectName(u"line_7")
        self.line_7.setFrameShape(QFrame.Shape.HLine)
        self.line_7.setFrameShadow(QFrame.Shadow.Sunken)

        self.verticalLayout_25.addWidget(self.line_7)


        self.verticalLayout_28.addLayout(self.verticalLayout_25)

        self.verticalLayout_22 = QVBoxLayout()
        self.verticalLayout_22.setObjectName(u"verticalLayout_22")
        self.verticalLayout_22.setContentsMargins(-1, -1, -1, 0)
        self.tw_settings = QTabWidget(self.frame_right)
        self.tw_settings.setObjectName(u"tw_settings")
        self.tw_settings.setEnabled(True)
        self.tw_settings.setFont(font)
        self.tw_settings.setContextMenuPolicy(Qt.ContextMenuPolicy.NoContextMenu)
        self.tw_settings.setStyleSheet(u"")
        self.tw_settings.setTabPosition(QTabWidget.TabPosition.North)
        self.tw_settings.setTabShape(QTabWidget.TabShape.Rounded)
        self.tw_settings.setIconSize(QSize(16, 16))
        self.tw_settings.setElideMode(Qt.TextElideMode.ElideRight)
        self.tw_settings.setUsesScrollButtons(True)
        self.tw_settings.setDocumentMode(True)
        self.tw_settings.setTabsClosable(False)
        self.tw_settings.setMovable(True)
        self.tw_settings.setTabBarAutoHide(True)
        self.tab_setOpenShortSpec = QWidget()
        self.tab_setOpenShortSpec.setObjectName(u"tab_setOpenShortSpec")
        self.tab_setOpenShortSpec.setEnabled(True)
        self.verticalLayout_21 = QVBoxLayout(self.tab_setOpenShortSpec)
        self.verticalLayout_21.setObjectName(u"verticalLayout_21")
        self.verticalLayout_21.setContentsMargins(12, 20, 12, 0)
        self.verticalLayout_23 = QVBoxLayout()
        self.verticalLayout_23.setSpacing(15)
        self.verticalLayout_23.setObjectName(u"verticalLayout_23")
        self.verticalLayout_23.setContentsMargins(-1, -1, -1, 0)
        self.groupBox_9 = QGroupBox(self.tab_setOpenShortSpec)
        self.groupBox_9.setObjectName(u"groupBox_9")
        self.verticalLayout_62 = QVBoxLayout(self.groupBox_9)
        self.verticalLayout_62.setObjectName(u"verticalLayout_62")
        self.verticalLayout_62.setContentsMargins(12, 9, 12, 12)
        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_6.setSpacing(20)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalLayout_6.setSizeConstraint(QLayout.SizeConstraint.SetNoConstraint)
        self.horizontalLayout_6.setContentsMargins(-1, -1, 0, 0)
        self.label_3 = QLabel(self.groupBox_9)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setEnabled(True)

        self.horizontalLayout_6.addWidget(self.label_3)

        self.cb_ScriptFilePath = QComboBox(self.groupBox_9)
        self.cb_ScriptFilePath.setObjectName(u"cb_ScriptFilePath")
        self.cb_ScriptFilePath.setEnabled(True)
        self.cb_ScriptFilePath.setMinimumSize(QSize(119, 26))
        self.cb_ScriptFilePath.setMaximumSize(QSize(16777215, 26))
        self.cb_ScriptFilePath.setStyleSheet(u"QComboBox {\n"
"    border: 1px solid gray;\n"
"    border-radius: 3px;\n"
"    padding: 1px 18px 1px 3px;\n"
"    min-width: 6em;\n"
"}\n"
"QComboBox::disabled {\n"
"    border: 1px solid gray;\n"
"    border-radius: 3px;\n"
"    padding: 1px 18px 1px 3px;\n"
"    min-width: 6em;\n"
"	background-color:white;\n"
"}\n"
"\n"
"\n"
"QComboBox::drop-down {\n"
"    subcontrol-origin: padding;\n"
"    subcontrol-position: top right;\n"
"    width: 25px;\n"
"\n"
"    border-left-width: 1px;\n"
"    border-left-color: darkgray;\n"
"    border-left-style: solid; /* just a single line */\n"
"    border-top-right-radius: 3px; /* same radius as the QComboBox */\n"
"    border-bottom-right-radius: 3px;\n"
"}\n"
"\n"
"QComboBox::down-arrow {\n"
"    image: url(:/icon/res/icon/down_b_arrow_icon.png)\n"
"}\n"
"\n"
"QComboBox::down-arrow:disabled {\n"
"    image: url(:/icon/res/icon/down_b_arrow_icon_gray.jpg)\n"
"}\n"
"\n"
"QComboBox::down-arrow:on { /* shift the arrow when popup is open */\n"
"    top: 1px;\n"
"    left: 1px;"
                        "\n"
"}")
        self.cb_ScriptFilePath.setEditable(True)
        self.cb_ScriptFilePath.setMinimumContentsLength(0)
        self.cb_ScriptFilePath.setDuplicatesEnabled(False)
        self.cb_ScriptFilePath.setFrame(True)

        self.horizontalLayout_6.addWidget(self.cb_ScriptFilePath)

        self.horizontalLayout_8 = QHBoxLayout()
        self.horizontalLayout_8.setSpacing(20)
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.pb_loadscript = QPushButton(self.groupBox_9)
        self.pb_loadscript.setObjectName(u"pb_loadscript")
        self.pb_loadscript.setEnabled(True)
        sizePolicy2.setHeightForWidth(self.pb_loadscript.sizePolicy().hasHeightForWidth())
        self.pb_loadscript.setSizePolicy(sizePolicy2)
        self.pb_loadscript.setMinimumSize(QSize(0, 25))
        self.pb_loadscript.setMaximumSize(QSize(16777215, 25))
        self.pb_loadscript.setStyleSheet(u"QPushButton{\n"
"	color: rgb(58, 134, 255);\n"
"	background-color: white;\n"
"	border: 1px solid rgb(58, 134, 255);\n"
"	border-radius: 5px;\n"
"}\n"
"/*(QPushButton:hover{\n"
"	color: white;\n"
"	background-color: rgb(58, 134, 255);\n"
"	border-radius: 5px;\n"
"}*/\n"
"QPushButton:pressed {\n"
"	padding-top: 3px;\n"
"    padding-left: 3px;\n"
" }\n"
"QPushButton:disabled {\n"
"	color: #7f7f7f;\n"
"	border: 1px solid rgb(127, 127, 127);\n"
" }")
        icon1 = QIcon()
        icon1.addFile(u":/icon/res/icon/refresh_arrow_icon.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.pb_loadscript.setIcon(icon1)

        self.horizontalLayout_8.addWidget(self.pb_loadscript)

        self.horizontalLayout_8.setStretch(0, 1)

        self.horizontalLayout_6.addLayout(self.horizontalLayout_8)

        self.horizontalLayout_6.setStretch(0, 1)
        self.horizontalLayout_6.setStretch(1, 1)
        self.horizontalLayout_6.setStretch(2, 1)

        self.verticalLayout_62.addLayout(self.horizontalLayout_6)

        self.plainTextEdit = QPlainTextEdit(self.groupBox_9)
        self.plainTextEdit.setObjectName(u"plainTextEdit")
        self.plainTextEdit.setFrameShape(QFrame.Shape.NoFrame)
        self.plainTextEdit.setFrameShadow(QFrame.Shadow.Sunken)

        self.verticalLayout_62.addWidget(self.plainTextEdit)


        self.verticalLayout_23.addWidget(self.groupBox_9)

        self.groupBox_7 = QGroupBox(self.tab_setOpenShortSpec)
        self.groupBox_7.setObjectName(u"groupBox_7")
        self.verticalLayout_56 = QVBoxLayout(self.groupBox_7)
        self.verticalLayout_56.setSpacing(5)
        self.verticalLayout_56.setObjectName(u"verticalLayout_56")
        self.verticalLayout_56.setContentsMargins(12, 9, 12, 9)
        self.horizontalLayout_21 = QHBoxLayout()
        self.horizontalLayout_21.setSpacing(20)
        self.horizontalLayout_21.setObjectName(u"horizontalLayout_21")
        self.horizontalLayout_21.setContentsMargins(-1, -1, 0, 0)
        self.label_8 = QLabel(self.groupBox_7)
        self.label_8.setObjectName(u"label_8")

        self.horizontalLayout_21.addWidget(self.label_8)

        self.spinBox_carrierCount = QSpinBox(self.groupBox_7)
        self.spinBox_carrierCount.setObjectName(u"spinBox_carrierCount")
        self.spinBox_carrierCount.setMinimum(1)
        self.spinBox_carrierCount.setMaximum(2)

        self.horizontalLayout_21.addWidget(self.spinBox_carrierCount)

        self.spinBox = QSpinBox(self.groupBox_7)
        self.spinBox.setObjectName(u"spinBox")
        self.spinBox.setEnabled(False)
        self.spinBox.setMinimum(1)
        self.spinBox.setMaximum(2)

        self.horizontalLayout_21.addWidget(self.spinBox)

        self.horizontalLayout_21.setStretch(0, 1)
        self.horizontalLayout_21.setStretch(1, 1)
        self.horizontalLayout_21.setStretch(2, 1)

        self.verticalLayout_56.addLayout(self.horizontalLayout_21)

        self.horizontalLayout_27 = QHBoxLayout()
        self.horizontalLayout_27.setSpacing(20)
        self.horizontalLayout_27.setObjectName(u"horizontalLayout_27")
        self.horizontalLayout_27.setContentsMargins(-1, -1, 0, 0)
        self.label_11 = QLabel(self.groupBox_7)
        self.label_11.setObjectName(u"label_11")

        self.horizontalLayout_27.addWidget(self.label_11)

        self.spinBox_module_Rows = QSpinBox(self.groupBox_7)
        self.spinBox_module_Rows.setObjectName(u"spinBox_module_Rows")
        self.spinBox_module_Rows.setMinimum(1)
        self.spinBox_module_Rows.setMaximum(4)

        self.horizontalLayout_27.addWidget(self.spinBox_module_Rows)

        self.spinBox_module_columns = QSpinBox(self.groupBox_7)
        self.spinBox_module_columns.setObjectName(u"spinBox_module_columns")
        self.spinBox_module_columns.setMinimum(1)
        self.spinBox_module_columns.setMaximum(10)

        self.horizontalLayout_27.addWidget(self.spinBox_module_columns)

        self.horizontalLayout_27.setStretch(0, 1)
        self.horizontalLayout_27.setStretch(1, 1)
        self.horizontalLayout_27.setStretch(2, 1)

        self.verticalLayout_56.addLayout(self.horizontalLayout_27)


        self.verticalLayout_23.addWidget(self.groupBox_7)

        self.horizontalLayout_19 = QHBoxLayout()
        self.horizontalLayout_19.setSpacing(20)
        self.horizontalLayout_19.setObjectName(u"horizontalLayout_19")
        self.label_4 = QLabel(self.tab_setOpenShortSpec)
        self.label_4.setObjectName(u"label_4")

        self.horizontalLayout_19.addWidget(self.label_4)

        self.label_6 = QLabel(self.tab_setOpenShortSpec)
        self.label_6.setObjectName(u"label_6")

        self.horizontalLayout_19.addWidget(self.label_6)

        self.pb_SaveScript = QPushButton(self.tab_setOpenShortSpec)
        self.pb_SaveScript.setObjectName(u"pb_SaveScript")
        self.pb_SaveScript.setEnabled(True)
        sizePolicy2.setHeightForWidth(self.pb_SaveScript.sizePolicy().hasHeightForWidth())
        self.pb_SaveScript.setSizePolicy(sizePolicy2)
        self.pb_SaveScript.setMinimumSize(QSize(0, 28))
        self.pb_SaveScript.setMaximumSize(QSize(16777215, 28))
        self.pb_SaveScript.setStyleSheet(u"QPushButton{\n"
"	color: rgb(58, 134, 255);\n"
"	background-color: white;\n"
"	border: 1px solid rgb(58, 134, 255);\n"
"	border-radius: 5px;\n"
"}\n"
"/*(QPushButton:hover{\n"
"	color: white;\n"
"	background-color: rgb(58, 134, 255);\n"
"	border-radius: 5px;\n"
"}*/\n"
"QPushButton:pressed {\n"
"	padding-top: 3px;\n"
"    padding-left: 3px;\n"
" }\n"
"QPushButton:disabled {\n"
"	color: #7f7f7f;\n"
"	border: 1px solid rgb(127, 127, 127);\n"
" }")
        icon2 = QIcon()
        icon2.addFile(u":/icon/res/icon/save_log.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.pb_SaveScript.setIcon(icon2)

        self.horizontalLayout_19.addWidget(self.pb_SaveScript)

        self.horizontalLayout_19.setStretch(0, 1)
        self.horizontalLayout_19.setStretch(1, 1)
        self.horizontalLayout_19.setStretch(2, 1)

        self.verticalLayout_23.addLayout(self.horizontalLayout_19)


        self.verticalLayout_21.addLayout(self.verticalLayout_23)

        self.tw_settings.addTab(self.tab_setOpenShortSpec, "")
        self.tab_3 = QWidget()
        self.tab_3.setObjectName(u"tab_3")
        self.horizontalLayout_5 = QHBoxLayout(self.tab_3)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setContentsMargins(12, 20, 12, 0)
        self.verticalLayout_42 = QVBoxLayout()
        self.verticalLayout_42.setSpacing(15)
        self.verticalLayout_42.setObjectName(u"verticalLayout_42")
        self.verticalLayout_42.setContentsMargins(-1, 0, -1, -1)
        self.verticalLayout_19 = QVBoxLayout()
        self.verticalLayout_19.setSpacing(5)
        self.verticalLayout_19.setObjectName(u"verticalLayout_19")
        self.verticalLayout_19.setContentsMargins(-1, 0, -1, -1)
        self.horizontalLayout_30 = QHBoxLayout()
        self.horizontalLayout_30.setSpacing(20)
        self.horizontalLayout_30.setObjectName(u"horizontalLayout_30")
        self.horizontalLayout_30.setSizeConstraint(QLayout.SizeConstraint.SetNoConstraint)
        self.horizontalLayout_30.setContentsMargins(-1, -1, 0, 0)
        self.label_16 = QLabel(self.tab_3)
        self.label_16.setObjectName(u"label_16")
        self.label_16.setEnabled(True)

        self.horizontalLayout_30.addWidget(self.label_16)

        self.cb_firmware = QComboBox(self.tab_3)
        self.cb_firmware.setObjectName(u"cb_firmware")
        self.cb_firmware.setEnabled(True)
        self.cb_firmware.setMinimumSize(QSize(119, 26))
        self.cb_firmware.setStyleSheet(u"QComboBox {\n"
"    border: 1px solid gray;\n"
"    border-radius: 3px;\n"
"    padding: 1px 18px 1px 3px;\n"
"    min-width: 6em;\n"
"}\n"
"QComboBox::disabled {\n"
"    border: 1px solid gray;\n"
"    border-radius: 3px;\n"
"    padding: 1px 18px 1px 3px;\n"
"    min-width: 6em;\n"
"	background-color:white;\n"
"}\n"
"\n"
"\n"
"QComboBox::drop-down {\n"
"    subcontrol-origin: padding;\n"
"    subcontrol-position: top right;\n"
"    width: 25px;\n"
"\n"
"    border-left-width: 1px;\n"
"    border-left-color: darkgray;\n"
"    border-left-style: solid; /* just a single line */\n"
"    border-top-right-radius: 3px; /* same radius as the QComboBox */\n"
"    border-bottom-right-radius: 3px;\n"
"}\n"
"\n"
"QComboBox::down-arrow {\n"
"    image: url(:/icon/res/icon/down_b_arrow_icon.png)\n"
"}\n"
"\n"
"QComboBox::down-arrow:disabled {\n"
"    image: url(:/icon/res/icon/down_b_arrow_icon_gray.jpg)\n"
"}\n"
"\n"
"QComboBox::down-arrow:on { /* shift the arrow when popup is open */\n"
"    top: 1px;\n"
"    left: 1px;"
                        "\n"
"}")
        self.cb_firmware.setEditable(True)
        self.cb_firmware.setMinimumContentsLength(0)
        self.cb_firmware.setDuplicatesEnabled(False)
        self.cb_firmware.setFrame(True)

        self.horizontalLayout_30.addWidget(self.cb_firmware)

        self.horizontalLayout_31 = QHBoxLayout()
        self.horizontalLayout_31.setSpacing(20)
        self.horizontalLayout_31.setObjectName(u"horizontalLayout_31")
        self.pb_upload_Firmware = QPushButton(self.tab_3)
        self.pb_upload_Firmware.setObjectName(u"pb_upload_Firmware")
        self.pb_upload_Firmware.setEnabled(True)
        sizePolicy2.setHeightForWidth(self.pb_upload_Firmware.sizePolicy().hasHeightForWidth())
        self.pb_upload_Firmware.setSizePolicy(sizePolicy2)
        self.pb_upload_Firmware.setMinimumSize(QSize(0, 28))
        self.pb_upload_Firmware.setMaximumSize(QSize(16777215, 28))
        self.pb_upload_Firmware.setStyleSheet(u"QPushButton{\n"
"	color: rgb(58, 134, 255);\n"
"	background-color: white;\n"
"	border: 1px solid rgb(58, 134, 255);\n"
"	border-radius: 5px;\n"
"}\n"
"/*(QPushButton:hover{\n"
"	color: white;\n"
"	background-color: rgb(58, 134, 255);\n"
"	border-radius: 5px;\n"
"}*/\n"
"QPushButton:pressed {\n"
"	padding-top: 3px;\n"
"    padding-left: 3px;\n"
" }\n"
"QPushButton:disabled {\n"
"	color: #7f7f7f;\n"
"	border: 1px solid rgb(127, 127, 127);\n"
" }")
        self.pb_upload_Firmware.setIcon(icon2)

        self.horizontalLayout_31.addWidget(self.pb_upload_Firmware)

        self.horizontalLayout_31.setStretch(0, 1)

        self.horizontalLayout_30.addLayout(self.horizontalLayout_31)

        self.horizontalLayout_30.setStretch(0, 1)
        self.horizontalLayout_30.setStretch(1, 1)
        self.horizontalLayout_30.setStretch(2, 1)

        self.verticalLayout_19.addLayout(self.horizontalLayout_30)

        self.horizontalLayout_28 = QHBoxLayout()
        self.horizontalLayout_28.setSpacing(20)
        self.horizontalLayout_28.setObjectName(u"horizontalLayout_28")
        self.horizontalLayout_28.setSizeConstraint(QLayout.SizeConstraint.SetNoConstraint)
        self.horizontalLayout_28.setContentsMargins(-1, -1, 0, 0)
        self.label_13 = QLabel(self.tab_3)
        self.label_13.setObjectName(u"label_13")
        self.label_13.setEnabled(True)

        self.horizontalLayout_28.addWidget(self.label_13)

        self.cb_scriptSelect = QComboBox(self.tab_3)
        self.cb_scriptSelect.setObjectName(u"cb_scriptSelect")
        self.cb_scriptSelect.setEnabled(True)
        self.cb_scriptSelect.setMinimumSize(QSize(119, 26))
        self.cb_scriptSelect.setStyleSheet(u"QComboBox {\n"
"    border: 1px solid gray;\n"
"    border-radius: 3px;\n"
"    padding: 1px 18px 1px 3px;\n"
"    min-width: 6em;\n"
"}\n"
"QComboBox::disabled {\n"
"    border: 1px solid gray;\n"
"    border-radius: 3px;\n"
"    padding: 1px 18px 1px 3px;\n"
"    min-width: 6em;\n"
"	background-color:white;\n"
"}\n"
"\n"
"\n"
"QComboBox::drop-down {\n"
"    subcontrol-origin: padding;\n"
"    subcontrol-position: top right;\n"
"    width: 25px;\n"
"\n"
"    border-left-width: 1px;\n"
"    border-left-color: darkgray;\n"
"    border-left-style: solid; /* just a single line */\n"
"    border-top-right-radius: 3px; /* same radius as the QComboBox */\n"
"    border-bottom-right-radius: 3px;\n"
"}\n"
"\n"
"QComboBox::down-arrow {\n"
"    image: url(:/icon/res/icon/down_b_arrow_icon.png)\n"
"}\n"
"\n"
"QComboBox::down-arrow:disabled {\n"
"    image: url(:/icon/res/icon/down_b_arrow_icon_gray.jpg)\n"
"}\n"
"\n"
"QComboBox::down-arrow:on { /* shift the arrow when popup is open */\n"
"    top: 1px;\n"
"    left: 1px;"
                        "\n"
"}")
        self.cb_scriptSelect.setEditable(True)
        self.cb_scriptSelect.setMinimumContentsLength(0)
        self.cb_scriptSelect.setDuplicatesEnabled(False)
        self.cb_scriptSelect.setFrame(True)

        self.horizontalLayout_28.addWidget(self.cb_scriptSelect)

        self.horizontalLayout_29 = QHBoxLayout()
        self.horizontalLayout_29.setSpacing(20)
        self.horizontalLayout_29.setObjectName(u"horizontalLayout_29")
        self.pb_upload_Script = QPushButton(self.tab_3)
        self.pb_upload_Script.setObjectName(u"pb_upload_Script")
        self.pb_upload_Script.setEnabled(True)
        sizePolicy2.setHeightForWidth(self.pb_upload_Script.sizePolicy().hasHeightForWidth())
        self.pb_upload_Script.setSizePolicy(sizePolicy2)
        self.pb_upload_Script.setMinimumSize(QSize(0, 28))
        self.pb_upload_Script.setMaximumSize(QSize(16777215, 28))
        self.pb_upload_Script.setStyleSheet(u"QPushButton{\n"
"	color: rgb(58, 134, 255);\n"
"	background-color: white;\n"
"	border: 1px solid rgb(58, 134, 255);\n"
"	border-radius: 5px;\n"
"}\n"
"/*(QPushButton:hover{\n"
"	color: white;\n"
"	background-color: rgb(58, 134, 255);\n"
"	border-radius: 5px;\n"
"}*/\n"
"QPushButton:pressed {\n"
"	padding-top: 3px;\n"
"    padding-left: 3px;\n"
" }\n"
"QPushButton:disabled {\n"
"	color: #7f7f7f;\n"
"	border: 1px solid rgb(127, 127, 127);\n"
" }")
        self.pb_upload_Script.setIcon(icon2)

        self.horizontalLayout_29.addWidget(self.pb_upload_Script)

        self.horizontalLayout_29.setStretch(0, 1)

        self.horizontalLayout_28.addLayout(self.horizontalLayout_29)

        self.horizontalLayout_28.setStretch(0, 1)
        self.horizontalLayout_28.setStretch(1, 1)
        self.horizontalLayout_28.setStretch(2, 1)

        self.verticalLayout_19.addLayout(self.horizontalLayout_28)


        self.verticalLayout_42.addLayout(self.verticalLayout_19)

        self.tableWidget = QTableWidget(self.tab_3)
        if (self.tableWidget.columnCount() < 7):
            self.tableWidget.setColumnCount(7)
        __qtablewidgetitem = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(4, __qtablewidgetitem4)
        __qtablewidgetitem5 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(5, __qtablewidgetitem5)
        __qtablewidgetitem6 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(6, __qtablewidgetitem6)
        if (self.tableWidget.rowCount() < 32):
            self.tableWidget.setRowCount(32)
        __qtablewidgetitem7 = QTableWidgetItem()
        self.tableWidget.setItem(0, 1, __qtablewidgetitem7)
        __qtablewidgetitem8 = QTableWidgetItem()
        self.tableWidget.setItem(0, 2, __qtablewidgetitem8)
        __qtablewidgetitem9 = QTableWidgetItem()
        self.tableWidget.setItem(0, 3, __qtablewidgetitem9)
        __qtablewidgetitem10 = QTableWidgetItem()
        self.tableWidget.setItem(1, 1, __qtablewidgetitem10)
        __qtablewidgetitem11 = QTableWidgetItem()
        self.tableWidget.setItem(1, 2, __qtablewidgetitem11)
        __qtablewidgetitem12 = QTableWidgetItem()
        self.tableWidget.setItem(1, 3, __qtablewidgetitem12)
        __qtablewidgetitem13 = QTableWidgetItem()
        self.tableWidget.setItem(2, 1, __qtablewidgetitem13)
        __qtablewidgetitem14 = QTableWidgetItem()
        self.tableWidget.setItem(2, 2, __qtablewidgetitem14)
        __qtablewidgetitem15 = QTableWidgetItem()
        self.tableWidget.setItem(2, 3, __qtablewidgetitem15)
        __qtablewidgetitem16 = QTableWidgetItem()
        self.tableWidget.setItem(3, 1, __qtablewidgetitem16)
        __qtablewidgetitem17 = QTableWidgetItem()
        self.tableWidget.setItem(3, 2, __qtablewidgetitem17)
        __qtablewidgetitem18 = QTableWidgetItem()
        self.tableWidget.setItem(3, 3, __qtablewidgetitem18)
        __qtablewidgetitem19 = QTableWidgetItem()
        self.tableWidget.setItem(4, 1, __qtablewidgetitem19)
        __qtablewidgetitem20 = QTableWidgetItem()
        self.tableWidget.setItem(4, 2, __qtablewidgetitem20)
        __qtablewidgetitem21 = QTableWidgetItem()
        self.tableWidget.setItem(4, 3, __qtablewidgetitem21)
        __qtablewidgetitem22 = QTableWidgetItem()
        self.tableWidget.setItem(5, 1, __qtablewidgetitem22)
        __qtablewidgetitem23 = QTableWidgetItem()
        self.tableWidget.setItem(5, 2, __qtablewidgetitem23)
        __qtablewidgetitem24 = QTableWidgetItem()
        self.tableWidget.setItem(5, 3, __qtablewidgetitem24)
        __qtablewidgetitem25 = QTableWidgetItem()
        self.tableWidget.setItem(6, 1, __qtablewidgetitem25)
        __qtablewidgetitem26 = QTableWidgetItem()
        self.tableWidget.setItem(6, 2, __qtablewidgetitem26)
        __qtablewidgetitem27 = QTableWidgetItem()
        self.tableWidget.setItem(6, 3, __qtablewidgetitem27)
        __qtablewidgetitem28 = QTableWidgetItem()
        self.tableWidget.setItem(7, 1, __qtablewidgetitem28)
        __qtablewidgetitem29 = QTableWidgetItem()
        self.tableWidget.setItem(7, 2, __qtablewidgetitem29)
        __qtablewidgetitem30 = QTableWidgetItem()
        self.tableWidget.setItem(7, 3, __qtablewidgetitem30)
        __qtablewidgetitem31 = QTableWidgetItem()
        self.tableWidget.setItem(8, 1, __qtablewidgetitem31)
        __qtablewidgetitem32 = QTableWidgetItem()
        self.tableWidget.setItem(8, 2, __qtablewidgetitem32)
        __qtablewidgetitem33 = QTableWidgetItem()
        self.tableWidget.setItem(8, 3, __qtablewidgetitem33)
        __qtablewidgetitem34 = QTableWidgetItem()
        self.tableWidget.setItem(9, 1, __qtablewidgetitem34)
        __qtablewidgetitem35 = QTableWidgetItem()
        self.tableWidget.setItem(9, 2, __qtablewidgetitem35)
        __qtablewidgetitem36 = QTableWidgetItem()
        self.tableWidget.setItem(9, 3, __qtablewidgetitem36)
        __qtablewidgetitem37 = QTableWidgetItem()
        self.tableWidget.setItem(10, 1, __qtablewidgetitem37)
        __qtablewidgetitem38 = QTableWidgetItem()
        self.tableWidget.setItem(10, 2, __qtablewidgetitem38)
        __qtablewidgetitem39 = QTableWidgetItem()
        self.tableWidget.setItem(10, 3, __qtablewidgetitem39)
        __qtablewidgetitem40 = QTableWidgetItem()
        self.tableWidget.setItem(11, 1, __qtablewidgetitem40)
        __qtablewidgetitem41 = QTableWidgetItem()
        self.tableWidget.setItem(11, 2, __qtablewidgetitem41)
        __qtablewidgetitem42 = QTableWidgetItem()
        self.tableWidget.setItem(11, 3, __qtablewidgetitem42)
        __qtablewidgetitem43 = QTableWidgetItem()
        self.tableWidget.setItem(12, 1, __qtablewidgetitem43)
        __qtablewidgetitem44 = QTableWidgetItem()
        self.tableWidget.setItem(12, 2, __qtablewidgetitem44)
        __qtablewidgetitem45 = QTableWidgetItem()
        self.tableWidget.setItem(12, 3, __qtablewidgetitem45)
        __qtablewidgetitem46 = QTableWidgetItem()
        self.tableWidget.setItem(13, 1, __qtablewidgetitem46)
        __qtablewidgetitem47 = QTableWidgetItem()
        self.tableWidget.setItem(13, 2, __qtablewidgetitem47)
        __qtablewidgetitem48 = QTableWidgetItem()
        self.tableWidget.setItem(13, 3, __qtablewidgetitem48)
        __qtablewidgetitem49 = QTableWidgetItem()
        self.tableWidget.setItem(14, 1, __qtablewidgetitem49)
        __qtablewidgetitem50 = QTableWidgetItem()
        self.tableWidget.setItem(14, 2, __qtablewidgetitem50)
        __qtablewidgetitem51 = QTableWidgetItem()
        self.tableWidget.setItem(14, 3, __qtablewidgetitem51)
        __qtablewidgetitem52 = QTableWidgetItem()
        self.tableWidget.setItem(15, 1, __qtablewidgetitem52)
        __qtablewidgetitem53 = QTableWidgetItem()
        self.tableWidget.setItem(15, 2, __qtablewidgetitem53)
        __qtablewidgetitem54 = QTableWidgetItem()
        self.tableWidget.setItem(15, 3, __qtablewidgetitem54)
        __qtablewidgetitem55 = QTableWidgetItem()
        self.tableWidget.setItem(16, 1, __qtablewidgetitem55)
        __qtablewidgetitem56 = QTableWidgetItem()
        self.tableWidget.setItem(16, 2, __qtablewidgetitem56)
        __qtablewidgetitem57 = QTableWidgetItem()
        self.tableWidget.setItem(16, 3, __qtablewidgetitem57)
        __qtablewidgetitem58 = QTableWidgetItem()
        self.tableWidget.setItem(17, 1, __qtablewidgetitem58)
        __qtablewidgetitem59 = QTableWidgetItem()
        self.tableWidget.setItem(17, 2, __qtablewidgetitem59)
        __qtablewidgetitem60 = QTableWidgetItem()
        self.tableWidget.setItem(17, 3, __qtablewidgetitem60)
        __qtablewidgetitem61 = QTableWidgetItem()
        self.tableWidget.setItem(18, 1, __qtablewidgetitem61)
        __qtablewidgetitem62 = QTableWidgetItem()
        self.tableWidget.setItem(18, 2, __qtablewidgetitem62)
        __qtablewidgetitem63 = QTableWidgetItem()
        self.tableWidget.setItem(18, 3, __qtablewidgetitem63)
        __qtablewidgetitem64 = QTableWidgetItem()
        self.tableWidget.setItem(19, 1, __qtablewidgetitem64)
        __qtablewidgetitem65 = QTableWidgetItem()
        self.tableWidget.setItem(19, 2, __qtablewidgetitem65)
        __qtablewidgetitem66 = QTableWidgetItem()
        self.tableWidget.setItem(19, 3, __qtablewidgetitem66)
        __qtablewidgetitem67 = QTableWidgetItem()
        self.tableWidget.setItem(20, 1, __qtablewidgetitem67)
        __qtablewidgetitem68 = QTableWidgetItem()
        self.tableWidget.setItem(20, 2, __qtablewidgetitem68)
        __qtablewidgetitem69 = QTableWidgetItem()
        self.tableWidget.setItem(20, 3, __qtablewidgetitem69)
        __qtablewidgetitem70 = QTableWidgetItem()
        self.tableWidget.setItem(21, 1, __qtablewidgetitem70)
        __qtablewidgetitem71 = QTableWidgetItem()
        self.tableWidget.setItem(21, 2, __qtablewidgetitem71)
        __qtablewidgetitem72 = QTableWidgetItem()
        self.tableWidget.setItem(21, 3, __qtablewidgetitem72)
        __qtablewidgetitem73 = QTableWidgetItem()
        self.tableWidget.setItem(22, 1, __qtablewidgetitem73)
        __qtablewidgetitem74 = QTableWidgetItem()
        self.tableWidget.setItem(22, 2, __qtablewidgetitem74)
        __qtablewidgetitem75 = QTableWidgetItem()
        self.tableWidget.setItem(22, 3, __qtablewidgetitem75)
        __qtablewidgetitem76 = QTableWidgetItem()
        self.tableWidget.setItem(23, 1, __qtablewidgetitem76)
        __qtablewidgetitem77 = QTableWidgetItem()
        self.tableWidget.setItem(23, 2, __qtablewidgetitem77)
        __qtablewidgetitem78 = QTableWidgetItem()
        self.tableWidget.setItem(23, 3, __qtablewidgetitem78)
        __qtablewidgetitem79 = QTableWidgetItem()
        self.tableWidget.setItem(24, 1, __qtablewidgetitem79)
        __qtablewidgetitem80 = QTableWidgetItem()
        self.tableWidget.setItem(24, 2, __qtablewidgetitem80)
        __qtablewidgetitem81 = QTableWidgetItem()
        self.tableWidget.setItem(24, 3, __qtablewidgetitem81)
        __qtablewidgetitem82 = QTableWidgetItem()
        self.tableWidget.setItem(25, 1, __qtablewidgetitem82)
        __qtablewidgetitem83 = QTableWidgetItem()
        self.tableWidget.setItem(25, 2, __qtablewidgetitem83)
        __qtablewidgetitem84 = QTableWidgetItem()
        self.tableWidget.setItem(25, 3, __qtablewidgetitem84)
        __qtablewidgetitem85 = QTableWidgetItem()
        self.tableWidget.setItem(26, 1, __qtablewidgetitem85)
        __qtablewidgetitem86 = QTableWidgetItem()
        self.tableWidget.setItem(26, 2, __qtablewidgetitem86)
        __qtablewidgetitem87 = QTableWidgetItem()
        self.tableWidget.setItem(26, 3, __qtablewidgetitem87)
        __qtablewidgetitem88 = QTableWidgetItem()
        self.tableWidget.setItem(27, 1, __qtablewidgetitem88)
        __qtablewidgetitem89 = QTableWidgetItem()
        self.tableWidget.setItem(27, 2, __qtablewidgetitem89)
        __qtablewidgetitem90 = QTableWidgetItem()
        self.tableWidget.setItem(27, 3, __qtablewidgetitem90)
        __qtablewidgetitem91 = QTableWidgetItem()
        self.tableWidget.setItem(28, 1, __qtablewidgetitem91)
        __qtablewidgetitem92 = QTableWidgetItem()
        self.tableWidget.setItem(28, 2, __qtablewidgetitem92)
        __qtablewidgetitem93 = QTableWidgetItem()
        self.tableWidget.setItem(28, 3, __qtablewidgetitem93)
        __qtablewidgetitem94 = QTableWidgetItem()
        self.tableWidget.setItem(29, 1, __qtablewidgetitem94)
        __qtablewidgetitem95 = QTableWidgetItem()
        self.tableWidget.setItem(29, 2, __qtablewidgetitem95)
        __qtablewidgetitem96 = QTableWidgetItem()
        self.tableWidget.setItem(29, 3, __qtablewidgetitem96)
        __qtablewidgetitem97 = QTableWidgetItem()
        self.tableWidget.setItem(30, 1, __qtablewidgetitem97)
        __qtablewidgetitem98 = QTableWidgetItem()
        self.tableWidget.setItem(30, 2, __qtablewidgetitem98)
        __qtablewidgetitem99 = QTableWidgetItem()
        self.tableWidget.setItem(30, 3, __qtablewidgetitem99)
        __qtablewidgetitem100 = QTableWidgetItem()
        self.tableWidget.setItem(31, 1, __qtablewidgetitem100)
        __qtablewidgetitem101 = QTableWidgetItem()
        self.tableWidget.setItem(31, 2, __qtablewidgetitem101)
        __qtablewidgetitem102 = QTableWidgetItem()
        self.tableWidget.setItem(31, 3, __qtablewidgetitem102)
        self.tableWidget.setObjectName(u"tableWidget")
        self.tableWidget.setAlternatingRowColors(True)
        self.tableWidget.setRowCount(32)
        self.tableWidget.horizontalHeader().setDefaultSectionSize(85)
        self.tableWidget.horizontalHeader().setStretchLastSection(True)
        self.tableWidget.verticalHeader().setVisible(True)
        self.tableWidget.verticalHeader().setHighlightSections(False)
        self.tableWidget.verticalHeader().setStretchLastSection(False)

        self.verticalLayout_42.addWidget(self.tableWidget)


        self.horizontalLayout_5.addLayout(self.verticalLayout_42)

        self.tw_settings.addTab(self.tab_3, "")
        self.tab_4 = QWidget()
        self.tab_4.setObjectName(u"tab_4")
        self.horizontalLayout_7 = QHBoxLayout(self.tab_4)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.horizontalLayout_7.setContentsMargins(12, 20, 12, 0)
        self.verticalLayout_41 = QVBoxLayout()
        self.verticalLayout_41.setSpacing(15)
        self.verticalLayout_41.setObjectName(u"verticalLayout_41")
        self.verticalLayout_41.setContentsMargins(-1, 0, -1, 0)
        self.scrollArea_4 = QScrollArea(self.tab_4)
        self.scrollArea_4.setObjectName(u"scrollArea_4")
        self.scrollArea_4.setStyleSheet(u"background-color: white;\n"
"")
        self.scrollArea_4.setFrameShape(QFrame.Shape.NoFrame)
        self.scrollArea_4.setWidgetResizable(True)
        self.scrollAreaWidgetContents_4 = QWidget()
        self.scrollAreaWidgetContents_4.setObjectName(u"scrollAreaWidgetContents_4")
        self.scrollAreaWidgetContents_4.setGeometry(QRect(0, 0, 690, 457))
        self.verticalLayout_43 = QVBoxLayout(self.scrollAreaWidgetContents_4)
        self.verticalLayout_43.setSpacing(15)
        self.verticalLayout_43.setObjectName(u"verticalLayout_43")
        self.verticalLayout_43.setContentsMargins(0, 0, 0, 0)
        self.tabWidget_2 = QTabWidget(self.scrollAreaWidgetContents_4)
        self.tabWidget_2.setObjectName(u"tabWidget_2")
        self.tabWidget_2.setContextMenuPolicy(Qt.ContextMenuPolicy.NoContextMenu)
        self.tabWidget_2.setDocumentMode(True)
        self.tab_7 = QWidget()
        self.tab_7.setObjectName(u"tab_7")
        self.verticalLayout_63 = QVBoxLayout(self.tab_7)
        self.verticalLayout_63.setSpacing(15)
        self.verticalLayout_63.setObjectName(u"verticalLayout_63")
        self.verticalLayout_63.setContentsMargins(9, 20, -1, -1)
        self.horizontalLayout_17 = QHBoxLayout()
        self.horizontalLayout_17.setObjectName(u"horizontalLayout_17")
        self.horizontalLayout_17.setContentsMargins(-1, -1, 0, 0)
        self.groupBox_8 = QGroupBox(self.tab_7)
        self.groupBox_8.setObjectName(u"groupBox_8")
        self.verticalLayout_49 = QVBoxLayout(self.groupBox_8)
        self.verticalLayout_49.setSpacing(15)
        self.verticalLayout_49.setObjectName(u"verticalLayout_49")
        self.verticalLayout_49.setContentsMargins(12, 9, 12, 9)
        self.verticalLayout_45 = QVBoxLayout()
        self.verticalLayout_45.setSpacing(5)
        self.verticalLayout_45.setObjectName(u"verticalLayout_45")
        self.verticalLayout_45.setContentsMargins(-1, -1, -1, 0)
        self.horizontalLayout_41 = QHBoxLayout()
        self.horizontalLayout_41.setSpacing(20)
        self.horizontalLayout_41.setObjectName(u"horizontalLayout_41")
        self.label_25 = QLabel(self.groupBox_8)
        self.label_25.setObjectName(u"label_25")

        self.horizontalLayout_41.addWidget(self.label_25)

        self.le_mes_ipAddress_2 = QLineEdit(self.groupBox_8)
        self.le_mes_ipAddress_2.setObjectName(u"le_mes_ipAddress_2")

        self.horizontalLayout_41.addWidget(self.le_mes_ipAddress_2)

        self.horizontalLayout_41.setStretch(0, 1)
        self.horizontalLayout_41.setStretch(1, 1)

        self.verticalLayout_45.addLayout(self.horizontalLayout_41)

        self.horizontalLayout_73 = QHBoxLayout()
        self.horizontalLayout_73.setSpacing(20)
        self.horizontalLayout_73.setObjectName(u"horizontalLayout_73")
        self.label_76 = QLabel(self.groupBox_8)
        self.label_76.setObjectName(u"label_76")

        self.horizontalLayout_73.addWidget(self.label_76)

        self.le_mes_portNumber_2 = QLineEdit(self.groupBox_8)
        self.le_mes_portNumber_2.setObjectName(u"le_mes_portNumber_2")

        self.horizontalLayout_73.addWidget(self.le_mes_portNumber_2)

        self.horizontalLayout_73.setStretch(0, 1)
        self.horizontalLayout_73.setStretch(1, 1)

        self.verticalLayout_45.addLayout(self.horizontalLayout_73)

        self.horizontalLayout_76 = QHBoxLayout()
        self.horizontalLayout_76.setSpacing(20)
        self.horizontalLayout_76.setObjectName(u"horizontalLayout_76")
        self.label_79 = QLabel(self.groupBox_8)
        self.label_79.setObjectName(u"label_79")

        self.horizontalLayout_76.addWidget(self.label_79)

        self.le_mes_portNumber_5 = QLineEdit(self.groupBox_8)
        self.le_mes_portNumber_5.setObjectName(u"le_mes_portNumber_5")

        self.horizontalLayout_76.addWidget(self.le_mes_portNumber_5)

        self.horizontalLayout_76.setStretch(0, 1)
        self.horizontalLayout_76.setStretch(1, 1)

        self.verticalLayout_45.addLayout(self.horizontalLayout_76)


        self.verticalLayout_49.addLayout(self.verticalLayout_45)


        self.horizontalLayout_17.addWidget(self.groupBox_8)

        self.groupBox_6 = QGroupBox(self.tab_7)
        self.groupBox_6.setObjectName(u"groupBox_6")
        self.verticalLayout_44 = QVBoxLayout(self.groupBox_6)
        self.verticalLayout_44.setSpacing(15)
        self.verticalLayout_44.setObjectName(u"verticalLayout_44")
        self.verticalLayout_44.setContentsMargins(12, 9, 12, 9)
        self.verticalLayout_46 = QVBoxLayout()
        self.verticalLayout_46.setSpacing(5)
        self.verticalLayout_46.setObjectName(u"verticalLayout_46")
        self.verticalLayout_46.setContentsMargins(-1, -1, -1, 0)
        self.horizontalLayout_43 = QHBoxLayout()
        self.horizontalLayout_43.setSpacing(10)
        self.horizontalLayout_43.setObjectName(u"horizontalLayout_43")
        self.label_28 = QLabel(self.groupBox_6)
        self.label_28.setObjectName(u"label_28")

        self.horizontalLayout_43.addWidget(self.label_28)

        self.le_mes_ipAddress_4 = QLineEdit(self.groupBox_6)
        self.le_mes_ipAddress_4.setObjectName(u"le_mes_ipAddress_4")

        self.horizontalLayout_43.addWidget(self.le_mes_ipAddress_4)

        self.horizontalLayout_43.setStretch(0, 1)
        self.horizontalLayout_43.setStretch(1, 1)

        self.verticalLayout_46.addLayout(self.horizontalLayout_43)

        self.horizontalLayout_74 = QHBoxLayout()
        self.horizontalLayout_74.setSpacing(10)
        self.horizontalLayout_74.setObjectName(u"horizontalLayout_74")
        self.label_77 = QLabel(self.groupBox_6)
        self.label_77.setObjectName(u"label_77")

        self.horizontalLayout_74.addWidget(self.label_77)

        self.le_mes_portNumber_3 = QLineEdit(self.groupBox_6)
        self.le_mes_portNumber_3.setObjectName(u"le_mes_portNumber_3")

        self.horizontalLayout_74.addWidget(self.le_mes_portNumber_3)

        self.horizontalLayout_74.setStretch(0, 1)
        self.horizontalLayout_74.setStretch(1, 1)

        self.verticalLayout_46.addLayout(self.horizontalLayout_74)

        self.horizontalLayout_77 = QHBoxLayout()
        self.horizontalLayout_77.setSpacing(10)
        self.horizontalLayout_77.setObjectName(u"horizontalLayout_77")
        self.label_80 = QLabel(self.groupBox_6)
        self.label_80.setObjectName(u"label_80")

        self.horizontalLayout_77.addWidget(self.label_80)

        self.le_mes_portNumber_6 = QLineEdit(self.groupBox_6)
        self.le_mes_portNumber_6.setObjectName(u"le_mes_portNumber_6")

        self.horizontalLayout_77.addWidget(self.le_mes_portNumber_6)

        self.horizontalLayout_77.setStretch(0, 1)
        self.horizontalLayout_77.setStretch(1, 1)

        self.verticalLayout_46.addLayout(self.horizontalLayout_77)


        self.verticalLayout_44.addLayout(self.verticalLayout_46)


        self.horizontalLayout_17.addWidget(self.groupBox_6)


        self.verticalLayout_63.addLayout(self.horizontalLayout_17)

        self.horizontalLayout_33 = QHBoxLayout()
        self.horizontalLayout_33.setSpacing(20)
        self.horizontalLayout_33.setObjectName(u"horizontalLayout_33")
        self.horizontalLayout_33.setContentsMargins(-1, 0, -1, -1)
        self.label_32 = QLabel(self.tab_7)
        self.label_32.setObjectName(u"label_32")

        self.horizontalLayout_33.addWidget(self.label_32)

        self.label_35 = QLabel(self.tab_7)
        self.label_35.setObjectName(u"label_35")

        self.horizontalLayout_33.addWidget(self.label_35)

        self.pb_mes_messageLog_clear_4 = QPushButton(self.tab_7)
        self.pb_mes_messageLog_clear_4.setObjectName(u"pb_mes_messageLog_clear_4")
        self.pb_mes_messageLog_clear_4.setMinimumSize(QSize(0, 26))
        self.pb_mes_messageLog_clear_4.setMaximumSize(QSize(16777215, 26))
        self.pb_mes_messageLog_clear_4.setStyleSheet(u"QPushButton{\n"
"	color: rgb(58, 134, 255);\n"
"	background-color: white;\n"
"	border: 1px solid rgb(58, 134, 255);\n"
"	border-radius: 5px;\n"
"}\n"
"/*(QPushButton:hover{\n"
"	color: white;\n"
"	background-color: rgb(58, 134, 255);\n"
"	border-radius: 5px;\n"
"}*/\n"
"QPushButton:pressed {\n"
"	padding-top: 3px;\n"
"    padding-left: 3px;\n"
" }\n"
"QPushButton:disabled {\n"
"	color: #7f7f7f;\n"
"	border: 1px solid rgb(127, 127, 127);\n"
" }")
        self.pb_mes_messageLog_clear_4.setIcon(icon2)

        self.horizontalLayout_33.addWidget(self.pb_mes_messageLog_clear_4)

        self.horizontalLayout_33.setStretch(0, 1)
        self.horizontalLayout_33.setStretch(1, 1)
        self.horizontalLayout_33.setStretch(2, 1)

        self.verticalLayout_63.addLayout(self.horizontalLayout_33)

        self.verticalSpacer_4 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_63.addItem(self.verticalSpacer_4)

        self.tabWidget_2.addTab(self.tab_7, "")
        self.tab_8 = QWidget()
        self.tab_8.setObjectName(u"tab_8")
        self.verticalLayout_57 = QVBoxLayout(self.tab_8)
        self.verticalLayout_57.setSpacing(15)
        self.verticalLayout_57.setObjectName(u"verticalLayout_57")
        self.verticalLayout_57.setContentsMargins(-1, 20, -1, 9)
        self.splitter_barcodeLeft = QSplitter(self.tab_8)
        self.splitter_barcodeLeft.setObjectName(u"splitter_barcodeLeft")
        self.splitter_barcodeLeft.setStyleSheet(u"#splitter_barcodeLeft::handle{\n"
"	background-color: white;\n"
"	image: url(:/icon/res/icon/dot_menu_more_horizontal_icon.png)\n"
"}\n"
"#splitter_barcodeLeft::handle:pressed {\n"
"}")
        self.splitter_barcodeLeft.setOrientation(Qt.Orientation.Vertical)
        self.splitter_barcodeLeft.setHandleWidth(15)
        self.verticalLayoutWidget_2 = QWidget(self.splitter_barcodeLeft)
        self.verticalLayoutWidget_2.setObjectName(u"verticalLayoutWidget_2")
        self.horizontalLayout_12 = QHBoxLayout(self.verticalLayoutWidget_2)
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
        self.horizontalLayout_12.setContentsMargins(0, 0, 0, 0)
        self.graphicsView = QGraphicsView(self.verticalLayoutWidget_2)
        self.graphicsView.setObjectName(u"graphicsView")

        self.horizontalLayout_12.addWidget(self.graphicsView)

        self.splitter_barcodeLeft.addWidget(self.verticalLayoutWidget_2)
        self.verticalLayoutWidget_3 = QWidget(self.splitter_barcodeLeft)
        self.verticalLayoutWidget_3.setObjectName(u"verticalLayoutWidget_3")
        self.verticalLayout_48 = QVBoxLayout(self.verticalLayoutWidget_3)
        self.verticalLayout_48.setObjectName(u"verticalLayout_48")
        self.verticalLayout_48.setContentsMargins(0, 0, 0, 0)
        self.textBrowser = QTextBrowser(self.verticalLayoutWidget_3)
        self.textBrowser.setObjectName(u"textBrowser")

        self.verticalLayout_48.addWidget(self.textBrowser)

        self.splitter_barcodeLeft.addWidget(self.verticalLayoutWidget_3)

        self.verticalLayout_57.addWidget(self.splitter_barcodeLeft)

        self.horizontalLayout_36 = QHBoxLayout()
        self.horizontalLayout_36.setSpacing(20)
        self.horizontalLayout_36.setObjectName(u"horizontalLayout_36")
        self.label_27 = QLabel(self.tab_8)
        self.label_27.setObjectName(u"label_27")

        self.horizontalLayout_36.addWidget(self.label_27)

        self.label_37 = QLabel(self.tab_8)
        self.label_37.setObjectName(u"label_37")

        self.horizontalLayout_36.addWidget(self.label_37)

        self.pb_mes_messageLog_clear_6 = QPushButton(self.tab_8)
        self.pb_mes_messageLog_clear_6.setObjectName(u"pb_mes_messageLog_clear_6")
        self.pb_mes_messageLog_clear_6.setMinimumSize(QSize(0, 26))
        self.pb_mes_messageLog_clear_6.setMaximumSize(QSize(16777215, 26))
        self.pb_mes_messageLog_clear_6.setStyleSheet(u"QPushButton{\n"
"	color: rgb(58, 134, 255);\n"
"	background-color: white;\n"
"	border: 1px solid rgb(58, 134, 255);\n"
"	border-radius: 5px;\n"
"}\n"
"/*(QPushButton:hover{\n"
"	color: white;\n"
"	background-color: rgb(58, 134, 255);\n"
"	border-radius: 5px;\n"
"}*/\n"
"QPushButton:pressed {\n"
"	padding-top: 3px;\n"
"    padding-left: 3px;\n"
" }\n"
"QPushButton:disabled {\n"
"	color: #7f7f7f;\n"
"	border: 1px solid rgb(127, 127, 127);\n"
" }")
        self.pb_mes_messageLog_clear_6.setIcon(icon2)

        self.horizontalLayout_36.addWidget(self.pb_mes_messageLog_clear_6)

        self.horizontalLayout_36.setStretch(0, 1)
        self.horizontalLayout_36.setStretch(1, 1)
        self.horizontalLayout_36.setStretch(2, 1)

        self.verticalLayout_57.addLayout(self.horizontalLayout_36)

        self.tabWidget_2.addTab(self.tab_8, "")
        self.tab_9 = QWidget()
        self.tab_9.setObjectName(u"tab_9")
        self.verticalLayout_69 = QVBoxLayout(self.tab_9)
        self.verticalLayout_69.setSpacing(15)
        self.verticalLayout_69.setObjectName(u"verticalLayout_69")
        self.verticalLayout_69.setContentsMargins(-1, 20, -1, 9)
        self.splitter_barcodeRight = QSplitter(self.tab_9)
        self.splitter_barcodeRight.setObjectName(u"splitter_barcodeRight")
        self.splitter_barcodeRight.setStyleSheet(u"#splitter_barcodeRight::handle{\n"
"	background-color: white;\n"
"	image: url(:/icon/res/icon/dot_menu_more_horizontal_icon.png)\n"
"}\n"
"#splitter_barcodeRight::handle:pressed {\n"
"}")
        self.splitter_barcodeRight.setOrientation(Qt.Orientation.Vertical)
        self.splitter_barcodeRight.setHandleWidth(15)
        self.verticalLayoutWidget_8 = QWidget(self.splitter_barcodeRight)
        self.verticalLayoutWidget_8.setObjectName(u"verticalLayoutWidget_8")
        self.horizontalLayout_47 = QHBoxLayout(self.verticalLayoutWidget_8)
        self.horizontalLayout_47.setObjectName(u"horizontalLayout_47")
        self.horizontalLayout_47.setContentsMargins(0, 0, 0, 0)
        self.graphicsView_3 = QGraphicsView(self.verticalLayoutWidget_8)
        self.graphicsView_3.setObjectName(u"graphicsView_3")

        self.horizontalLayout_47.addWidget(self.graphicsView_3)

        self.splitter_barcodeRight.addWidget(self.verticalLayoutWidget_8)
        self.verticalLayoutWidget_9 = QWidget(self.splitter_barcodeRight)
        self.verticalLayoutWidget_9.setObjectName(u"verticalLayoutWidget_9")
        self.verticalLayout_68 = QVBoxLayout(self.verticalLayoutWidget_9)
        self.verticalLayout_68.setObjectName(u"verticalLayout_68")
        self.verticalLayout_68.setContentsMargins(0, 0, 0, 0)
        self.textBrowser_3 = QTextBrowser(self.verticalLayoutWidget_9)
        self.textBrowser_3.setObjectName(u"textBrowser_3")

        self.verticalLayout_68.addWidget(self.textBrowser_3)

        self.splitter_barcodeRight.addWidget(self.verticalLayoutWidget_9)

        self.verticalLayout_69.addWidget(self.splitter_barcodeRight)

        self.horizontalLayout_32 = QHBoxLayout()
        self.horizontalLayout_32.setSpacing(20)
        self.horizontalLayout_32.setObjectName(u"horizontalLayout_32")
        self.label_26 = QLabel(self.tab_9)
        self.label_26.setObjectName(u"label_26")

        self.horizontalLayout_32.addWidget(self.label_26)

        self.label_36 = QLabel(self.tab_9)
        self.label_36.setObjectName(u"label_36")

        self.horizontalLayout_32.addWidget(self.label_36)

        self.pb_mes_messageLog_clear_3 = QPushButton(self.tab_9)
        self.pb_mes_messageLog_clear_3.setObjectName(u"pb_mes_messageLog_clear_3")
        self.pb_mes_messageLog_clear_3.setMinimumSize(QSize(0, 26))
        self.pb_mes_messageLog_clear_3.setMaximumSize(QSize(16777215, 26))
        self.pb_mes_messageLog_clear_3.setStyleSheet(u"QPushButton{\n"
"	color: rgb(58, 134, 255);\n"
"	background-color: white;\n"
"	border: 1px solid rgb(58, 134, 255);\n"
"	border-radius: 5px;\n"
"}\n"
"/*(QPushButton:hover{\n"
"	color: white;\n"
"	background-color: rgb(58, 134, 255);\n"
"	border-radius: 5px;\n"
"}*/\n"
"QPushButton:pressed {\n"
"	padding-top: 3px;\n"
"    padding-left: 3px;\n"
" }\n"
"QPushButton:disabled {\n"
"	color: #7f7f7f;\n"
"	border: 1px solid rgb(127, 127, 127);\n"
" }")
        self.pb_mes_messageLog_clear_3.setIcon(icon2)

        self.horizontalLayout_32.addWidget(self.pb_mes_messageLog_clear_3)

        self.horizontalLayout_32.setStretch(0, 1)
        self.horizontalLayout_32.setStretch(1, 1)
        self.horizontalLayout_32.setStretch(2, 1)

        self.verticalLayout_69.addLayout(self.horizontalLayout_32)

        self.tabWidget_2.addTab(self.tab_9, "")

        self.verticalLayout_43.addWidget(self.tabWidget_2)

        self.scrollArea_4.setWidget(self.scrollAreaWidgetContents_4)

        self.verticalLayout_41.addWidget(self.scrollArea_4)


        self.horizontalLayout_7.addLayout(self.verticalLayout_41)

        self.tw_settings.addTab(self.tab_4, "")
        self.tab_configMes = QWidget()
        self.tab_configMes.setObjectName(u"tab_configMes")
        self.verticalLayout_10 = QVBoxLayout(self.tab_configMes)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.verticalLayout_10.setContentsMargins(12, 20, 12, 0)
        self.verticalLayout_4 = QVBoxLayout()
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.tw_mesConfig = QTabWidget(self.tab_configMes)
        self.tw_mesConfig.setObjectName(u"tw_mesConfig")
        self.tw_mesConfig.setUsesScrollButtons(True)
        self.tw_mesConfig.setDocumentMode(True)
        self.tw_mesConfig.setTabsClosable(False)
        self.tw_mesConfig.setTabBarAutoHide(False)
        self.tab = QWidget()
        self.tab.setObjectName(u"tab")
        self.tab.setContextMenuPolicy(Qt.ContextMenuPolicy.ActionsContextMenu)
        self.verticalLayout_20 = QVBoxLayout(self.tab)
        self.verticalLayout_20.setObjectName(u"verticalLayout_20")
        self.verticalLayout_20.setContentsMargins(0, 20, 0, 0)
        self.verticalLayout_24 = QVBoxLayout()
        self.verticalLayout_24.setObjectName(u"verticalLayout_24")
        self.scrollArea = QScrollArea(self.tab)
        self.scrollArea.setObjectName(u"scrollArea")
        self.scrollArea.setStyleSheet(u"background-color: white;")
        self.scrollArea.setFrameShape(QFrame.Shape.NoFrame)
        self.scrollArea.setFrameShadow(QFrame.Shadow.Sunken)
        self.scrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 688, 411))
        self.verticalLayout_36 = QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout_36.setObjectName(u"verticalLayout_36")
        self.verticalLayout_36.setContentsMargins(12, 12, 12, 12)
        self.verticalLayout_30 = QVBoxLayout()
        self.verticalLayout_30.setSpacing(15)
        self.verticalLayout_30.setObjectName(u"verticalLayout_30")
        self.verticalLayout_30.setContentsMargins(-1, -1, -1, 0)
        self.groupBox_3 = QGroupBox(self.scrollAreaWidgetContents)
        self.groupBox_3.setObjectName(u"groupBox_3")
        self.verticalLayout_34 = QVBoxLayout(self.groupBox_3)
        self.verticalLayout_34.setSpacing(10)
        self.verticalLayout_34.setObjectName(u"verticalLayout_34")
        self.verticalLayout_34.setContentsMargins(12, 9, 12, 9)
        self.verticalLayout_38 = QVBoxLayout()
        self.verticalLayout_38.setSpacing(5)
        self.verticalLayout_38.setObjectName(u"verticalLayout_38")
        self.verticalLayout_38.setContentsMargins(-1, -1, -1, 0)
        self.horizontalLayout_22 = QHBoxLayout()
        self.horizontalLayout_22.setSpacing(20)
        self.horizontalLayout_22.setObjectName(u"horizontalLayout_22")
        self.label_12 = QLabel(self.groupBox_3)
        self.label_12.setObjectName(u"label_12")

        self.horizontalLayout_22.addWidget(self.label_12)

        self.le_mes_changeUser_id = QLineEdit(self.groupBox_3)
        self.le_mes_changeUser_id.setObjectName(u"le_mes_changeUser_id")
        self.le_mes_changeUser_id.setStyleSheet(u"")

        self.horizontalLayout_22.addWidget(self.le_mes_changeUser_id)

        self.horizontalLayout_22.setStretch(0, 1)
        self.horizontalLayout_22.setStretch(1, 1)

        self.verticalLayout_38.addLayout(self.horizontalLayout_22)

        self.horizontalLayout_24 = QHBoxLayout()
        self.horizontalLayout_24.setSpacing(20)
        self.horizontalLayout_24.setObjectName(u"horizontalLayout_24")
        self.label_17 = QLabel(self.groupBox_3)
        self.label_17.setObjectName(u"label_17")

        self.horizontalLayout_24.addWidget(self.label_17)

        self.le_mes_changeUser_password = QLineEdit(self.groupBox_3)
        self.le_mes_changeUser_password.setObjectName(u"le_mes_changeUser_password")
        self.le_mes_changeUser_password.setEchoMode(QLineEdit.EchoMode.Password)

        self.horizontalLayout_24.addWidget(self.le_mes_changeUser_password)

        self.horizontalLayout_24.setStretch(0, 1)
        self.horizontalLayout_24.setStretch(1, 1)

        self.verticalLayout_38.addLayout(self.horizontalLayout_24)


        self.verticalLayout_34.addLayout(self.verticalLayout_38)

        self.horizontalLayout_25 = QHBoxLayout()
        self.horizontalLayout_25.setSpacing(20)
        self.horizontalLayout_25.setObjectName(u"horizontalLayout_25")
        self.pb_mes_changeUser_clearAll = QPushButton(self.groupBox_3)
        self.pb_mes_changeUser_clearAll.setObjectName(u"pb_mes_changeUser_clearAll")
        self.pb_mes_changeUser_clearAll.setMinimumSize(QSize(0, 26))
        self.pb_mes_changeUser_clearAll.setMaximumSize(QSize(16777215, 26))
        self.pb_mes_changeUser_clearAll.setStyleSheet(u"QPushButton{\n"
"	color: rgb(58, 134, 255);\n"
"	background-color: white;\n"
"	border: 1px solid rgb(58, 134, 255);\n"
"	border-radius: 5px;\n"
"}\n"
"/*(QPushButton:hover{\n"
"	color: white;\n"
"	background-color: rgb(58, 134, 255);\n"
"	border-radius: 5px;\n"
"}*/\n"
"QPushButton:pressed {\n"
"	padding-top: 3px;\n"
"    padding-left: 3px;\n"
" }\n"
"QPushButton:disabled {\n"
"	color: #7f7f7f;\n"
"	border: 1px solid rgb(127, 127, 127);\n"
" }")

        self.horizontalLayout_25.addWidget(self.pb_mes_changeUser_clearAll)

        self.pb_mes_changeUser_request = QPushButton(self.groupBox_3)
        self.pb_mes_changeUser_request.setObjectName(u"pb_mes_changeUser_request")
        self.pb_mes_changeUser_request.setEnabled(True)
        self.pb_mes_changeUser_request.setMinimumSize(QSize(0, 26))
        self.pb_mes_changeUser_request.setMaximumSize(QSize(16777215, 26))
        self.pb_mes_changeUser_request.setStyleSheet(u"QPushButton{\n"
"	color: rgb(58, 134, 255);\n"
"	background-color: white;\n"
"	border: 1px solid rgb(58, 134, 255);\n"
"	border-radius: 5px;\n"
"}\n"
"/*(QPushButton:hover{\n"
"	color: white;\n"
"	background-color: rgb(58, 134, 255);\n"
"	border-radius: 5px;\n"
"}*/\n"
"QPushButton:pressed {\n"
"	padding-top: 3px;\n"
"    padding-left: 3px;\n"
" }\n"
"QPushButton:disabled {\n"
"	color: #7f7f7f;\n"
"	border: 1px solid rgb(127, 127, 127);\n"
" }")

        self.horizontalLayout_25.addWidget(self.pb_mes_changeUser_request)


        self.verticalLayout_34.addLayout(self.horizontalLayout_25)


        self.verticalLayout_30.addWidget(self.groupBox_3)

        self.groupBox_5 = QGroupBox(self.scrollAreaWidgetContents)
        self.groupBox_5.setObjectName(u"groupBox_5")
        self.verticalLayout_35 = QVBoxLayout(self.groupBox_5)
        self.verticalLayout_35.setSpacing(10)
        self.verticalLayout_35.setObjectName(u"verticalLayout_35")
        self.verticalLayout_35.setContentsMargins(12, 9, 12, 9)
        self.tb_mes_messageLog = QTextBrowser(self.groupBox_5)
        self.tb_mes_messageLog.setObjectName(u"tb_mes_messageLog")

        self.verticalLayout_35.addWidget(self.tb_mes_messageLog)

        self.horizontalLayout_26 = QHBoxLayout()
        self.horizontalLayout_26.setSpacing(20)
        self.horizontalLayout_26.setObjectName(u"horizontalLayout_26")
        self.label_24 = QLabel(self.groupBox_5)
        self.label_24.setObjectName(u"label_24")

        self.horizontalLayout_26.addWidget(self.label_24)

        self.pb_mes_messageLog_clear = QPushButton(self.groupBox_5)
        self.pb_mes_messageLog_clear.setObjectName(u"pb_mes_messageLog_clear")
        self.pb_mes_messageLog_clear.setMinimumSize(QSize(0, 26))
        self.pb_mes_messageLog_clear.setMaximumSize(QSize(16777215, 26))
        self.pb_mes_messageLog_clear.setStyleSheet(u"QPushButton{\n"
"	color: rgb(58, 134, 255);\n"
"	background-color: white;\n"
"	border: 1px solid rgb(58, 134, 255);\n"
"	border-radius: 5px;\n"
"}\n"
"/*(QPushButton:hover{\n"
"	color: white;\n"
"	background-color: rgb(58, 134, 255);\n"
"	border-radius: 5px;\n"
"}*/\n"
"QPushButton:pressed {\n"
"	padding-top: 3px;\n"
"    padding-left: 3px;\n"
" }\n"
"QPushButton:disabled {\n"
"	color: #7f7f7f;\n"
"	border: 1px solid rgb(127, 127, 127);\n"
" }")

        self.horizontalLayout_26.addWidget(self.pb_mes_messageLog_clear)

        self.horizontalLayout_26.setStretch(0, 1)
        self.horizontalLayout_26.setStretch(1, 1)

        self.verticalLayout_35.addLayout(self.horizontalLayout_26)


        self.verticalLayout_30.addWidget(self.groupBox_5)


        self.verticalLayout_36.addLayout(self.verticalLayout_30)

        self.scrollArea.setWidget(self.scrollAreaWidgetContents)

        self.verticalLayout_24.addWidget(self.scrollArea)


        self.verticalLayout_20.addLayout(self.verticalLayout_24)

        self.tw_mesConfig.addTab(self.tab, "")
        self.tab_2 = QWidget()
        self.tab_2.setObjectName(u"tab_2")
        self.verticalLayout_29 = QVBoxLayout(self.tab_2)
        self.verticalLayout_29.setObjectName(u"verticalLayout_29")
        self.verticalLayout_29.setContentsMargins(0, 20, 0, 0)
        self.verticalLayout_26 = QVBoxLayout()
        self.verticalLayout_26.setObjectName(u"verticalLayout_26")
        self.scrollArea_2 = QScrollArea(self.tab_2)
        self.scrollArea_2.setObjectName(u"scrollArea_2")
        self.scrollArea_2.setStyleSheet(u"background-color: white;")
        self.scrollArea_2.setFrameShape(QFrame.Shape.NoFrame)
        self.scrollArea_2.setFrameShadow(QFrame.Shadow.Sunken)
        self.scrollArea_2.setWidgetResizable(True)
        self.scrollAreaWidgetContents_2 = QWidget()
        self.scrollAreaWidgetContents_2.setObjectName(u"scrollAreaWidgetContents_2")
        self.scrollAreaWidgetContents_2.setGeometry(QRect(0, 0, 250, 415))
        self.verticalLayout_37 = QVBoxLayout(self.scrollAreaWidgetContents_2)
        self.verticalLayout_37.setObjectName(u"verticalLayout_37")
        self.verticalLayout_37.setContentsMargins(12, 12, 12, 12)
        self.verticalLayout_32 = QVBoxLayout()
        self.verticalLayout_32.setSpacing(15)
        self.verticalLayout_32.setObjectName(u"verticalLayout_32")
        self.verticalLayout_32.setContentsMargins(-1, -1, -1, 0)
        self.groupBox_14 = QGroupBox(self.scrollAreaWidgetContents_2)
        self.groupBox_14.setObjectName(u"groupBox_14")
        self.verticalLayout_53 = QVBoxLayout(self.groupBox_14)
        self.verticalLayout_53.setSpacing(10)
        self.verticalLayout_53.setObjectName(u"verticalLayout_53")
        self.verticalLayout_53.setContentsMargins(12, 9, 12, 9)
        self.verticalLayout_55 = QVBoxLayout()
        self.verticalLayout_55.setSpacing(5)
        self.verticalLayout_55.setObjectName(u"verticalLayout_55")
        self.verticalLayout_55.setContentsMargins(-1, -1, -1, 0)
        self.horizontalLayout_93 = QHBoxLayout()
        self.horizontalLayout_93.setSpacing(10)
        self.horizontalLayout_93.setObjectName(u"horizontalLayout_93")
        self.label_96 = QLabel(self.groupBox_14)
        self.label_96.setObjectName(u"label_96")
        self.label_96.setEnabled(True)

        self.horizontalLayout_93.addWidget(self.label_96)

        self.le_mes_currentUserId = QLineEdit(self.groupBox_14)
        self.le_mes_currentUserId.setObjectName(u"le_mes_currentUserId")
        self.le_mes_currentUserId.setEnabled(True)
        self.le_mes_currentUserId.setReadOnly(True)

        self.horizontalLayout_93.addWidget(self.le_mes_currentUserId)

        self.horizontalLayout_93.setStretch(0, 1)
        self.horizontalLayout_93.setStretch(1, 1)

        self.verticalLayout_55.addLayout(self.horizontalLayout_93)


        self.verticalLayout_53.addLayout(self.verticalLayout_55)


        self.verticalLayout_32.addWidget(self.groupBox_14)

        self.groupBox_13 = QGroupBox(self.scrollAreaWidgetContents_2)
        self.groupBox_13.setObjectName(u"groupBox_13")
        self.verticalLayout_52 = QVBoxLayout(self.groupBox_13)
        self.verticalLayout_52.setSpacing(10)
        self.verticalLayout_52.setObjectName(u"verticalLayout_52")
        self.verticalLayout_52.setContentsMargins(12, 9, 12, 9)
        self.horizontalLayout_35 = QHBoxLayout()
        self.horizontalLayout_35.setSpacing(10)
        self.horizontalLayout_35.setObjectName(u"horizontalLayout_35")
        self.horizontalLayout_35.setContentsMargins(-1, -1, -1, 0)
        self.label_22 = QLabel(self.groupBox_13)
        self.label_22.setObjectName(u"label_22")
        self.label_22.setEnabled(False)

        self.horizontalLayout_35.addWidget(self.label_22)

        self.sb_machineNumber = QSpinBox(self.groupBox_13)
        self.sb_machineNumber.setObjectName(u"sb_machineNumber")
        self.sb_machineNumber.setEnabled(False)
        self.sb_machineNumber.setMinimum(0)
        self.sb_machineNumber.setMaximum(1000)
        self.sb_machineNumber.setValue(0)
        self.sb_machineNumber.setDisplayIntegerBase(10)

        self.horizontalLayout_35.addWidget(self.sb_machineNumber)

        self.horizontalLayout_35.setStretch(0, 1)
        self.horizontalLayout_35.setStretch(1, 1)

        self.verticalLayout_52.addLayout(self.horizontalLayout_35)

        self.verticalLayout_54 = QVBoxLayout()
        self.verticalLayout_54.setSpacing(5)
        self.verticalLayout_54.setObjectName(u"verticalLayout_54")
        self.verticalLayout_54.setContentsMargins(-1, -1, -1, 0)
        self.horizontalLayout_40 = QHBoxLayout()
        self.horizontalLayout_40.setSpacing(10)
        self.horizontalLayout_40.setObjectName(u"horizontalLayout_40")
        self.label_23 = QLabel(self.groupBox_13)
        self.label_23.setObjectName(u"label_23")

        self.horizontalLayout_40.addWidget(self.label_23)

        self.le_mes_ipAddress = QLineEdit(self.groupBox_13)
        self.le_mes_ipAddress.setObjectName(u"le_mes_ipAddress")

        self.horizontalLayout_40.addWidget(self.le_mes_ipAddress)

        self.horizontalLayout_40.setStretch(0, 1)
        self.horizontalLayout_40.setStretch(1, 1)

        self.verticalLayout_54.addLayout(self.horizontalLayout_40)

        self.horizontalLayout_72 = QHBoxLayout()
        self.horizontalLayout_72.setSpacing(10)
        self.horizontalLayout_72.setObjectName(u"horizontalLayout_72")
        self.label_75 = QLabel(self.groupBox_13)
        self.label_75.setObjectName(u"label_75")

        self.horizontalLayout_72.addWidget(self.label_75)

        self.le_mes_portNumber = QLineEdit(self.groupBox_13)
        self.le_mes_portNumber.setObjectName(u"le_mes_portNumber")

        self.horizontalLayout_72.addWidget(self.le_mes_portNumber)

        self.horizontalLayout_72.setStretch(0, 1)
        self.horizontalLayout_72.setStretch(1, 1)

        self.verticalLayout_54.addLayout(self.horizontalLayout_72)

        self.horizontalLayout_82 = QHBoxLayout()
        self.horizontalLayout_82.setSpacing(10)
        self.horizontalLayout_82.setObjectName(u"horizontalLayout_82")
        self.label_85 = QLabel(self.groupBox_13)
        self.label_85.setObjectName(u"label_85")

        self.horizontalLayout_82.addWidget(self.label_85)

        self.le_mes_equipmentId = QLineEdit(self.groupBox_13)
        self.le_mes_equipmentId.setObjectName(u"le_mes_equipmentId")
        self.le_mes_equipmentId.setStyleSheet(u"")
        self.le_mes_equipmentId.setReadOnly(True)

        self.horizontalLayout_82.addWidget(self.le_mes_equipmentId)

        self.horizontalLayout_82.setStretch(0, 1)
        self.horizontalLayout_82.setStretch(1, 1)

        self.verticalLayout_54.addLayout(self.horizontalLayout_82)

        self.horizontalLayout_83 = QHBoxLayout()
        self.horizontalLayout_83.setSpacing(10)
        self.horizontalLayout_83.setObjectName(u"horizontalLayout_83")
        self.label_86 = QLabel(self.groupBox_13)
        self.label_86.setObjectName(u"label_86")
        self.label_86.setEnabled(False)

        self.horizontalLayout_83.addWidget(self.label_86)

        self.le_mes_subEquipmentId = QLineEdit(self.groupBox_13)
        self.le_mes_subEquipmentId.setObjectName(u"le_mes_subEquipmentId")
        self.le_mes_subEquipmentId.setEnabled(False)

        self.horizontalLayout_83.addWidget(self.le_mes_subEquipmentId)

        self.horizontalLayout_83.setStretch(0, 1)
        self.horizontalLayout_83.setStretch(1, 1)

        self.verticalLayout_54.addLayout(self.horizontalLayout_83)

        self.horizontalLayout_84 = QHBoxLayout()
        self.horizontalLayout_84.setSpacing(10)
        self.horizontalLayout_84.setObjectName(u"horizontalLayout_84")
        self.label_87 = QLabel(self.groupBox_13)
        self.label_87.setObjectName(u"label_87")
        self.label_87.setEnabled(True)

        self.horizontalLayout_84.addWidget(self.label_87)

        self.le_mes_stepId = QLineEdit(self.groupBox_13)
        self.le_mes_stepId.setObjectName(u"le_mes_stepId")
        self.le_mes_stepId.setEnabled(True)

        self.horizontalLayout_84.addWidget(self.le_mes_stepId)

        self.horizontalLayout_84.setStretch(0, 1)
        self.horizontalLayout_84.setStretch(1, 1)

        self.verticalLayout_54.addLayout(self.horizontalLayout_84)

        self.horizontalLayout_85 = QHBoxLayout()
        self.horizontalLayout_85.setSpacing(10)
        self.horizontalLayout_85.setObjectName(u"horizontalLayout_85")
        self.label_88 = QLabel(self.groupBox_13)
        self.label_88.setObjectName(u"label_88")
        self.label_88.setEnabled(True)

        self.horizontalLayout_85.addWidget(self.label_88)

        self.le_mes_equipmentTypeCode = QLineEdit(self.groupBox_13)
        self.le_mes_equipmentTypeCode.setObjectName(u"le_mes_equipmentTypeCode")
        self.le_mes_equipmentTypeCode.setEnabled(True)

        self.horizontalLayout_85.addWidget(self.le_mes_equipmentTypeCode)

        self.horizontalLayout_85.setStretch(0, 1)
        self.horizontalLayout_85.setStretch(1, 1)

        self.verticalLayout_54.addLayout(self.horizontalLayout_85)

        self.horizontalLayout_86 = QHBoxLayout()
        self.horizontalLayout_86.setSpacing(10)
        self.horizontalLayout_86.setObjectName(u"horizontalLayout_86")
        self.label_89 = QLabel(self.groupBox_13)
        self.label_89.setObjectName(u"label_89")
        self.label_89.setEnabled(False)

        self.horizontalLayout_86.addWidget(self.label_89)

        self.le_mes_softwareVersion = QLineEdit(self.groupBox_13)
        self.le_mes_softwareVersion.setObjectName(u"le_mes_softwareVersion")
        self.le_mes_softwareVersion.setEnabled(False)

        self.horizontalLayout_86.addWidget(self.le_mes_softwareVersion)

        self.horizontalLayout_86.setStretch(0, 1)
        self.horizontalLayout_86.setStretch(1, 1)

        self.verticalLayout_54.addLayout(self.horizontalLayout_86)

        self.horizontalLayout_87 = QHBoxLayout()
        self.horizontalLayout_87.setSpacing(10)
        self.horizontalLayout_87.setObjectName(u"horizontalLayout_87")
        self.label_90 = QLabel(self.groupBox_13)
        self.label_90.setObjectName(u"label_90")
        self.label_90.setEnabled(False)

        self.horizontalLayout_87.addWidget(self.label_90)

        self.le_mes_softwareHashCode = QLineEdit(self.groupBox_13)
        self.le_mes_softwareHashCode.setObjectName(u"le_mes_softwareHashCode")
        self.le_mes_softwareHashCode.setEnabled(False)

        self.horizontalLayout_87.addWidget(self.le_mes_softwareHashCode)

        self.horizontalLayout_87.setStretch(0, 1)
        self.horizontalLayout_87.setStretch(1, 1)

        self.verticalLayout_54.addLayout(self.horizontalLayout_87)


        self.verticalLayout_52.addLayout(self.verticalLayout_54)


        self.verticalLayout_32.addWidget(self.groupBox_13)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_32.addItem(self.verticalSpacer)


        self.verticalLayout_37.addLayout(self.verticalLayout_32)

        self.scrollArea_2.setWidget(self.scrollAreaWidgetContents_2)

        self.verticalLayout_26.addWidget(self.scrollArea_2)


        self.verticalLayout_29.addLayout(self.verticalLayout_26)

        self.tw_mesConfig.addTab(self.tab_2, "")

        self.verticalLayout_4.addWidget(self.tw_mesConfig)


        self.verticalLayout_10.addLayout(self.verticalLayout_4)

        self.tw_settings.addTab(self.tab_configMes, "")
        self.tab_system = QWidget()
        self.tab_system.setObjectName(u"tab_system")
        self.tab_system.setEnabled(True)
        self.verticalLayout_39 = QVBoxLayout(self.tab_system)
        self.verticalLayout_39.setSpacing(20)
        self.verticalLayout_39.setObjectName(u"verticalLayout_39")
        self.verticalLayout_39.setContentsMargins(12, 20, 12, 0)
        self.horizontalLayout_14 = QHBoxLayout()
        self.horizontalLayout_14.setSpacing(20)
        self.horizontalLayout_14.setObjectName(u"horizontalLayout_14")
        self.horizontalLayout_14.setContentsMargins(-1, -1, 0, 0)
        self.label_9 = QLabel(self.tab_system)
        self.label_9.setObjectName(u"label_9")

        self.horizontalLayout_14.addWidget(self.label_9)

        self.pb_setLockUnlock_3 = QPushButton(self.tab_system)
        self.pb_setLockUnlock_3.setObjectName(u"pb_setLockUnlock_3")
        self.pb_setLockUnlock_3.setEnabled(True)
        sizePolicy2.setHeightForWidth(self.pb_setLockUnlock_3.sizePolicy().hasHeightForWidth())
        self.pb_setLockUnlock_3.setSizePolicy(sizePolicy2)
        self.pb_setLockUnlock_3.setMinimumSize(QSize(0, 26))
        self.pb_setLockUnlock_3.setMaximumSize(QSize(16777215, 26))
        self.pb_setLockUnlock_3.setStyleSheet(u"QPushButton{\n"
"	color: rgb(58, 134, 255);\n"
"	background-color: white;\n"
"	border: 1px solid rgb(58, 134, 255);\n"
"	border-radius: 5px;\n"
"}\n"
"/*(QPushButton:hover{\n"
"	color: white;\n"
"	background-color: rgb(58, 134, 255);\n"
"	border-radius: 5px;\n"
"}*/\n"
"QPushButton:pressed {\n"
"	padding-top: 3px;\n"
"    padding-left: 3px;\n"
" }\n"
"QPushButton:disabled {\n"
"	color: #7f7f7f;\n"
"	border: 1px solid rgb(127, 127, 127);\n"
" }")
        icon3 = QIcon()
        icon3.addFile(u":/icon/res/icon/key_lock.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.pb_setLockUnlock_3.setIcon(icon3)

        self.horizontalLayout_14.addWidget(self.pb_setLockUnlock_3)

        self.horizontalLayout_14.setStretch(0, 1)
        self.horizontalLayout_14.setStretch(1, 1)

        self.verticalLayout_39.addLayout(self.horizontalLayout_14)

        self.verticalLayout_17 = QVBoxLayout()
        self.verticalLayout_17.setObjectName(u"verticalLayout_17")
        self.toolBox = QToolBox(self.tab_system)
        self.toolBox.setObjectName(u"toolBox")
        self.toolBox.setStyleSheet(u"background-color: white;")
        self.page = QWidget()
        self.page.setObjectName(u"page")
        self.page.setGeometry(QRect(0, 0, 222, 56))
        self.verticalLayout_13 = QVBoxLayout(self.page)
        self.verticalLayout_13.setObjectName(u"verticalLayout_13")
        self.verticalLayout_12 = QVBoxLayout()
        self.verticalLayout_12.setSpacing(6)
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.verticalLayout_12.setContentsMargins(-1, -1, -1, 0)
        self.verticalLayout_18 = QVBoxLayout()
        self.verticalLayout_18.setObjectName(u"verticalLayout_18")
        self.verticalLayout_18.setContentsMargins(-1, -1, -1, 0)
        self.horizontalLayout_15 = QHBoxLayout()
        self.horizontalLayout_15.setSpacing(20)
        self.horizontalLayout_15.setObjectName(u"horizontalLayout_15")
        self.horizontalLayout_15.setContentsMargins(-1, -1, -1, 0)
        self.horizontalLayout_16 = QHBoxLayout()
        self.horizontalLayout_16.setSpacing(20)
        self.horizontalLayout_16.setObjectName(u"horizontalLayout_16")
        self.label_10 = QLabel(self.page)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setEnabled(True)

        self.horizontalLayout_16.addWidget(self.label_10)

        self.label_5 = QLabel(self.page)
        self.label_5.setObjectName(u"label_5")

        self.horizontalLayout_16.addWidget(self.label_5)


        self.horizontalLayout_15.addLayout(self.horizontalLayout_16)

        self.pushButton_startTest = QPushButton(self.page)
        self.pushButton_startTest.setObjectName(u"pushButton_startTest")
        self.pushButton_startTest.setEnabled(True)
        self.pushButton_startTest.setMinimumSize(QSize(0, 26))
        self.pushButton_startTest.setMaximumSize(QSize(16777215, 26))
        self.pushButton_startTest.setStyleSheet(u"QPushButton{\n"
"	color: rgb(58, 134, 255);\n"
"	background-color: white;\n"
"	border: 1px solid rgb(58, 134, 255);\n"
"	border-radius: 5px;\n"
"}\n"
"/*(QPushButton:hover{\n"
"	color: white;\n"
"	background-color: rgb(58, 134, 255);\n"
"	border-radius: 5px;\n"
"}*/\n"
"QPushButton:pressed {\n"
"	padding-top: 3px;\n"
"    padding-left: 3px;\n"
" }\n"
"QPushButton:disabled {\n"
"	color: #7f7f7f;\n"
"	border: 1px solid rgb(127, 127, 127);\n"
" }")
        icon4 = QIcon()
        icon4.addFile(u":/icon/res/icon/test_start.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.pushButton_startTest.setIcon(icon4)

        self.horizontalLayout_15.addWidget(self.pushButton_startTest)

        self.horizontalLayout_15.setStretch(0, 1)
        self.horizontalLayout_15.setStretch(1, 1)

        self.verticalLayout_18.addLayout(self.horizontalLayout_15)


        self.verticalLayout_12.addLayout(self.verticalLayout_18)

        self.verticalSpacer_3 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_12.addItem(self.verticalSpacer_3)


        self.verticalLayout_13.addLayout(self.verticalLayout_12)

        self.toolBox.addItem(self.page, u"Execute a command")
        self.page_3 = QWidget()
        self.page_3.setObjectName(u"page_3")
        self.page_3.setGeometry(QRect(0, 0, 690, 319))
        self.horizontalLayout_3 = QHBoxLayout(self.page_3)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.verticalLayout_11 = QVBoxLayout()
        self.verticalLayout_11.setSpacing(15)
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.verticalLayout_11.setContentsMargins(0, -1, -1, 0)
        self.scrollArea_3 = QScrollArea(self.page_3)
        self.scrollArea_3.setObjectName(u"scrollArea_3")
        self.scrollArea_3.setFrameShape(QFrame.Shape.NoFrame)
        self.scrollArea_3.setWidgetResizable(True)
        self.scrollAreaWidgetContents_3 = QWidget()
        self.scrollAreaWidgetContents_3.setObjectName(u"scrollAreaWidgetContents_3")
        self.scrollAreaWidgetContents_3.setGeometry(QRect(0, 0, 670, 299))
        self.verticalLayout_40 = QVBoxLayout(self.scrollAreaWidgetContents_3)
        self.verticalLayout_40.setSpacing(15)
        self.verticalLayout_40.setObjectName(u"verticalLayout_40")
        self.verticalLayout_40.setContentsMargins(0, 0, 0, 0)
        self.groupBox = QGroupBox(self.scrollAreaWidgetContents_3)
        self.groupBox.setObjectName(u"groupBox")

        self.verticalLayout_40.addWidget(self.groupBox)

        self.groupBox_2 = QGroupBox(self.scrollAreaWidgetContents_3)
        self.groupBox_2.setObjectName(u"groupBox_2")

        self.verticalLayout_40.addWidget(self.groupBox_2)

        self.groupBox_4 = QGroupBox(self.scrollAreaWidgetContents_3)
        self.groupBox_4.setObjectName(u"groupBox_4")

        self.verticalLayout_40.addWidget(self.groupBox_4)

        self.scrollArea_3.setWidget(self.scrollAreaWidgetContents_3)

        self.verticalLayout_11.addWidget(self.scrollArea_3)


        self.horizontalLayout_3.addLayout(self.verticalLayout_11)

        self.toolBox.addItem(self.page_3, u"IO Control")
        self.page_2 = QWidget()
        self.page_2.setObjectName(u"page_2")
        self.page_2.setGeometry(QRect(0, 0, 243, 86))
        self.verticalLayout_15 = QVBoxLayout(self.page_2)
        self.verticalLayout_15.setObjectName(u"verticalLayout_15")
        self.verticalLayout_9 = QVBoxLayout()
        self.verticalLayout_9.setSpacing(15)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.verticalLayout_9.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_14 = QVBoxLayout()
        self.verticalLayout_14.setSpacing(5)
        self.verticalLayout_14.setObjectName(u"verticalLayout_14")
        self.verticalLayout_14.setContentsMargins(-1, -1, -1, 0)
        self.horizontalLayout_18 = QHBoxLayout()
        self.horizontalLayout_18.setSpacing(20)
        self.horizontalLayout_18.setObjectName(u"horizontalLayout_18")
        self.horizontalLayout_18.setContentsMargins(-1, -1, 0, 0)
        self.label_14 = QLabel(self.page_2)
        self.label_14.setObjectName(u"label_14")

        self.horizontalLayout_18.addWidget(self.label_14)

        self.dateEdit_date = QDateEdit(self.page_2)
        self.dateEdit_date.setObjectName(u"dateEdit_date")

        self.horizontalLayout_18.addWidget(self.dateEdit_date)


        self.verticalLayout_14.addLayout(self.horizontalLayout_18)

        self.horizontalLayout_20 = QHBoxLayout()
        self.horizontalLayout_20.setSpacing(20)
        self.horizontalLayout_20.setObjectName(u"horizontalLayout_20")
        self.horizontalLayout_20.setContentsMargins(-1, -1, 0, 0)
        self.label_19 = QLabel(self.page_2)
        self.label_19.setObjectName(u"label_19")

        self.horizontalLayout_20.addWidget(self.label_19)

        self.timeEdit_time = QTimeEdit(self.page_2)
        self.timeEdit_time.setObjectName(u"timeEdit_time")
        self.timeEdit_time.setMaximumDate(QDate(2000, 1, 1))

        self.horizontalLayout_20.addWidget(self.timeEdit_time)


        self.verticalLayout_14.addLayout(self.horizontalLayout_20)


        self.verticalLayout_9.addLayout(self.verticalLayout_14)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_9.addItem(self.verticalSpacer_2)


        self.verticalLayout_15.addLayout(self.verticalLayout_9)

        self.toolBox.addItem(self.page_2, u"Set date/time")

        self.verticalLayout_17.addWidget(self.toolBox)


        self.verticalLayout_39.addLayout(self.verticalLayout_17)

        self.tw_settings.addTab(self.tab_system, "")

        self.verticalLayout_22.addWidget(self.tw_settings)


        self.verticalLayout_28.addLayout(self.verticalLayout_22)


        self.verticalLayout_7.addWidget(self.frame_right)

        self.splitter_mainWindow.addWidget(self.mainFrame_right)

        self.horizontalLayout.addWidget(self.splitter_mainWindow)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.verticalLayout.setStretch(0, 1)
        self.verticalLayout.setStretch(2, 15)

        self.verticalLayout_2.addLayout(self.verticalLayout)

        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        self.tabWidget.setCurrentIndex(0)
        self.tw_settings.setCurrentIndex(2)
        self.tabWidget_2.setCurrentIndex(0)
        self.tw_mesConfig.setCurrentIndex(0)
        self.toolBox.setCurrentIndex(1)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"ID Mapping_32Ch", None))
        self.label_logoLeft.setText("")
        self.label_dateTime.setText(QCoreApplication.translate("MainWindow", u"25/03/09 12:00:00", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"SEM ID Mapping Server_32Ch", None))
        self.label_30.setText("")
        self.label_logoRight.setText("")
        self.lbl_equipmentId.setText(QCoreApplication.translate("MainWindow", u"Model Name: xxx", None))
        self.label_15.setText(QCoreApplication.translate("MainWindow", u"Customer:", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"Model Name:", None))
        self.label_21.setText(QCoreApplication.translate("MainWindow", u"Select Number:", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_5), QCoreApplication.translate("MainWindow", u"Job Log", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_6), QCoreApplication.translate("MainWindow", u"Job Log_All", None))
        self.label_29.setText(QCoreApplication.translate("MainWindow", u"Settings", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Customer:", None))
        self.label_20.setText(QCoreApplication.translate("MainWindow", u"Model Name:", None))
        self.groupBox_9.setTitle(QCoreApplication.translate("MainWindow", u"Module Script", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Script:", None))
        self.pb_loadscript.setText(QCoreApplication.translate("MainWindow", u"Load", None))
        self.groupBox_7.setTitle(QCoreApplication.translate("MainWindow", u"Carrier && Module", None))
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"Carrier(Rows x Colums):", None))
        self.label_11.setText(QCoreApplication.translate("MainWindow", u"Module(Rows x Colums):", None))
        self.label_4.setText("")
        self.label_6.setText("")
        self.pb_SaveScript.setText(QCoreApplication.translate("MainWindow", u"Save", None))
        self.tw_settings.setTabText(self.tw_settings.indexOf(self.tab_setOpenShortSpec), QCoreApplication.translate("MainWindow", u"Model Info", None))
        self.label_16.setText(QCoreApplication.translate("MainWindow", u"Firmware:", None))
        self.pb_upload_Firmware.setText(QCoreApplication.translate("MainWindow", u"Upload Firmware", None))
        self.label_13.setText(QCoreApplication.translate("MainWindow", u"Script:", None))
        self.pb_upload_Script.setText(QCoreApplication.translate("MainWindow", u"Upload Model Script", None))
        ___qtablewidgetitem = self.tableWidget.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("MainWindow", u"Status", None));
        ___qtablewidgetitem1 = self.tableWidget.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("MainWindow", u"IP Address", None));
        ___qtablewidgetitem2 = self.tableWidget.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("MainWindow", u"Bank No.", None));
        ___qtablewidgetitem3 = self.tableWidget.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("MainWindow", u"Port No.", None));
        ___qtablewidgetitem4 = self.tableWidget.horizontalHeaderItem(4)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("MainWindow", u"F/W Version", None));
        ___qtablewidgetitem5 = self.tableWidget.horizontalHeaderItem(5)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("MainWindow", u"Script Name", None));
        ___qtablewidgetitem6 = self.tableWidget.horizontalHeaderItem(6)
        ___qtablewidgetitem6.setText(QCoreApplication.translate("MainWindow", u"Descriptions", None));

        __sortingEnabled = self.tableWidget.isSortingEnabled()
        self.tableWidget.setSortingEnabled(False)
        ___qtablewidgetitem7 = self.tableWidget.item(0, 1)
        ___qtablewidgetitem7.setText(QCoreApplication.translate("MainWindow", u"192.168.0.1", None));
        ___qtablewidgetitem8 = self.tableWidget.item(0, 2)
        ___qtablewidgetitem8.setText(QCoreApplication.translate("MainWindow", u"1", None));
        ___qtablewidgetitem9 = self.tableWidget.item(0, 3)
        ___qtablewidgetitem9.setText(QCoreApplication.translate("MainWindow", u"1", None));
        ___qtablewidgetitem10 = self.tableWidget.item(1, 1)
        ___qtablewidgetitem10.setText(QCoreApplication.translate("MainWindow", u"192.168.0.2", None));
        ___qtablewidgetitem11 = self.tableWidget.item(1, 2)
        ___qtablewidgetitem11.setText(QCoreApplication.translate("MainWindow", u"1", None));
        ___qtablewidgetitem12 = self.tableWidget.item(1, 3)
        ___qtablewidgetitem12.setText(QCoreApplication.translate("MainWindow", u"2", None));
        ___qtablewidgetitem13 = self.tableWidget.item(2, 1)
        ___qtablewidgetitem13.setText(QCoreApplication.translate("MainWindow", u"192.168.0.3", None));
        ___qtablewidgetitem14 = self.tableWidget.item(2, 2)
        ___qtablewidgetitem14.setText(QCoreApplication.translate("MainWindow", u"1", None));
        ___qtablewidgetitem15 = self.tableWidget.item(2, 3)
        ___qtablewidgetitem15.setText(QCoreApplication.translate("MainWindow", u"3", None));
        ___qtablewidgetitem16 = self.tableWidget.item(3, 1)
        ___qtablewidgetitem16.setText(QCoreApplication.translate("MainWindow", u"192.168.0.4", None));
        ___qtablewidgetitem17 = self.tableWidget.item(3, 2)
        ___qtablewidgetitem17.setText(QCoreApplication.translate("MainWindow", u"1", None));
        ___qtablewidgetitem18 = self.tableWidget.item(3, 3)
        ___qtablewidgetitem18.setText(QCoreApplication.translate("MainWindow", u"4", None));
        ___qtablewidgetitem19 = self.tableWidget.item(4, 1)
        ___qtablewidgetitem19.setText(QCoreApplication.translate("MainWindow", u"192.168.0.5", None));
        ___qtablewidgetitem20 = self.tableWidget.item(4, 2)
        ___qtablewidgetitem20.setText(QCoreApplication.translate("MainWindow", u"2", None));
        ___qtablewidgetitem21 = self.tableWidget.item(4, 3)
        ___qtablewidgetitem21.setText(QCoreApplication.translate("MainWindow", u"1", None));
        ___qtablewidgetitem22 = self.tableWidget.item(5, 1)
        ___qtablewidgetitem22.setText(QCoreApplication.translate("MainWindow", u"192.168.0.6", None));
        ___qtablewidgetitem23 = self.tableWidget.item(5, 2)
        ___qtablewidgetitem23.setText(QCoreApplication.translate("MainWindow", u"2", None));
        ___qtablewidgetitem24 = self.tableWidget.item(5, 3)
        ___qtablewidgetitem24.setText(QCoreApplication.translate("MainWindow", u"2", None));
        ___qtablewidgetitem25 = self.tableWidget.item(6, 1)
        ___qtablewidgetitem25.setText(QCoreApplication.translate("MainWindow", u"192.168.0.7", None));
        ___qtablewidgetitem26 = self.tableWidget.item(6, 2)
        ___qtablewidgetitem26.setText(QCoreApplication.translate("MainWindow", u"2", None));
        ___qtablewidgetitem27 = self.tableWidget.item(6, 3)
        ___qtablewidgetitem27.setText(QCoreApplication.translate("MainWindow", u"3", None));
        ___qtablewidgetitem28 = self.tableWidget.item(7, 1)
        ___qtablewidgetitem28.setText(QCoreApplication.translate("MainWindow", u"192.168.0.8", None));
        ___qtablewidgetitem29 = self.tableWidget.item(7, 2)
        ___qtablewidgetitem29.setText(QCoreApplication.translate("MainWindow", u"2", None));
        ___qtablewidgetitem30 = self.tableWidget.item(7, 3)
        ___qtablewidgetitem30.setText(QCoreApplication.translate("MainWindow", u"4", None));
        ___qtablewidgetitem31 = self.tableWidget.item(8, 1)
        ___qtablewidgetitem31.setText(QCoreApplication.translate("MainWindow", u"192.168.0.9", None));
        ___qtablewidgetitem32 = self.tableWidget.item(8, 2)
        ___qtablewidgetitem32.setText(QCoreApplication.translate("MainWindow", u"3", None));
        ___qtablewidgetitem33 = self.tableWidget.item(8, 3)
        ___qtablewidgetitem33.setText(QCoreApplication.translate("MainWindow", u"1", None));
        ___qtablewidgetitem34 = self.tableWidget.item(9, 1)
        ___qtablewidgetitem34.setText(QCoreApplication.translate("MainWindow", u"192.168.0.10", None));
        ___qtablewidgetitem35 = self.tableWidget.item(9, 2)
        ___qtablewidgetitem35.setText(QCoreApplication.translate("MainWindow", u"3", None));
        ___qtablewidgetitem36 = self.tableWidget.item(9, 3)
        ___qtablewidgetitem36.setText(QCoreApplication.translate("MainWindow", u"2", None));
        ___qtablewidgetitem37 = self.tableWidget.item(10, 1)
        ___qtablewidgetitem37.setText(QCoreApplication.translate("MainWindow", u"192.168.0.11", None));
        ___qtablewidgetitem38 = self.tableWidget.item(10, 2)
        ___qtablewidgetitem38.setText(QCoreApplication.translate("MainWindow", u"3", None));
        ___qtablewidgetitem39 = self.tableWidget.item(10, 3)
        ___qtablewidgetitem39.setText(QCoreApplication.translate("MainWindow", u"3", None));
        ___qtablewidgetitem40 = self.tableWidget.item(11, 1)
        ___qtablewidgetitem40.setText(QCoreApplication.translate("MainWindow", u"192.168.0.12", None));
        ___qtablewidgetitem41 = self.tableWidget.item(11, 2)
        ___qtablewidgetitem41.setText(QCoreApplication.translate("MainWindow", u"3", None));
        ___qtablewidgetitem42 = self.tableWidget.item(11, 3)
        ___qtablewidgetitem42.setText(QCoreApplication.translate("MainWindow", u"4", None));
        ___qtablewidgetitem43 = self.tableWidget.item(12, 1)
        ___qtablewidgetitem43.setText(QCoreApplication.translate("MainWindow", u"192.168.0.13", None));
        ___qtablewidgetitem44 = self.tableWidget.item(12, 2)
        ___qtablewidgetitem44.setText(QCoreApplication.translate("MainWindow", u"4", None));
        ___qtablewidgetitem45 = self.tableWidget.item(12, 3)
        ___qtablewidgetitem45.setText(QCoreApplication.translate("MainWindow", u"1", None));
        ___qtablewidgetitem46 = self.tableWidget.item(13, 1)
        ___qtablewidgetitem46.setText(QCoreApplication.translate("MainWindow", u"192.168.0.14", None));
        ___qtablewidgetitem47 = self.tableWidget.item(13, 2)
        ___qtablewidgetitem47.setText(QCoreApplication.translate("MainWindow", u"4", None));
        ___qtablewidgetitem48 = self.tableWidget.item(13, 3)
        ___qtablewidgetitem48.setText(QCoreApplication.translate("MainWindow", u"2", None));
        ___qtablewidgetitem49 = self.tableWidget.item(14, 1)
        ___qtablewidgetitem49.setText(QCoreApplication.translate("MainWindow", u"192.168.0.15", None));
        ___qtablewidgetitem50 = self.tableWidget.item(14, 2)
        ___qtablewidgetitem50.setText(QCoreApplication.translate("MainWindow", u"4", None));
        ___qtablewidgetitem51 = self.tableWidget.item(14, 3)
        ___qtablewidgetitem51.setText(QCoreApplication.translate("MainWindow", u"3", None));
        ___qtablewidgetitem52 = self.tableWidget.item(15, 1)
        ___qtablewidgetitem52.setText(QCoreApplication.translate("MainWindow", u"192.168.0.16", None));
        ___qtablewidgetitem53 = self.tableWidget.item(15, 2)
        ___qtablewidgetitem53.setText(QCoreApplication.translate("MainWindow", u"4", None));
        ___qtablewidgetitem54 = self.tableWidget.item(15, 3)
        ___qtablewidgetitem54.setText(QCoreApplication.translate("MainWindow", u"4", None));
        ___qtablewidgetitem55 = self.tableWidget.item(16, 1)
        ___qtablewidgetitem55.setText(QCoreApplication.translate("MainWindow", u"192.168.0.17", None));
        ___qtablewidgetitem56 = self.tableWidget.item(16, 2)
        ___qtablewidgetitem56.setText(QCoreApplication.translate("MainWindow", u"5", None));
        ___qtablewidgetitem57 = self.tableWidget.item(16, 3)
        ___qtablewidgetitem57.setText(QCoreApplication.translate("MainWindow", u"1", None));
        ___qtablewidgetitem58 = self.tableWidget.item(17, 1)
        ___qtablewidgetitem58.setText(QCoreApplication.translate("MainWindow", u"192.168.0.18", None));
        ___qtablewidgetitem59 = self.tableWidget.item(17, 2)
        ___qtablewidgetitem59.setText(QCoreApplication.translate("MainWindow", u"5", None));
        ___qtablewidgetitem60 = self.tableWidget.item(17, 3)
        ___qtablewidgetitem60.setText(QCoreApplication.translate("MainWindow", u"2", None));
        ___qtablewidgetitem61 = self.tableWidget.item(18, 1)
        ___qtablewidgetitem61.setText(QCoreApplication.translate("MainWindow", u"192.168.0.19", None));
        ___qtablewidgetitem62 = self.tableWidget.item(18, 2)
        ___qtablewidgetitem62.setText(QCoreApplication.translate("MainWindow", u"5", None));
        ___qtablewidgetitem63 = self.tableWidget.item(18, 3)
        ___qtablewidgetitem63.setText(QCoreApplication.translate("MainWindow", u"3", None));
        ___qtablewidgetitem64 = self.tableWidget.item(19, 1)
        ___qtablewidgetitem64.setText(QCoreApplication.translate("MainWindow", u"192.168.0.20", None));
        ___qtablewidgetitem65 = self.tableWidget.item(19, 2)
        ___qtablewidgetitem65.setText(QCoreApplication.translate("MainWindow", u"5", None));
        ___qtablewidgetitem66 = self.tableWidget.item(19, 3)
        ___qtablewidgetitem66.setText(QCoreApplication.translate("MainWindow", u"4", None));
        ___qtablewidgetitem67 = self.tableWidget.item(20, 1)
        ___qtablewidgetitem67.setText(QCoreApplication.translate("MainWindow", u"192.168.0.21", None));
        ___qtablewidgetitem68 = self.tableWidget.item(20, 2)
        ___qtablewidgetitem68.setText(QCoreApplication.translate("MainWindow", u"6", None));
        ___qtablewidgetitem69 = self.tableWidget.item(20, 3)
        ___qtablewidgetitem69.setText(QCoreApplication.translate("MainWindow", u"1", None));
        ___qtablewidgetitem70 = self.tableWidget.item(21, 1)
        ___qtablewidgetitem70.setText(QCoreApplication.translate("MainWindow", u"192.168.0.22", None));
        ___qtablewidgetitem71 = self.tableWidget.item(21, 2)
        ___qtablewidgetitem71.setText(QCoreApplication.translate("MainWindow", u"6", None));
        ___qtablewidgetitem72 = self.tableWidget.item(21, 3)
        ___qtablewidgetitem72.setText(QCoreApplication.translate("MainWindow", u"2", None));
        ___qtablewidgetitem73 = self.tableWidget.item(22, 1)
        ___qtablewidgetitem73.setText(QCoreApplication.translate("MainWindow", u"192.168.0.23", None));
        ___qtablewidgetitem74 = self.tableWidget.item(22, 2)
        ___qtablewidgetitem74.setText(QCoreApplication.translate("MainWindow", u"6", None));
        ___qtablewidgetitem75 = self.tableWidget.item(22, 3)
        ___qtablewidgetitem75.setText(QCoreApplication.translate("MainWindow", u"3", None));
        ___qtablewidgetitem76 = self.tableWidget.item(23, 1)
        ___qtablewidgetitem76.setText(QCoreApplication.translate("MainWindow", u"192.168.0.24", None));
        ___qtablewidgetitem77 = self.tableWidget.item(23, 2)
        ___qtablewidgetitem77.setText(QCoreApplication.translate("MainWindow", u"6", None));
        ___qtablewidgetitem78 = self.tableWidget.item(23, 3)
        ___qtablewidgetitem78.setText(QCoreApplication.translate("MainWindow", u"4", None));
        ___qtablewidgetitem79 = self.tableWidget.item(24, 1)
        ___qtablewidgetitem79.setText(QCoreApplication.translate("MainWindow", u"192.168.0.25", None));
        ___qtablewidgetitem80 = self.tableWidget.item(24, 2)
        ___qtablewidgetitem80.setText(QCoreApplication.translate("MainWindow", u"7", None));
        ___qtablewidgetitem81 = self.tableWidget.item(24, 3)
        ___qtablewidgetitem81.setText(QCoreApplication.translate("MainWindow", u"1", None));
        ___qtablewidgetitem82 = self.tableWidget.item(25, 1)
        ___qtablewidgetitem82.setText(QCoreApplication.translate("MainWindow", u"192.168.0.26", None));
        ___qtablewidgetitem83 = self.tableWidget.item(25, 2)
        ___qtablewidgetitem83.setText(QCoreApplication.translate("MainWindow", u"7", None));
        ___qtablewidgetitem84 = self.tableWidget.item(25, 3)
        ___qtablewidgetitem84.setText(QCoreApplication.translate("MainWindow", u"2", None));
        ___qtablewidgetitem85 = self.tableWidget.item(26, 1)
        ___qtablewidgetitem85.setText(QCoreApplication.translate("MainWindow", u"192.168.0.27", None));
        ___qtablewidgetitem86 = self.tableWidget.item(26, 2)
        ___qtablewidgetitem86.setText(QCoreApplication.translate("MainWindow", u"7", None));
        ___qtablewidgetitem87 = self.tableWidget.item(26, 3)
        ___qtablewidgetitem87.setText(QCoreApplication.translate("MainWindow", u"3", None));
        ___qtablewidgetitem88 = self.tableWidget.item(27, 1)
        ___qtablewidgetitem88.setText(QCoreApplication.translate("MainWindow", u"192.168.0.28", None));
        ___qtablewidgetitem89 = self.tableWidget.item(27, 2)
        ___qtablewidgetitem89.setText(QCoreApplication.translate("MainWindow", u"7", None));
        ___qtablewidgetitem90 = self.tableWidget.item(27, 3)
        ___qtablewidgetitem90.setText(QCoreApplication.translate("MainWindow", u"4", None));
        ___qtablewidgetitem91 = self.tableWidget.item(28, 1)
        ___qtablewidgetitem91.setText(QCoreApplication.translate("MainWindow", u"192.168.0.29", None));
        ___qtablewidgetitem92 = self.tableWidget.item(28, 2)
        ___qtablewidgetitem92.setText(QCoreApplication.translate("MainWindow", u"8", None));
        ___qtablewidgetitem93 = self.tableWidget.item(28, 3)
        ___qtablewidgetitem93.setText(QCoreApplication.translate("MainWindow", u"1", None));
        ___qtablewidgetitem94 = self.tableWidget.item(29, 1)
        ___qtablewidgetitem94.setText(QCoreApplication.translate("MainWindow", u"192.168.0.30", None));
        ___qtablewidgetitem95 = self.tableWidget.item(29, 2)
        ___qtablewidgetitem95.setText(QCoreApplication.translate("MainWindow", u"8", None));
        ___qtablewidgetitem96 = self.tableWidget.item(29, 3)
        ___qtablewidgetitem96.setText(QCoreApplication.translate("MainWindow", u"2", None));
        ___qtablewidgetitem97 = self.tableWidget.item(30, 1)
        ___qtablewidgetitem97.setText(QCoreApplication.translate("MainWindow", u"192.168.0.31", None));
        ___qtablewidgetitem98 = self.tableWidget.item(30, 2)
        ___qtablewidgetitem98.setText(QCoreApplication.translate("MainWindow", u"8", None));
        ___qtablewidgetitem99 = self.tableWidget.item(30, 3)
        ___qtablewidgetitem99.setText(QCoreApplication.translate("MainWindow", u"3", None));
        ___qtablewidgetitem100 = self.tableWidget.item(31, 1)
        ___qtablewidgetitem100.setText(QCoreApplication.translate("MainWindow", u"192.168.0.32", None));
        ___qtablewidgetitem101 = self.tableWidget.item(31, 2)
        ___qtablewidgetitem101.setText(QCoreApplication.translate("MainWindow", u"8", None));
        ___qtablewidgetitem102 = self.tableWidget.item(31, 3)
        ___qtablewidgetitem102.setText(QCoreApplication.translate("MainWindow", u"4", None));
        self.tableWidget.setSortingEnabled(__sortingEnabled)

        self.tw_settings.setTabText(self.tw_settings.indexOf(self.tab_3), QCoreApplication.translate("MainWindow", u"Clients", None))
        self.groupBox_8.setTitle(QCoreApplication.translate("MainWindow", u"Left Camera", None))
        self.label_25.setText(QCoreApplication.translate("MainWindow", u"Brightness:", None))
        self.le_mes_ipAddress_2.setText("")
        self.label_76.setText(QCoreApplication.translate("MainWindow", u"Sharpness:", None))
        self.le_mes_portNumber_2.setText("")
        self.label_79.setText(QCoreApplication.translate("MainWindow", u"Threshold:", None))
        self.le_mes_portNumber_5.setText("")
        self.groupBox_6.setTitle(QCoreApplication.translate("MainWindow", u"Right Camera", None))
        self.label_28.setText(QCoreApplication.translate("MainWindow", u"Brightness:", None))
        self.le_mes_ipAddress_4.setText("")
        self.label_77.setText(QCoreApplication.translate("MainWindow", u"Sharpness:", None))
        self.le_mes_portNumber_3.setText("")
        self.label_80.setText(QCoreApplication.translate("MainWindow", u"Threshold:", None))
        self.le_mes_portNumber_6.setText("")
        self.label_32.setText("")
        self.label_35.setText("")
        self.pb_mes_messageLog_clear_4.setText(QCoreApplication.translate("MainWindow", u"Save", None))
        self.tabWidget_2.setTabText(self.tabWidget_2.indexOf(self.tab_7), QCoreApplication.translate("MainWindow", u"Parameters", None))
        self.label_27.setText("")
        self.label_37.setText("")
        self.pb_mes_messageLog_clear_6.setText(QCoreApplication.translate("MainWindow", u"Scan Barcode", None))
        self.tabWidget_2.setTabText(self.tabWidget_2.indexOf(self.tab_8), QCoreApplication.translate("MainWindow", u"Scan Test_Left", None))
        self.label_26.setText("")
        self.label_36.setText("")
        self.pb_mes_messageLog_clear_3.setText(QCoreApplication.translate("MainWindow", u"Scan Barcode", None))
        self.tabWidget_2.setTabText(self.tabWidget_2.indexOf(self.tab_9), QCoreApplication.translate("MainWindow", u"ScanTest_Right", None))
        self.tw_settings.setTabText(self.tw_settings.indexOf(self.tab_4), QCoreApplication.translate("MainWindow", u"Camea", None))
        self.groupBox_3.setTitle(QCoreApplication.translate("MainWindow", u"Change User", None))
        self.label_12.setText(QCoreApplication.translate("MainWindow", u"User ID:", None))
        self.label_17.setText(QCoreApplication.translate("MainWindow", u"Password:", None))
        self.le_mes_changeUser_password.setText("")
        self.pb_mes_changeUser_clearAll.setText(QCoreApplication.translate("MainWindow", u"Clear All", None))
        self.pb_mes_changeUser_request.setText(QCoreApplication.translate("MainWindow", u"User Change Request", None))
        self.groupBox_5.setTitle(QCoreApplication.translate("MainWindow", u"Message Log", None))
        self.label_24.setText("")
        self.pb_mes_messageLog_clear.setText(QCoreApplication.translate("MainWindow", u"Clear Log", None))
        self.tw_mesConfig.setTabText(self.tw_mesConfig.indexOf(self.tab), QCoreApplication.translate("MainWindow", u"Work", None))
        self.groupBox_14.setTitle(QCoreApplication.translate("MainWindow", u"User", None))
        self.label_96.setText(QCoreApplication.translate("MainWindow", u"Current User ID:", None))
        self.le_mes_currentUserId.setText("")
        self.groupBox_13.setTitle(QCoreApplication.translate("MainWindow", u"Equipment", None))
        self.label_22.setText(QCoreApplication.translate("MainWindow", u"Machine Number:", None))
        self.label_23.setText(QCoreApplication.translate("MainWindow", u"IP Address:", None))
        self.le_mes_ipAddress.setText("")
        self.label_75.setText(QCoreApplication.translate("MainWindow", u"Port Number:", None))
        self.le_mes_portNumber.setText("")
        self.label_85.setText(QCoreApplication.translate("MainWindow", u"Equipmnet ID:", None))
        self.le_mes_equipmentId.setText("")
        self.label_86.setText(QCoreApplication.translate("MainWindow", u"Sub Equipmnet ID:", None))
        self.le_mes_subEquipmentId.setText("")
        self.label_87.setText(QCoreApplication.translate("MainWindow", u"Step ID:", None))
        self.le_mes_stepId.setText("")
        self.label_88.setText(QCoreApplication.translate("MainWindow", u"Equipment Type Code:", None))
        self.le_mes_equipmentTypeCode.setText("")
        self.label_89.setText(QCoreApplication.translate("MainWindow", u"Software Version:", None))
        self.le_mes_softwareVersion.setText("")
        self.label_90.setText(QCoreApplication.translate("MainWindow", u"Software Hash Code:", None))
        self.le_mes_softwareHashCode.setText("")
        self.tw_mesConfig.setTabText(self.tw_mesConfig.indexOf(self.tab_2), QCoreApplication.translate("MainWindow", u"Settings", None))
        self.tw_settings.setTabText(self.tw_settings.indexOf(self.tab_configMes), QCoreApplication.translate("MainWindow", u"MES", None))
        self.label_9.setText(QCoreApplication.translate("MainWindow", u"Lock / Unlock:", None))
        self.pb_setLockUnlock_3.setText(QCoreApplication.translate("MainWindow", u"Locked", None))
        self.label_10.setText(QCoreApplication.translate("MainWindow", u"Manual Test:", None))
        self.label_5.setText("")
        self.pushButton_startTest.setText(QCoreApplication.translate("MainWindow", u"Start Test", None))
        self.toolBox.setItemText(self.toolBox.indexOf(self.page), QCoreApplication.translate("MainWindow", u"Execute a command", None))
        self.groupBox.setTitle(QCoreApplication.translate("MainWindow", u"Air Cylinder", None))
        self.groupBox_2.setTitle(QCoreApplication.translate("MainWindow", u"Tower Lamp", None))
        self.groupBox_4.setTitle(QCoreApplication.translate("MainWindow", u"Switch", None))
        self.toolBox.setItemText(self.toolBox.indexOf(self.page_3), QCoreApplication.translate("MainWindow", u"IO Control", None))
        self.label_14.setText(QCoreApplication.translate("MainWindow", u"Date(yyyy/MM/dd):", None))
        self.dateEdit_date.setDisplayFormat(QCoreApplication.translate("MainWindow", u"yyyy/MM/dd", None))
        self.label_19.setText(QCoreApplication.translate("MainWindow", u"Time:", None))
        self.toolBox.setItemText(self.toolBox.indexOf(self.page_2), QCoreApplication.translate("MainWindow", u"Set date/time", None))
        self.tw_settings.setTabText(self.tw_settings.indexOf(self.tab_system), QCoreApplication.translate("MainWindow", u"System", None))
    # retranslateUi

