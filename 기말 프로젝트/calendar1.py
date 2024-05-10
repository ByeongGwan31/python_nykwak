import tkinter as tk
from tkinter import simpledialog
import numpy as np
import matplotlib.pyplot as plt
import calendar
from datetime import datetime

class HighlightCalendar:
    def __init__(self, master):
        self.master = master
        self.master.title("Highlight a Date on Calendar")

        # 사용자로부터 날짜 입력 받기
        self.input_date = simpledialog.askstring("Input", "Enter date (YYYY-MM-DD):", parent=self.master)
        self.year, self.month, self.day = map(int, self.input_date.split('-'))
        
        # 달력 생성 및 날짜 강조
        self.draw_calendar(self.year, self.month, self.day)

    def draw_calendar(self, year, month, day):
        # 달력 데이터 생성
        cal = calendar.monthcalendar(year, month)
        fig, ax = plt.subplots(figsize=(8, 6))
        ax.set_title(f"Calendar for {month}/{year}")

        # 달력을 표현하는 히트맵 생성
        cmap = plt.cm.Blues
        cax = ax.matshow(cal, interpolation='nearest', cmap=cmap)

        # 각 날짜 레이블 추가
        for (i, j), val in np.ndenumerate(cal):
            ax.text(j, i, val, ha='center', va='center', color='black')
            if val == day:
                # 선택된 날짜 강조
                ax.text(j, i, val, ha='center', va='center', color='red', fontweight='bold')

        plt.show()

root = tk.Tk()
app = HighlightCalendar(root)
root.mainloop()
