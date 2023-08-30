import tkinter
from tkinter import *
from selenium import webdriver
from selenium.webdriver import Chrome, ChromeOptions
from selenium.webdriver.chrome.options import Options
import time
import environment_variables as env
import functions.reportHelper as rp
import tests.search_test as search


class window_design:
    def __init__(self):
        root = Tk()
        root.title("Symphio tester")
        # root.geometry("500x500")
        # root.resizable(False, False)
        # tkinter.Label(frm, "Hello World!").grid(0, 0)
        # tkinter.Button(frm, "Quit", root.destroy).grid(1, 0)
        icon = PhotoImage(file="pics/favicon.png")
        root.iconphoto(True, icon)

        image = PhotoImage(file="pics/faviconblack.png")
        image.zoom(25)
        image = image.subsample(32)
        image_label = Label(root, image=image)
        image_label.grid(row=0, column=0, padx=5, pady=5, sticky=W)

        name_label = Label(root, text="Enter string to search!")
        name_label.grid(row=1, column=0, padx=5, pady=5)

        self.string_search = StringVar()
        name_entry = Entry(root, textvariable=self.string_search)
        name_entry.grid(row=2, column=0, padx=5, pady=5)
        name_entry.insert(0, 'Buy icecream')

        button_start = Button(root, text="Start search test", command=self.start_tests)
        button_start.grid(row=1, column=2, padx=5, pady=5)

        info_text = Label(root, text="Run browser in hidden mode?")
        info_text.grid(row=3, column=0, padx=5, pady=5)

        self.string_hidden = StringVar()
        self.check_box_custom = Checkbutton(root, text='Browser in detached mode', variable=self.string_hidden, onvalue=1, offvalue=0)
        self.check_box_custom.grid(row=3, column=1, padx=5, pady=5)
        self.string_hidden.set('0')

        self.bnt_exit = Button(root, text="Quit", command=root.destroy)
        self.bnt_exit.grid(row=4, column=3)
        # --------------------------------------------------
        self.result = StringVar()
        result_label = Label(root, textvariable=self.result)
        result_label.grid(row=10, column=0, padx=5, pady=5)
        # --------------------------------------------------

        root.mainloop()

    # -------------------------------------
    def start_tests(self):
        rp.create_report_file()
        options = Options()
        options.add_argument("window-size=1600,800")
        if self.string_hidden.get() == '1':
            options.add_argument("--headless")

        driver = webdriver.Chrome(options)

        search.search_test(driver, env.get_env('main_url'), self.string_search.get())

        self.result.set('Test ended')
        time.sleep(5)
        try:
            driver.close()
            print("Browser closed SUCCESSFULLY")
        except Exception as e:
            print("Browser closing ERROR")
            rp.write_error_message(str(e))


window_design()
