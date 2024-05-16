import os
import re

def update_links_in_file(file_path):
    with open(file_path, 'r') as file:
        content = file.read()

    updated_content = re.sub(r'\[(.*?)\]\((.*?\.md)\)', lambda m: f"[{m.group(1)}]({m.group(2)[:-3]}/)", content)

    if updated_content != content:
        with open(file_path, 'w') as file:
            file.write(updated_content)
        print(f"Updated links in file: {file_path}")  # Log statement
        return True
    return False

def walk_through_files():
    changed = False
    for root, _, files in os.walk('..'):
        print(files)
        for file in files:
            print(file)
            if file.endswith('.md'):
                print("IS GOOD")
                file_path = os.path.join(root, file)
                if update_links_in_file(file_path):
                    changed = True
    return changed

if __name__ == "__main__":
    changes_made = walk_through_files()
    with open('changes_made.txt', 'w') as f:
        f.write('true' if changes_made else 'false')
    exit(0)
