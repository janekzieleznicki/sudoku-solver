from sudoku import Sudoku
import json

def generator():
    puzzle = Sudoku(3).difficulty(0.5)
    solution = puzzle.solve()
    return {
        'puzzle': puzzle.board,
        'solution': solution.board
    }
with open('samples.json', 'w', encoding='utf-8') as f:
    json.dump([generator() for x in range(10)],f,ensure_ascii=False, indent=2)

