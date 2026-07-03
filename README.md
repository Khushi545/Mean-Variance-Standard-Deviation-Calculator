
# Mean-Variance-Standard Deviation Calculator

A Python function that calculates statistical measures on a 3×3 matrix.

## What it does
Takes a list of 9 numbers, converts it into a 3×3 NumPy matrix, and returns the following statistics calculated across both axes and the flattened matrix:
- Mean
- Variance
- Standard Deviation
- Max
- Min
- Sum

## Example
```python
calculate([0,1,2,3,4,5,6,7,8])
```
Returns:
```python
{
  'mean': [[3.0, 4.0, 5.0], [1.0, 4.0, 7.0], 4.0],
  'variance': [[6.0, 6.0, 6.0], [0.666, 0.666, 0.666], 6.666],
  'standard deviation': [[2.449, 2.449, 2.449], [0.816, 0.816, 0.816], 2.581],
  'max': [[6, 7, 8], [2, 5, 8], 8],
  'min': [[0, 1, 2], [0, 3, 6], 0],
  'sum': [[9, 12, 15], [3, 12, 21], 36]
}
```

## How to Run
```bash
python main.py
```

## Technologies Used
- Python 3
- NumPy

## Files
| File | Description |
|------|-------------|
| `mean_var_std.py` | Main solution file |
| `main.py` | Runs the function and tests |
| `test_module.py` | Unit tests |

## License
MIT

---
