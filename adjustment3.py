import numpy as np

# Function to get initial approximations from the user
def get_initial_approximations():
    x0 = float(input("Enter initial approximation for x (x0): "))
    y0 = float(input("Enter initial approximation for y (y0): "))
    return x0, y0

# Function to form J matrix
def form_J_matrix(x0, y0):
    J = np.array([[2*x0 + 3*y0, 3*x0 - 2*y0],
                  [21*x0, 6*y0],
                  [2 - 6*y0, 6*y0 - 6*x0]])
    return J

# Function to form K matrix
def form_K_matrix(x0, y0):
    K = np.array([[7 - (x0**2 + 3*x0*y0 - y0**2)],
                  [55.2 - (7*x0**3 - 3*y0**2)],
                  [-1.2 - (2*x0 - 6*x0*y0 + 3*y0**2)]])
    return K

# Function to calculate N matrix
def calculate_N_matrix(J):
    N = np.dot(J.T, J)
    return N

# Function to calculate N^-1
def calculate_inverse_N(N):
    N_inv = np.linalg.inv(N)
    return N_inv

# Function to calculate N^-1 * (J^T * K)
def calculate_result(N_inv, J, K):
    result = np.dot(N_inv, np.dot(J.T, K))
    return result

# Main function
def main():
    # Get initial approximations
    x0, y0 = get_initial_approximations()

    # Perform iterations until convergence
    max_iterations = 100
    tolerance = 1e-6
    x_prev = x0
    y_prev = y0

    for iteration in range(max_iterations):
        # Form J matrix
        J = form_J_matrix(x_prev, y_prev)

        # Form K matrix
        K = form_K_matrix(x_prev, y_prev)

        # Calculate N matrix
        N = calculate_N_matrix(J)

        # Calculate N^-1
        N_inv = calculate_inverse_N(N)

        # Calculate result
        result = calculate_result(N_inv, J, K)

        # Update x and y
        dx, dy = result
        x = x_prev + dx[0]
        y = y_prev + dy[0]

        # Check for convergence
        if abs(x - x_prev) < tolerance and abs(y - y_prev) < tolerance:
            print(f"Converged after {iteration + 1} iterations.")
            break

        # Output results for current iteration
        print(f"Iteration {iteration + 1}:")
        print(f"   x: {x:.6f}, y: {y:.6f}")
        print(f"   dx: {dx[0]}, dy: {dy[0]}")
        print()

        # Update previous values for next iteration
        x_prev = x
        y_prev = y
    else:
        print("Maximum number of iterations reached without convergence.")

if __name__ == "__main__":
    main()
