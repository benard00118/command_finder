import sqlite3

def create_database():
    conn = sqlite3.connect('linux_commands.db')
    c = conn.cursor()

    c.execute('''CREATE TABLE IF NOT EXISTS commands
                (id INTEGER PRIMARY KEY, command TEXT UNIQUE, meaning TEXT)''')

    commands_data = [
    ('ls', 'List directory contents'),
    ('cd', 'Change directory'),
    ('mkdir', 'Make directories'),
    ('cp', 'Copy files and directories'),
    ('mv', 'Move or rename files and directories'),
    ('rm', 'Remove files and directories'),
    ('cat', 'Concatenate files and print on the standard output'),
    ('grep', 'Print lines matching a pattern'),
    ('chmod', 'Change file mode bits'),
    ('sudo', 'Execute a command as another user'),
    ('tar', 'Manipulate archive files'),
    ('ssh', 'Secure Shell - access remote machine'),
    ('ping', 'Send ICMP ECHO_REQUEST to network hosts'),
    ('tail', 'Display the last part of a file'),
    ('head', 'Display the first part of a file'),
    ('locate', 'Find files by name'),
    ('man', 'Display the manual pages for commands'),
    ('gedit', 'Open a text editor'),
    ('grub', 'Grand Unified Bootloader - manage boot options'),
    ('apt', 'Advanced Package Tool - package manager for Debian-based systems'),
    ('apt-get', 'Command-line interface for package management in Debian-based systems'),
    ('aptitude', 'Terminal-based package manager for Debian-based systems'),
    ('snap', 'Package manager for managing applications in snap format'),
    ('clear', 'Clear the terminal screen'),
    ('su', 'Switch user or become another user'),
    ('adduser', 'Interactive command to add a new user'),
    ('useradd', 'Command-line utility to create a new user or update default new user information'),
    ('userdel', 'Command to delete a user account and related files'),
    ('open', 'Open a file or directory with the default application'),
    ('code', 'Launch Visual Studio Code editor'),
    ('nano', 'Text editor for Unix-like operating systems'),
    ('help', 'Display information about builtin commands'),
    ('--fix-broken', 'Fix broken packages in APT package management system'),
    ('service', 'Manage system services'),
    ('kill', 'Send a signal to a process, terminating it'),
    ('pwd', 'Print the current working directory'),
    ('history', 'Display the command history'),
    ('wget', 'Download files from the internet'),
    ('tree', 'List contents of directories in a tree-like format'),
    ('wc', 'Count words, lines, and characters in a file'),
    ('touch', 'Create an empty file or update the timestamp of a file'),
    ('vi', 'Vi text editor'),
    ('rmdir', 'Remove directory'),
    ('df', 'Display free disk space'),
    ('less', 'View file contents one page at a time'),
    ('tar', 'Manipulate archive files'),
    ('uname', 'Print system information'),
    ('sed', 'Stream editor for filtering and transforming text'),
    ('lscpu', 'Display information about the CPU architecture'),
    ('exit', 'Exit the shell or terminal session'),
    ('ip', 'Show/manipulate routing, devices, policy routing and tunnels'),
    ('mount', 'Mount a filesystem'),
    ('zcat', 'Concatenate and display compressed files'),
    ('time', 'Time a simple command or give resource usage'),
    ('shutdown', 'Shutdown or restart the system'),
    ('systemctl', 'Control the systemd system and service manager'),
    ('cal', 'Display a calendar'),
    ('date', 'Display or set the system date and time'),
    ('gunzip', 'Decompress files created by gzip'),
    ('gzip', 'Compress files using the GNU zip compression format'),
    ('od', 'Dump files in octal and other formats'),
    ('sort', 'Sort lines of text files'),
    ('tr', 'Translate or delete characters'),
    ('tee', 'Read from standard input and write to standard output and files'),
    ('comm', 'Compare two sorted files line by line'),
    ('groupadd', 'Create a new group'),
    ('passwd', 'Change user password'),
    ('tac', 'Concatenate and print files in reverse'),
    ('id', 'Print real and effective user and group IDs'),
    ('echo', 'Display a line of text'),
    ('alias', 'Create an alias for a command'),
    ('chown', 'Change file owner and group'),
    ('chgrp', 'Change group ownership'),
    ('find', 'Search for files in a directory hierarchy'),
    ('cut', 'Remove sections from each line of files'),
    ('hostname', 'Print or set the system\'s hostname'),
    ('ps', 'Report a snapshot of the current processes'),
    ('top', 'Display Linux processes'),
    ('df', 'Display disk space usage'),
    ('du', 'Estimate file space usage'),
    ('diff', 'Compare files line by line'),
    ('gzip', 'Compress files'),
    ('gunzip', 'Decompress files'),
    ('grep', 'Search text for patterns'),
    ('head', 'Output the first part of files'),
    ('tail', 'Output the last part of files'),
    ('touch', 'Change file timestamps'),
    ('mv', 'Move files'),
    ('rm', 'Remove files or directories'),
    ('cp', 'Copy files or directories'),
    ('pwd', 'Print working directory'),
    ('clear', 'Clear the terminal screen'),
    ('history', 'Command history'),
    ('man', 'Display manual pages'),
    ('apropos', 'Search the manual page names and descriptions'),
    ('info', 'Display program information'),
    ('whatis', 'Display one-line manual page descriptions'),
    ('uname', 'Print system information'),
    ('date', 'Print or set the system date and time'),
    ('hostname', 'Print or set the system name'),
    ('uptime', 'Display system uptime'),
    ('free', 'Display amount of free and used memory in the system'),
    ('ps', 'Report a snapshot of the current processes'),
    ('top', 'Display Linux processes'),
     ('mount', 'Mount a filesystem'),
    ('umount', 'Unmount a previously mounted filesystem'),
    ('lsof', 'List open files'),
    ('ifconfig', 'Configure network interface parameters'),
    ('fsck', 'Check and repair a Linux filesystem'),
    ('reboot', 'Reboot the system'),
    ('iwconfig', 'Configure a wireless network interface'),
]

    for command, meaning in commands_data:
        try:
            c.execute("INSERT OR IGNORE INTO commands (command, meaning) VALUES (?, ?)", (command, meaning))
        except sqlite3.IntegrityError:
            print(f"Command '{command}' already exists in the database.")

    conn.commit()
    conn.close()

def search_commands(keyword):
    with sqlite3.connect('linux_commands.db') as conn:
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM commands WHERE command LIKE ? OR meaning LIKE ?", 
                    ('%' + keyword + '%', '%' + keyword + '%'))
        found_commands = cursor.fetchall()
    return found_commands

def main():
    create_database()

    keyword = input("Enter a keyword to search for commands: ")
    found_commands = search_commands(keyword)
    if found_commands:
        print("Found commands matching the search:")
        for command in found_commands:
            print(f"Command: {command[1]}, Meaning: {command[2]}")
    else:
        print("No commands found matching the search.")

if __name__ == "__main__":
    main()
