from typing import Optional

def segment_intersection_2d(
        p1:tuple[float, float], 
        p2:tuple[float, float], 
        p3:tuple[float, float], 
        p4:tuple[float, float]) -> Optional[tuple[float, float]]:
    
    x1, y1 = p1
    x2, y2 = p2
    x3, y3 = p3
    x4, y4 = p4

    denom = (y4 - y3) * (x2 - x1) - (x4 - x3) * (y2 - y1)
    if denom == 0:
        return None

    ua = ((x4 - x3) * (y1 - y3) - (y4 - y3) * (x1 - x3)) / denom
    ub = ((x2 - x1) * (y1 - y3) - (y2 - y1) * (x1 - x3)) / denom

    if 0 <= ua <= 1 and 0 <= ub <= 1:
        ix = x1 + ua * (x2 - x1)
        iy = y1 + ua * (y2 - y1)
        return (ix, iy)
    return None
