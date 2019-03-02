import walk


class TestWalk:

    def test_list_files(self):
        testdir = "./TestDirectory/ListFiles"
        assert 100 == len(walk.list_files(testdir))
