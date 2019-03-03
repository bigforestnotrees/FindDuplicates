import find_duplicates
import pytest


class TestFindDuplicates:

    @pytest.fixture(scope="session", autouse=True)
    def found(self):
        found = find_duplicates.FindDuplicates("./TestDirectory").find_all()
        yield found

    def test_duplicates(self, found):
        assert 1 == len(found.duplicates)

    def test_hardlinks(self, found):
        assert 0 == len(found.hard_links)

    def test_zerobytes(self, found):
        assert 0 == len(found.zero_bytes)

    def test_reset(self, found):
        assert 0 == len(found.hard_links)
        found.reset()
        found.find_all()
        assert 0 == len(found.hard_links)
