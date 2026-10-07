# Linux

Linux is a core engineering foundation for working with servers, backend, cloud, containers, CI/CD, databases, and AI infrastructure.

Linux → Operate → Inspect → Troubleshoot → Automate

## Linux Architecture

[01. Linux & Shell Fundamentals](./01_Linux_and_Shell_Fundamentals/)
├── [README.md](./01_Linux_and_Shell_Fundamentals/README.md)
└── [examples.sh](./01_Linux_and_Shell_Fundamentals/examples.sh)

[02. Filesystem & Navigation](./02_Filesystem_and_Navigation/)
├── [README.md](./02_Filesystem_and_Navigation/README.md)
└── [examples.sh](./02_Filesystem_and_Navigation/examples.sh)

[03. Files & Directories](./03_Files_and_Directories/)
├── [README.md](./03_Files_and_Directories/README.md)
└── [examples.sh](./03_Files_and_Directories/examples.sh)

[04. Reading & Inspecting Files](./04_Reading_and_Inspecting_Files/)
├── [README.md](./04_Reading_and_Inspecting_Files/README.md)
└── [examples.sh](./04_Reading_and_Inspecting_Files/examples.sh)

[05. Search & Text Processing](./05_Search_and_Text_Processing/)
├── [README.md](./05_Search_and_Text_Processing/README.md)
└── [examples.sh](./05_Search_and_Text_Processing/examples.sh)

[06. Pipes, Redirection & Shell Control](./06_Pipes_Redirection_and_Shell_Control/)
├── [README.md](./06_Pipes_Redirection_and_Shell_Control/README.md)
└── [examples.sh](./06_Pipes_Redirection_and_Shell_Control/examples.sh)

[07. Processes & Job Control](./07_Processes_and_Job_Control/)
├── [README.md](./07_Processes_and_Job_Control/README.md)
└── [examples.sh](./07_Processes_and_Job_Control/examples.sh)

[08. Disk & System Resources](./08_Disk_and_System_Resources/)
├── [README.md](./08_Disk_and_System_Resources/README.md)
└── [examples.sh](./08_Disk_and_System_Resources/examples.sh)

[09. Users, Ownership & Permissions](./09_Users_Ownership_and_Permissions/)
├── [README.md](./09_Users_Ownership_and_Permissions/README.md)
└── [examples.sh](./09_Users_Ownership_and_Permissions/examples.sh)

[10. Environment Variables & PATH](./10_Environment_Variables_and_PATH/)
├── [README.md](./10_Environment_Variables_and_PATH/README.md)
└── [examples.sh](./10_Environment_Variables_and_PATH/examples.sh)

[11. Archives & Compression](./11_Archives_and_Compression/)
├── [README.md](./11_Archives_and_Compression/README.md)
└── [examples.sh](./11_Archives_and_Compression/examples.sh)

[12. Shell Editing & Productivity](./12_Shell_Editing_and_Productivity/)
├── [README.md](./12_Shell_Editing_and_Productivity/README.md)
└── [examples.sh](./12_Shell_Editing_and_Productivity/examples.sh)

[13. Services & System Logs](./13_Services_and_System_Logs/)
├── [README.md](./13_Services_and_System_Logs/README.md)
└── [examples.sh](./13_Services_and_System_Logs/examples.sh)

[14. Linux Networking](./14_Linux_Networking/)
├── [README.md](./14_Linux_Networking/README.md)
└── [examples.sh](./14_Linux_Networking/examples.sh)

[15. SSH & Remote Computing](./15_SSH_and_Remote_Computing/)
├── [README.md](./15_SSH_and_Remote_Computing/README.md)
└── [examples.sh](./15_SSH_and_Remote_Computing/examples.sh)

[16. Basic Bash Scripting](./16_Basic_Bash_Scripting/)
├── [README.md](./16_Basic_Bash_Scripting/README.md)
└── [examples.sh](./16_Basic_Bash_Scripting/examples.sh)

## 01. Linux & Shell Fundamentals
**Commands:** `whoami` · `man` · `clear` · `date` · `history`
`OS → Linux → Terminal → Shell → Bash → Commands`
**Achieve:** Understand the Linux command-line environment.

## 02. Filesystem & Navigation
**Commands:** `pwd` · `ls` · `cd`
`Filesystem → Paths → Current directory → Navigation`
**Achieve:** Navigate Linux using absolute and relative paths.

## 03. Files & Directories
**Commands:** `mkdir` · `touch` · `rmdir` · `rm` · `mv` · `cp` · `ln` · `open`
`Path → File/Directory → Create → Copy → Move → Link → Remove`
**Achieve:** Manage files, directories, and links safely.

## 04. Reading & Inspecting Files
**Commands:** `cat` · `less` · `head` · `tail` · `echo` · `wc` · `sort` · `uniq` · `diff`
`File → Read → Inspect → Count → Sort → Compare`
**Achieve:** Inspect and compare text efficiently.

## 05. Search & Text Processing
**Commands:** `find` · `grep` · `xargs` · `sed` · `awk`
`Files → Find → Filter → Transform → Extract → Pipeline`
**Achieve:** Search and process text from the command line.

## 06. Pipes, Redirection & Shell Control
**Operators:** `|` · `>` · `>>` · `2>` · `2>&1` · `&` · `&&` · `||` · `$?`
`stdin(0) → Command → stdout(1) / stderr(2) → File/Pipeline`
**Achieve:** Control output, errors, pipelines, and execution flow.

## 07. Processes & Job Control
**Commands:** `ps` · `top` · `pgrep` · `kill` · `pkill` · `killall` · `jobs` · `bg` · `fg`
`Program → Process → PID → Signal → Foreground/Background`
**Achieve:** Inspect and control running processes.

## 08. Disk & System Resources
**Commands:** `du` · `df` · `free` · `lsof`
`Disk usage/capacity + Memory + Open files`
**Achieve:** Diagnose basic storage and resource problems.

## 09. Users, Ownership & Permissions
**Commands:** `who` · `su` · `sudo` · `passwd` · `chown` · `chmod`
`User → Group → Owner → rwx permissions → Access`
**Achieve:** Understand Linux access control and ownership.

## 10. Environment Variables & PATH
**Commands:** `printenv` · `env` · `export` · `which` · `command -v` · `source` · `alias`
`Shell → Variables → Environment → PATH → Executable lookup`
**Achieve:** Understand shell configuration and executable discovery.

## 11. Archives & Compression
**Commands:** `gzip` · `gunzip` · `tar`
`Files → Archive → Compress → Extract`
**Achieve:** Package and compress files for storage and transfer.

## 12. Shell Editing & Productivity
**Commands:** `nano`
`Terminal → Editor → File → Save/Exit`
**Achieve:** Edit scripts and configuration files from the terminal.

## 13. Services & System Logs
**Commands:** `systemctl` · `journalctl`
`Service/Daemon → Lifecycle → Logs → Troubleshooting`
**Achieve:** Inspect services and diagnose failures through logs.

## 14. Linux Networking
**Commands:** `ip` · `ping` · `curl` · `ss`
`Interface → IP → Route → Port → Socket → Service`
**Achieve:** Inspect interfaces, routes, ports, and basic traffic.

## 15. SSH & Remote Computing
**Commands:** `ssh` · `ssh -p`
`Local client → SSH → Remote server → Remote process`
**Achieve:** Understand secure remote shell access and keys.

## 16. Basic Bash Scripting
**Syntax:** variables · positional arguments · `if/elif/else` · `case` · arrays · loops · functions · `exit` · `$?`
`Script → Input → Logic → Commands → Exit status`
**Achieve:** Automate repeatable Linux tasks with Bash.
