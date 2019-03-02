import comparefile


class TestCompareFile:

    def test_cmp(self):
        testdir = "./TestDirectory/TestCompareFile/"
        assert True is comparefile.cmp("".join([testdir, "f1.txt"]),
                                       "".join([testdir, "f3_equals_f1.txt"]))
        assert False is comparefile.cmp("".join([testdir, "f1.txt"]),
                                        "".join([testdir, "f2.txt"]))

    def test_inode_cmp(self):
        assert True is comparefile.inode_cmp(1234, 1234)
        assert False is comparefile.inode_cmp(123, 1234)
