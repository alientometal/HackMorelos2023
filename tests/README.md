## Testing

The project includes a test suite that can be run using the following command:

`pytest`

To run a specific test file, use the following command:

`pytest tests/test_file.py`

### Guidelines

When writing tests, follow these guidelines:  

- Use descriptive test function names
- Test only one thing per test function
- Write a separate test function for each edge case
- Use fixtures to set up test data and avoid code duplication
- Use `assert` statements to check expected outcomes
- Include docstrings with each test function, describing what is being tested and why

## Code Coverage

Code coverage reports can be generated using the following command:

`pytest --cov=app tests/`

The coverage report will be available in the `htmlcov/` directory.

### Guidelines

We aim for a code coverage of at least 80%. To achieve this, follow these guidelines:

- Write tests that cover all the branches and conditional statements in the code
- Use `assert` statements to check expected outcomes
- Use tools such as mocks or stubs to test external dependencies
<!-- TBD
## Continuous Integration

We use continuous integration to automatically run tests on each pull request. The CI build status is visible on the repository's main page.
-->