import sys
import re
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
        # 달력 범위 설정
        self.calendar.setMinimumDate(QDate(2022, 1, 1))
        self.calendar.setMaximumDate(QDate(2027, 12, 31))
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
        self.setWindowTitle('식품 관리 캘린더')
        self.calendar.clicked.connect(self.calendarClicked)

    def is_valid_date(self, date_str):
        try:
            date = QDate.fromString(date_str, "yyyy-MM-dd")
            if not date.isValid():
                return False
            year = date.year()
            month = date.month()
            day = date.day()
            if not (2022 <= year <= 2026):
                return False
            if not (1 <= month <= 12):
                return False
            if day > QDate(year, month, 1).daysInMonth():
                return False
            return True
        except:
            return False

    def addProductInfo(self):
        date = self.calendar.selectedDate()
        category, _ = QInputDialog.getText(self, "카테고리 입력하기", "카테고리를 입력하시오")
        product, _ = QInputDialog.getText(self, "물품명 입력하기", "물품명을 입력하시오")
        quantity, _ = QInputDialog.getInt(self, "개수 입력하기", "개수를 입력하시오 (숫자만 가능)")
        
        manufacture, _ = QInputDialog.getText(self, "제조일자 입력하기", "제조일자를 입력하시오 (YYYY-MM-DD)")
        if not re.match(r'^\d{4}-\d{2}-\d{2}$', manufacture) or not self.is_valid_date(manufacture):
            QMessageBox.warning(self, "입력 오류", "제조일자는 2022-2026년 범위 내에서 yyyy-mm-dd 형식으로 입력해주세요.")
            return
        
        expiry, _ = QInputDialog.getText(self, "유통기한 입력하기", "유통기한을 입력하시오 (YYYY-MM-DD)")
        if not re.match(r'^\d{4}-\d{2}-\d{2}$', expiry) or not self.is_valid_date(expiry):
            QMessageBox.warning(self, "입력 오류", "유통기한은 2022-2027년 범위 내에서 yyyy-mm-dd 형식으로 입력해주세요.")
            return
        
        expiryDate = QDate.fromString(expiry, "yyyy-MM-dd")
        if expiryDate.isValid():
            if expiryDate not in self.productData:
                self.productData[expiryDate] = []
            self.productData[expiryDate].append((category, product, quantity, manufacture))
            self.updateDateTextFormat(expiryDate)
            self.calendar.update()
        else:
            QMessageBox.warning(self, "입력 오류", "유효한 유통기한을 입력해주세요.")

    def deleteProductInfo(self):
        date = self.calendar.selectedDate()
        if date in self.productData:
            items = []
            for idx, prod in enumerate(self.productData[date]):
                item = f"{idx + 1}. {prod[1]} ({prod[0]}, {prod[2]}개)"
                items.append(item)
            items_str = "\n".join(items)
            item, ok = QInputDialog.getItem(self, "제품 삭제", "삭제할 제품을 선택하세요:", items_str.split('\n'), 0, False)
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
            for category, product, quantity, manufacture in entries:
                manufactureDate = QDate.fromString(manufacture, "yyyy-MM-dd").toString('yyyy년 MM월 dd일')
                products.append(f"제조일자: {manufactureDate} | 카테고리 : {category} | {product} {quantity}개 | {date.toString('yyyy년 MM월 dd일')}까지")
        products.sort(key = lambda x: QDate.fromString(x.split(' | ')[-1].split('까지')[0], 'yyyy년 MM월 dd일'))
        textEdit.setText("\n".join(products))
        layout.addWidget(textEdit)
        dialog.setLayout(layout)
        dialog.resize(800, 600)
        dialog.exec_()

    def updateDateTextFormat(self, date):
        if date in self.productData:
            format = QTextCharFormat()
            format.setForeground(QColor('purple'))
            format.setFontWeight(QFont.Bold)
            self.calendar.setDateTextFormat(date, format)
        else:
            self.calendar.setDateTextFormat(date, QTextCharFormat())

    def calendarClicked(self, date):
        self.displayProductInfo(date)

    def displayProductInfo(self, date):
        if date in self.productData:
            info_text = ""
            for idx, (category, product, quantity, manufacture) in enumerate(self.productData[date], 1):
                manufactureDate = QDate.fromString(manufacture, "yyyy-MM-dd").toString('yyyy년 MM월 dd일')
                info_text += f"제조일자: {manufactureDate}<br/>"
                info_text += f"{category} | <b style='color:black;'>{product}</b> <b style='color:blue;'>{quantity}개</b><br/>"
            info_text += f"<b style='color:red;'>⚠️ 유통기한: {date.toString('MM월 dd일')}</b>"
            self.infoLabel.setText(info_text)
            self.infoLabel.setTextFormat(Qt.RichText)
        else:
            self.infoLabel.setText("이 날짜에 등록된 정보가 없습니다.")

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = CalendarWindow()
    ex.show()
    sys.exit(app.exec_())
