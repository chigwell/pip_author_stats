[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Downloads](https://static.pepy.tech/badge/pip-author-stats)](https://pepy.tech/project/pip-author-stats)

# PyPI Author Stats Reporter

The PyPI Author Stats Reporter is a Python package designed to fetch and analyze PyPI package data for a specific author. It generates comprehensive reports detailing package downloads and other statistics, offering valuable insights into the usage and popularity of an author's packages.

## Installation

To install PyPI Author Stats Reporter, use pip:

```bash
pip install pip-author-stats
```

## Usage

### As a Python Module

PyPI Author Stats Reporter can also be integrated into your Python scripts.

Example:

```python
from pip_author_stats.report_generator import generate_report

# Generate a report for a specific PyPI author
report = generate_report('your-pypi-author-username')
print(report)
```

## Report Details

The generated report includes:

- Total number of packages by the author.
- Total number of downloads across all packages.
- Average number of downloads per package.
- Maximum and minimum number of downloads for individual packages.
- The name of the most downloaded package.

## Output Example

When you run PyPI Author Stats Reporter, it outputs a JSON formatted report with detailed statistics. Here is an example snippet:

```json
{
  "Summary Report": {
    "Total Packages": 5,
    "Total Downloads": 15000,
    "Average Downloads": 3000,
    "Max Downloads": 5000,
    "Min Downloads": 1000,
    "Package with Most Downloads": "example-package"
  },
  "Detailed Report": [
    {
      "package": "example-package",
      "total_downloads": 5000
    },
    // More package data...
  ]
}
```

## Contributing

Contributions, issues, and feature requests are welcome! Feel free to fork, modify, and make pull requests to enhance the functionalities of this tool.

## License

[MIT](https://choosealicense.com/licenses/mit/)
