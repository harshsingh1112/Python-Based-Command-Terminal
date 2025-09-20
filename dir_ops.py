import os

def cd(args):
    if not args:
        print("⚠️ Usage: cd <directory>")
        return
    try:
        os.chdir(args[0])
    except FileNotFoundError:
        print(f"❌ No such directory: {args[0]}")

def pwd():
    print(os.getcwd())
