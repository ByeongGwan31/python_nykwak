import tkinter as tk
from tkinter import simpledialog, messagebox, Label
from tkinter.font import Font
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import numpy as np
import calendar
from datetime import datetime
from matplotlib.backend_bases import MouseEvent

class AnnualCalendar:
    def __init__(self, master):
        self.master = master
        self.master.title("Expiry Date Manager")
        self.data = {}
        self.selected_date = None
        self.previous_date = None

        self.fig, self.axes = plt.subplots(3, 4, figsize=(18, 12))
        self.fig.subplots_adjust(hspace=0.5, wspace=0.3)

        self.calendars = {}
        for i in range(12):
            ax = self.axes[i // 4, i % 4]
            month = i + 1
            cal_array, cal_text = self.draw_month_calendar(2024, month, ax)
            ax.set_title(calendar.month_name[month], fontsize=14, color='darkblue')
            self.calendars[month] = (ax, cal_array, cal_text)

        self.canvas = FigureCanvasTkAgg(self.fig, master=self.master)
        self.canvas.mpl_connect('button_press_event', self.on_click)
        self.canvas_widget = self.canvas.get_tk_widget()
        self.canvas_widget.pack(fill=tk.BOTH, expand=True)

        self.bold_font = Font(family="Helvetica", size=12, weight="bold")
        self.info_label = Label(master, text="Click a date to add details", height=4, font=("Helvetica", 12))
        self.info_label.pack(fill=tk.BOTH, side=tk.BOTTOM)

        tk.Button(master, text="Add Expiry Date", command=self.add_expiry_date).pack(side=tk.BOTTOM)

    def draw_month_calendar(self, year, month, ax):
        cal = np.array(calendar.monthcalendar(year, month))
        cal_text = {}
        ax.matshow(cal, cmap='coolwarm', alpha=0.3)

        for (i, j), val in np.ndenumerate(cal):
            if val != 0:
                text_item = ax.text(j, i, str(val), ha='center', va='center', color='black', fontsize=14)
                cal_text[val] = text_item
        return cal, cal_text

    def add_expiry_date(self):
        if self.selected_date:
            category = simpledialog.askstring("Input", "카테고리를 입력하시오:", parent=self.master)
            product = simpledialog.askstring("Input", "제품을 입력하시오:", parent=self.master)
            quantity = simpledialog.askstring("Input", "수량을 입력하시오 (숫자만):", parent=self.master)
            expiry = simpledialog.askstring("Input", "유통기한을 입력하시오 (MM-DD):", parent=self.master)

            info = f"[{category}] \"{product}\" - {quantity}개\n유통기한: {expiry}까지"
            self.data[self.selected_date] = info
            self.update_date_color(self.selected_date, 'red')
            self.display_info(self.selected_date)

    def update_date_color(self, date, color):
        ax, cal_array, cal_text = self.calendars[date.month]
        if date.day in cal_text:
            cal_text[date.day].set_backgroundcolor(color)
            self.canvas.draw()

    def display_info(self, date):
        info = self.data.get(date, "No details")
        self.info_label.config(text=info, font=self.bold_font)

    def on_click(self, event: MouseEvent):
        for month, (ax, cal, cal_text) in self.calendars.items():
            if event.inaxes == ax:
                y, x = int(event.ydata), int(event.xdata)
                try:
                    day = cal[y, x]
                    if day != 0:
                        date = datetime(2024, month, day)
                        self.selected_date = date
                        self.display_info(date)
                        self.update_date_color(date, 'blue')
                except IndexError:
                    continue

root = tk.Tk()
app = AnnualCalendar(root)
root.mainloop()
