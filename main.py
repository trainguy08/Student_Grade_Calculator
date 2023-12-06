from gui import *


def main():
    window = Tk()
    window.title('Project')
    window.geometry('900x1080')
    window.resizable(True, True)
    Gui(window)
    window.mainloop()


if __name__ == '__main__':
    main()


