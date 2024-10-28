import numpy as np
import matplotlib.pyplot as plt

def plot_histogram_curve(classes, frequencies):
    # Calculate the midpoint of each class
    midpoints = [(classes[i] + classes[i+1]) / 2 for i in range(len(classes) - 1)]

    # Plot histogram
    plt.figure(figsize=(10, 5))
    plt.bar(midpoints, frequencies, width=np.diff(classes), align='center', edgecolor='black', alpha=0.7)
    
    # Plot curve
    x_curve = np.linspace(classes[0], classes[-1], 100)
    y_curve = np.interp(x_curve, midpoints, frequencies)
    plt.plot(x_curve, y_curve, color='red', linestyle='-', linewidth=2, label='Curve')

    plt.xlabel('Classes')
    plt.ylabel('Frequency')
    plt.title('Histogram with Curve')
    plt.legend()
    plt.grid(True)
    plt.show()

def main():
    # Input number of classes
    num_classes = int(input("Enter the number of classes: "))
    
    # Input values of relative frequencies
    print("Enter the values of relative frequencies for each class:")
    frequencies = []
    for i in range(num_classes):
        frequency = float(input(f"Frequency for class {i+1}: "))
        frequencies.append(frequency)
    
    # Generate classes based on the number of classes
    classes = list(range(1, num_classes+2))
    
    # Plot histogram with curve
    plot_histogram_curve(classes, frequencies)

if __name__ == "__main__":
    main()
