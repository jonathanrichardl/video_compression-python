

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(858, 635)
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(310, 50, 221, 31))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.okButton = QtWidgets.QPushButton(Form)
        self.okButton.setGeometry(QtCore.QRect(670, 560, 93, 28))
        self.okButton.setObjectName("okButton")
        self.widget = QtWidgets.QWidget(Form)
        self.widget.setGeometry(QtCore.QRect(120, 150, 603, 311))
        self.widget.setObjectName("widget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.widget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.tab0 = QtWidgets.QLineEdit(self.widget)
        self.tab0.setObjectName("tab0")
        self.verticalLayout.addWidget(self.tab0)
        self.tab2 = QtWidgets.QLineEdit(self.widget)
        self.tab2.setObjectName("tab2")
        self.verticalLayout.addWidget(self.tab2)
        self.tab3 = QtWidgets.QLineEdit(self.widget)
        self.tab3.setObjectName("tab3")
        self.verticalLayout.addWidget(self.tab3)
        self.tab9 = QtWidgets.QLineEdit(self.widget)
        self.tab9.setObjectName("tab9")
        self.verticalLayout.addWidget(self.tab9)
        self.tab10 = QtWidgets.QLineEdit(self.widget)
        self.tab10.setObjectName("tab10")
        self.verticalLayout.addWidget(self.tab10)
        self.tab20 = QtWidgets.QLineEdit(self.widget)
        self.tab20.setObjectName("tab20")
        self.verticalLayout.addWidget(self.tab20)
        self.tab21 = QtWidgets.QLineEdit(self.widget)
        self.tab21.setObjectName("tab21")
        self.verticalLayout.addWidget(self.tab21)
        self.tab35 = QtWidgets.QLineEdit(self.widget)
        self.tab35.setObjectName("tab35")
        self.verticalLayout.addWidget(self.tab35)
        self.horizontalLayout.addLayout(self.verticalLayout)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.tab1 = QtWidgets.QLineEdit(self.widget)
        self.tab1.setObjectName("tab1")
        self.verticalLayout_2.addWidget(self.tab1)
        self.tab4 = QtWidgets.QLineEdit(self.widget)
        self.tab4.setObjectName("tab4")
        self.verticalLayout_2.addWidget(self.tab4)
        self.tab8 = QtWidgets.QLineEdit(self.widget)
        self.tab8.setObjectName("tab8")
        self.verticalLayout_2.addWidget(self.tab8)
        self.tab11 = QtWidgets.QLineEdit(self.widget)
        self.tab11.setObjectName("tab11")
        self.verticalLayout_2.addWidget(self.tab11)
        self.tab19 = QtWidgets.QLineEdit(self.widget)
        self.tab19.setObjectName("tab19")
        self.verticalLayout_2.addWidget(self.tab19)
        self.tab22 = QtWidgets.QLineEdit(self.widget)
        self.tab22.setObjectName("tab22")
        self.verticalLayout_2.addWidget(self.tab22)
        self.tab34 = QtWidgets.QLineEdit(self.widget)
        self.tab34.setObjectName("tab34")
        self.verticalLayout_2.addWidget(self.tab34)
        self.tab36 = QtWidgets.QLineEdit(self.widget)
        self.tab36.setObjectName("tab36")
        self.verticalLayout_2.addWidget(self.tab36)
        self.horizontalLayout.addLayout(self.verticalLayout_2)
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.tab5 = QtWidgets.QLineEdit(self.widget)
        self.tab5.setObjectName("tab5")
        self.verticalLayout_3.addWidget(self.tab5)
        self.tab7 = QtWidgets.QLineEdit(self.widget)
        self.tab7.setObjectName("tab7")
        self.verticalLayout_3.addWidget(self.tab7)
        self.tab12 = QtWidgets.QLineEdit(self.widget)
        self.tab12.setObjectName("tab12")
        self.verticalLayout_3.addWidget(self.tab12)
        self.tab18 = QtWidgets.QLineEdit(self.widget)
        self.tab18.setObjectName("tab18")
        self.verticalLayout_3.addWidget(self.tab18)
        self.tab23 = QtWidgets.QLineEdit(self.widget)
        self.tab23.setObjectName("tab23")
        self.verticalLayout_3.addWidget(self.tab23)
        self.tab33 = QtWidgets.QLineEdit(self.widget)
        self.tab33.setObjectName("tab33")
        self.verticalLayout_3.addWidget(self.tab33)
        self.tab37 = QtWidgets.QLineEdit(self.widget)
        self.tab37.setObjectName("tab37")
        self.verticalLayout_3.addWidget(self.tab37)
        self.tab48 = QtWidgets.QLineEdit(self.widget)
        self.tab48.setObjectName("tab48")
        self.verticalLayout_3.addWidget(self.tab48)
        self.horizontalLayout.addLayout(self.verticalLayout_3)
        self.verticalLayout_4 = QtWidgets.QVBoxLayout()
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.tab6 = QtWidgets.QLineEdit(self.widget)
        self.tab6.setObjectName("tab6")
        self.verticalLayout_4.addWidget(self.tab6)
        self.tab13 = QtWidgets.QLineEdit(self.widget)
        self.tab13.setObjectName("tab13")
        self.verticalLayout_4.addWidget(self.tab13)
        self.tab17 = QtWidgets.QLineEdit(self.widget)
        self.tab17.setObjectName("tab17")
        self.verticalLayout_4.addWidget(self.tab17)
        self.tab24 = QtWidgets.QLineEdit(self.widget)
        self.tab24.setObjectName("tab24")
        self.verticalLayout_4.addWidget(self.tab24)
        self.tab32 = QtWidgets.QLineEdit(self.widget)
        self.tab32.setObjectName("tab32")
        self.verticalLayout_4.addWidget(self.tab32)
        self.tab38 = QtWidgets.QLineEdit(self.widget)
        self.tab38.setObjectName("tab38")
        self.verticalLayout_4.addWidget(self.tab38)
        self.tab47 = QtWidgets.QLineEdit(self.widget)
        self.tab47.setObjectName("tab47")
        self.verticalLayout_4.addWidget(self.tab47)
        self.tab49 = QtWidgets.QLineEdit(self.widget)
        self.tab49.setObjectName("tab49")
        self.verticalLayout_4.addWidget(self.tab49)
        self.horizontalLayout.addLayout(self.verticalLayout_4)
        self.verticalLayout_5 = QtWidgets.QVBoxLayout()
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.tab14 = QtWidgets.QLineEdit(self.widget)
        self.tab14.setObjectName("tab14")
        self.verticalLayout_5.addWidget(self.tab14)
        self.tab16 = QtWidgets.QLineEdit(self.widget)
        self.tab16.setObjectName("tab16")
        self.verticalLayout_5.addWidget(self.tab16)
        self.tab25 = QtWidgets.QLineEdit(self.widget)
        self.tab25.setObjectName("tab25")
        self.verticalLayout_5.addWidget(self.tab25)
        self.tab31 = QtWidgets.QLineEdit(self.widget)
        self.tab31.setObjectName("tab31")
        self.verticalLayout_5.addWidget(self.tab31)
        self.tab39 = QtWidgets.QLineEdit(self.widget)
        self.tab39.setObjectName("tab39")
        self.verticalLayout_5.addWidget(self.tab39)
        self.tab46 = QtWidgets.QLineEdit(self.widget)
        self.tab46.setObjectName("tab46")
        self.verticalLayout_5.addWidget(self.tab46)
        self.tab50 = QtWidgets.QLineEdit(self.widget)
        self.tab50.setObjectName("tab50")
        self.verticalLayout_5.addWidget(self.tab50)
        self.tab57 = QtWidgets.QLineEdit(self.widget)
        self.tab57.setObjectName("tab57")
        self.verticalLayout_5.addWidget(self.tab57)
        self.horizontalLayout.addLayout(self.verticalLayout_5)
        self.verticalLayout_6 = QtWidgets.QVBoxLayout()
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.tab15 = QtWidgets.QLineEdit(self.widget)
        self.tab15.setObjectName("tab15")
        self.verticalLayout_6.addWidget(self.tab15)
        self.tab26 = QtWidgets.QLineEdit(self.widget)
        self.tab26.setObjectName("tab26")
        self.verticalLayout_6.addWidget(self.tab26)
        self.tab30 = QtWidgets.QLineEdit(self.widget)
        self.tab30.setObjectName("tab30")
        self.verticalLayout_6.addWidget(self.tab30)
        self.tab40 = QtWidgets.QLineEdit(self.widget)
        self.tab40.setObjectName("tab40")
        self.verticalLayout_6.addWidget(self.tab40)
        self.tab45 = QtWidgets.QLineEdit(self.widget)
        self.tab45.setObjectName("tab45")
        self.verticalLayout_6.addWidget(self.tab45)
        self.tab51 = QtWidgets.QLineEdit(self.widget)
        self.tab51.setObjectName("tab51")
        self.verticalLayout_6.addWidget(self.tab51)
        self.tab56 = QtWidgets.QLineEdit(self.widget)
        self.tab56.setObjectName("tab56")
        self.verticalLayout_6.addWidget(self.tab56)
        self.tab58 = QtWidgets.QLineEdit(self.widget)
        self.tab58.setObjectName("tab58")
        self.verticalLayout_6.addWidget(self.tab58)
        self.horizontalLayout.addLayout(self.verticalLayout_6)
        self.verticalLayout_7 = QtWidgets.QVBoxLayout()
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.tab27 = QtWidgets.QLineEdit(self.widget)
        self.tab27.setObjectName("tab27")
        self.verticalLayout_7.addWidget(self.tab27)
        self.tab29 = QtWidgets.QLineEdit(self.widget)
        self.tab29.setObjectName("tab29")
        self.verticalLayout_7.addWidget(self.tab29)
        self.tab41 = QtWidgets.QLineEdit(self.widget)
        self.tab41.setObjectName("tab41")
        self.verticalLayout_7.addWidget(self.tab41)
        self.tab44 = QtWidgets.QLineEdit(self.widget)
        self.tab44.setObjectName("tab44")
        self.verticalLayout_7.addWidget(self.tab44)
        self.tab52 = QtWidgets.QLineEdit(self.widget)
        self.tab52.setObjectName("tab52")
        self.verticalLayout_7.addWidget(self.tab52)
        self.tab55 = QtWidgets.QLineEdit(self.widget)
        self.tab55.setObjectName("tab55")
        self.verticalLayout_7.addWidget(self.tab55)
        self.tab59 = QtWidgets.QLineEdit(self.widget)
        self.tab59.setObjectName("tab59")
        self.verticalLayout_7.addWidget(self.tab59)
        self.tab62 = QtWidgets.QLineEdit(self.widget)
        self.tab62.setObjectName("tab62")
        self.verticalLayout_7.addWidget(self.tab62)
        self.horizontalLayout.addLayout(self.verticalLayout_7)
        self.verticalLayout_8 = QtWidgets.QVBoxLayout()
        self.verticalLayout_8.setObjectName("verticalLayout_8")
        self.tab28 = QtWidgets.QLineEdit(self.widget)
        self.tab28.setObjectName("tab28")
        self.verticalLayout_8.addWidget(self.tab28)
        self.tab42 = QtWidgets.QLineEdit(self.widget)
        self.tab42.setObjectName("tab42")
        self.verticalLayout_8.addWidget(self.tab42)
        self.tab43 = QtWidgets.QLineEdit(self.widget)
        self.tab43.setObjectName("tab43")
        self.verticalLayout_8.addWidget(self.tab43)
        self.tab53 = QtWidgets.QLineEdit(self.widget)
        self.tab53.setObjectName("tab53")
        self.verticalLayout_8.addWidget(self.tab53)
        self.tab54 = QtWidgets.QLineEdit(self.widget)
        self.tab54.setObjectName("tab54")
        self.verticalLayout_8.addWidget(self.tab54)
        self.tab60 = QtWidgets.QLineEdit(self.widget)
        self.tab60.setObjectName("tab60")
        self.verticalLayout_8.addWidget(self.tab60)
        self.tab61 = QtWidgets.QLineEdit(self.widget)
        self.tab61.setObjectName("tab61")
        self.verticalLayout_8.addWidget(self.tab61)
        self.tab63 = QtWidgets.QLineEdit(self.widget)
        self.tab63.setObjectName("tab63")
        self.verticalLayout_8.addWidget(self.tab63)
        self.horizontalLayout.addLayout(self.verticalLayout_8)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label.setText(_translate("Form", "Custom Quantization Table"))
        self.okButton.setText(_translate("Form", "OK"))

        self.tab0.setText('1'),
        self.tab1.setText('1'),
        self.tab2.setText('1'),
        self.tab3.setText('1'),
        self.tab4.setText('1'),
        self.tab5.setText('1'),
        self.tab6.setText('1'),
        self.tab7.setText('1'),
        self.tab8.setText('1'),
        self.tab9.setText('1'),
        self.tab10.setText('1'),
        self.tab11.setText('1'),
        self.tab12.setText('1'),
        self.tab13.setText('1'),
        self.tab14.setText('1'),
        self.tab15.setText('1'),
        self.tab16.setText('1'),
        self.tab17.setText('1'),
        self.tab18.setText('1'),
        self.tab19.setText('1'),
        self.tab20.setText('1'),
        self.tab21.setText('1'),
        self.tab22.setText('1'),
        self.tab23.setText('1'),
        self.tab24.setText('1'),
        self.tab25.setText('1'),
        self.tab26.setText('1'),
        self.tab27.setText('1'),
        self.tab28.setText('1'),
        self.tab29.setText('1'),
        self.tab30.setText('1'),
        self.tab31.setText('1'),
        self.tab32.setText('1'),
        self.tab33.setText('1'),
        self.tab34.setText('1'),
        self.tab35.setText('1'),
        self.tab36.setText('1'),
        self.tab37.setText('1'),
        self.tab38.setText('1'),
        self.tab39.setText('1'),
        self.tab40.setText('1'),
        self.tab41.setText('1'),
        self.tab42.setText('1'),
        self.tab43.setText('1'),
        self.tab44.setText('1'),
        self.tab45.setText('1'),
        self.tab46.setText('1'),
        self.tab47.setText('1'),
        self.tab48.setText('1'),
        self.tab49.setText('1'),
        self.tab50.setText('1'),
        self.tab51.setText('1'),
        self.tab52.setText('1'),
        self.tab53.setText('1'),
        self.tab54.setText('1'),
        self.tab55.setText('1'),
        self.tab56.setText('1'),
        self.tab57.setText('1'),
        self.tab58.setText('1'),
        self.tab59.setText('1'),
        self.tab60.setText('1'),
        self.tab61.setText('1'),
        self.tab62.setText('1'),
        self.tab63.setText('1'),

