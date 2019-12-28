from cx_Freeze import setup, Executable 
  
setup(name = "Craigslist" , 
      version = "0.1" , 
      description = "Beta version" , 
      options = {'build_exe': {'include_files': [os.path.join(sys.base_prefix, 'DLLs', 'sqlite3.dll'}]},
      executables = [Executable("main.py")]) 