def smart_home_system(temperature, humidity, motion_detected):
    if motion_detected:
        print("Motion detected: Turning lights ON")
    else:
        print("No motion: Turning lights OFF")

 
    if temperature > 30:
        print("Temperature is high:", temperature, "Turning fan ON")
    else:
        print("Temperature is normal:", temperature, " Fan OFF")

    if humidity < 30:
        print("Humidity is low:", humidity, "% - Turning humidifier ON")
    elif humidity > 70:
        print("Humidity is high:", humidity, "% - Turning dehumidifier ON")
    else:
        print("Humidity is normal:", humidity, "% - No action needed")

def main():
    print("Welcome to the Smart Home Automation System")

    try:
        temperature = float(input("Enter temperature (degree): "))
        humidity = float(input("Enter humidity (%): "))
        motion_input = input("Is motion detected? (yes/no): ").strip().lower()

        motion_detected = True if motion_input == "yes" else False

        print("\nSmart Home Actions:")

        smart_home_system(temperature, humidity, motion_detected)
     

    except ValueError:
        print("Invalid input. Please enter numeric values for temperature and humidity.")

if __name__ == "__main__":
    main()
