from PyQt5.QtGui import QColor

# 날짜에 색상을 추가하는 함수
def addColorToDate(self, date, color):
    format = QTextCharFormat()
    format.setBackground(QColor(color))
    self.calendarWidget_Test.setDateTextFormat(date, format)

# 선택된 날짜에 대한 정보를 보여주는 함수
def displayDateInfo(self, date):
    # 예시 정보, 실제로는 데이터베이스 또는 파일에서 정보를 읽어와야 할 수 있습니다.
    info = "No events"
    if date == QDate(2024, 4, 4):
        info = "Team Meeting at 10 AM"
    QMessageBox.information(self, "Date Information", f"Events on {date.toString()}: {info}")

# 클래스에 추가 메서드로 구현
class WindowClass(QMainWindow, form_class):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.initializeUI()

    def initializeUI(self):
        self.calendarWidget_Test.clicked.connect(self.calendarClicked)
        self.btn_addColor.clicked.connect(self.addColorToSelectedDate)
        self.btn_displayInfo.clicked.connect(self.displaySelectedDateInfo)

    def addColorToSelectedDate(self):
        # 선택된 날짜에 녹색을 추가합니다.
        selectedDate = self.calendarWidget_Test.selectedDate()
        self.addColorToDate(selectedDate, 'green')

    def displaySelectedDateInfo(self):
        # 선택된 날짜에 대한 정보를 표시합니다.
        selectedDate = self.calendarWidget_Test.selectedDate()
        self.displayDateInfo(selectedDate)

    # 기존 메서드들...
