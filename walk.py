import os
import stat


def list_subdirectories(full_directory_path):
    folders = []
    try:
        with os.scandir(full_directory_path) as directory:
            for entity in directory:
                if entity.is_dir():
                    folders.append(entity.path)
            directory.close()
    except FileNotFoundError:
        pass
    except PermissionError:
        pass
    return folders


def list_files(full_directory_path):
    files = []
    try:
        with os.scandir(full_directory_path) as directory:
            for entity in directory:
                if entity.is_file(follow_symlinks=False) \
                   and stat \
                        .S_ISREG(entity.stat(follow_symlinks=False).st_mode):
                    files.append(entity.path)
            directory.close()
    except FileNotFoundError:
        pass
    except PermissionError:
        pass
    return files
