from tkinter import *
from tkinter import ttk


class ClickerApp:
    def __init__(self):
        self.count = 0
        self.create_window()

    def click(self):
        self.count += 1
        self.hint.config(text=f"Counter: {self.count}")

    def create_window(self):
        root = Tk()
        root.title("Clicker")

        frame = ttk.Frame(root, padding=10)
        frame.grid()

        title = ttk.Label(frame, text="Click on button!").grid(column=0, row=0)
        self.hint = ttk.Label(frame, text=f"Counter: {self.count}")
        self.hint.grid(column=0, row=1)
        click_button = ttk.Button(frame, text="👆", command=self.click)
        click_button.grid(column=1, row=0)

        root.mainloop()


def main():
    app = ClickerApp()

if __name__ == "__main__":
    main()