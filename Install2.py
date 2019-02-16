from cx_Freeze import setup, Executable
import os

os.environ['TCL_LIBRARY'] ="C:\\Users\\Amit\\AppData\\Local\\Programs\\Python\\Python35-32\\tcl\\tcl8.6"
os.environ['TK_LIBRARY'] = "C:\\Users\\Amit\\AppData\\Local\\Programs\\Python\\Python35-32\\tcl\\tk8.6"
setup(name="install",
      version="2.0",
      author="Amit",
      description="My Installer",
      executables=[Executable(r"C:\Users\Amit\Desktop\gui\gui.py",
                   icon=r"C:\Users\Amit\Desktop\gui\Startup.ico",
                   shortcutName="Gui",
                   shortcutDir="DesktopFolder")]
     )
