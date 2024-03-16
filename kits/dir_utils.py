import os


def find_root(current_dir, flag_file='README.md'):
    if flag_file in os.listdir(current_dir):
        return current_dir
    else:
        parent_dir = os.path.dirname(current_dir)
        if parent_dir == current_dir:  # the root directory of system is reached
            raise FileNotFoundError(f"Can't find the root directory with the flag file {flag_file}!")
        return find_root(parent_dir, flag_file)


def change_root():
    root = find_root(os.path.dirname(__file__))
    os.chdir(root)
    return root
