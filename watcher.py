import sys, os
from watchfiles import watch, Change

if __name__ == "__main__":
    args = sys.argv
    if len(args) == 1:
        raise SystemExit(f"Usage: python3 {args[0]} <file_to_watch>")
    file_name = args[1]

    for changes in watch(file_name, debounce=500):
        for change, path in changes:
            if change == Change.modified:
                with open(path, "r") as file:
                    try:
                        file_directory = "/".join(path.split("/")[:-1])
                        os.chdir(file_directory)
                        code = file.read()
                        print("_" * 20, f"File {file_name} was modified", "_" * 20)
                        exec(code)
                    except Exception as e:
                        print(e)
