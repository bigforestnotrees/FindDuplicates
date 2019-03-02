class Files:
    def __init__(self, inode, filename):
        self.inodes = [inode]
        self.filenames = [filename]
        self.compares = [True]

    def __len__(self):
        return len(self.inodes)

    def __str__(self):
        return str(self.filenames)

    def remove(self, *, inode=None, filename=None):
        i = -1
        if inode:
            i = self.inodes.index(inode)
        elif filename:
            i = self.filenames.index(filename)
        return (self.inodes.pop(i), self.filenames.pop(i))

    def add_file(self, inode, filename):
        self.inodes.append(inode)
        self.filenames.append(filename)
        self.compares.append(True)
