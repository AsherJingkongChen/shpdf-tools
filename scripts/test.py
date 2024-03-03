def main():
    import pytest

    pytest.main(["--cov=src", "-s", "src"])
