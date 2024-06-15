import pytest


def pytest_addoption(parser):
    parser.addoption(
        "--write-results",
        action="store_true",
        default=False,
        help="Write test results instead of comparing them",
    )


@pytest.fixture
def write_results(request):
    return request.config.getoption("--write-results")
