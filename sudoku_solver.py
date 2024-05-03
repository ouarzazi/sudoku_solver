import streamlit as st

class SudokuSolver:
    def __init__(self, grid):
        self.grid = grid

    def afficher_grille(self):
        for ligne in self.grid:
            st.write(" ".join(map(str, ligne)))

    def est_valide(self, ligne, colonne, nombre):
        if nombre in self.grid[ligne] or nombre in [self.grid[i][colonne] for i in range(9)]:
            return False

        carre_ligne, carre_colonne = 3 * (ligne // 3), 3 * (colonne // 3)
        for i in range(carre_ligne, carre_ligne + 3):
            for j in range(carre_colonne, carre_colonne + 3):
                if self.grid[i][j] == nombre:
                    return False

        return True

    def trouver_case_vide(self):
        for i in range(9):
            for j in range(9):
                if self.grid[i][j] == 0:
                    return i, j
        return None, None  

    def resoudre(self):
        ligne, colonne = self.trouver_case_vide()

        if ligne is None and colonne is None:
            return True  

        for nombre in range(1, 10):
            if self.est_valide(ligne, colonne, nombre):
                self.grid[ligne][colonne] = nombre

                if self.resoudre():
                    return True  

                self.grid[ligne][colonne] = 0  

        return False

def main():
    st.title("Sudoku Solver")

    st.subheader("Enter the Sudoku grid (use 0 for empty cells):")
    grid = [[0 for _ in range(9)] for _ in range(9)]

    col1, col2, col3 = st.columns(3)
    for i in range(9):
        for j in range(9):
            with col1 if j < 3 else col2 if j < 6 else col3:
                grid[i][j] = st.number_input(f"R{i+1}, C{j+1}", min_value=0, max_value=9, step=1, format="%d")

    solver = SudokuSolver(grid)

    st.subheader("Starting grid:")
    solver.afficher_grille()

    if st.button("Solve", key="solve_button"):
        if solver.resoudre():
            st.subheader("Solved grid:")
            solver.afficher_grille()
        else:
            st.subheader("No solution found.")

if __name__ == "__main__":
    main()
