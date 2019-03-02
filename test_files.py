import files


class TestFiles:

    def test_remove(self):
        f1 = files.Files(1, "1.txt")
        f1.remove(filename="1.txt")
        assert 0 == len(f1)
        f2 = files.Files(2, "2.txt")
        f2.remove(inode=2)
        assert 0 == len(f2)

    def test_add_file(self):
        f1 = files.Files(1, "1.txt")
        f1.add_file(2, "2.txt")
        assert 2 == len(f1)
