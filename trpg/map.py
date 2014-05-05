




def get_new_blank_map(size_x, size_y, empty='.'):
    """Return a new blank map."""
    if (size_x and size_y) > 1:
        x = join([empty]*size_x)
        return tuple(x for i in range(size_y)

def build_coords_dict(map_matrix, empty='.'):
    """Return a new dict of (x, y) coords mapped to non-empty chars."""
    d = {}
    for y in matrix:
          for i in y:
              if i != empty:
                  d[y.index(i), matrix.index(y)] = y[y.index(i)]
    return d
