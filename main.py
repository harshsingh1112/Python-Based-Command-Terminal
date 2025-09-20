def example_file_op():
    print("File operation example")

def example_dir_op():
    print("Directory operation example")
def example_system_op():
    print("System operation example")
def example_helper():
    print("Helper function example")


def example_terminal_helper():
    print("Terminal helper example")
import os
import subprocess

def main():
    print("🚀 Python Command Terminal - Type 'help' for commands, 'exit' to quit")
    
    while True:
        cmd = input(f"{os.getcwd()} > ").strip()
        
        if cmd == "exit":
            break
        elif cmd.startswith("ls"):
            args = cmd.split()
            path = args[1] if len(args) > 1 else "."
            try:
                print("\n".join(os.listdir(path)))
            except FileNotFoundError:
                print(f"No such directory: {path}")
        elif cmd.startswith("cd"):
            args = cmd.split()
            if len(args) > 1:
                try:
                    os.chdir(args[1])
                except FileNotFoundError:
                    print(f"No such directory: {args[1]}")
        elif cmd == "pwd":
            print(os.getcwd())
        elif cmd.startswith("mkdir"):
            args = cmd.split()
            if len(args) > 1:
                try:
                    os.mkdir(args[1])
                except FileExistsError:
                    print(f"Directory already exists: {args[1]}")
        elif cmd.startswith("rm"):
            args = cmd.split()
            if len(args) > 1:
                try:
                    os.remove(args[1])
                except FileNotFoundError:
                    print(f"No such file: {args[1]}")
        elif cmd == "ps":
            subprocess.run(["ps"])
        elif cmd == "help":
            print("""
Available Commands:
    ls [dir]       - List files in directory
    cd <dir>       - Change directory
    pwd            - Print working directory
    mkdir <name>   - Create a new directory
    rm <name>      - Remove file or directory
    ps             - Show running processes
    help           - Show this help menu
    exit           - Exit terminal
            """)
        else:
            print(f"Command '{cmd}' not recognized. Type 'help' for options.")

if __name__ == "__main__":
    main()
