import numpy as np

def main():
    # Get the number of rows and columns from the user
    rows = int(input("Enter the number of rows: "))
    columns = int(input("Enter the number of columns: "))

    # Initialize an empty matrix
    matrix = []

    # Get the elements of the matrix from the user
    print("Enter the elements of the matrix:")
    for i in range(rows):
        row = []
        for j in range(columns):
            element = float(input(f"Enter element [{i+1},{j+1}]: "))
            row.append(element)
        matrix.append(row)

    # Convert the list of lists into a NumPy array
    matrix = np.array(matrix)

    # Find the inverse of the matrix
    try:
        matrix_inverse = np.linalg.inv(matrix)
        print("Inverse of the matrix:")
        print(matrix_inverse)
    except np.linalg.LinAlgError:
        print("The matrix is singular. It does not have an inverse.")

if __name__ == "__main__":
    main()
