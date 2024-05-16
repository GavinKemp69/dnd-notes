import os
import re

def update_links_in_file(file_path):
    with open(file_path, 'r') as file:
        content = file.read()
        print(f"Content of {file}")
        print(content)
        updated_content = re.sub(r'\[(.*?)\]\((.*?\.md)\)', lambda m: f"[{m.group(1)}]({m.group(2)[:-3]}/)", content)
        if updated_content != content:
            print("Actual change happened")
            with open(file_path, 'w') as file:
                file.write(updated_content)
            print(f"Updated links in file: {file_path}")  # Log statement
            return True
        else:
            print("But no change happened!")
    return False
        

def walk_through_files():
    changed = False
    for root, _, files in os.walk('..'):
        for file in files:
            if file.endswith('.md'):
                file_path = os.path.join(root, file)
                print(file_path)
                if update_links_in_file(file_path):
                    print("IS THREE GOOD")
                    changed = True
    return changed

if __name__ == "__main__":
    changes_made = walk_through_files()
    if changes_made:
        print("OK")
        exit(0)
    else:
        print("NM")
        exit(1)
