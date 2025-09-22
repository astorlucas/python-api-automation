# Python API Automation Framework

### Preconditions that the environment needs
- Python 3.11 or higher
- pip (Python package installer)
- Git

### Clone the repository
```bash
git clone <repository-url>
cd python-api-automation
```
### Install needed dependencies
```bash
pip install -r requirements.txt
```
### Run ALL tests
```bash
pytest
```
### Run specific test file
```bash
pytest tests/test_get_books.py
```
### Run specific test
```bash
pytest tests/test_get_books.py::test_get_all_books
```
### Run Tests with pytest markers
```bash
# Runs only regression tests
pytest -m regression
```
```
```
### Run Tests and Generate Report
```bash
pytest --html=reports/custom-report.html
```
### View Reports
```bash
# Open the latest report
start reports/report-*.html  # Windows
open reports/report-*.html   # macOS
xdg-open reports/report-*.html  # Linux
```

### Environment
The project uses `environment.json` for configuration, it contains:

```json
{
    "base_url": "https://fakerestapi.azurewebsites.net/api/v1"
}
```

### Test Data
Test data is stored in the `data/` directory:
- `book_data.json` - Valid book data
- `book_data_nullable.json` - Data with nullable fields
- `book_data_invalid_date.json` - Invalid date format
- `book_data_extra_property.json` - Data with extra properties
- `book_data_update.json` - Data for update operations

### GET Operations
- **TC1**: Schema validation for all books
- **TC2**: Basic GET all books
- **TC3**: Unsupported method (OPTIONS)
- **TC4**: Get specific book by ID
- **TC5**: Get non-existing book (404)

### POST Operations
- **TC6**: Create book with valid data
- **TC7**: Create book with nullable fields
- **TC8**: Create book with no body (400)
- **TC9**: Create book with invalid date (400)
- **TC10**: Create book with extra properties (400)

### PUT Operations
- **TC11**: Update existing book
- **TC12**: Update with invalid data (400)

### DELETE Operations
- **TC13**: Delete existing book
- **TC14**: Delete invalid book ID (400)
- **TC15**: Delete with long ID (400)

### GitHub Actions
- **Trigger**: Push to main branch
- **Environment**: Ubuntu latest with Python 3.11
- **Reports**: HTML test reports uploaded as artifacts
- **Status**: Continues on test failures for reporting purpouses



