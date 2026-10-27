import time
import shutil
from pathlib import Path
from datetime import datetime
import winsound  # مكتبة مدمجة في بايثون لتشغيل الأصوات (خاصة بنظام ويندوز)

# تحديد مسار سطح المكتب
desktop_path = Path.home() / "Desktop"

# تحديد ملف السجل (Log File) على سطح المكتب
log_file_path = desktop_path / "organizer_log.txt"

# الفئات، الامتدادات، والمجلدات
categories = {
    "imgas": {".png", ".jpg", ".jpeg", ".gif", ".webp"},           # الصور
    "Noat": {".txt", ".pdf", ".docx", ".doc", ".pptx", ".xlsx"},    # المستندات والنصوص
    "Archives": {".zip", ".rar", ".7z", ".tar"},                    # الملفات المضغوطة
    "Media": {".mp4", ".mp3", ".mkv", ".avi", ".wav"}               # الوسائط
}

def play_sound_alert():
    """دالة لتشغيل صوت تنبيه النظام عند نقل الملف"""
    try:
        # تشغيل صوت بتردد 1000 هيرتز ولمدة 300 ميللي ثانية
        winsound.Beep(1000, 300)
    except Exception as e:
        print(f"تعذر تشغيل الصوت: {e}")

def write_log(message, play_sound=False):
    """A function to write to the log and play a sound, if requested."""
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    log_entry = f"[{timestamp}] {message}"
    
    # طباعة في الشاشة
    print(log_entry)
    
    # حفظ في ملف السجل
    with open(log_file_path, "a", encoding="utf-8") as log_file:
        log_file.write(log_entry + "\n")
        
    # تشغيل الصوت إذا كانت المفعلة True
    if play_sound:
        play_sound_alert()

# بدء التشغيل
print("👀 Monitoring the desktop, with logging and audio alerts enabled...")
print("Press (Ctrl + C) to stop the program at any time.")
print("=" * 65)

write_log("Starting the monitoring and automated organization program.")

try:
    while True:
        for item in desktop_path.iterdir():
            if item.is_file():
                # تجاهل ملف السجل لكي لا يتم نقله
                if item.name == "organizer_log.txt":
                    continue
                
                file_suffix = item.suffix.lower()
                
                # فحص الامتدادات والمجلدات
                for folder_name, extensions in categories.items():
                    if file_suffix in extensions:
                        target_folder = desktop_path / folder_name
                        target_folder.mkdir(parents=True, exist_ok=True)
                        target_path = target_folder / item.name
                        
                        # تأخير بسيط لضمان اكتمال حفظ الملف
                        time.sleep(0.5)
                        
                        # نقل الملف
                        shutil.move(item, target_path)
                        
                        # رسالة النجاح (مع تفعيل الصوت بـ True)
                        msg = f"تم نقل الملف '{item.name}' ⬅️ إلى مجلد '{folder_name}'"
                        write_log(msg, play_sound=True)
                        break
                        
        # استراحة ثانيتين بين كل عملية فحص وأخرى لتجنب استهلاك المعالج
        time.sleep(2)

except KeyboardInterrupt:
     write_log("The monitoring program was stopped by the user.")
     print("\n🛑 The program has been stopped successfully. Logs have been saved to the file (organizer_log.txt).")