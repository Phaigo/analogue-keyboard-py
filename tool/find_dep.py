import os
import re
from collections import deque

def search_dependency(source, directory):
    source_path = os.path.join(directory, source)
    if not os.path.exists(source_path):
        raise FileNotFoundError(f"File {source_path} not found")
    
    # breadth-first search for all dependencies
    found = []
    queue = deque([source_path])

    while queue:
        current_path = queue.popleft()

        if current_path in found or not os.path.exists(current_path):
            continue

        if current_path.endswith(".cpp"):
            found.append(current_path)

        with open(current_path) as f:
            lines = f.readlines()
            for line in lines:
                res = re.search(r'#include "(.+?)"', line)
                if res:
                    included_file = res.group(1)
                    queue.append(os.path.join(directory, included_file))
                    queue.append(os.path.join(directory, included_file.replace(".hpp", ".cpp")))

    return [f for f in found if f.endswith(".cpp")]



def main():
    target_directory = "../Soup/soup/"
    target_file = "AnalogueKeyboard.cpp"
    dependencies = search_dependency(target_file, target_directory)
    print(";".join(dependencies),end="")


if __name__ == "__main__":
    main()
