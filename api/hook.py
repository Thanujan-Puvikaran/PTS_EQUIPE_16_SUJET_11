import os


def find_file(fullname, extension, path=""):
    """find a notebook, given its name and an optional path
    This turns "foo.bar" into "foo/bar.ipynb"
    and tries turning "Foo_Bar" into "Foo Bar" if Foo_Bar
    does not exist.
    """
    name = fullname.rsplit(".", 1)[-1]
    FILE_PATH = file_path(name, extension, path=path)
    if os.path.isfile(FILE_PATH):
        print("The file was found: ")
        return FILE_PATH
    # let import Notebook_Name find "Notebook Name.ipynb"

    name = name.replace("_", " ")
    FILE_PATH = file_path(name, extension, path=path)
    if os.path.isfile(FILE_PATH):
        print("The file was found: ")
        return FILE_PATH
    print("no such file")


def file_path(name, extension=".ipynb", path=""):
    fullpath = path + "%s" % (name + extension)
    ROOT_PATH = os.path.dirname(os.path.abspath(fullpath))
    return os.path.join(ROOT_PATH, name + extension)
