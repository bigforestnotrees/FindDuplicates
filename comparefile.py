import filecmp


def inode_cmp(inode1, inode2):
    return inode1 == inode2


def cmp(file1, file2):
    return filecmp.cmp(file1, file2, shallow=False)
