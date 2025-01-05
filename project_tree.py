import os


def load_gitignore(gitignore_path):
    ignored = set()
    try:
        with open(gitignore_path, 'r') as f:
            for line in f:
                line = line.strip()
                if line and not line.startswith('#'):
                    ignored.add(line)
    except FileNotFoundError:
        pass
    return ignored


def print_tree(startpath, ignore_set, prefix=''):
    folder_content = os.listdir(startpath)

    # Sort the content to have consistent ordering
    folder_content.sort()

    # Filter out ignored files and directories
    filtered_content = \
        [item for item in folder_content if item not in ignore_set]

    for i, item in enumerate(filtered_content):
        path = os.path.join(startpath, item)
        is_last = i == len(filtered_content) - 1
        connector = '└── ' if is_last else '├── '

        print(prefix + connector + item)

        if os.path.isdir(path):
            new_prefix = prefix + ('    ' if is_last else '│   ')
            print_tree(path, ignore_set, new_prefix)


if __name__ == "__main__":
    project_root = '.'  # Укажите путь к корню проекта
    gitignore_path = os.path.join(project_root, '.gitignore')
    ignore_set = load_gitignore(gitignore_path)

    print_tree(project_root, ignore_set)
