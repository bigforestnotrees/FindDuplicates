import walk


class TestWalk:

    def test_list_subdirectories(self):
        testdir = "./TestDirectory/ListSubdirectories"
        assert 100 == len(walk.list_subdirectories(testdir))

    def test_list_files(self):
        testdir = "./TestDirectory/ListFiles"
        assert 100 == len(walk.list_files(testdir))
