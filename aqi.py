def calculate_aqi(concentration):
    """
    Calculates a simplified Air Quality Index based on PM2.5 concentration present in the air baser on the data from sensors.
    """
    if 0 <= concentration <= 12:
        return "Good", "Green"
    elif 12.1 <= concentration <= 35.4:
        return "Moderate", "Yellow"
    elif 35.5 <= concentration <= 55.4:
        return "Unhealthy for Sensitive Groups", "Orange"
    elif 55.5 <= concentration <= 150.4:
        return "Unhealthy", "Red"
    elif 150.5 <= concentration <= 250.4:
        return "Very Unhealthy", "Purple"
    else:
        return "Hazardous", "Maroon"

def main():
    try:
        val = float(input("Enter PM2.5 concentration (ug/m3): "))
        status, color = calculate_aqi(val)
        print(f"Air Quality Status: {status}")
        print(f"Alert Color: {color}")
    except ValueError:
        print("Invalid input. Please enter a numerical value.")

if __name__ == "__main__":
    main()
