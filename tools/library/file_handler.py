import os


def load_file(file_path, file_name):
    file_path = os.path.join(file_path, file_name)
    with open(file_path, 'r') as f:
        contents = f.read()
    return contents


def save_file(file_path, file_name, contents):
    file_path = os.path.join(file_path, file_name)
    with open(file_path, 'w') as f:
        f.write(contents)


def get_file_path(directory_name, file_name=None):
    if not os.path.exists(directory_name):
        os.makedirs(directory_name)
    return (
        os.path.join(os.getcwd(), directory_name, file_name)
        if file_name
        else os.path.join(os.getcwd(), directory_name)
    )
