# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'tps.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *

import ui.tps_rc

class Ui_TandaPaySimulationWindow(object):
    def setupUi(self, TandaPaySimulationWindow):
        if not TandaPaySimulationWindow.objectName():
            TandaPaySimulationWindow.setObjectName(u"TandaPaySimulationWindow")
        TandaPaySimulationWindow.resize(1170, 835)
        font = QFont()
        font.setPointSize(12)
        TandaPaySimulationWindow.setFont(font)
        self.centralwidget = QWidget(TandaPaySimulationWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setSpacing(20)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(10, 10, 10, 10)
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(10, 10, 10, 10)
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        self.label.setMinimumSize(QSize(200, 0))

        self.horizontalLayout.addWidget(self.label)

        self.result_path = QLineEdit(self.centralwidget)
        self.result_path.setObjectName(u"result_path")
        self.result_path.setReadOnly(True)

        self.horizontalLayout.addWidget(self.result_path)

        self.btn_result_path = QToolButton(self.centralwidget)
        self.btn_result_path.setObjectName(u"btn_result_path")
        icon = QIcon()
        icon.addFile(u":/img/img/Open.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_result_path.setIcon(icon)
        self.btn_result_path.setIconSize(QSize(30, 30))

        self.horizontalLayout.addWidget(self.btn_result_path)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.tabWidget = QTabWidget(self.centralwidget)
        self.tabWidget.setObjectName(u"tabWidget")
        self.tab = QWidget()
        self.tab.setObjectName(u"tab")
        self.verticalLayout_4 = QVBoxLayout(self.tab)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setSpacing(30)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.groupBox = QGroupBox(self.tab)
        self.groupBox.setObjectName(u"groupBox")
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.groupBox.sizePolicy().hasHeightForWidth())
        self.groupBox.setSizePolicy(sizePolicy)
        self.groupBox.setMinimumSize(QSize(0, 0))
        self.verticalLayout_2 = QVBoxLayout(self.groupBox)
        self.verticalLayout_2.setSpacing(15)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setSpacing(10)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.label_4 = QLabel(self.groupBox)
        self.label_4.setObjectName(u"label_4")

        self.horizontalLayout_5.addWidget(self.label_4)

        self.ev_0 = QSpinBox(self.groupBox)
        self.ev_0.setObjectName(u"ev_0")
        self.ev_0.setMinimumSize(QSize(70, 0))
        self.ev_0.setMaximumSize(QSize(70, 16777215))
        self.ev_0.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.ev_0.setMinimum(1)
        self.ev_0.setMaximum(9999)
        self.ev_0.setValue(60)

        self.horizontalLayout_5.addWidget(self.ev_0)


        self.verticalLayout_2.addLayout(self.horizontalLayout_5)

        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_6.setSpacing(10)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.label_5 = QLabel(self.groupBox)
        self.label_5.setObjectName(u"label_5")
        sizePolicy1 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.label_5.sizePolicy().hasHeightForWidth())
        self.label_5.setSizePolicy(sizePolicy1)

        self.horizontalLayout_6.addWidget(self.label_5)

        self.ev_1 = QSpinBox(self.groupBox)
        self.ev_1.setObjectName(u"ev_1")
        self.ev_1.setMinimumSize(QSize(70, 0))
        self.ev_1.setMaximumSize(QSize(70, 16777215))
        self.ev_1.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.ev_1.setMinimum(4)
        self.ev_1.setMaximum(9999)
        self.ev_1.setValue(1000)

        self.horizontalLayout_6.addWidget(self.ev_1)


        self.verticalLayout_2.addLayout(self.horizontalLayout_6)

        self.horizontalLayout_7 = QHBoxLayout()
        self.horizontalLayout_7.setSpacing(10)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.label_6 = QLabel(self.groupBox)
        self.label_6.setObjectName(u"label_6")

        self.horizontalLayout_7.addWidget(self.label_6)

        self.ev_2 = QSpinBox(self.groupBox)
        self.ev_2.setObjectName(u"ev_2")
        self.ev_2.setMinimumSize(QSize(70, 0))
        self.ev_2.setMaximumSize(QSize(70, 16777215))
        self.ev_2.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.ev_2.setMinimum(0)
        self.ev_2.setMaximum(100)
        self.ev_2.setValue(40)

        self.horizontalLayout_7.addWidget(self.ev_2)


        self.verticalLayout_2.addLayout(self.horizontalLayout_7)

        self.horizontalLayout_8 = QHBoxLayout()
        self.horizontalLayout_8.setSpacing(10)
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.label_7 = QLabel(self.groupBox)
        self.label_7.setObjectName(u"label_7")

        self.horizontalLayout_8.addWidget(self.label_7)

        self.ev_3 = QSpinBox(self.groupBox)
        self.ev_3.setObjectName(u"ev_3")
        self.ev_3.setMinimumSize(QSize(70, 0))
        self.ev_3.setMaximumSize(QSize(70, 16777215))
        self.ev_3.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.ev_3.setMinimum(0)
        self.ev_3.setMaximum(100)
        self.ev_3.setValue(27)

        self.horizontalLayout_8.addWidget(self.ev_3)


        self.verticalLayout_2.addLayout(self.horizontalLayout_8)

        self.horizontalLayout_9 = QHBoxLayout()
        self.horizontalLayout_9.setSpacing(10)
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.label_8 = QLabel(self.groupBox)
        self.label_8.setObjectName(u"label_8")

        self.horizontalLayout_9.addWidget(self.label_8)

        self.ev_4 = QSpinBox(self.groupBox)
        self.ev_4.setObjectName(u"ev_4")
        self.ev_4.setMinimumSize(QSize(70, 0))
        self.ev_4.setMaximumSize(QSize(70, 16777215))
        self.ev_4.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.ev_4.setMinimum(0)
        self.ev_4.setMaximum(100)
        self.ev_4.setValue(10)

        self.horizontalLayout_9.addWidget(self.ev_4)


        self.verticalLayout_2.addLayout(self.horizontalLayout_9)

        self.horizontalLayout_10 = QHBoxLayout()
        self.horizontalLayout_10.setSpacing(10)
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.label_9 = QLabel(self.groupBox)
        self.label_9.setObjectName(u"label_9")

        self.horizontalLayout_10.addWidget(self.label_9)

        self.ev_5 = QSpinBox(self.groupBox)
        self.ev_5.setObjectName(u"ev_5")
        self.ev_5.setMinimumSize(QSize(70, 0))
        self.ev_5.setMaximumSize(QSize(70, 16777215))
        self.ev_5.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.ev_5.setMinimum(0)
        self.ev_5.setMaximum(100)
        self.ev_5.setValue(70)

        self.horizontalLayout_10.addWidget(self.ev_5)


        self.verticalLayout_2.addLayout(self.horizontalLayout_10)

        self.horizontalLayout_11 = QHBoxLayout()
        self.horizontalLayout_11.setSpacing(10)
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.label_10 = QLabel(self.groupBox)
        self.label_10.setObjectName(u"label_10")

        self.horizontalLayout_11.addWidget(self.label_10)

        self.ev_6 = QSpinBox(self.groupBox)
        self.ev_6.setObjectName(u"ev_6")
        self.ev_6.setMinimumSize(QSize(70, 0))
        self.ev_6.setMaximumSize(QSize(70, 16777215))
        self.ev_6.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.ev_6.setMinimum(2)
        self.ev_6.setMaximum(4)
        self.ev_6.setValue(2)

        self.horizontalLayout_11.addWidget(self.ev_6)


        self.verticalLayout_2.addLayout(self.horizontalLayout_11)

        self.horizontalLayout_12 = QHBoxLayout()
        self.horizontalLayout_12.setSpacing(10)
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
        self.label_11 = QLabel(self.groupBox)
        self.label_11.setObjectName(u"label_11")

        self.horizontalLayout_12.addWidget(self.label_11)

        self.ev_7 = QSpinBox(self.groupBox)
        self.ev_7.setObjectName(u"ev_7")
        self.ev_7.setMinimumSize(QSize(70, 0))
        self.ev_7.setMaximumSize(QSize(70, 16777215))
        self.ev_7.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.ev_7.setMinimum(0)
        self.ev_7.setMaximum(3)
        self.ev_7.setValue(3)

        self.horizontalLayout_12.addWidget(self.ev_7)


        self.verticalLayout_2.addLayout(self.horizontalLayout_12)

        self.horizontalLayout_28 = QHBoxLayout()
        self.horizontalLayout_28.setSpacing(10)
        self.horizontalLayout_28.setObjectName(u"horizontalLayout_28")
        self.label_12 = QLabel(self.groupBox)
        self.label_12.setObjectName(u"label_12")

        self.horizontalLayout_28.addWidget(self.label_12)

        self.ev_8 = QSpinBox(self.groupBox)
        self.ev_8.setObjectName(u"ev_8")
        self.ev_8.setMinimumSize(QSize(70, 0))
        self.ev_8.setMaximumSize(QSize(70, 16777215))
        self.ev_8.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.ev_8.setMinimum(0)
        self.ev_8.setMaximum(100)
        self.ev_8.setValue(33)

        self.horizontalLayout_28.addWidget(self.ev_8)


        self.verticalLayout_2.addLayout(self.horizontalLayout_28)


        self.horizontalLayout_4.addWidget(self.groupBox)

        self.groupBox_2 = QGroupBox(self.tab)
        self.groupBox_2.setObjectName(u"groupBox_2")
        sizePolicy.setHeightForWidth(self.groupBox_2.sizePolicy().hasHeightForWidth())
        self.groupBox_2.setSizePolicy(sizePolicy)
        self.verticalLayout_3 = QVBoxLayout(self.groupBox_2)
        self.verticalLayout_3.setSpacing(20)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.horizontalLayout_18 = QHBoxLayout()
        self.horizontalLayout_18.setObjectName(u"horizontalLayout_18")
        self.label_13 = QLabel(self.groupBox_2)
        self.label_13.setObjectName(u"label_13")

        self.horizontalLayout_18.addWidget(self.label_13)

        self.pv_0 = QSpinBox(self.groupBox_2)
        self.pv_0.setObjectName(u"pv_0")
        self.pv_0.setMinimumSize(QSize(70, 0))
        self.pv_0.setMaximumSize(QSize(70, 16777215))
        self.pv_0.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.pv_0.setMinimum(1)
        self.pv_0.setMaximum(100)
        self.pv_0.setValue(10)

        self.horizontalLayout_18.addWidget(self.pv_0)


        self.verticalLayout_3.addLayout(self.horizontalLayout_18)

        self.horizontalLayout_19 = QHBoxLayout()
        self.horizontalLayout_19.setObjectName(u"horizontalLayout_19")
        self.label_14 = QLabel(self.groupBox_2)
        self.label_14.setObjectName(u"label_14")
        sizePolicy1.setHeightForWidth(self.label_14.sizePolicy().hasHeightForWidth())
        self.label_14.setSizePolicy(sizePolicy1)

        self.horizontalLayout_19.addWidget(self.label_14)

        self.pv_1 = QSpinBox(self.groupBox_2)
        self.pv_1.setObjectName(u"pv_1")
        self.pv_1.setMinimumSize(QSize(70, 0))
        self.pv_1.setMaximumSize(QSize(70, 16777215))
        self.pv_1.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.pv_1.setMinimum(1)
        self.pv_1.setMaximum(100)
        self.pv_1.setValue(2)

        self.horizontalLayout_19.addWidget(self.pv_1)


        self.verticalLayout_3.addLayout(self.horizontalLayout_19)

        self.horizontalLayout_20 = QHBoxLayout()
        self.horizontalLayout_20.setObjectName(u"horizontalLayout_20")
        self.label_15 = QLabel(self.groupBox_2)
        self.label_15.setObjectName(u"label_15")

        self.horizontalLayout_20.addWidget(self.label_15)

        self.pv_2 = QSpinBox(self.groupBox_2)
        self.pv_2.setObjectName(u"pv_2")
        self.pv_2.setMinimumSize(QSize(70, 0))
        self.pv_2.setMaximumSize(QSize(70, 16777215))
        self.pv_2.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.pv_2.setMinimum(0)
        self.pv_2.setMaximum(9999)
        self.pv_2.setValue(70)

        self.horizontalLayout_20.addWidget(self.pv_2)


        self.verticalLayout_3.addLayout(self.horizontalLayout_20)

        self.horizontalLayout_22 = QHBoxLayout()
        self.horizontalLayout_22.setObjectName(u"horizontalLayout_22")
        self.label_16 = QLabel(self.groupBox_2)
        self.label_16.setObjectName(u"label_16")

        self.horizontalLayout_22.addWidget(self.label_16)

        self.pv_3 = QSpinBox(self.groupBox_2)
        self.pv_3.setObjectName(u"pv_3")
        self.pv_3.setMinimumSize(QSize(70, 0))
        self.pv_3.setMaximumSize(QSize(70, 16777215))
        self.pv_3.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.pv_3.setMinimum(0)
        self.pv_3.setMaximum(100)
        self.pv_3.setValue(8)

        self.horizontalLayout_22.addWidget(self.pv_3)


        self.verticalLayout_3.addLayout(self.horizontalLayout_22)

        self.horizontalLayout_23 = QHBoxLayout()
        self.horizontalLayout_23.setObjectName(u"horizontalLayout_23")
        self.label_17 = QLabel(self.groupBox_2)
        self.label_17.setObjectName(u"label_17")

        self.horizontalLayout_23.addWidget(self.label_17)

        self.pv_4 = QSpinBox(self.groupBox_2)
        self.pv_4.setObjectName(u"pv_4")
        self.pv_4.setMinimumSize(QSize(70, 0))
        self.pv_4.setMaximumSize(QSize(70, 16777215))
        self.pv_4.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.pv_4.setMinimum(0)
        self.pv_4.setMaximum(100)
        self.pv_4.setValue(77)

        self.horizontalLayout_23.addWidget(self.pv_4)


        self.verticalLayout_3.addLayout(self.horizontalLayout_23)

        self.horizontalLayout_24 = QHBoxLayout()
        self.horizontalLayout_24.setObjectName(u"horizontalLayout_24")
        self.label_18 = QLabel(self.groupBox_2)
        self.label_18.setObjectName(u"label_18")

        self.horizontalLayout_24.addWidget(self.label_18)

        self.pv_5 = QSpinBox(self.groupBox_2)
        self.pv_5.setObjectName(u"pv_5")
        self.pv_5.setMinimumSize(QSize(70, 0))
        self.pv_5.setMaximumSize(QSize(70, 16777215))
        self.pv_5.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.pv_5.setMinimum(0)
        self.pv_5.setMaximum(100)
        self.pv_5.setValue(5)

        self.horizontalLayout_24.addWidget(self.pv_5)


        self.verticalLayout_3.addLayout(self.horizontalLayout_24)

        self.groupBox_3 = QGroupBox(self.groupBox_2)
        self.groupBox_3.setObjectName(u"groupBox_3")
        sizePolicy2 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.groupBox_3.sizePolicy().hasHeightForWidth())
        self.groupBox_3.setSizePolicy(sizePolicy2)
        self.layout_graph = QVBoxLayout(self.groupBox_3)
        self.layout_graph.setObjectName(u"layout_graph")

        self.verticalLayout_3.addWidget(self.groupBox_3)


        self.horizontalLayout_4.addWidget(self.groupBox_2)


        self.verticalLayout_4.addLayout(self.horizontalLayout_4)

        self.widget = QWidget(self.tab)
        self.widget.setObjectName(u"widget")
        self.widget.setMinimumSize(QSize(0, 50))
        self.horizontalLayout_25 = QHBoxLayout(self.widget)
        self.horizontalLayout_25.setSpacing(30)
        self.horizontalLayout_25.setObjectName(u"horizontalLayout_25")
        self.horizontalLayout_25.setContentsMargins(0, 0, 0, 0)
        self.horizontalSpacer = QSpacerItem(323, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_25.addItem(self.horizontalSpacer)

        self.btn_start_single = QPushButton(self.widget)
        self.btn_start_single.setObjectName(u"btn_start_single")
        self.btn_start_single.setMinimumSize(QSize(0, 35))

        self.horizontalLayout_25.addWidget(self.btn_start_single)

        self.btn_exit = QPushButton(self.widget)
        self.btn_exit.setObjectName(u"btn_exit")
        self.btn_exit.setMinimumSize(QSize(0, 35))

        self.horizontalLayout_25.addWidget(self.btn_exit)

        self.horizontalSpacer_2 = QSpacerItem(323, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_25.addItem(self.horizontalSpacer_2)


        self.verticalLayout_4.addWidget(self.widget)

        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QWidget()
        self.tab_2.setObjectName(u"tab_2")
        self.verticalLayout_7 = QVBoxLayout(self.tab_2)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.horizontalLayout_13 = QHBoxLayout()
        self.horizontalLayout_13.setSpacing(30)
        self.horizontalLayout_13.setObjectName(u"horizontalLayout_13")
        self.groupBox_4 = QGroupBox(self.tab_2)
        self.groupBox_4.setObjectName(u"groupBox_4")
        sizePolicy.setHeightForWidth(self.groupBox_4.sizePolicy().hasHeightForWidth())
        self.groupBox_4.setSizePolicy(sizePolicy)
        self.verticalLayout_5 = QVBoxLayout(self.groupBox_4)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setSpacing(10)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.label_32 = QLabel(self.groupBox_4)
        self.label_32.setObjectName(u"label_32")
        sizePolicy3 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Preferred)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.label_32.sizePolicy().hasHeightForWidth())
        self.label_32.setSizePolicy(sizePolicy3)
        self.label_32.setMinimumSize(QSize(50, 0))
        self.label_32.setMaximumSize(QSize(50, 16777215))

        self.horizontalLayout_2.addWidget(self.label_32)

        self.g_ev0 = QComboBox(self.groupBox_4)
        self.g_ev0.addItem("")
        self.g_ev0.addItem("")
        self.g_ev0.addItem("")
        self.g_ev0.addItem("")
        self.g_ev0.addItem("")
        self.g_ev0.addItem("")
        self.g_ev0.setObjectName(u"g_ev0")
        sizePolicy4 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(self.g_ev0.sizePolicy().hasHeightForWidth())
        self.g_ev0.setSizePolicy(sizePolicy4)
        self.g_ev0.setMinimumSize(QSize(70, 25))
        self.g_ev0.setMaximumSize(QSize(16777215, 25))

        self.horizontalLayout_2.addWidget(self.g_ev0)

        self.widget_3 = QWidget(self.groupBox_4)
        self.widget_3.setObjectName(u"widget_3")
        sizePolicy1.setHeightForWidth(self.widget_3.sizePolicy().hasHeightForWidth())
        self.widget_3.setSizePolicy(sizePolicy1)
        self.widget_3.setMinimumSize(QSize(300, 0))
        self.layout_ev0 = QHBoxLayout(self.widget_3)
        self.layout_ev0.setObjectName(u"layout_ev0")
        self.layout_ev0.setContentsMargins(0, 0, 0, 0)

        self.horizontalLayout_2.addWidget(self.widget_3)


        self.verticalLayout_5.addLayout(self.horizontalLayout_2)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setSpacing(10)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.label_33 = QLabel(self.groupBox_4)
        self.label_33.setObjectName(u"label_33")
        sizePolicy3.setHeightForWidth(self.label_33.sizePolicy().hasHeightForWidth())
        self.label_33.setSizePolicy(sizePolicy3)
        self.label_33.setMinimumSize(QSize(50, 0))
        self.label_33.setMaximumSize(QSize(50, 16777215))

        self.horizontalLayout_3.addWidget(self.label_33)

        self.g_ev2 = QComboBox(self.groupBox_4)
        self.g_ev2.addItem("")
        self.g_ev2.addItem("")
        self.g_ev2.addItem("")
        self.g_ev2.addItem("")
        self.g_ev2.addItem("")
        self.g_ev2.addItem("")
        self.g_ev2.setObjectName(u"g_ev2")
        sizePolicy4.setHeightForWidth(self.g_ev2.sizePolicy().hasHeightForWidth())
        self.g_ev2.setSizePolicy(sizePolicy4)
        self.g_ev2.setMinimumSize(QSize(70, 25))
        self.g_ev2.setMaximumSize(QSize(16777215, 25))

        self.horizontalLayout_3.addWidget(self.g_ev2)

        self.widget_4 = QWidget(self.groupBox_4)
        self.widget_4.setObjectName(u"widget_4")
        sizePolicy1.setHeightForWidth(self.widget_4.sizePolicy().hasHeightForWidth())
        self.widget_4.setSizePolicy(sizePolicy1)
        self.widget_4.setMinimumSize(QSize(300, 0))
        self.layout_ev2 = QHBoxLayout(self.widget_4)
        self.layout_ev2.setObjectName(u"layout_ev2")
        self.layout_ev2.setContentsMargins(0, 0, 0, 0)

        self.horizontalLayout_3.addWidget(self.widget_4)


        self.verticalLayout_5.addLayout(self.horizontalLayout_3)

        self.horizontalLayout_14 = QHBoxLayout()
        self.horizontalLayout_14.setSpacing(10)
        self.horizontalLayout_14.setObjectName(u"horizontalLayout_14")
        self.label_34 = QLabel(self.groupBox_4)
        self.label_34.setObjectName(u"label_34")
        sizePolicy3.setHeightForWidth(self.label_34.sizePolicy().hasHeightForWidth())
        self.label_34.setSizePolicy(sizePolicy3)
        self.label_34.setMinimumSize(QSize(50, 0))
        self.label_34.setMaximumSize(QSize(50, 16777215))

        self.horizontalLayout_14.addWidget(self.label_34)

        self.g_ev3 = QComboBox(self.groupBox_4)
        self.g_ev3.addItem("")
        self.g_ev3.addItem("")
        self.g_ev3.addItem("")
        self.g_ev3.addItem("")
        self.g_ev3.addItem("")
        self.g_ev3.addItem("")
        self.g_ev3.setObjectName(u"g_ev3")
        sizePolicy4.setHeightForWidth(self.g_ev3.sizePolicy().hasHeightForWidth())
        self.g_ev3.setSizePolicy(sizePolicy4)
        self.g_ev3.setMinimumSize(QSize(70, 25))
        self.g_ev3.setMaximumSize(QSize(16777215, 25))

        self.horizontalLayout_14.addWidget(self.g_ev3)

        self.widget_5 = QWidget(self.groupBox_4)
        self.widget_5.setObjectName(u"widget_5")
        sizePolicy1.setHeightForWidth(self.widget_5.sizePolicy().hasHeightForWidth())
        self.widget_5.setSizePolicy(sizePolicy1)
        self.widget_5.setMinimumSize(QSize(300, 0))
        self.layout_ev3 = QHBoxLayout(self.widget_5)
        self.layout_ev3.setObjectName(u"layout_ev3")
        self.layout_ev3.setContentsMargins(0, 0, 0, 0)

        self.horizontalLayout_14.addWidget(self.widget_5)


        self.verticalLayout_5.addLayout(self.horizontalLayout_14)

        self.horizontalLayout_15 = QHBoxLayout()
        self.horizontalLayout_15.setSpacing(10)
        self.horizontalLayout_15.setObjectName(u"horizontalLayout_15")
        self.label_35 = QLabel(self.groupBox_4)
        self.label_35.setObjectName(u"label_35")
        sizePolicy3.setHeightForWidth(self.label_35.sizePolicy().hasHeightForWidth())
        self.label_35.setSizePolicy(sizePolicy3)
        self.label_35.setMinimumSize(QSize(50, 0))
        self.label_35.setMaximumSize(QSize(50, 16777215))

        self.horizontalLayout_15.addWidget(self.label_35)

        self.g_ev4 = QComboBox(self.groupBox_4)
        self.g_ev4.addItem("")
        self.g_ev4.addItem("")
        self.g_ev4.addItem("")
        self.g_ev4.addItem("")
        self.g_ev4.addItem("")
        self.g_ev4.addItem("")
        self.g_ev4.setObjectName(u"g_ev4")
        sizePolicy4.setHeightForWidth(self.g_ev4.sizePolicy().hasHeightForWidth())
        self.g_ev4.setSizePolicy(sizePolicy4)
        self.g_ev4.setMinimumSize(QSize(70, 25))
        self.g_ev4.setMaximumSize(QSize(16777215, 25))

        self.horizontalLayout_15.addWidget(self.g_ev4)

        self.widget_6 = QWidget(self.groupBox_4)
        self.widget_6.setObjectName(u"widget_6")
        sizePolicy1.setHeightForWidth(self.widget_6.sizePolicy().hasHeightForWidth())
        self.widget_6.setSizePolicy(sizePolicy1)
        self.widget_6.setMinimumSize(QSize(300, 0))
        self.layout_ev4 = QHBoxLayout(self.widget_6)
        self.layout_ev4.setObjectName(u"layout_ev4")
        self.layout_ev4.setContentsMargins(0, 0, 0, 0)

        self.horizontalLayout_15.addWidget(self.widget_6)


        self.verticalLayout_5.addLayout(self.horizontalLayout_15)

        self.horizontalLayout_16 = QHBoxLayout()
        self.horizontalLayout_16.setSpacing(10)
        self.horizontalLayout_16.setObjectName(u"horizontalLayout_16")
        self.label_36 = QLabel(self.groupBox_4)
        self.label_36.setObjectName(u"label_36")
        sizePolicy3.setHeightForWidth(self.label_36.sizePolicy().hasHeightForWidth())
        self.label_36.setSizePolicy(sizePolicy3)
        self.label_36.setMinimumSize(QSize(50, 0))
        self.label_36.setMaximumSize(QSize(50, 16777215))

        self.horizontalLayout_16.addWidget(self.label_36)

        self.g_ev5 = QComboBox(self.groupBox_4)
        self.g_ev5.addItem("")
        self.g_ev5.addItem("")
        self.g_ev5.addItem("")
        self.g_ev5.addItem("")
        self.g_ev5.addItem("")
        self.g_ev5.addItem("")
        self.g_ev5.setObjectName(u"g_ev5")
        sizePolicy4.setHeightForWidth(self.g_ev5.sizePolicy().hasHeightForWidth())
        self.g_ev5.setSizePolicy(sizePolicy4)
        self.g_ev5.setMinimumSize(QSize(70, 25))
        self.g_ev5.setMaximumSize(QSize(16777215, 25))

        self.horizontalLayout_16.addWidget(self.g_ev5)

        self.widget_7 = QWidget(self.groupBox_4)
        self.widget_7.setObjectName(u"widget_7")
        sizePolicy1.setHeightForWidth(self.widget_7.sizePolicy().hasHeightForWidth())
        self.widget_7.setSizePolicy(sizePolicy1)
        self.widget_7.setMinimumSize(QSize(300, 0))
        self.layout_ev5 = QHBoxLayout(self.widget_7)
        self.layout_ev5.setObjectName(u"layout_ev5")
        self.layout_ev5.setContentsMargins(0, 0, 0, 0)

        self.horizontalLayout_16.addWidget(self.widget_7)


        self.verticalLayout_5.addLayout(self.horizontalLayout_16)

        self.horizontalLayout_17 = QHBoxLayout()
        self.horizontalLayout_17.setSpacing(10)
        self.horizontalLayout_17.setObjectName(u"horizontalLayout_17")
        self.label_37 = QLabel(self.groupBox_4)
        self.label_37.setObjectName(u"label_37")
        sizePolicy3.setHeightForWidth(self.label_37.sizePolicy().hasHeightForWidth())
        self.label_37.setSizePolicy(sizePolicy3)
        self.label_37.setMinimumSize(QSize(50, 0))
        self.label_37.setMaximumSize(QSize(50, 16777215))

        self.horizontalLayout_17.addWidget(self.label_37)

        self.g_ev6 = QComboBox(self.groupBox_4)
        self.g_ev6.addItem("")
        self.g_ev6.addItem("")
        self.g_ev6.addItem("")
        self.g_ev6.addItem("")
        self.g_ev6.setObjectName(u"g_ev6")
        sizePolicy4.setHeightForWidth(self.g_ev6.sizePolicy().hasHeightForWidth())
        self.g_ev6.setSizePolicy(sizePolicy4)
        self.g_ev6.setMinimumSize(QSize(70, 25))
        self.g_ev6.setMaximumSize(QSize(16777215, 25))

        self.horizontalLayout_17.addWidget(self.g_ev6)

        self.widget_8 = QWidget(self.groupBox_4)
        self.widget_8.setObjectName(u"widget_8")
        sizePolicy1.setHeightForWidth(self.widget_8.sizePolicy().hasHeightForWidth())
        self.widget_8.setSizePolicy(sizePolicy1)
        self.widget_8.setMinimumSize(QSize(300, 0))
        self.layout_ev6 = QHBoxLayout(self.widget_8)
        self.layout_ev6.setObjectName(u"layout_ev6")
        self.layout_ev6.setContentsMargins(0, 0, 0, 0)

        self.horizontalLayout_17.addWidget(self.widget_8)


        self.verticalLayout_5.addLayout(self.horizontalLayout_17)

        self.horizontalLayout_21 = QHBoxLayout()
        self.horizontalLayout_21.setSpacing(10)
        self.horizontalLayout_21.setObjectName(u"horizontalLayout_21")
        self.label_38 = QLabel(self.groupBox_4)
        self.label_38.setObjectName(u"label_38")
        sizePolicy3.setHeightForWidth(self.label_38.sizePolicy().hasHeightForWidth())
        self.label_38.setSizePolicy(sizePolicy3)
        self.label_38.setMinimumSize(QSize(50, 0))
        self.label_38.setMaximumSize(QSize(50, 16777215))

        self.horizontalLayout_21.addWidget(self.label_38)

        self.g_ev7 = QComboBox(self.groupBox_4)
        self.g_ev7.addItem("")
        self.g_ev7.addItem("")
        self.g_ev7.addItem("")
        self.g_ev7.addItem("")
        self.g_ev7.addItem("")
        self.g_ev7.addItem("")
        self.g_ev7.setObjectName(u"g_ev7")
        sizePolicy4.setHeightForWidth(self.g_ev7.sizePolicy().hasHeightForWidth())
        self.g_ev7.setSizePolicy(sizePolicy4)
        self.g_ev7.setMinimumSize(QSize(70, 25))
        self.g_ev7.setMaximumSize(QSize(16777215, 25))

        self.horizontalLayout_21.addWidget(self.g_ev7)

        self.widget_9 = QWidget(self.groupBox_4)
        self.widget_9.setObjectName(u"widget_9")
        sizePolicy1.setHeightForWidth(self.widget_9.sizePolicy().hasHeightForWidth())
        self.widget_9.setSizePolicy(sizePolicy1)
        self.widget_9.setMinimumSize(QSize(300, 0))
        self.layout_ev7 = QHBoxLayout(self.widget_9)
        self.layout_ev7.setObjectName(u"layout_ev7")
        self.layout_ev7.setContentsMargins(0, 0, 0, 0)

        self.horizontalLayout_21.addWidget(self.widget_9)


        self.verticalLayout_5.addLayout(self.horizontalLayout_21)

        self.horizontalLayout_27 = QHBoxLayout()
        self.horizontalLayout_27.setObjectName(u"horizontalLayout_27")
        self.label_39 = QLabel(self.groupBox_4)
        self.label_39.setObjectName(u"label_39")
        sizePolicy3.setHeightForWidth(self.label_39.sizePolicy().hasHeightForWidth())
        self.label_39.setSizePolicy(sizePolicy3)
        self.label_39.setMinimumSize(QSize(50, 0))
        self.label_39.setMaximumSize(QSize(50, 16777215))

        self.horizontalLayout_27.addWidget(self.label_39)

        self.widget_16 = QWidget(self.groupBox_4)
        self.widget_16.setObjectName(u"widget_16")
        self.layout_ev8 = QHBoxLayout(self.widget_16)
        self.layout_ev8.setSpacing(0)
        self.layout_ev8.setObjectName(u"layout_ev8")
        self.layout_ev8.setContentsMargins(0, 0, 0, 0)
        self.horizontalSpacer_5 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.layout_ev8.addItem(self.horizontalSpacer_5)

        self.ev8 = QSpinBox(self.widget_16)
        self.ev8.setObjectName(u"ev8")
        self.ev8.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.ev8.setMaximum(100)

        self.layout_ev8.addWidget(self.ev8)


        self.horizontalLayout_27.addWidget(self.widget_16)


        self.verticalLayout_5.addLayout(self.horizontalLayout_27)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_5.addItem(self.verticalSpacer)


        self.horizontalLayout_13.addWidget(self.groupBox_4)

        self.groupBox_5 = QGroupBox(self.tab_2)
        self.groupBox_5.setObjectName(u"groupBox_5")
        sizePolicy.setHeightForWidth(self.groupBox_5.sizePolicy().hasHeightForWidth())
        self.groupBox_5.setSizePolicy(sizePolicy)
        self.verticalLayout_6 = QVBoxLayout(self.groupBox_5)
        self.verticalLayout_6.setSpacing(10)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.horizontalLayout_29 = QHBoxLayout()
        self.horizontalLayout_29.setSpacing(10)
        self.horizontalLayout_29.setObjectName(u"horizontalLayout_29")
        self.label_41 = QLabel(self.groupBox_5)
        self.label_41.setObjectName(u"label_41")
        sizePolicy3.setHeightForWidth(self.label_41.sizePolicy().hasHeightForWidth())
        self.label_41.setSizePolicy(sizePolicy3)
        self.label_41.setMinimumSize(QSize(50, 0))
        self.label_41.setMaximumSize(QSize(50, 16777215))

        self.horizontalLayout_29.addWidget(self.label_41)

        self.g_pv0 = QComboBox(self.groupBox_5)
        self.g_pv0.addItem("")
        self.g_pv0.addItem("")
        self.g_pv0.addItem("")
        self.g_pv0.addItem("")
        self.g_pv0.addItem("")
        self.g_pv0.addItem("")
        self.g_pv0.setObjectName(u"g_pv0")
        sizePolicy4.setHeightForWidth(self.g_pv0.sizePolicy().hasHeightForWidth())
        self.g_pv0.setSizePolicy(sizePolicy4)
        self.g_pv0.setMinimumSize(QSize(70, 25))
        self.g_pv0.setMaximumSize(QSize(16777215, 25))

        self.horizontalLayout_29.addWidget(self.g_pv0)

        self.widget_10 = QWidget(self.groupBox_5)
        self.widget_10.setObjectName(u"widget_10")
        sizePolicy1.setHeightForWidth(self.widget_10.sizePolicy().hasHeightForWidth())
        self.widget_10.setSizePolicy(sizePolicy1)
        self.widget_10.setMinimumSize(QSize(300, 0))
        self.layout_pv0 = QHBoxLayout(self.widget_10)
        self.layout_pv0.setObjectName(u"layout_pv0")
        self.layout_pv0.setContentsMargins(0, 0, 0, 0)

        self.horizontalLayout_29.addWidget(self.widget_10)


        self.verticalLayout_6.addLayout(self.horizontalLayout_29)

        self.horizontalLayout_30 = QHBoxLayout()
        self.horizontalLayout_30.setSpacing(10)
        self.horizontalLayout_30.setObjectName(u"horizontalLayout_30")
        self.label_42 = QLabel(self.groupBox_5)
        self.label_42.setObjectName(u"label_42")
        sizePolicy3.setHeightForWidth(self.label_42.sizePolicy().hasHeightForWidth())
        self.label_42.setSizePolicy(sizePolicy3)
        self.label_42.setMinimumSize(QSize(50, 0))
        self.label_42.setMaximumSize(QSize(50, 16777215))

        self.horizontalLayout_30.addWidget(self.label_42)

        self.g_pv1 = QComboBox(self.groupBox_5)
        self.g_pv1.addItem("")
        self.g_pv1.addItem("")
        self.g_pv1.addItem("")
        self.g_pv1.addItem("")
        self.g_pv1.addItem("")
        self.g_pv1.addItem("")
        self.g_pv1.setObjectName(u"g_pv1")
        sizePolicy4.setHeightForWidth(self.g_pv1.sizePolicy().hasHeightForWidth())
        self.g_pv1.setSizePolicy(sizePolicy4)
        self.g_pv1.setMinimumSize(QSize(70, 25))
        self.g_pv1.setMaximumSize(QSize(16777215, 25))

        self.horizontalLayout_30.addWidget(self.g_pv1)

        self.widget_11 = QWidget(self.groupBox_5)
        self.widget_11.setObjectName(u"widget_11")
        sizePolicy1.setHeightForWidth(self.widget_11.sizePolicy().hasHeightForWidth())
        self.widget_11.setSizePolicy(sizePolicy1)
        self.widget_11.setMinimumSize(QSize(300, 0))
        self.layout_pv1 = QHBoxLayout(self.widget_11)
        self.layout_pv1.setObjectName(u"layout_pv1")
        self.layout_pv1.setContentsMargins(0, 0, 0, 0)

        self.horizontalLayout_30.addWidget(self.widget_11)


        self.verticalLayout_6.addLayout(self.horizontalLayout_30)

        self.horizontalLayout_31 = QHBoxLayout()
        self.horizontalLayout_31.setSpacing(10)
        self.horizontalLayout_31.setObjectName(u"horizontalLayout_31")
        self.label_43 = QLabel(self.groupBox_5)
        self.label_43.setObjectName(u"label_43")
        sizePolicy3.setHeightForWidth(self.label_43.sizePolicy().hasHeightForWidth())
        self.label_43.setSizePolicy(sizePolicy3)
        self.label_43.setMinimumSize(QSize(50, 0))
        self.label_43.setMaximumSize(QSize(50, 16777215))

        self.horizontalLayout_31.addWidget(self.label_43)

        self.g_pv2 = QComboBox(self.groupBox_5)
        self.g_pv2.addItem("")
        self.g_pv2.addItem("")
        self.g_pv2.addItem("")
        self.g_pv2.addItem("")
        self.g_pv2.addItem("")
        self.g_pv2.addItem("")
        self.g_pv2.setObjectName(u"g_pv2")
        sizePolicy4.setHeightForWidth(self.g_pv2.sizePolicy().hasHeightForWidth())
        self.g_pv2.setSizePolicy(sizePolicy4)
        self.g_pv2.setMinimumSize(QSize(70, 25))
        self.g_pv2.setMaximumSize(QSize(16777215, 25))

        self.horizontalLayout_31.addWidget(self.g_pv2)

        self.widget_12 = QWidget(self.groupBox_5)
        self.widget_12.setObjectName(u"widget_12")
        sizePolicy1.setHeightForWidth(self.widget_12.sizePolicy().hasHeightForWidth())
        self.widget_12.setSizePolicy(sizePolicy1)
        self.widget_12.setMinimumSize(QSize(300, 0))
        self.layout_pv2 = QHBoxLayout(self.widget_12)
        self.layout_pv2.setObjectName(u"layout_pv2")
        self.layout_pv2.setContentsMargins(0, 0, 0, 0)

        self.horizontalLayout_31.addWidget(self.widget_12)


        self.verticalLayout_6.addLayout(self.horizontalLayout_31)

        self.horizontalLayout_32 = QHBoxLayout()
        self.horizontalLayout_32.setSpacing(10)
        self.horizontalLayout_32.setObjectName(u"horizontalLayout_32")
        self.label_44 = QLabel(self.groupBox_5)
        self.label_44.setObjectName(u"label_44")
        sizePolicy3.setHeightForWidth(self.label_44.sizePolicy().hasHeightForWidth())
        self.label_44.setSizePolicy(sizePolicy3)
        self.label_44.setMinimumSize(QSize(50, 0))
        self.label_44.setMaximumSize(QSize(50, 16777215))

        self.horizontalLayout_32.addWidget(self.label_44)

        self.g_pv3 = QComboBox(self.groupBox_5)
        self.g_pv3.addItem("")
        self.g_pv3.addItem("")
        self.g_pv3.addItem("")
        self.g_pv3.addItem("")
        self.g_pv3.addItem("")
        self.g_pv3.addItem("")
        self.g_pv3.setObjectName(u"g_pv3")
        sizePolicy4.setHeightForWidth(self.g_pv3.sizePolicy().hasHeightForWidth())
        self.g_pv3.setSizePolicy(sizePolicy4)
        self.g_pv3.setMinimumSize(QSize(70, 25))
        self.g_pv3.setMaximumSize(QSize(16777215, 25))

        self.horizontalLayout_32.addWidget(self.g_pv3)

        self.widget_13 = QWidget(self.groupBox_5)
        self.widget_13.setObjectName(u"widget_13")
        sizePolicy1.setHeightForWidth(self.widget_13.sizePolicy().hasHeightForWidth())
        self.widget_13.setSizePolicy(sizePolicy1)
        self.widget_13.setMinimumSize(QSize(300, 0))
        self.layout_pv3 = QHBoxLayout(self.widget_13)
        self.layout_pv3.setObjectName(u"layout_pv3")
        self.layout_pv3.setContentsMargins(0, 0, 0, 0)

        self.horizontalLayout_32.addWidget(self.widget_13)


        self.verticalLayout_6.addLayout(self.horizontalLayout_32)

        self.horizontalLayout_33 = QHBoxLayout()
        self.horizontalLayout_33.setSpacing(10)
        self.horizontalLayout_33.setObjectName(u"horizontalLayout_33")
        self.label_45 = QLabel(self.groupBox_5)
        self.label_45.setObjectName(u"label_45")
        sizePolicy3.setHeightForWidth(self.label_45.sizePolicy().hasHeightForWidth())
        self.label_45.setSizePolicy(sizePolicy3)
        self.label_45.setMinimumSize(QSize(50, 0))
        self.label_45.setMaximumSize(QSize(50, 16777215))

        self.horizontalLayout_33.addWidget(self.label_45)

        self.g_pv4 = QComboBox(self.groupBox_5)
        self.g_pv4.addItem("")
        self.g_pv4.addItem("")
        self.g_pv4.addItem("")
        self.g_pv4.addItem("")
        self.g_pv4.addItem("")
        self.g_pv4.addItem("")
        self.g_pv4.setObjectName(u"g_pv4")
        sizePolicy4.setHeightForWidth(self.g_pv4.sizePolicy().hasHeightForWidth())
        self.g_pv4.setSizePolicy(sizePolicy4)
        self.g_pv4.setMinimumSize(QSize(70, 25))
        self.g_pv4.setMaximumSize(QSize(16777215, 25))

        self.horizontalLayout_33.addWidget(self.g_pv4)

        self.widget_14 = QWidget(self.groupBox_5)
        self.widget_14.setObjectName(u"widget_14")
        sizePolicy1.setHeightForWidth(self.widget_14.sizePolicy().hasHeightForWidth())
        self.widget_14.setSizePolicy(sizePolicy1)
        self.widget_14.setMinimumSize(QSize(300, 0))
        self.layout_pv4 = QHBoxLayout(self.widget_14)
        self.layout_pv4.setObjectName(u"layout_pv4")
        self.layout_pv4.setContentsMargins(0, 0, 0, 0)

        self.horizontalLayout_33.addWidget(self.widget_14)


        self.verticalLayout_6.addLayout(self.horizontalLayout_33)

        self.horizontalLayout_34 = QHBoxLayout()
        self.horizontalLayout_34.setSpacing(10)
        self.horizontalLayout_34.setObjectName(u"horizontalLayout_34")
        self.label_46 = QLabel(self.groupBox_5)
        self.label_46.setObjectName(u"label_46")
        sizePolicy3.setHeightForWidth(self.label_46.sizePolicy().hasHeightForWidth())
        self.label_46.setSizePolicy(sizePolicy3)
        self.label_46.setMinimumSize(QSize(50, 0))
        self.label_46.setMaximumSize(QSize(50, 16777215))

        self.horizontalLayout_34.addWidget(self.label_46)

        self.g_pv5 = QComboBox(self.groupBox_5)
        self.g_pv5.addItem("")
        self.g_pv5.addItem("")
        self.g_pv5.addItem("")
        self.g_pv5.addItem("")
        self.g_pv5.addItem("")
        self.g_pv5.addItem("")
        self.g_pv5.setObjectName(u"g_pv5")
        sizePolicy4.setHeightForWidth(self.g_pv5.sizePolicy().hasHeightForWidth())
        self.g_pv5.setSizePolicy(sizePolicy4)
        self.g_pv5.setMinimumSize(QSize(70, 25))
        self.g_pv5.setMaximumSize(QSize(16777215, 25))

        self.horizontalLayout_34.addWidget(self.g_pv5)

        self.widget_15 = QWidget(self.groupBox_5)
        self.widget_15.setObjectName(u"widget_15")
        sizePolicy1.setHeightForWidth(self.widget_15.sizePolicy().hasHeightForWidth())
        self.widget_15.setSizePolicy(sizePolicy1)
        self.widget_15.setMinimumSize(QSize(300, 0))
        self.layout_pv5 = QHBoxLayout(self.widget_15)
        self.layout_pv5.setObjectName(u"layout_pv5")
        self.layout_pv5.setContentsMargins(0, 0, 0, 0)

        self.horizontalLayout_34.addWidget(self.widget_15)


        self.verticalLayout_6.addLayout(self.horizontalLayout_34)

        self.groupBox_6 = QGroupBox(self.groupBox_5)
        self.groupBox_6.setObjectName(u"groupBox_6")
        sizePolicy2.setHeightForWidth(self.groupBox_6.sizePolicy().hasHeightForWidth())
        self.groupBox_6.setSizePolicy(sizePolicy2)
        self.groupBox_6.setMinimumSize(QSize(0, 300))
        self.layout_graph_matrix = QVBoxLayout(self.groupBox_6)
        self.layout_graph_matrix.setObjectName(u"layout_graph_matrix")

        self.verticalLayout_6.addWidget(self.groupBox_6)


        self.horizontalLayout_13.addWidget(self.groupBox_5)


        self.verticalLayout_7.addLayout(self.horizontalLayout_13)

        self.progressBar = QProgressBar(self.tab_2)
        self.progressBar.setObjectName(u"progressBar")
        self.progressBar.setValue(0)
        self.progressBar.setAlignment(Qt.AlignCenter)

        self.verticalLayout_7.addWidget(self.progressBar)

        self.widget_2 = QWidget(self.tab_2)
        self.widget_2.setObjectName(u"widget_2")
        self.widget_2.setMinimumSize(QSize(0, 50))
        self.horizontalLayout_26 = QHBoxLayout(self.widget_2)
        self.horizontalLayout_26.setSpacing(30)
        self.horizontalLayout_26.setObjectName(u"horizontalLayout_26")
        self.horizontalLayout_26.setContentsMargins(0, 0, 0, 0)
        self.horizontalSpacer_3 = QSpacerItem(323, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_26.addItem(self.horizontalSpacer_3)

        self.btn_start_matrix = QPushButton(self.widget_2)
        self.btn_start_matrix.setObjectName(u"btn_start_matrix")
        self.btn_start_matrix.setMinimumSize(QSize(0, 35))

        self.horizontalLayout_26.addWidget(self.btn_start_matrix)

        self.btn_default = QPushButton(self.widget_2)
        self.btn_default.setObjectName(u"btn_default")
        self.btn_default.setMinimumSize(QSize(0, 35))

        self.horizontalLayout_26.addWidget(self.btn_default)

        self.btn_exit_matrix = QPushButton(self.widget_2)
        self.btn_exit_matrix.setObjectName(u"btn_exit_matrix")
        self.btn_exit_matrix.setMinimumSize(QSize(0, 35))

        self.horizontalLayout_26.addWidget(self.btn_exit_matrix)

        self.horizontalSpacer_4 = QSpacerItem(323, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_26.addItem(self.horizontalSpacer_4)


        self.verticalLayout_7.addWidget(self.widget_2)

        self.tabWidget.addTab(self.tab_2, "")

        self.verticalLayout.addWidget(self.tabWidget)

        TandaPaySimulationWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(TandaPaySimulationWindow)
        self.statusbar.setObjectName(u"statusbar")
        TandaPaySimulationWindow.setStatusBar(self.statusbar)

        self.retranslateUi(TandaPaySimulationWindow)

        self.tabWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(TandaPaySimulationWindow)
    # setupUi

    def retranslateUi(self, TandaPaySimulationWindow):
        TandaPaySimulationWindow.setWindowTitle(QCoreApplication.translate("TandaPaySimulationWindow", u"TandaPay Simulation", None))
        self.label.setText(QCoreApplication.translate("TandaPaySimulationWindow", u"Result Path:", None))
        self.btn_result_path.setText("")
        self.groupBox.setTitle(QCoreApplication.translate("TandaPaySimulationWindow", u"ENVIRONMENTAL VARIABLES", None))
        self.label_4.setText(QCoreApplication.translate("TandaPaySimulationWindow", u"EV1 - Group member number", None))
#if QT_CONFIG(tooltip)
        self.ev_0.setToolTip(QCoreApplication.translate("TandaPaySimulationWindow", u"How many members are in the group?", None))
#endif // QT_CONFIG(tooltip)
        self.label_5.setText(QCoreApplication.translate("TandaPaySimulationWindow", u"EV2 - Average take-home pay for group members", None))
#if QT_CONFIG(tooltip)
        self.ev_1.setToolTip(QCoreApplication.translate("TandaPaySimulationWindow", u"Average take-home pay for group members?", None))
#endif // QT_CONFIG(tooltip)
        self.label_6.setText(QCoreApplication.translate("TandaPaySimulationWindow", u"EV3 - Chance of a claim(%)", None))
#if QT_CONFIG(tooltip)
        self.ev_2.setToolTip(QCoreApplication.translate("TandaPaySimulationWindow", u"What is the chance of a claim each month?", None))
#endif // QT_CONFIG(tooltip)
        self.label_7.setText(QCoreApplication.translate("TandaPaySimulationWindow", u"EV4 - Honest defectors(%)", None))
#if QT_CONFIG(tooltip)
        self.ev_3.setToolTip(QCoreApplication.translate("TandaPaySimulationWindow", u"What is the percentage of honest defectors?", None))
#endif // QT_CONFIG(tooltip)
        self.label_8.setText(QCoreApplication.translate("TandaPaySimulationWindow", u"EV5 - Low-morale members(%)", None))
#if QT_CONFIG(tooltip)
        self.ev_4.setToolTip(QCoreApplication.translate("TandaPaySimulationWindow", u"What is the percentage of low-morale members?", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(tooltip)
        self.label_9.setToolTip(QCoreApplication.translate("TandaPaySimulationWindow", u"What is the percentage of members who are unwilling to act alone? ", None))
#endif // QT_CONFIG(tooltip)
        self.label_9.setText(QCoreApplication.translate("TandaPaySimulationWindow", u"EV6 - Dependent members(%)", None))
#if QT_CONFIG(tooltip)
        self.ev_5.setToolTip(QCoreApplication.translate("TandaPaySimulationWindow", u"What is the percentage of members who are unwilling to act alone?", None))
#endif // QT_CONFIG(tooltip)
        self.label_10.setText(QCoreApplication.translate("TandaPaySimulationWindow", u"EV7 - Dependent member threshold", None))
#if QT_CONFIG(tooltip)
        self.ev_6.setToolTip(QCoreApplication.translate("TandaPaySimulationWindow", u"What is the member threshold needed for dependent members to defect?", None))
#endif // QT_CONFIG(tooltip)
        self.label_11.setText(QCoreApplication.translate("TandaPaySimulationWindow", u"EV8 - Any additional periods?", None))
#if QT_CONFIG(tooltip)
        self.ev_7.setToolTip(QCoreApplication.translate("TandaPaySimulationWindow", u"Once the group stabilizes how many additional periods will there be?", None))
#endif // QT_CONFIG(tooltip)
        self.label_12.setText(QCoreApplication.translate("TandaPaySimulationWindow", u"EV9 - Low-morale quit (%)", None))
#if QT_CONFIG(tooltip)
        self.ev_8.setToolTip(QCoreApplication.translate("TandaPaySimulationWindow", u"Once the group stabilizes how many additional periods will there be?", None))
#endif // QT_CONFIG(tooltip)
        self.groupBox_2.setTitle(QCoreApplication.translate("TandaPaySimulationWindow", u"PRICING VARIABLES", None))
        self.label_13.setText(QCoreApplication.translate("TandaPaySimulationWindow", u"PV1 - Start floor price increase %", None))
#if QT_CONFIG(tooltip)
        self.pv_0.setToolTip(QCoreApplication.translate("TandaPaySimulationWindow", u"The premium price must exceed this minimum threshold", None))
#endif // QT_CONFIG(tooltip)
        self.label_14.setText(QCoreApplication.translate("TandaPaySimulationWindow", u"PV2 - Start floor skip result %", None))
#if QT_CONFIG(tooltip)
        self.pv_1.setToolTip(QCoreApplication.translate("TandaPaySimulationWindow", u"Before this many policyholders decide to leave", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(tooltip)
        self.label_15.setToolTip(QCoreApplication.translate("TandaPaySimulationWindow", u"The maximum premium price increase threshold", None))
#endif // QT_CONFIG(tooltip)
        self.label_15.setText(QCoreApplication.translate("TandaPaySimulationWindow", u"PV3 - End limit price increase %", None))
        self.label_16.setText(QCoreApplication.translate("TandaPaySimulationWindow", u"PV4 - End limit skip result %", None))
#if QT_CONFIG(tooltip)
        self.pv_3.setToolTip(QCoreApplication.translate("TandaPaySimulationWindow", u"Resulting in this percentage of policyholders deciding to leave", None))
#endif // QT_CONFIG(tooltip)
        self.label_17.setText(QCoreApplication.translate("TandaPaySimulationWindow", u"PV5 - Runaway collapse price increase %", None))
#if QT_CONFIG(tooltip)
        self.pv_4.setToolTip(QCoreApplication.translate("TandaPaySimulationWindow", u" If the premium increases beyond this percentage", None))
#endif // QT_CONFIG(tooltip)
        self.label_18.setText(QCoreApplication.translate("TandaPaySimulationWindow", u"PV6 - Runaway collapse skip result %", None))
#if QT_CONFIG(tooltip)
        self.pv_5.setToolTip(QCoreApplication.translate("TandaPaySimulationWindow", u"Then this percentage of policyholders will leave every period", None))
#endif // QT_CONFIG(tooltip)
        self.groupBox_3.setTitle(QCoreApplication.translate("TandaPaySimulationWindow", u"Pricing Graph", None))
        self.btn_start_single.setText(QCoreApplication.translate("TandaPaySimulationWindow", u"Start", None))
        self.btn_exit.setText(QCoreApplication.translate("TandaPaySimulationWindow", u"Exit", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), QCoreApplication.translate("TandaPaySimulationWindow", u"Single Run", None))
        self.groupBox_4.setTitle(QCoreApplication.translate("TandaPaySimulationWindow", u"ENVIRONMENTAL VARIABLES", None))
#if QT_CONFIG(tooltip)
        self.label_32.setToolTip(QCoreApplication.translate("TandaPaySimulationWindow", u"Group member number", None))
#endif // QT_CONFIG(tooltip)
        self.label_32.setText(QCoreApplication.translate("TandaPaySimulationWindow", u"EV1", None))
        self.g_ev0.setItemText(0, QCoreApplication.translate("TandaPaySimulationWindow", u"N/A", None))
        self.g_ev0.setItemText(1, QCoreApplication.translate("TandaPaySimulationWindow", u"1", None))
        self.g_ev0.setItemText(2, QCoreApplication.translate("TandaPaySimulationWindow", u"2", None))
        self.g_ev0.setItemText(3, QCoreApplication.translate("TandaPaySimulationWindow", u"3", None))
        self.g_ev0.setItemText(4, QCoreApplication.translate("TandaPaySimulationWindow", u"4", None))
        self.g_ev0.setItemText(5, QCoreApplication.translate("TandaPaySimulationWindow", u"5", None))

#if QT_CONFIG(tooltip)
        self.g_ev0.setToolTip(QCoreApplication.translate("TandaPaySimulationWindow", u"Group member number", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(tooltip)
        self.widget_3.setToolTip(QCoreApplication.translate("TandaPaySimulationWindow", u"Group member number", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(tooltip)
        self.label_33.setToolTip(QCoreApplication.translate("TandaPaySimulationWindow", u"Chance of a claim", None))
#endif // QT_CONFIG(tooltip)
        self.label_33.setText(QCoreApplication.translate("TandaPaySimulationWindow", u"EV3", None))
        self.g_ev2.setItemText(0, QCoreApplication.translate("TandaPaySimulationWindow", u"N/A", None))
        self.g_ev2.setItemText(1, QCoreApplication.translate("TandaPaySimulationWindow", u"1", None))
        self.g_ev2.setItemText(2, QCoreApplication.translate("TandaPaySimulationWindow", u"2", None))
        self.g_ev2.setItemText(3, QCoreApplication.translate("TandaPaySimulationWindow", u"3", None))
        self.g_ev2.setItemText(4, QCoreApplication.translate("TandaPaySimulationWindow", u"4", None))
        self.g_ev2.setItemText(5, QCoreApplication.translate("TandaPaySimulationWindow", u"5", None))

#if QT_CONFIG(tooltip)
        self.g_ev2.setToolTip(QCoreApplication.translate("TandaPaySimulationWindow", u"Chance of a claim", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(tooltip)
        self.widget_4.setToolTip(QCoreApplication.translate("TandaPaySimulationWindow", u"Chance of a claim", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(tooltip)
        self.label_34.setToolTip(QCoreApplication.translate("TandaPaySimulationWindow", u"Honest defector %", None))
#endif // QT_CONFIG(tooltip)
        self.label_34.setText(QCoreApplication.translate("TandaPaySimulationWindow", u"EV4", None))
        self.g_ev3.setItemText(0, QCoreApplication.translate("TandaPaySimulationWindow", u"N/A", None))
        self.g_ev3.setItemText(1, QCoreApplication.translate("TandaPaySimulationWindow", u"1", None))
        self.g_ev3.setItemText(2, QCoreApplication.translate("TandaPaySimulationWindow", u"2", None))
        self.g_ev3.setItemText(3, QCoreApplication.translate("TandaPaySimulationWindow", u"3", None))
        self.g_ev3.setItemText(4, QCoreApplication.translate("TandaPaySimulationWindow", u"4", None))
        self.g_ev3.setItemText(5, QCoreApplication.translate("TandaPaySimulationWindow", u"5", None))

#if QT_CONFIG(tooltip)
        self.g_ev3.setToolTip(QCoreApplication.translate("TandaPaySimulationWindow", u"Honest defector %", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(tooltip)
        self.widget_5.setToolTip(QCoreApplication.translate("TandaPaySimulationWindow", u"Honest defector %", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(tooltip)
        self.label_35.setToolTip(QCoreApplication.translate("TandaPaySimulationWindow", u"Low-morale %", None))
#endif // QT_CONFIG(tooltip)
        self.label_35.setText(QCoreApplication.translate("TandaPaySimulationWindow", u"EV5", None))
        self.g_ev4.setItemText(0, QCoreApplication.translate("TandaPaySimulationWindow", u"N/A", None))
        self.g_ev4.setItemText(1, QCoreApplication.translate("TandaPaySimulationWindow", u"1", None))
        self.g_ev4.setItemText(2, QCoreApplication.translate("TandaPaySimulationWindow", u"2", None))
        self.g_ev4.setItemText(3, QCoreApplication.translate("TandaPaySimulationWindow", u"3", None))
        self.g_ev4.setItemText(4, QCoreApplication.translate("TandaPaySimulationWindow", u"4", None))
        self.g_ev4.setItemText(5, QCoreApplication.translate("TandaPaySimulationWindow", u"5", None))

#if QT_CONFIG(tooltip)
        self.g_ev4.setToolTip(QCoreApplication.translate("TandaPaySimulationWindow", u"Low-morale %", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(tooltip)
        self.widget_6.setToolTip(QCoreApplication.translate("TandaPaySimulationWindow", u"Low-morale %", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(tooltip)
        self.label_36.setToolTip(QCoreApplication.translate("TandaPaySimulationWindow", u"Dependent members %", None))
#endif // QT_CONFIG(tooltip)
        self.label_36.setText(QCoreApplication.translate("TandaPaySimulationWindow", u"EV6", None))
        self.g_ev5.setItemText(0, QCoreApplication.translate("TandaPaySimulationWindow", u"N/A", None))
        self.g_ev5.setItemText(1, QCoreApplication.translate("TandaPaySimulationWindow", u"1", None))
        self.g_ev5.setItemText(2, QCoreApplication.translate("TandaPaySimulationWindow", u"2", None))
        self.g_ev5.setItemText(3, QCoreApplication.translate("TandaPaySimulationWindow", u"3", None))
        self.g_ev5.setItemText(4, QCoreApplication.translate("TandaPaySimulationWindow", u"4", None))
        self.g_ev5.setItemText(5, QCoreApplication.translate("TandaPaySimulationWindow", u"5", None))

#if QT_CONFIG(tooltip)
        self.g_ev5.setToolTip(QCoreApplication.translate("TandaPaySimulationWindow", u"Dependent members %", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(tooltip)
        self.widget_7.setToolTip(QCoreApplication.translate("TandaPaySimulationWindow", u"Dependent members %", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(tooltip)
        self.label_37.setToolTip(QCoreApplication.translate("TandaPaySimulationWindow", u"Dependent member threshold", None))
#endif // QT_CONFIG(tooltip)
        self.label_37.setText(QCoreApplication.translate("TandaPaySimulationWindow", u"EV7", None))
        self.g_ev6.setItemText(0, QCoreApplication.translate("TandaPaySimulationWindow", u"N/A", None))
        self.g_ev6.setItemText(1, QCoreApplication.translate("TandaPaySimulationWindow", u"1", None))
        self.g_ev6.setItemText(2, QCoreApplication.translate("TandaPaySimulationWindow", u"2", None))
        self.g_ev6.setItemText(3, QCoreApplication.translate("TandaPaySimulationWindow", u"3", None))

#if QT_CONFIG(tooltip)
        self.g_ev6.setToolTip(QCoreApplication.translate("TandaPaySimulationWindow", u"Dependent member threshold", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(tooltip)
        self.widget_8.setToolTip(QCoreApplication.translate("TandaPaySimulationWindow", u"Dependent member threshold", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(tooltip)
        self.label_38.setToolTip(QCoreApplication.translate("TandaPaySimulationWindow", u"Any additional periods?\n"
"", None))
#endif // QT_CONFIG(tooltip)
        self.label_38.setText(QCoreApplication.translate("TandaPaySimulationWindow", u"EV8", None))
        self.g_ev7.setItemText(0, QCoreApplication.translate("TandaPaySimulationWindow", u"N/A", None))
        self.g_ev7.setItemText(1, QCoreApplication.translate("TandaPaySimulationWindow", u"1", None))
        self.g_ev7.setItemText(2, QCoreApplication.translate("TandaPaySimulationWindow", u"2", None))
        self.g_ev7.setItemText(3, QCoreApplication.translate("TandaPaySimulationWindow", u"3", None))
        self.g_ev7.setItemText(4, QCoreApplication.translate("TandaPaySimulationWindow", u"4", None))
        self.g_ev7.setItemText(5, QCoreApplication.translate("TandaPaySimulationWindow", u"5", None))

#if QT_CONFIG(tooltip)
        self.g_ev7.setToolTip(QCoreApplication.translate("TandaPaySimulationWindow", u"Any additional periods?\n"
"", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(tooltip)
        self.widget_9.setToolTip(QCoreApplication.translate("TandaPaySimulationWindow", u"Any additional periods?\n"
"", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(tooltip)
        self.label_39.setToolTip(QCoreApplication.translate("TandaPaySimulationWindow", u"Low-morale quit %", None))
#endif // QT_CONFIG(tooltip)
        self.label_39.setText(QCoreApplication.translate("TandaPaySimulationWindow", u"EV9", None))
        self.groupBox_5.setTitle(QCoreApplication.translate("TandaPaySimulationWindow", u"PRICING VARIABLES", None))
#if QT_CONFIG(tooltip)
        self.label_41.setToolTip(QCoreApplication.translate("TandaPaySimulationWindow", u"Start floor price increase %", None))
#endif // QT_CONFIG(tooltip)
        self.label_41.setText(QCoreApplication.translate("TandaPaySimulationWindow", u"PV1", None))
        self.g_pv0.setItemText(0, QCoreApplication.translate("TandaPaySimulationWindow", u"N/A", None))
        self.g_pv0.setItemText(1, QCoreApplication.translate("TandaPaySimulationWindow", u"1", None))
        self.g_pv0.setItemText(2, QCoreApplication.translate("TandaPaySimulationWindow", u"2", None))
        self.g_pv0.setItemText(3, QCoreApplication.translate("TandaPaySimulationWindow", u"3", None))
        self.g_pv0.setItemText(4, QCoreApplication.translate("TandaPaySimulationWindow", u"4", None))
        self.g_pv0.setItemText(5, QCoreApplication.translate("TandaPaySimulationWindow", u"5", None))

#if QT_CONFIG(tooltip)
        self.g_pv0.setToolTip(QCoreApplication.translate("TandaPaySimulationWindow", u"Start floor price increase %", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(tooltip)
        self.widget_10.setToolTip(QCoreApplication.translate("TandaPaySimulationWindow", u"Start floor price increase %", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(tooltip)
        self.label_42.setToolTip(QCoreApplication.translate("TandaPaySimulationWindow", u"Start floor skip result %", None))
#endif // QT_CONFIG(tooltip)
        self.label_42.setText(QCoreApplication.translate("TandaPaySimulationWindow", u"PV2", None))
        self.g_pv1.setItemText(0, QCoreApplication.translate("TandaPaySimulationWindow", u"N/A", None))
        self.g_pv1.setItemText(1, QCoreApplication.translate("TandaPaySimulationWindow", u"1", None))
        self.g_pv1.setItemText(2, QCoreApplication.translate("TandaPaySimulationWindow", u"2", None))
        self.g_pv1.setItemText(3, QCoreApplication.translate("TandaPaySimulationWindow", u"3", None))
        self.g_pv1.setItemText(4, QCoreApplication.translate("TandaPaySimulationWindow", u"4", None))
        self.g_pv1.setItemText(5, QCoreApplication.translate("TandaPaySimulationWindow", u"5", None))

#if QT_CONFIG(tooltip)
        self.g_pv1.setToolTip(QCoreApplication.translate("TandaPaySimulationWindow", u"Start floor skip result %", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(tooltip)
        self.widget_11.setToolTip(QCoreApplication.translate("TandaPaySimulationWindow", u"Start floor skip result %", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(tooltip)
        self.label_43.setToolTip(QCoreApplication.translate("TandaPaySimulationWindow", u"End limit price increase %", None))
#endif // QT_CONFIG(tooltip)
        self.label_43.setText(QCoreApplication.translate("TandaPaySimulationWindow", u"PV3", None))
        self.g_pv2.setItemText(0, QCoreApplication.translate("TandaPaySimulationWindow", u"N/A", None))
        self.g_pv2.setItemText(1, QCoreApplication.translate("TandaPaySimulationWindow", u"1", None))
        self.g_pv2.setItemText(2, QCoreApplication.translate("TandaPaySimulationWindow", u"2", None))
        self.g_pv2.setItemText(3, QCoreApplication.translate("TandaPaySimulationWindow", u"3", None))
        self.g_pv2.setItemText(4, QCoreApplication.translate("TandaPaySimulationWindow", u"4", None))
        self.g_pv2.setItemText(5, QCoreApplication.translate("TandaPaySimulationWindow", u"5", None))

#if QT_CONFIG(tooltip)
        self.g_pv2.setToolTip(QCoreApplication.translate("TandaPaySimulationWindow", u"End limit price increase %", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(tooltip)
        self.widget_12.setToolTip(QCoreApplication.translate("TandaPaySimulationWindow", u"End limit price increase %", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(tooltip)
        self.label_44.setToolTip(QCoreApplication.translate("TandaPaySimulationWindow", u"End limit skip result %", None))
#endif // QT_CONFIG(tooltip)
        self.label_44.setText(QCoreApplication.translate("TandaPaySimulationWindow", u"PV4", None))
        self.g_pv3.setItemText(0, QCoreApplication.translate("TandaPaySimulationWindow", u"N/A", None))
        self.g_pv3.setItemText(1, QCoreApplication.translate("TandaPaySimulationWindow", u"1", None))
        self.g_pv3.setItemText(2, QCoreApplication.translate("TandaPaySimulationWindow", u"2", None))
        self.g_pv3.setItemText(3, QCoreApplication.translate("TandaPaySimulationWindow", u"3", None))
        self.g_pv3.setItemText(4, QCoreApplication.translate("TandaPaySimulationWindow", u"4", None))
        self.g_pv3.setItemText(5, QCoreApplication.translate("TandaPaySimulationWindow", u"5", None))

#if QT_CONFIG(tooltip)
        self.g_pv3.setToolTip(QCoreApplication.translate("TandaPaySimulationWindow", u"End limit skip result %", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(tooltip)
        self.widget_13.setToolTip(QCoreApplication.translate("TandaPaySimulationWindow", u"End limit skip result %", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(tooltip)
        self.label_45.setToolTip(QCoreApplication.translate("TandaPaySimulationWindow", u"Runaway collapse price increase %", None))
#endif // QT_CONFIG(tooltip)
        self.label_45.setText(QCoreApplication.translate("TandaPaySimulationWindow", u"PV5", None))
        self.g_pv4.setItemText(0, QCoreApplication.translate("TandaPaySimulationWindow", u"N/A", None))
        self.g_pv4.setItemText(1, QCoreApplication.translate("TandaPaySimulationWindow", u"1", None))
        self.g_pv4.setItemText(2, QCoreApplication.translate("TandaPaySimulationWindow", u"2", None))
        self.g_pv4.setItemText(3, QCoreApplication.translate("TandaPaySimulationWindow", u"3", None))
        self.g_pv4.setItemText(4, QCoreApplication.translate("TandaPaySimulationWindow", u"4", None))
        self.g_pv4.setItemText(5, QCoreApplication.translate("TandaPaySimulationWindow", u"5", None))

#if QT_CONFIG(tooltip)
        self.g_pv4.setToolTip(QCoreApplication.translate("TandaPaySimulationWindow", u"Runaway collapse price increase %", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(tooltip)
        self.widget_14.setToolTip(QCoreApplication.translate("TandaPaySimulationWindow", u"Runaway collapse price increase %", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(tooltip)
        self.label_46.setToolTip(QCoreApplication.translate("TandaPaySimulationWindow", u"Runaway collapse skip result %", None))
#endif // QT_CONFIG(tooltip)
        self.label_46.setText(QCoreApplication.translate("TandaPaySimulationWindow", u"PV6", None))
        self.g_pv5.setItemText(0, QCoreApplication.translate("TandaPaySimulationWindow", u"N/A", None))
        self.g_pv5.setItemText(1, QCoreApplication.translate("TandaPaySimulationWindow", u"1", None))
        self.g_pv5.setItemText(2, QCoreApplication.translate("TandaPaySimulationWindow", u"2", None))
        self.g_pv5.setItemText(3, QCoreApplication.translate("TandaPaySimulationWindow", u"3", None))
        self.g_pv5.setItemText(4, QCoreApplication.translate("TandaPaySimulationWindow", u"4", None))
        self.g_pv5.setItemText(5, QCoreApplication.translate("TandaPaySimulationWindow", u"5", None))

#if QT_CONFIG(tooltip)
        self.g_pv5.setToolTip(QCoreApplication.translate("TandaPaySimulationWindow", u"Runaway collapse skip result %", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(tooltip)
        self.widget_15.setToolTip(QCoreApplication.translate("TandaPaySimulationWindow", u"Runaway collapse skip result %", None))
#endif // QT_CONFIG(tooltip)
        self.groupBox_6.setTitle(QCoreApplication.translate("TandaPaySimulationWindow", u"Pricing Graph", None))
        self.btn_start_matrix.setText(QCoreApplication.translate("TandaPaySimulationWindow", u"Start", None))
        self.btn_default.setText(QCoreApplication.translate("TandaPaySimulationWindow", u"Default", None))
        self.btn_exit_matrix.setText(QCoreApplication.translate("TandaPaySimulationWindow", u"Exit", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), QCoreApplication.translate("TandaPaySimulationWindow", u"Matrix Run", None))
    # retranslateUi

