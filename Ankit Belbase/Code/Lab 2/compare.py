import matplotlib.pyplot as plt

def dda_line(x0,y0,x1,y1):
    dx,dy = x1-x0, y1-y0
    s = max(abs(dx),abs(dy))
    if s==0: return [(x0,y0)]
    xi,yi = dx/s, dy/s
    x,y = x0,y0
    pts=[]
    for _ in range(s+1):
        pts.append((int(round(x)),int(round(y))))
        x+=xi; y+=yi
    return pts

def bresenham_line(x0,y0,x1,y1):
    x,y = x0,y0
    dx,dy = abs(x1-x0), abs(y1-y0)
    sx = 1 if x0<x1 else -1
    sy = 1 if y0<y1 else -1
    pts=[]
    if dx>=dy:
        err = dx//2
        for _ in range(dx+1):
            pts.append((x,y))
            x += sx
            err -= dy
            if err < 0:
                y += sy
                err += dx
    else:
        err = dy//2
        for _ in range(dy+1):
            pts.append((x,y))
            y += sy
            err -= dx
            if err < 0:
                x += sx
                err += dy
    return pts

octants = [(0,0,10,3),(0,0,3,10),(0,0,-3,10),(0,0,-10,3),
           (0,0,-10,-3),(0,0,-3,-10),(0,0,3,-10),(0,0,10,-3)]
for i, (x0, y0, x1, y1) in enumerate(octants):
    b = bresenham_line(x0, y0, x1, y1)
    d = dda_line(x0, y0, x1, y1)
    
    bx, by = zip(*b) if b else ([], [])
    dx, dy = zip(*d) if d else ([], [])
    
    plt.subplot(2, 4, i+1)
    plt.scatter(bx, by, c='blue', label='Bresenham')
    plt.scatter(dx, dy, c='orange', label='DDA')
    plt.plot([x0, x1], [y0, y1], c='gray', linestyle='--')
    plt.grid(True)
    plt.title(f"Octant {i+1}")
    plt.legend()
plt.show()
