# segment_intersection_2d
Calculate the intersection point of line segments in a two-dimensional plane.

## Install

```bash
pip install segment_intersection_2d
```

## Usage

```python
from segment_intersection_2d import segment_intersection_2d

line_1_p_1 = (0, 0)
line_1_p_2 = (1, 1)
line_2_p_1 = (1, 0)
line_2_p_2 = (0, 1)
crs = segment_intersection_2d(line_1_p_1, line_1_p_2, line_2_p_1, line_2_p_2)
print(crs) # (0.5, 0.5)

line_1_p_1 = (0, 1)
line_1_p_2 = (0, 0)
line_2_p_1 = (1, 1)
line_2_p_2 = (1, 0)
crs = segment_intersection_2d(line_1_p_1, line_1_p_2, line_2_p_1, line_2_p_2)
print(crs) # None
```
