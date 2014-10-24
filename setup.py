from distutils.core import setup
import py2exe

setup(name='Yprogs',
      version='0.3',
      py_modules=['yprogs'],
      console=['yprogs.py'],
      options={'py2exe': {'excludes': ['Tkconstants', 'Tkinter', 'Tcl', '_imagingtk', 'PIL._imagingtk', 'ImageTk', 'PIL.ImageTk', 'FixTk']}}
      )
