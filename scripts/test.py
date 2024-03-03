def main():
    import pytest

    return pytest.main(["--cov=src", "-s", "src"])
