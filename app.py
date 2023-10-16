from flask import Flask, request, jsonify

app = Flask(__name__)


def detect_shapes(matrix):
    rows, cols = len(matrix), len(matrix[0])
    visited = [[False] * cols for _ in range(rows)]
    shapes = {}

    def dfs(r, c, target):
        if (r < 0 or r >= rows or c < 0 or c >= cols or
                matrix[r][c] != target or visited[r][c]):
            return []

        visited[r][c] = True
        cells = [(r, c)]
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]

        for dr, dc in directions:
            cells += dfs(r + dr, c + dc, target)

        return cells

    for r in range(rows):
        for c in range(cols):
            if not visited[r][c]:
                shape_cells = dfs(r, c, matrix[r][c])
                min_r = min([cell[0] for cell in shape_cells])
                max_r = max([cell[0] for cell in shape_cells])
                min_c = min([cell[1] for cell in shape_cells])
                max_c = max([cell[1] for cell in shape_cells])

                height, width = max_r - min_r + 1, max_c - min_c + 1
                shape_area = len(shape_cells)

                if height == width and shape_area == height * width:
                    shape = 'square'
                elif height > width and shape_area == height * width:
                    shape = 'vertical rectangle'
                elif height < width and shape_area == height * width:
                    shape = 'horizontal rectangle'
                else:
                    shape = 'polygon'

                # Determine location
                center_row = (min_r + max_r) / 2
                center_col = (min_c + max_c) / 2

                if shape == 'square':
                    if center_row < rows / 2 and center_col < cols / 2:
                        location = 'top left'
                    elif center_row < rows / 2:
                        location = 'top right'
                    elif center_col < cols / 2:
                        location = 'bottom left'
                    else:
                        location = 'bottom right'

                elif shape == 'vertical rectangle':
                    if center_col < cols / 2:
                        location = 'left'
                    else:
                        location = 'right'

                elif shape == 'horizontal rectangle':
                    if center_row < rows / 2:
                        location = 'top left'
                    else:
                        location = 'bottom left'

                else:  # shape == 'polygon'
                  if center_row < rows / 3 and center_col < cols / 3:
                      location = 'top left'
                  elif max_c == cols - 1 and min_c > (2 * cols) / 3:
                      location = 'right'
                  elif center_row < rows / 3 and center_col > cols / 2:
                      location = 'top right'
                  elif center_row > (2 * rows) / 3 and center_col < cols / 3:
                      location = 'bottom left'
                  elif abs(center_row - rows / 2) <= 1 and center_col < cols / 3:
                      location = 'middle left'
                  elif center_col < cols / 3:
                      location = 'left'
                  elif abs(center_row - rows / 2) <= 1 and center_col > cols / 2:
                      location = 'middle right'
                  else:
                      location = 'middle'
                shapes[matrix[r][c]] = {
                    'shape': shape,
                    'location': [location]
                }

    return shapes

@app.route('/detect_shapes', methods=['POST'])
def detect_shapes_endpoint():
    data = request.json
    if data is None:
        return jsonify({'error': 'Invalid JSON data'}), 400

    matrix = data.get('matrix')
    if not matrix:
        return jsonify({'error': 'Matrix not found in JSON data'}), 400

    # Call the detect_shapes function with the matrix data
    shapes = detect_shapes(matrix)

    return jsonify(shapes)


if __name__ == '__main__':
    app.run(debug=True)