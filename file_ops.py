import os
import shutil

def ls(args):
    path = args[0] if args else "."
    try:
        for item in os.listdir(path):
            print(item)
    except FileNotFoundError:
        print(f"❌ No such directory: {path}")

def mkdir(args):
    if not args:
        print("⚠️ Usage: mkdir <directory_name>")
        return
    try:
        os.makedirs(args[0], exist_ok=True)
        print(f"✅ Directory created: {args[0]}")
    except Exception as e:
        print(f"❌ Error creating directory: {e}")

def rm(args):
    if not args:
        print("⚠️ Usage: rm <file_or_directory>")
        return
    target = args[0]
    try:
        if os.path.isdir(target):
            shutil.rmtree(target)
        else:
            os.remove(target)
        print(f"✅ Removed: {target}")
    except FileNotFoundError:
        print(f"❌ Not found: {target}")
    except Exception as e:
        print(f"❌ Error: {e}")
