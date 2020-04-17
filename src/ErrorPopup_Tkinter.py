'''
Python Tkinter 를 사용하여 Tk GUI 툴킷을 바인딩

https://docs.python.org/3/library/tkinter.html

여러 예외 상황에 대해 사용자에게 오류 문구 출력
'''

from tkinter import *
import tkinter.messagebox

def loadWrongPath(absPath):
    win = Tk()
    win.title("오류")

    errorText = "\n" + absPath + "\n\n파일을 불러올 수 없습니다.\n"
    lbl = Label(win, text=errorText)
    lbl.grid(row=2, column=1)

    btn = Button(win, text="확인", width=8, command=win.destroy)
    btn.grid(row=3, column=1)

    win.mainloop()

def loadWrongForm(absPath):
    win = Tk()
    win.title("오류")

    errorText = "\n" + absPath + "\n\n양식에 맞지 않은 파일입니다.\n\nA1[URL], B1[KEYWORD] 양식을 맞춰주세요.\n\n"
    lbl = Label(win, text=errorText)
    lbl.grid(row=2, column=1)

    btn = Button(win, text="확인", width=8, command=win.destroy)
    btn.grid(row=3, column=1)

    win.mainloop()

def NoneTableData():
    win = Tk()
    win.title("오류")

    errorText = "\n\n저장할 데이터가 없습니다.\n"
    lbl = Label(win, text=errorText)
    lbl.grid(row=2, column=1)

    btn = Button(win, text="확인", width=8, command=win.destroy)
    btn.grid(row=3, column=1)

    win.mainloop()

def PageBtnError():
    win = Tk()
    win.title("오류")

    errorText = "없는 페이지입니다."
    lbl = Label(win, text=errorText)
    lbl.grid(row=2, column=1)

    btn = Button(win, text="확인", width=8, command=win.destroy)
    btn.grid(row=3, column=1)

    win.mainloop()

def FileLoadError():
    win = Tk()
    win.title("오류")

    errorText = "지원하지 않는 파일형식입니다."
    lbl = Label(win, text=errorText)
    lbl.grid(row=2, column=1)

    btn = Button(win, text="확인", width=8, command=win.destroy)
    btn.grid(row=3, column=1)

    win.mainloop()

def SearchDisable():
    win = Tk()
    win.title("오류")

    errorText = "검색을 시작할 수 없습니다."
    lbl = Label(win, text=errorText)
    lbl.grid(row=2, column=1)

    btn = Button(win, text="확인", width=8, command=win.destroy)
    btn.grid(row=3, column=1)

    win.mainloop()