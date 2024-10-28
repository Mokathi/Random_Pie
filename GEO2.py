import numpy as np
import matplotlib.pyplot as plt

def plot_histogram_curve(classes, frequencies, curve_color='red', curve_style='-'):
    # Calculate the midpoint of each class
    midpoints = [(classes[i] + classes[i+1]) / 2 for i in range(len(classes) - 1)]

    # Plot histogram
    plt.figure(figsize=(10, 5))
    plt.bar(midpoints, frequencies, width=np.diff(classes), align='center', edgecolor='black', alpha=0.7)
    
    # Plot first curve
    x_curve = np.linspace(classes[0], classes[-1], 100)
    y_curve = np.interp(x_curve, midpoints, frequencies)
    plt.plot(x_curve, y_curve, color=curve_color, linestyle=curve_style, linewidth=2, label='Curve 1')

    # Plot second curve
    y_curve_smooth = np.convolve(y_curve, np.ones(10)/10, mode='valid') # Smooth the curve
    x_curve_smooth = np.linspace(classes[0], classes[-1], len(y_curve_smooth))
    plt.plot(x_curve_smooth, y_curve_smooth, color='blue', linestyle='--', linewidth=2, label='Curve 2')

    plt.xlabel('Classes')
    plt.ylabel('Relative Freq')
    plt.title('Relative Freq Against Class No.s')
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
    
    # Plot histogram with curves
    plot_histogram_curve(classes, frequencies)

if __name__ == "__main__":
    main()
