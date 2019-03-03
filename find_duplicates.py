import os
import sys
import comparefile
import walk
import itertools
from files import Files


class FindDuplicates:

    def __init__(self, directory_to_search=None):
        top = "."
        if directory_to_search is not None:
            top = str(directory_to_search)
        self.directories = [top]
        self.duplicates = []
        self.all_files = dict()
        self.searched = 0
        self.zero_bytes = []
        self.hard_links = []

    def find_all(self):
        while self.searched != len(self.directories):
            # look in unsearched directories
            for directory in self.directories[self.searched:]:
                # for each file in the directory
                for f in walk.list_files(directory):
                    # get its filesize
                    filesize = os.stat(f).st_size
                    # get its inode
                    inode = os.stat(f).st_ino
                    # get its path
                    # if the filesize is already in our dictionary,
                    if os.stat(f).st_size in self.all_files:
                        # add to the list of filenames in the object Files
                        self.all_files[filesize].add_file(inode, f)
                    else:
                        # otherwise, create a new instance of the class Files
                        self.all_files[filesize] = Files(inode, f)
                # we have now searched an additional directory
                self.searched += 1
                # append the subdirectories to directories to be searched.
                for d in walk.list_subdirectories(directory):
                    self.directories.append(d)
        # for each file we processed
        for size in self.all_files:
            # if it had no contents, it can be listed or ignored.
            if size == 0:
                self.zero_bytes = list(self.all_files[size].filenames)
            # if there was more than one file with the same size
            elif len(self.all_files[size]) >= 2:
                # Deal with hardlinks
                # inodes is an iterator filled with tuples containing
                # the inodes of 2 files of the same size. Combinations
                # divides all of the inodes into groups of 2 for every
                # possible combination of inode without repetition
                inodes = \
                    itertools.combinations(self.all_files[size].inodes, 2)
                # hardlinks is a list of indexes for files that have
                # been determined to be hardlinks.
                hardlinks = []
                for inodepair in inodes:
                    if comparefile.inode_cmp(*inodepair):
                        num = inodepair[0]
                        first = self.all_files[size].inodes.index(num)
                        second = \
                            self.all_files[size].inodes.index(num, first + 1)
                        hardlinks.append(second)

                for index in hardlinks:
                    hl = str(self.all_files[size].filenames[index])
                    self.hard_links.append(hl)

                # if there are hard links
                if len(hardlinks) > 0:
                    for hardlink_index in hardlinks:
                        # change the compare flag in each subsequent hard link
                        # from the first to False.
                        self.all_files[size].compares[hardlink_index] = False

                # Deal with files
                samesizedfiles = self.all_files[size]
                for i in range(len(samesizedfiles.filenames)-1):
                    if samesizedfiles.compares[i] is True \
                       and samesizedfiles.compares[i+1] is True:
                        if comparefile\
                            .cmp(samesizedfiles.filenames[i],
                                 samesizedfiles.filenames[i + 1]):
                            self.duplicates \
                                .append((samesizedfiles.filenames[i],
                                         samesizedfiles.filenames[i + 1]))

        return self

    def reset(self):
        self.directories = [self.directories[0]]
        self.duplicates = []
        self.all_files = dict()
        self.searched = 0
        self.zero_bytes = []
        self.hard_links = []


if __name__ == "__main__":
    fd = None
    if len(sys.argv) > 1:
        fd = FindDuplicates(str(sys.argv[1]))
    else:
        fd = FindDuplicates()
    fd = fd.find_all()

    for dup in fd.duplicates:
        # print the duplicate file
        print(f"Duplicate file found. {dup[0]} is a duplicate of {dup[1]}.")
