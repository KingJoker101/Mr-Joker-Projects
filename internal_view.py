# Form implementation generated from reading ui file 'internal_view.ui'
#
# Created by: PyQt6 UI code generator 6.3.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.

import sys
from PyQt6.QtWidgets import QApplication, QWidget, QTableWidget, QTableWidgetItem, QPushButton, QHeaderView, QHBoxLayout, QVBoxLayout
from PyQt6.QtCore import Qt

from access import loadExcelData

class i_app(QWidget):
    def __init__(self):
        super().__init__()
        self.window_width, self.window_height = 700, 500
        self.resize(self.window_width, self.window_height)
        self.setWindowTitle('Transaction')

        layout = QVBoxLayout()
        self.setLayout(layout)

        self.table = QTableWidget()
        layout.addWidget(self.table)

        self.button = QPushButton('&Load Data')
        self.button.clicked.connect(lambda _, xl_path=excel_file_path, sheet_name=worksheet_name: loadExcelData(self, xl_path, sheet_name, QTableWidgetItem))
        layout.addWidget(self.button)

excel_file_path = 'transaction.xlsx'
worksheet_name = 'SalesOrders'
