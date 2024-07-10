# PalMonitor
## PalMonitor is a tool to keep palserver online and healthy.
----
### 功能：
1.监控服务器，当服务器崩溃时自动重启
2.定期重启服务器，这个间隔默认为9小时（相关变量：re_time）
3.定期备份服务器存档，这个间隔默认为1小时，最大同时存在10个备份（相关变量：backup_time）
 - 为契合不同WindowsServer服务器，你可以根据需要修改路径，应使用双反斜杠"\"（相关变量：save_locate、backuped_path，分别为服务器存档地址 与 备份地址）
### 说明：
1.Release已自带Python runtime，无需预先配置Python
如欲自行配置请下载源码
Features:
1.Monitor the server and automatically restart the server when it crashes
2.Restart the server periodically, with the default interval of 9 hours (related variable: re_time)
3.Periodically backup server archives. The default interval is 1 hour. A maximum of 10 backup files can be created simultaneously (related variable: backup_time).
 - To fit different WindowsServer servers, you can modify the path as needed, should use double backslash "\" (related variables: save_locate, backuped_path, respectively, the server archive address and backup address)
Instructions:
1.Release comes with its own Python runtime, so there is no need to pre-configure Python.
2.If you want to configure yourself, please download the source code.

----
# PalServer Automation Script

This Python script automates management tasks for PalServer, a server application.

## Features

- **PalMonitor**: Monitors PalServer and restarts if it stops.
- **AutoRestart**: Periodically restarts PalServer to maintain uptime.
- **AutoBackup**: Backs up PalServer save games regularly to prevent data loss.

## Setup

1. **Requirements**: Python installed on your system.
2. **Configuration**: Edit script variables (`program_locate`, `save_locate`, etc.) to match your setup.
3. **Execution**: Run the script with administrator privileges for full functionality.

## Usage

- Adjust `re_time` and `backup_time` intervals as needed.
- Ensure Python environment variables are set correctly.
- Designed for Windows environments due to usage of `tasklist` and `taskkill` commands.

## Dependencies

- Uses standard Python libraries: `subprocess`, `time`, `os`, `sched`, `zipfile`, `threading`.
----
![效果预览](https://github.com/WhiteCloudOL/PalMonitor/blob/main/images/quikview.png "效果预览")
