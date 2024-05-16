import sys
from PyQt5.QtCore import QDate, Qt
from PyQt5.QtGui import QFont, QColor, QTextCharFormat
from PyQt5.QtWidgets import QApplication, QMainWindow, QCalendarWidget, QPushButton, QVBoxLayout, QWidget, QLabel, QInputDialog, QMessageBox, QDialog, QVBoxLayout, QTextEdit

class CalendarWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()
        self.productData = {}

    def initUI(self):
        self.centralWidget = QWidget(self)
        self.setCentralWidget(self.centralWidget)
        self.layout = QVBoxLayout(self.centralWidget)
        self.calendar = QCalendarWidget(self)
        self.calendar.setGridVisible(True)
        self.layout.addWidget(self.calendar)
        self.infoLabel = QLabel("제품을 입력해주세요", self)
        self.layout.addWidget(self.infoLabel)
        self.btnAddInfo = QPushButton("제품 입력", self)
        self.btnAddInfo.clicked.connect(self.addProductInfo)
        self.layout.addWidget(self.btnAddInfo)
        self.btnDeleteInfo = QPushButton("제품 삭제", self)
        self.btnDeleteInfo.clicked.connect(self.deleteProductInfo)
        self.layout.addWidget(self.btnDeleteInfo)
        self.btnViewAll = QPushButton("모든 제품 조회", self)
        self.btnViewAll.clicked.connect(self.viewAllProducts)
        self.layout.addWidget(self.btnViewAll)
        self.setGeometry(300, 300, 1400, 800)
        self.setWindowTitle('Product Expiry Date Tracker')
        self.calendar.clicked.connect(self.calendarClicked)

    def addProductInfo(self):
        date = self.calendar.selectedDate()
        category, _ = QInputDialog.getText(self, "Input Dialog", "카테고리를 입력하시오")
        product, _ = QInputDialog.getText(self, "Input Dialog", "물품명을 입력하시오")
        quantity, _ = QInputDialog.getInt(self, "Input Dialog", "개수를 입력하시오 (숫자만 가능)")
        expiry, _ = QInputDialog.getText(self, "Input Dialog", "유통기한을 입력하시오 (MM-DD)")
        expiryDate = QDate.fromString(f"{date.year()}-{expiry}", "yyyy-MM-dd")
        if expiryDate not in self.productData:
            self.productData[expiryDate] = []
        self.productData[expiryDate].append((category, product, quantity))
        self.updateDateTextFormat(expiryDate)
        self.calendar.update()

    def deleteProductInfo(self):
        date = self.calendar.selectedDate()
        if date in self.productData:
            items = "\n".join([f"{idx + 1}. {prod[1]} ({prod[0]}, {prod[2]}개)" for idx, prod in enumerate(self.productData[date])])
            item, ok = QInputDialog.getItem(self, "제품 삭제", "삭제할 제품을 선택하세요:", items.split('\n'), 0, False)
            if ok and item:
                index = int(item.split('.')[0]) - 1
                del self.productData[date][index]
                QMessageBox.information(self, "제품 삭제", "제품이 삭제되었습니다.")
                if not self.productData[date]:
                    del self.productData[date]
                self.updateDateTextFormat(date)
        else:
            QMessageBox.information(self, "제품 삭제", "이 날짜에 등록된 제품이 없습니다.")

    def viewAllProducts(self):
        dialog = QDialog(self)
        dialog.setWindowTitle("모든 유통기한 조회")
        layout = QVBoxLayout()
        textEdit = QTextEdit()
        textEdit.setReadOnly(True)
        products = []
        for date, entries in sorted(self.productData.items()):
            for category, product, quantity in entries:
                products.append(f"{category} | {product} {quantity}개 | {date.toString('MM월 dd일')}")
        textEdit.setText("\n".join(products))
        layout.addWidget(textEdit)
        dialog.setLayout(layout)
        dialog.exec_()

    def updateDateTextFormat(self, date):
        if date in self.productData:
            count = len(self.productData[date])
            format = QTextCharFormat()
            exponent = "¹²³⁴⁵⁶⁷⁸⁹"[count - 1] if count > 1 else ''
            format.setToolTip(f"{count}개 정보 있음")
            format.setForeground(QColor('purple'))
            format.setFontWeight(QFont.Bold)
            dateText = date.toString('d') + exponent
            self.calendar.setDateTextFormat(date, format)
        else:
            self.calendar.setDateTextFormat(date, QTextCharFormat())

    def calendarClicked(self, date):
        self.displayProductInfo(date)

    def displayProductInfo(self, date):
        if date in self.productData:
            info_text = f"{date.toString('yyyy년 MM월 dd일 dddd')}<br/>"
            for idx, (category, product, quantity) in enumerate(self.productData[date], 1):
                info_text += f"{category} | <b style='color:black;'>{product}</b> <b style='color:blue;'>{quantity}개</b><br/>"
            info_text += f"<b style='color:red;'>⚠️ 유통기한: {date.toString('MM월 dd일 dddd')}</b>"
            self.infoLabel.setText(info_text)
            self.infoLabel.setTextFormat(Qt.RichText)
        else:
            self.infoLabel.setText("이 날짜에 등록된 정보가 없습니다.")

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = CalendarWindow()
    ex.show()
    sys.exit(app.exec_())
