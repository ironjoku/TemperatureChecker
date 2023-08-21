def get_temperature_unit():
    unit_choice = input("Choose temperature unit (Celsius or Fahrenheit): ")
    return unit_choice.lower()

def convert_to_celsius(fahrenheit_temp):
    celsius_temp = (fahrenheit_temp - 32) * 5/9
    return celsius_temp

def check_fever(temp, threshold):
    if temp >= threshold:
        return True
    else:
        return False

def main():
    students = ["James", "Amaka", "Yinka", "Kene", "Tunde", "Chima"]
    fever_threshold = 38.0  # Celsius by default

    unit_choice = get_temperature_unit()
    if unit_choice == "fahrenheit":
        fever_threshold = convert_to_celsius(fever_threshold)

    temperature_data = {}

    for student in students:
        temp_str = input(f"Hello {student}, Enter your temperature: ")
        try:
            temp = float(temp_str)
            temperature_data[student] = temp

            if check_fever(temp, fever_threshold):
                print(f"Hello {student}, you have a fever.")
            else:
                print("No fever.")

        except ValueError:
            print("Invalid input. Please enter a valid temperature.")

    print("Temperature Check Complete for all students.")

    if temperature_data:
        calculate_and_display_statistics(temperature_data)
    else:
        print("No temperature data available.")

def calculate_and_display_statistics(data):
    avg_temp = sum(data.values()) / len(data)
    max_temp = max(data.values())
    min_temp = min(data.values())

    print(f"Average Temperature: {avg_temp:.2f}")
    print(f"Maximum Temperature: {max_temp:.2f}")
    print(f"Minimum Temperature: {min_temp:.2f}")

if __name__ == "__main__":
    main()
