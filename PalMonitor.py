#Run as Administrator

import subprocess
import time, os
import sched, zipfile
import threading

program = "PalServer.exe"  # Your program name
program_locate = "C:\\Users\\Administrator\\Desktop\\steamcmd\\steamapps\\common\\PalServer\\PalServer.exe" # The path of the program you have chosen
save_locate = "C:\\Users\\Administrator\\Desktop\\steamcmd\\steamapps\\common\\PalServer\\Pal\\Saved\\SaveGames" # The path of Saves
backuped_path = "C:\\Users\\Administrator\\Desktop\\Backups" # The path of zips(backupedfiles).
max_backups = 10  # Max files in the Backuped_path
re_time = 9 * 60 * 60  # unit:seconds
backup_time = 1 * 60 * 60  # unit:seconds
strf_style = "%Y-%m-%d %H:%M:%S"
zipped_style = "%Y%m%d_%H%M%S"


# Check Process
# geek-docs.com
def check_process(process_name):
    command = 'tasklist /FI "IMAGENAME eq {0}"'.format(process_name)
    output = subprocess.check_output(command, shell=True)
    if process_name.encode() in output:
        return True
    else:
        return False


def repeat_function(scheduler, interval):
    PalMonitor()
    scheduler.enter(interval, 1, repeat_function, (scheduler, interval))


def PalMonitor():
    if not check_process(program):
        t = time.strftime(strf_style, time.localtime(time.time()))
        print("[PalMonitor][%s]Missing program!Program will be restarted in a few seceonds."% t)
        subprocess.Popen(program_locate)
        t = time.strftime(strf_style, time.localtime(time.time()))
        print("[PalMonitor][%s]Program is restarted now."% t)
    """
    # 此语段选择使用，定时打印正常运行
    else:
        t = time.strftime(strf_style, time.localtime(time.time()))
        # print("[PalMonitor]" + t + " Program is running well.")
    """



def task_monitor():
    print("[PalMonitor]Pal monitoring task has been initiated.  >>>Monitoring...")
    scheduler = sched.scheduler(time.time, time.sleep)
    scheduler.enter(0, 1, repeat_function, (scheduler, 5))
    scheduler.run()


def task_auto_restart():
    print("[AutoRestart]The auto-restart task has been initiated.  >>>Current interval: %s seconds" % re_time)
    while True:
        time.sleep(re_time)
        print("[AutoRestart]The PalServer is restarted now.")
        os.system("taskkill /F /IM PalServer-Win64-Shipping-Cmd.exe")


def task_auto_backup():
    def zip_folder(folder_path, zip_path):
        with zipfile.ZipFile(zip_path, 'w', zipfile.ZIP_DEFLATED) as zipf:
            for root, _, files in os.walk(folder_path):
                for file in files:
                    file_path = os.path.join(root, file)
                    zipf.write(file_path, os.path.relpath(file_path, folder_path))

    print("[AutoBackup]The auto-backup task has been initiated.  >>>Current interval: %s seconds" % backup_time)
    while True:
        # get local time
        t = time.strftime(zipped_style, time.localtime(time.time()))
        # zipping files
        print("[AutoBackup]The PalServer is backuping now.")
        zipped_path = "%s\\PalBackup_%s.zip" % (backuped_path , t)
        zip_folder(save_locate, zipped_path)
        t = time.strftime(strf_style, time.localtime(time.time()))
        print("[AutoBackup][%s]The PalServer is backuped Successfully." % t)

        # obsolete backups
        all_files = os.listdir(backuped_path)
        length = len(all_files)
        if length > max_backups:
            t = time.strftime(strf_style, time.localtime(time.time()))
            print("[AutoBackup][%s]Removing obsolete backups." % t)
            delete_num = length - max_backups
            all_files.sort(reverse=True)
            for i in range(delete_num):
                delete_f = all_files.pop()
                os.remove("%s\\%s" % (backuped_path, delete_f))
            t = time.strftime(strf_style, time.localtime(time.time()))
            print("[AutoBackup][%s]Removed %s backups." % (t, delete_num))

        # wait time
        time.sleep(backup_time)


if __name__ == '__main__':
    t1 = threading.Thread(target=task_monitor)
    t2 = threading.Thread(target=task_auto_restart)
    t3 = threading.Thread(target=task_auto_backup)
    t1.start()
    t2.start()
    t3.start()
