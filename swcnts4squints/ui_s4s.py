# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'swcnts4squints2.ui'
#
# Created: Tue Sep 24 01:22:15 2013
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

class Ui_S4S(object):
    def setupUi(self, S4S):
        S4S.setObjectName(_fromUtf8("S4S"))
        S4S.resize(815, 537)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(S4S.sizePolicy().hasHeightForWidth())
        S4S.setSizePolicy(sizePolicy)
        self.centralwidget = QtGui.QWidget(S4S)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.verticalLayout_7 = QtGui.QVBoxLayout(self.centralwidget)
        self.verticalLayout_7.setObjectName(_fromUtf8("verticalLayout_7"))
        self.stackedWidget = QtGui.QStackedWidget(self.centralwidget)
        self.stackedWidget.setObjectName(_fromUtf8("stackedWidget"))
        self.stackedWidgetPage1 = QtGui.QWidget()
        self.stackedWidgetPage1.setObjectName(_fromUtf8("stackedWidgetPage1"))
        self.verticalLayout_6 = QtGui.QVBoxLayout(self.stackedWidgetPage1)
        self.verticalLayout_6.setObjectName(_fromUtf8("verticalLayout_6"))
        self.horizontalLayout_26 = QtGui.QHBoxLayout()
        self.horizontalLayout_26.setObjectName(_fromUtf8("horizontalLayout_26"))
        self.horizontalLayout_17 = QtGui.QHBoxLayout()
        self.horizontalLayout_17.setObjectName(_fromUtf8("horizontalLayout_17"))
        self.verticalLayout_4 = QtGui.QVBoxLayout()
        self.verticalLayout_4.setObjectName(_fromUtf8("verticalLayout_4"))
        self.horizontalLayout_4 = QtGui.QHBoxLayout()
        self.horizontalLayout_4.setObjectName(_fromUtf8("horizontalLayout_4"))
        self.label = QtGui.QLabel(self.stackedWidgetPage1)
        font = QtGui.QFont()
        font.setPointSize(25)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label.setObjectName(_fromUtf8("label"))
        self.horizontalLayout_4.addWidget(self.label)
        self.n_spinBox = QtGui.QSpinBox(self.stackedWidgetPage1)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.n_spinBox.sizePolicy().hasHeightForWidth())
        self.n_spinBox.setSizePolicy(sizePolicy)
        self.n_spinBox.setMinimumSize(QtCore.QSize(65, 35))
        self.n_spinBox.setMaximumSize(QtCore.QSize(65, 35))
        font = QtGui.QFont()
        font.setPointSize(25)
        self.n_spinBox.setFont(font)
        self.n_spinBox.setProperty("value", 10)
        self.n_spinBox.setObjectName(_fromUtf8("n_spinBox"))
        self.horizontalLayout_4.addWidget(self.n_spinBox)
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem)
        self.label_2 = QtGui.QLabel(self.stackedWidgetPage1)
        font = QtGui.QFont()
        font.setPointSize(25)
        self.label_2.setFont(font)
        self.label_2.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label_2.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.horizontalLayout_4.addWidget(self.label_2)
        self.m_spinBox = QtGui.QSpinBox(self.stackedWidgetPage1)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.m_spinBox.sizePolicy().hasHeightForWidth())
        self.m_spinBox.setSizePolicy(sizePolicy)
        self.m_spinBox.setMinimumSize(QtCore.QSize(65, 35))
        self.m_spinBox.setMaximumSize(QtCore.QSize(65, 35))
        font = QtGui.QFont()
        font.setPointSize(25)
        self.m_spinBox.setFont(font)
        self.m_spinBox.setObjectName(_fromUtf8("m_spinBox"))
        self.horizontalLayout_4.addWidget(self.m_spinBox)
        spacerItem1 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem1)
        self.verticalLayout_4.addLayout(self.horizontalLayout_4)
        self.verticalLayout_2 = QtGui.QVBoxLayout()
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.label_12 = QtGui.QLabel(self.stackedWidgetPage1)
        self.label_12.setMinimumSize(QtCore.QSize(0, 40))
        self.label_12.setMaximumSize(QtCore.QSize(350, 40))
        font = QtGui.QFont()
        font.setPointSize(25)
        self.label_12.setFont(font)
        self.label_12.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_12.setObjectName(_fromUtf8("label_12"))
        self.verticalLayout_2.addWidget(self.label_12)
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.Nz_unit_cells_doubleSpinBox = QtGui.QDoubleSpinBox(self.stackedWidgetPage1)
        self.Nz_unit_cells_doubleSpinBox.setMinimumSize(QtCore.QSize(200, 35))
        self.Nz_unit_cells_doubleSpinBox.setMaximumSize(QtCore.QSize(200, 35))
        font = QtGui.QFont()
        font.setPointSize(25)
        self.Nz_unit_cells_doubleSpinBox.setFont(font)
        self.Nz_unit_cells_doubleSpinBox.setMinimum(0.01)
        self.Nz_unit_cells_doubleSpinBox.setMaximum(9999.0)
        self.Nz_unit_cells_doubleSpinBox.setProperty("value", 10.0)
        self.Nz_unit_cells_doubleSpinBox.setObjectName(_fromUtf8("Nz_unit_cells_doubleSpinBox"))
        self.horizontalLayout.addWidget(self.Nz_unit_cells_doubleSpinBox)
        spacerItem2 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem2)
        self.verticalLayout_2.addLayout(self.horizontalLayout)
        self.verticalLayout_4.addLayout(self.verticalLayout_2)
        self.verticalLayout_3 = QtGui.QVBoxLayout()
        self.verticalLayout_3.setObjectName(_fromUtf8("verticalLayout_3"))
        self.tubeLengthLabel = QtGui.QLabel(self.stackedWidgetPage1)
        self.tubeLengthLabel.setMinimumSize(QtCore.QSize(256, 40))
        self.tubeLengthLabel.setMaximumSize(QtCore.QSize(350, 40))
        font = QtGui.QFont()
        font.setPointSize(25)
        self.tubeLengthLabel.setFont(font)
        self.tubeLengthLabel.setScaledContents(False)
        self.tubeLengthLabel.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.tubeLengthLabel.setObjectName(_fromUtf8("tubeLengthLabel"))
        self.verticalLayout_3.addWidget(self.tubeLengthLabel)
        self.horizontalLayout_3 = QtGui.QHBoxLayout()
        self.horizontalLayout_3.setObjectName(_fromUtf8("horizontalLayout_3"))
        self.L_lineEdit = QtGui.QLineEdit(self.stackedWidgetPage1)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.L_lineEdit.sizePolicy().hasHeightForWidth())
        self.L_lineEdit.setSizePolicy(sizePolicy)
        self.L_lineEdit.setMinimumSize(QtCore.QSize(200, 35))
        self.L_lineEdit.setMaximumSize(QtCore.QSize(200, 35))
        font = QtGui.QFont()
        font.setPointSize(25)
        self.L_lineEdit.setFont(font)
        self.L_lineEdit.setPlaceholderText(_fromUtf8(""))
        self.L_lineEdit.setObjectName(_fromUtf8("L_lineEdit"))
        self.horizontalLayout_3.addWidget(self.L_lineEdit)
        spacerItem3 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem3)
        self.verticalLayout_3.addLayout(self.horizontalLayout_3)
        self.verticalLayout_4.addLayout(self.verticalLayout_3)
        self.verticalLayout = QtGui.QVBoxLayout()
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.label_3 = QtGui.QLabel(self.stackedWidgetPage1)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.MinimumExpanding, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_3.sizePolicy().hasHeightForWidth())
        self.label_3.setSizePolicy(sizePolicy)
        self.label_3.setMinimumSize(QtCore.QSize(0, 40))
        self.label_3.setMaximumSize(QtCore.QSize(350, 40))
        font = QtGui.QFont()
        font.setPointSize(25)
        self.label_3.setFont(font)
        self.label_3.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.verticalLayout.addWidget(self.label_3)
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.ccbond_doubleSpinBox = QtGui.QDoubleSpinBox(self.stackedWidgetPage1)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.MinimumExpanding, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.ccbond_doubleSpinBox.sizePolicy().hasHeightForWidth())
        self.ccbond_doubleSpinBox.setSizePolicy(sizePolicy)
        self.ccbond_doubleSpinBox.setMinimumSize(QtCore.QSize(150, 35))
        self.ccbond_doubleSpinBox.setMaximumSize(QtCore.QSize(175, 35))
        font = QtGui.QFont()
        font.setPointSize(25)
        self.ccbond_doubleSpinBox.setFont(font)
        self.ccbond_doubleSpinBox.setDecimals(4)
        self.ccbond_doubleSpinBox.setMinimum(0.0001)
        self.ccbond_doubleSpinBox.setSingleStep(0.0001)
        self.ccbond_doubleSpinBox.setProperty("value", 1.421)
        self.ccbond_doubleSpinBox.setObjectName(_fromUtf8("ccbond_doubleSpinBox"))
        self.horizontalLayout_2.addWidget(self.ccbond_doubleSpinBox)
        spacerItem4 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem4)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.verticalLayout_4.addLayout(self.verticalLayout)
        self.horizontalLayout_17.addLayout(self.verticalLayout_4)
        self.line_2 = QtGui.QFrame(self.stackedWidgetPage1)
        self.line_2.setFrameShape(QtGui.QFrame.VLine)
        self.line_2.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_2.setObjectName(_fromUtf8("line_2"))
        self.horizontalLayout_17.addWidget(self.line_2)
        self.verticalLayout_5 = QtGui.QVBoxLayout()
        self.verticalLayout_5.setObjectName(_fromUtf8("verticalLayout_5"))
        self.horizontalLayout_11 = QtGui.QHBoxLayout()
        self.horizontalLayout_11.setObjectName(_fromUtf8("horizontalLayout_11"))
        self.label_4 = QtGui.QLabel(self.stackedWidgetPage1)
        font = QtGui.QFont()
        font.setPointSize(20)
        self.label_4.setFont(font)
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.horizontalLayout_11.addWidget(self.label_4)
        self.Ch_lineEdit = QtGui.QLineEdit(self.stackedWidgetPage1)
        self.Ch_lineEdit.setMaximumSize(QtCore.QSize(125, 16777215))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.Ch_lineEdit.setFont(font)
        self.Ch_lineEdit.setAcceptDrops(False)
        self.Ch_lineEdit.setFrame(False)
        self.Ch_lineEdit.setReadOnly(True)
        self.Ch_lineEdit.setObjectName(_fromUtf8("Ch_lineEdit"))
        self.horizontalLayout_11.addWidget(self.Ch_lineEdit)
        self.label_8 = QtGui.QLabel(self.stackedWidgetPage1)
        font = QtGui.QFont()
        font.setPointSize(20)
        self.label_8.setFont(font)
        self.label_8.setObjectName(_fromUtf8("label_8"))
        self.horizontalLayout_11.addWidget(self.label_8)
        spacerItem5 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_11.addItem(spacerItem5)
        self.verticalLayout_5.addLayout(self.horizontalLayout_11)
        self.horizontalLayout_12 = QtGui.QHBoxLayout()
        self.horizontalLayout_12.setObjectName(_fromUtf8("horizontalLayout_12"))
        self.label_5 = QtGui.QLabel(self.stackedWidgetPage1)
        font = QtGui.QFont()
        font.setPointSize(20)
        self.label_5.setFont(font)
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.horizontalLayout_12.addWidget(self.label_5)
        self.dt_lineEdit = QtGui.QLineEdit(self.stackedWidgetPage1)
        self.dt_lineEdit.setMaximumSize(QtCore.QSize(125, 16777215))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.dt_lineEdit.setFont(font)
        self.dt_lineEdit.setAcceptDrops(False)
        self.dt_lineEdit.setFrame(False)
        self.dt_lineEdit.setReadOnly(True)
        self.dt_lineEdit.setObjectName(_fromUtf8("dt_lineEdit"))
        self.horizontalLayout_12.addWidget(self.dt_lineEdit)
        self.label_14 = QtGui.QLabel(self.stackedWidgetPage1)
        font = QtGui.QFont()
        font.setPointSize(20)
        self.label_14.setFont(font)
        self.label_14.setObjectName(_fromUtf8("label_14"))
        self.horizontalLayout_12.addWidget(self.label_14)
        spacerItem6 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_12.addItem(spacerItem6)
        self.verticalLayout_5.addLayout(self.horizontalLayout_12)
        self.horizontalLayout_13 = QtGui.QHBoxLayout()
        self.horizontalLayout_13.setObjectName(_fromUtf8("horizontalLayout_13"))
        self.label_7 = QtGui.QLabel(self.stackedWidgetPage1)
        font = QtGui.QFont()
        font.setPointSize(20)
        self.label_7.setFont(font)
        self.label_7.setObjectName(_fromUtf8("label_7"))
        self.horizontalLayout_13.addWidget(self.label_7)
        self.T_lineEdit = QtGui.QLineEdit(self.stackedWidgetPage1)
        self.T_lineEdit.setMaximumSize(QtCore.QSize(125, 16777215))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.T_lineEdit.setFont(font)
        self.T_lineEdit.setAcceptDrops(False)
        self.T_lineEdit.setFrame(False)
        self.T_lineEdit.setReadOnly(True)
        self.T_lineEdit.setObjectName(_fromUtf8("T_lineEdit"))
        self.horizontalLayout_13.addWidget(self.T_lineEdit)
        self.label_13 = QtGui.QLabel(self.stackedWidgetPage1)
        font = QtGui.QFont()
        font.setPointSize(20)
        self.label_13.setFont(font)
        self.label_13.setObjectName(_fromUtf8("label_13"))
        self.horizontalLayout_13.addWidget(self.label_13)
        spacerItem7 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_13.addItem(spacerItem7)
        self.verticalLayout_5.addLayout(self.horizontalLayout_13)
        self.horizontalLayout_14 = QtGui.QHBoxLayout()
        self.horizontalLayout_14.setObjectName(_fromUtf8("horizontalLayout_14"))
        self.chiral_angle_var_label = QtGui.QLabel(self.stackedWidgetPage1)
        font = QtGui.QFont()
        font.setPointSize(20)
        self.chiral_angle_var_label.setFont(font)
        self.chiral_angle_var_label.setTextFormat(QtCore.Qt.AutoText)
        self.chiral_angle_var_label.setObjectName(_fromUtf8("chiral_angle_var_label"))
        self.horizontalLayout_14.addWidget(self.chiral_angle_var_label)
        self.chiral_angle_lineEdit = QtGui.QLineEdit(self.stackedWidgetPage1)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.chiral_angle_lineEdit.sizePolicy().hasHeightForWidth())
        self.chiral_angle_lineEdit.setSizePolicy(sizePolicy)
        self.chiral_angle_lineEdit.setMaximumSize(QtCore.QSize(125, 16777215))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.chiral_angle_lineEdit.setFont(font)
        self.chiral_angle_lineEdit.setAcceptDrops(False)
        self.chiral_angle_lineEdit.setText(_fromUtf8(""))
        self.chiral_angle_lineEdit.setFrame(False)
        self.chiral_angle_lineEdit.setReadOnly(True)
        self.chiral_angle_lineEdit.setObjectName(_fromUtf8("chiral_angle_lineEdit"))
        self.horizontalLayout_14.addWidget(self.chiral_angle_lineEdit)
        self.chiral_angle_units_label = QtGui.QLabel(self.stackedWidgetPage1)
        font = QtGui.QFont()
        font.setPointSize(20)
        self.chiral_angle_units_label.setFont(font)
        self.chiral_angle_units_label.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.chiral_angle_units_label.setObjectName(_fromUtf8("chiral_angle_units_label"))
        self.horizontalLayout_14.addWidget(self.chiral_angle_units_label)
        spacerItem8 = QtGui.QSpacerItem(13, 17, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_14.addItem(spacerItem8)
        self.verticalLayout_5.addLayout(self.horizontalLayout_14)
        self.horizontalLayout_6 = QtGui.QHBoxLayout()
        self.horizontalLayout_6.setObjectName(_fromUtf8("horizontalLayout_6"))
        self.label_6 = QtGui.QLabel(self.stackedWidgetPage1)
        font = QtGui.QFont()
        font.setPointSize(20)
        self.label_6.setFont(font)
        self.label_6.setObjectName(_fromUtf8("label_6"))
        self.horizontalLayout_6.addWidget(self.label_6)
        self.Natoms_per_cell_lineEdit = QtGui.QLineEdit(self.stackedWidgetPage1)
        self.Natoms_per_cell_lineEdit.setMaximumSize(QtCore.QSize(100, 16777215))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.Natoms_per_cell_lineEdit.setFont(font)
        self.Natoms_per_cell_lineEdit.setAcceptDrops(False)
        self.Natoms_per_cell_lineEdit.setFrame(False)
        self.Natoms_per_cell_lineEdit.setReadOnly(True)
        self.Natoms_per_cell_lineEdit.setObjectName(_fromUtf8("Natoms_per_cell_lineEdit"))
        self.horizontalLayout_6.addWidget(self.Natoms_per_cell_lineEdit)
        spacerItem9 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_6.addItem(spacerItem9)
        self.verticalLayout_5.addLayout(self.horizontalLayout_6)
        self.horizontalLayout_5 = QtGui.QHBoxLayout()
        self.horizontalLayout_5.setObjectName(_fromUtf8("horizontalLayout_5"))
        self.label_9 = QtGui.QLabel(self.stackedWidgetPage1)
        font = QtGui.QFont()
        font.setPointSize(20)
        self.label_9.setFont(font)
        self.label_9.setObjectName(_fromUtf8("label_9"))
        self.horizontalLayout_5.addWidget(self.label_9)
        self.Natoms_per_tube_lineEdit = QtGui.QLineEdit(self.stackedWidgetPage1)
        self.Natoms_per_tube_lineEdit.setMaximumSize(QtCore.QSize(100, 16777215))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.Natoms_per_tube_lineEdit.setFont(font)
        self.Natoms_per_tube_lineEdit.setAcceptDrops(False)
        self.Natoms_per_tube_lineEdit.setFrame(False)
        self.Natoms_per_tube_lineEdit.setReadOnly(True)
        self.Natoms_per_tube_lineEdit.setObjectName(_fromUtf8("Natoms_per_tube_lineEdit"))
        self.horizontalLayout_5.addWidget(self.Natoms_per_tube_lineEdit)
        spacerItem10 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_5.addItem(spacerItem10)
        self.verticalLayout_5.addLayout(self.horizontalLayout_5)
        self.horizontalLayout_15 = QtGui.QHBoxLayout()
        self.horizontalLayout_15.setObjectName(_fromUtf8("horizontalLayout_15"))
        self.mass_var_label = QtGui.QLabel(self.stackedWidgetPage1)
        font = QtGui.QFont()
        font.setPointSize(20)
        self.mass_var_label.setFont(font)
        self.mass_var_label.setObjectName(_fromUtf8("mass_var_label"))
        self.horizontalLayout_15.addWidget(self.mass_var_label)
        self.mass_lineEdit = QtGui.QLineEdit(self.stackedWidgetPage1)
        self.mass_lineEdit.setMaximumSize(QtCore.QSize(150, 16777215))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.mass_lineEdit.setFont(font)
        self.mass_lineEdit.setAcceptDrops(False)
        self.mass_lineEdit.setFrame(False)
        self.mass_lineEdit.setReadOnly(True)
        self.mass_lineEdit.setObjectName(_fromUtf8("mass_lineEdit"))
        self.horizontalLayout_15.addWidget(self.mass_lineEdit)
        self.mass_units_label = QtGui.QLabel(self.stackedWidgetPage1)
        font = QtGui.QFont()
        font.setPointSize(20)
        self.mass_units_label.setFont(font)
        self.mass_units_label.setObjectName(_fromUtf8("mass_units_label"))
        self.horizontalLayout_15.addWidget(self.mass_units_label)
        spacerItem11 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_15.addItem(spacerItem11)
        self.verticalLayout_5.addLayout(self.horizontalLayout_15)
        self.horizontalLayout_16 = QtGui.QHBoxLayout()
        self.horizontalLayout_16.setObjectName(_fromUtf8("horizontalLayout_16"))
        self.density_var_label = QtGui.QLabel(self.stackedWidgetPage1)
        font = QtGui.QFont()
        font.setPointSize(20)
        self.density_var_label.setFont(font)
        self.density_var_label.setObjectName(_fromUtf8("density_var_label"))
        self.horizontalLayout_16.addWidget(self.density_var_label)
        self.density_lineEdit = QtGui.QLineEdit(self.stackedWidgetPage1)
        self.density_lineEdit.setMaximumSize(QtCore.QSize(150, 16777215))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.density_lineEdit.setFont(font)
        self.density_lineEdit.setAcceptDrops(False)
        self.density_lineEdit.setFrame(False)
        self.density_lineEdit.setReadOnly(True)
        self.density_lineEdit.setObjectName(_fromUtf8("density_lineEdit"))
        self.horizontalLayout_16.addWidget(self.density_lineEdit)
        self.density_units_label = QtGui.QLabel(self.stackedWidgetPage1)
        font = QtGui.QFont()
        font.setPointSize(20)
        self.density_units_label.setFont(font)
        self.density_units_label.setObjectName(_fromUtf8("density_units_label"))
        self.horizontalLayout_16.addWidget(self.density_units_label)
        spacerItem12 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_16.addItem(spacerItem12)
        self.verticalLayout_5.addLayout(self.horizontalLayout_16)
        self.horizontalLayout_17.addLayout(self.verticalLayout_5)
        self.horizontalLayout_26.addLayout(self.horizontalLayout_17)
        spacerItem13 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_26.addItem(spacerItem13)
        self.verticalLayout_6.addLayout(self.horizontalLayout_26)
        self.line = QtGui.QFrame(self.stackedWidgetPage1)
        self.line.setFrameShape(QtGui.QFrame.HLine)
        self.line.setFrameShadow(QtGui.QFrame.Sunken)
        self.line.setObjectName(_fromUtf8("line"))
        self.verticalLayout_6.addWidget(self.line)
        self.horizontalLayout_25 = QtGui.QHBoxLayout()
        self.horizontalLayout_25.setObjectName(_fromUtf8("horizontalLayout_25"))
        self.horizontalLayout_19 = QtGui.QHBoxLayout()
        self.horizontalLayout_19.setObjectName(_fromUtf8("horizontalLayout_19"))
        self.horizontalLayout_10 = QtGui.QHBoxLayout()
        self.horizontalLayout_10.setObjectName(_fromUtf8("horizontalLayout_10"))
        self.label_18 = QtGui.QLabel(self.stackedWidgetPage1)
        font = QtGui.QFont()
        font.setPointSize(20)
        self.label_18.setFont(font)
        self.label_18.setObjectName(_fromUtf8("label_18"))
        self.horizontalLayout_10.addWidget(self.label_18)
        self.d_lineEdit = QtGui.QLineEdit(self.stackedWidgetPage1)
        self.d_lineEdit.setMaximumSize(QtCore.QSize(50, 16777215))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.d_lineEdit.setFont(font)
        self.d_lineEdit.setAcceptDrops(False)
        self.d_lineEdit.setFrame(False)
        self.d_lineEdit.setReadOnly(True)
        self.d_lineEdit.setObjectName(_fromUtf8("d_lineEdit"))
        self.horizontalLayout_10.addWidget(self.d_lineEdit)
        spacerItem14 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_10.addItem(spacerItem14)
        self.horizontalLayout_19.addLayout(self.horizontalLayout_10)
        self.horizontalLayout_9 = QtGui.QHBoxLayout()
        self.horizontalLayout_9.setObjectName(_fromUtf8("horizontalLayout_9"))
        self.label_17 = QtGui.QLabel(self.stackedWidgetPage1)
        font = QtGui.QFont()
        font.setPointSize(20)
        self.label_17.setFont(font)
        self.label_17.setObjectName(_fromUtf8("label_17"))
        self.horizontalLayout_9.addWidget(self.label_17)
        self.dR_lineEdit = QtGui.QLineEdit(self.stackedWidgetPage1)
        self.dR_lineEdit.setMaximumSize(QtCore.QSize(50, 16777215))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.dR_lineEdit.setFont(font)
        self.dR_lineEdit.setAcceptDrops(False)
        self.dR_lineEdit.setFrame(False)
        self.dR_lineEdit.setReadOnly(True)
        self.dR_lineEdit.setObjectName(_fromUtf8("dR_lineEdit"))
        self.horizontalLayout_9.addWidget(self.dR_lineEdit)
        spacerItem15 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_9.addItem(spacerItem15)
        self.horizontalLayout_19.addLayout(self.horizontalLayout_9)
        self.horizontalLayout_25.addLayout(self.horizontalLayout_19)
        self.horizontalLayout_18 = QtGui.QHBoxLayout()
        self.horizontalLayout_18.setObjectName(_fromUtf8("horizontalLayout_18"))
        self.horizontalLayout_7 = QtGui.QHBoxLayout()
        self.horizontalLayout_7.setObjectName(_fromUtf8("horizontalLayout_7"))
        self.label_19 = QtGui.QLabel(self.stackedWidgetPage1)
        font = QtGui.QFont()
        font.setPointSize(20)
        self.label_19.setFont(font)
        self.label_19.setObjectName(_fromUtf8("label_19"))
        self.horizontalLayout_7.addWidget(self.label_19)
        self.t1_lineEdit = QtGui.QLineEdit(self.stackedWidgetPage1)
        self.t1_lineEdit.setMaximumSize(QtCore.QSize(50, 16777215))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.t1_lineEdit.setFont(font)
        self.t1_lineEdit.setAcceptDrops(False)
        self.t1_lineEdit.setFrame(False)
        self.t1_lineEdit.setReadOnly(True)
        self.t1_lineEdit.setObjectName(_fromUtf8("t1_lineEdit"))
        self.horizontalLayout_7.addWidget(self.t1_lineEdit)
        spacerItem16 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_7.addItem(spacerItem16)
        self.horizontalLayout_18.addLayout(self.horizontalLayout_7)
        self.horizontalLayout_8 = QtGui.QHBoxLayout()
        self.horizontalLayout_8.setObjectName(_fromUtf8("horizontalLayout_8"))
        self.label_20 = QtGui.QLabel(self.stackedWidgetPage1)
        font = QtGui.QFont()
        font.setPointSize(20)
        self.label_20.setFont(font)
        self.label_20.setObjectName(_fromUtf8("label_20"))
        self.horizontalLayout_8.addWidget(self.label_20)
        self.t2_lineEdit = QtGui.QLineEdit(self.stackedWidgetPage1)
        self.t2_lineEdit.setMaximumSize(QtCore.QSize(50, 16777215))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.t2_lineEdit.setFont(font)
        self.t2_lineEdit.setAcceptDrops(False)
        self.t2_lineEdit.setFrame(False)
        self.t2_lineEdit.setReadOnly(True)
        self.t2_lineEdit.setObjectName(_fromUtf8("t2_lineEdit"))
        self.horizontalLayout_8.addWidget(self.t2_lineEdit)
        spacerItem17 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_8.addItem(spacerItem17)
        self.horizontalLayout_18.addLayout(self.horizontalLayout_8)
        self.horizontalLayout_25.addLayout(self.horizontalLayout_18)
        self.horizontalLayout_20 = QtGui.QHBoxLayout()
        self.horizontalLayout_20.setObjectName(_fromUtf8("horizontalLayout_20"))
        self.horizontalLayout_21 = QtGui.QHBoxLayout()
        self.horizontalLayout_21.setObjectName(_fromUtf8("horizontalLayout_21"))
        self.label_21 = QtGui.QLabel(self.stackedWidgetPage1)
        font = QtGui.QFont()
        font.setPointSize(20)
        self.label_21.setFont(font)
        self.label_21.setObjectName(_fromUtf8("label_21"))
        self.horizontalLayout_21.addWidget(self.label_21)
        self.p_lineEdit = QtGui.QLineEdit(self.stackedWidgetPage1)
        self.p_lineEdit.setMaximumSize(QtCore.QSize(50, 16777215))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.p_lineEdit.setFont(font)
        self.p_lineEdit.setAcceptDrops(False)
        self.p_lineEdit.setFrame(False)
        self.p_lineEdit.setReadOnly(True)
        self.p_lineEdit.setObjectName(_fromUtf8("p_lineEdit"))
        self.horizontalLayout_21.addWidget(self.p_lineEdit)
        spacerItem18 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_21.addItem(spacerItem18)
        self.horizontalLayout_20.addLayout(self.horizontalLayout_21)
        self.horizontalLayout_22 = QtGui.QHBoxLayout()
        self.horizontalLayout_22.setObjectName(_fromUtf8("horizontalLayout_22"))
        self.label_22 = QtGui.QLabel(self.stackedWidgetPage1)
        font = QtGui.QFont()
        font.setPointSize(20)
        self.label_22.setFont(font)
        self.label_22.setObjectName(_fromUtf8("label_22"))
        self.horizontalLayout_22.addWidget(self.label_22)
        self.q_lineEdit = QtGui.QLineEdit(self.stackedWidgetPage1)
        self.q_lineEdit.setMaximumSize(QtCore.QSize(50, 16777215))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.q_lineEdit.setFont(font)
        self.q_lineEdit.setAcceptDrops(False)
        self.q_lineEdit.setFrame(False)
        self.q_lineEdit.setReadOnly(True)
        self.q_lineEdit.setObjectName(_fromUtf8("q_lineEdit"))
        self.horizontalLayout_22.addWidget(self.q_lineEdit)
        spacerItem19 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_22.addItem(spacerItem19)
        self.horizontalLayout_20.addLayout(self.horizontalLayout_22)
        self.horizontalLayout_23 = QtGui.QHBoxLayout()
        self.horizontalLayout_23.setObjectName(_fromUtf8("horizontalLayout_23"))
        self.label_23 = QtGui.QLabel(self.stackedWidgetPage1)
        font = QtGui.QFont()
        font.setPointSize(20)
        self.label_23.setFont(font)
        self.label_23.setObjectName(_fromUtf8("label_23"))
        self.horizontalLayout_23.addWidget(self.label_23)
        self.M_lineEdit = QtGui.QLineEdit(self.stackedWidgetPage1)
        self.M_lineEdit.setMaximumSize(QtCore.QSize(50, 16777215))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.M_lineEdit.setFont(font)
        self.M_lineEdit.setAcceptDrops(False)
        self.M_lineEdit.setFrame(False)
        self.M_lineEdit.setReadOnly(True)
        self.M_lineEdit.setObjectName(_fromUtf8("M_lineEdit"))
        self.horizontalLayout_23.addWidget(self.M_lineEdit)
        spacerItem20 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_23.addItem(spacerItem20)
        self.horizontalLayout_20.addLayout(self.horizontalLayout_23)
        self.horizontalLayout_25.addLayout(self.horizontalLayout_20)
        self.verticalLayout_6.addLayout(self.horizontalLayout_25)
        self.stackedWidget.addWidget(self.stackedWidgetPage1)
        self.page_3 = QtGui.QWidget()
        self.page_3.setObjectName(_fromUtf8("page_3"))
        self.label_15 = QtGui.QLabel(self.page_3)
        self.label_15.setGeometry(QtCore.QRect(20, 20, 350, 40))
        self.label_15.setMinimumSize(QtCore.QSize(0, 40))
        self.label_15.setMaximumSize(QtCore.QSize(350, 40))
        font = QtGui.QFont()
        font.setPointSize(25)
        self.label_15.setFont(font)
        self.label_15.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_15.setObjectName(_fromUtf8("label_15"))
        self.stackedWidget.addWidget(self.page_3)
        self.verticalLayout_7.addWidget(self.stackedWidget)
        S4S.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(S4S)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 815, 25))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        self.menuFile = QtGui.QMenu(self.menubar)
        self.menuFile.setObjectName(_fromUtf8("menuFile"))
        S4S.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(S4S)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        S4S.setStatusBar(self.statusbar)
        self.menuFile_Notes_on_Numbers = QtGui.QAction(S4S)
        self.menuFile_Notes_on_Numbers.setObjectName(_fromUtf8("menuFile_Notes_on_Numbers"))
        self.menuFile.addAction(self.menuFile_Notes_on_Numbers)
        self.menubar.addAction(self.menuFile.menuAction())

        self.retranslateUi(S4S)
        self.stackedWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(S4S)

    def retranslateUi(self, S4S):
        S4S.setWindowTitle(_translate("S4S", "SWCNTs4Squints", None))
        self.label.setText(_translate("S4S", "n =", None))
        self.label_2.setText(_translate("S4S", "m =", None))
        self.label_12.setText(_translate("S4S", "<html><head/><body><p>N<span style=\" vertical-align:sub;\">cells</span> = # Unit Cells</p></body></html>", None))
        self.tubeLengthLabel.setText(_translate("S4S", "L = tube length (nm)", None))
        self.label_3.setText(_translate("S4S", "<html><head/><body><p>a<span style=\" vertical-align:sub;\">CC</span> = C-C bond (&#8491;)</p></body></html>", None))
        self.label_4.setText(_translate("S4S", "<html><head/><body><p>C<span style=\" vertical-align:sub;\">h</span> =</p></body></html>", None))
        self.label_8.setText(_translate("S4S", "<html><head/><body><p>&#8491;</p></body></html>", None))
        self.label_5.setText(_translate("S4S", "<html><head/><body><p>d<span style=\" vertical-align:sub;\">t</span> =</p></body></html>", None))
        self.label_14.setText(_translate("S4S", "<html><head/><body><p>&#8491;</p></body></html>", None))
        self.label_7.setText(_translate("S4S", "T =", None))
        self.label_13.setText(_translate("S4S", "<html><head/><body><p>&#8491;</p></body></html>", None))
        self.chiral_angle_var_label.setText(_translate("S4S", "<html><head/><body><p>θ<span style=\" vertical-align:sub;\">Ch</span> =</p></body></html>", None))
        self.chiral_angle_units_label.setText(_translate("S4S", "<html><head/><body><p><span style=\" vertical-align:super;\">&deg;</span></p></body></html>", None))
        self.label_6.setText(_translate("S4S", "<html><head/><body><p>N<span style=\" vertical-align:sub;\">atoms/cell</span> =</p></body></html>", None))
        self.label_9.setText(_translate("S4S", "<html><head/><body><p>N<span style=\" vertical-align:sub;\">atoms/tube</span> =</p></body></html>", None))
        self.mass_var_label.setText(_translate("S4S", "<html><head/><body><p>m<span style=\" vertical-align:sub;\">tube</span> =</p></body></html>", None))
        self.mass_units_label.setText(_translate("S4S", "g", None))
        self.density_var_label.setText(_translate("S4S", "<html><head/><body><p>&rho;<span style=\" vertical-align:sub;\">bundle</span> =</p></body></html>", None))
        self.density_units_label.setText(_translate("S4S", "<html><head/><body><p>g/cm<span style=\" vertical-align:super;\">3</span></p></body></html>", None))
        self.label_18.setText(_translate("S4S", "d =", None))
        self.label_17.setText(_translate("S4S", "<html><head/><body><p>d<span style=\" vertical-align:sub;\">R</span> =</p></body></html>", None))
        self.label_19.setText(_translate("S4S", "<html><head/><body><p>t<span style=\" vertical-align:sub;\">1</span> =</p></body></html>", None))
        self.label_20.setText(_translate("S4S", "<html><head/><body><p>t<span style=\" vertical-align:sub;\">2</span> =</p></body></html>", None))
        self.label_21.setText(_translate("S4S", "<html><head/><body><p>p =</p></body></html>", None))
        self.label_22.setText(_translate("S4S", "<html><head/><body><p>q =</p></body></html>", None))
        self.label_23.setText(_translate("S4S", "<html><head/><body><p>M =</p></body></html>", None))
        self.label_15.setText(_translate("S4S", "<html><head/><body><p>N<span style=\" vertical-align:sub;\">tags</span> = # Taggable Sites</p></body></html>", None))
        self.menuFile.setTitle(_translate("S4S", "File", None))
        self.menuFile_Notes_on_Numbers.setText(_translate("S4S", "Notes on Numbers", None))

