from distutils.core import setup

setup(name='Yprogs',
      version='0.5',
      description='Front-End GUI application to open quickly folder without storing massive amounts of shortcuts.',
      author='Murat Özel',
      url='https://github.com/Nama',
      platforms=['Windows', 'Linux'],
      py_modules=['yprogs'],
      console=['yprogs.py'],
      data_files=['yprogs.ico', 'yprogs.ini', 'yprogs.kv', 'yprogs_bg.png']
      )
