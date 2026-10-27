import time
import shutil
from pathlib import Path
from datetime import datetime
import winsound  
# Specify the desktop path
desktop_path = Path.home() / "Desktop"

# Locating the log file on the desktop
log_file_path = desktop_path / "organizer_log.txt"

# الفئات، الامتدادات، والمجلدات
categories = {
    "imgas": {".png", ".jpg", ".jpeg", ".gif", ".webp"},           # the pictures
    "Noat": {".txt", ".pdf", ".docx", ".doc", ".pptx", ".xlsx"},    # Documents and texts
    "Archives": {".zip", ".rar", ".7z", ".tar"},                    # Compressed files
    "Media": {".mp4", ".mp3", ".mkv", ".avi", ".wav"}               # Media
}

def play_sound_alert():
    """A function to trigger the system alert sound when a file is transferred"""
    try:
        # تشغيل صوت بتردد 1000 هيرتز ولمدة 300 ميللي ثانية
        winsound.Beep(1000, 300)
    except Exception as e:
        print(f"Unable to play audio: {e}")

def write_log(message, play_sound=False):
    """A function to write to the log and play a sound, if requested."""
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    log_entry = f"[{timestamp}] {message}"
    
    # Screen printing
    print(log_entry)
    
    # Save to log file
    with open(log_file_path, "a", encoding="utf-8") as log_file:
        log_file.write(log_entry + "\n")
        
    # Play audio if enabled (True)
    if play_sound:
        play_sound_alert()

# Getting Started
print("👀 Monitoring the desktop, with logging and audio alerts enabled...")
print("Press (Ctrl + C) to stop the program at any time.")
print("=" * 65)

write_log("Starting the monitoring and automated organization program.")

try:
    while True:
        for item in desktop_path.iterdir():
            if item.is_file():
                # Ignore the log file so that it is not transferred
                if item.name == "organizer_log.txt":
                    continue
                
                file_suffix = item.suffix.lower()
                
                # Scan extensions and folders
                for folder_name, extensions in categories.items():
                    if file_suffix in extensions:
                        target_folder = desktop_path / folder_name
                        target_folder.mkdir(parents=True, exist_ok=True)
                        target_path = target_folder / item.name
                        
                        # A brief delay to ensure the file is completely saved
                        time.sleep(0.5)
                        
                        # Transfer file
                        shutil.move(item, target_path)
                        
                        # Success message (with sound enabled)
                        msg = f"تم نقل الملف '{item.name}' ⬅️ إلى مجلد '{folder_name}'"
                        write_log(msg, play_sound=True)
                        break
                        
        # Take a two-second break between each scan to avoid overloading the processor.
        time.sleep(2)

except KeyboardInterrupt:
     write_log("The monitoring program was stopped by the user.")
     print("\n🛑 The program has been stopped successfully. Logs have been saved to the file (organizer_log.txt).")
