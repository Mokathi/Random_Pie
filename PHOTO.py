def crude_height(h1, H, R1, P1, Rx_values):
    result = []
    actual_heights = []
    for Rx in Rx_values:
        try:
            h_x = h1 + (H - h1) * (Rx - R1) / (P1 + (Rx - R1))
            result.append(round(h_x, 5))
        except ZeroDivisionError:
            result.append(None)

    print("\nEnter the actual heights:")
    for i, Rx in enumerate(Rx_values):
        actual_height = float(input(f"Enter the actual height corresponding to Rx_{i + 1}: "))
        actual_heights.append(actual_height)

    # Calculate Δh as h' - h
    delta_heights = [round(actual - crude, 5) if crude is not None else None for actual, crude in
                     zip(actual_heights, result)]

    return result[:5], delta_heights[:5]


def main():
    try:
        h1 = float(input("Enter the value of h1 in meters: "))
        H = float(input("Enter the value of H in meters: "))
        R1 = float(input("Enter the value of R1 in meters: "))
        P1 = float(input("Enter the value of P1 in meters: "))

        Rx_values = []
        for i in range(5):
            Rx = float(input(f"Enter the value of Rx_{i + 1} in meters: "))
            Rx_values.append(Rx)

        crude_heights, delta_heights = crude_height(h1, H, R1, P1, Rx_values)

        print("\nCrude Heights:")
        print(crude_heights)
        print("\nDelta Heights (Δh = h' - h):")
        print(delta_heights)
    except ValueError:
        print("Invalid input. Please enter numeric values.")


if __name__ == "__main__":
    main()
