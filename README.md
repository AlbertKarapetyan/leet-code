# Punishment Number Calculation

## Description
This project implements a solution to calculate the punishment number of a given integer `n`. The punishment number is computed based on specific conditions, where the square of each number is partitioned into segments that sum up to the original number. The algorithm efficiently determines which numbers contribute to the punishment number sum.

## Features
- Implements an optimized function to compute the punishment number.
- Uses a generator function to split numbers into valid segmentations.
- Includes unit tests written in `unittest` to verify correctness.

## Installation
To run this project, ensure you have Python installed (version 3.6+ recommended). Clone the repository and navigate to the project directory.

```sh
# Clone the repository
git clone https://github.com/AlbertKarapetyan/leetcode.git
cd leet-code
```

## Usage
Run the script to calculate the punishment number for a given `n`:

```python
from solution import Solution

sol = Solution()
n = 10  # Example input
print(sol.punishment_number(n))
```

## Running Tests
Unit tests are included to verify the correctness of the implementation. Run the tests using:

```sh
python -m unittest
```

## Example
```
Input: n = 10
Output: 182
```

## License
This project is licensed under the MIT License.