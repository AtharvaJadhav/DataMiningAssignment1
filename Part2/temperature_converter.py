from dataclasses import dataclass


@dataclass
class TemperatureConverter:
    @staticmethod
    def to_fahrenheit(celsius: float) -> float:
        """Converts a temperature from Celsius to Fahrenheit."""
        return (celsius * 9/5) + 32

    @staticmethod
    def to_celsius(fahrenheit: float) -> float:
        """Converts a temperature from Fahrenheit to Celsius."""
        return (fahrenheit - 32) * 5/9

    # add a new method to convert from celsius to kelvin
    @staticmethod
    def to_kelvin(celsius: float) -> float:
        """Converts a temperature from Celsius to Kelvin."""
        return celsius + 273.15

    # add a new method to convert from kelvin to celsius
    @staticmethod
    def kelvin_to_celsius(kelvin: float) -> float:
        """Converts a temperature from Kelvin to Celsius."""
        return kelvin - 273.15

    # add a new method to convert from fahrenheit to kelvin
    @staticmethod
    def fahrenheit_to_kelvin(fahrenheit: float) -> float:
        """Converts a temperature from Fahrenheit to Kelvin."""
        return (fahrenheit - 32) * 5/9 + 273.15

    # add a new method to convert from kelvin to fahrenheit
    @staticmethod
    def kelvin_to_fahrenheit(kelvin: float) -> float:
        """Converts a temperature from Kelvin to Fahrenheit."""
        return (kelvin - 273.15) * 9/5 + 32


class UserInterface:
    @staticmethod
    def run():
        """Starts the temperature converter app and handles user input and output."""
        print("Welcome to the Temperature Converter App!")
        while True:
            # add a new option to convert from kelvin to celsius
            # add a new option to convert from celsius to kelvin
            # add a new option to convert from fahrenheit to kelvin
            # add a new option to convert from kelvin to fahrenheit

            print("\nPlease select an option:")
            print("1. Convert Celsius to Fahrenheit")
            print("2. Convert Fahrenheit to Celsius")
            # add a new option to convert from kelvin to celsius
            print("3. Convert Kelvin to Celsius")
            # add a new option to convert from celsius to kelvin
            print("4. Convert Celsius to Kelvin")
            # add a new option to convert from fahrenheit to kelvin
            print("5. Convert Fahrenheit to Kelvin")
            # add a new option to convert from kelvin to fahrenheit
            print("6. Convert Kelvin to Fahrenheit")

            print("7. Exit")

            choice = input("Enter your choice (1, 2, 3, 4, 5, 6 or 7): ")

            if choice == "1":
                celsius = float(input("Enter the temperature in Celsius: "))
                fahrenheit = TemperatureConverter.to_fahrenheit(celsius)
                print(f"The temperature in Fahrenheit is: {fahrenheit:.2f}°F")

            elif choice == "2":
                fahrenheit = float(
                    input("Enter the temperature in Fahrenheit: "))
                celsius = TemperatureConverter.to_celsius(fahrenheit)
                print(f"The temperature in Celsius is: {celsius:.2f}°C")

            # add a new option to convert from kelvin to celsius
            elif choice == "3":
                kelvin = float(input("Enter the temperature in Kelvin: "))
                celsius = TemperatureConverter.kelvin_to_celsius(kelvin)
                print(f"The temperature in Celsius is: {celsius:.2f}°C")

            # add a new option to convert from celsius to kelvin
            elif choice == "4":
                celsius = float(input("Enter the temperature in Celsius: "))
                kelvin = TemperatureConverter.to_kelvin(celsius)
                print(f"The temperature in Kelvin is: {kelvin:.2f}°K")

            # add a new option to convert from fahrenheit to kelvin
            elif choice == "5":
                fahrenheit = float(
                    input("Enter the temperature in Fahrenheit: "))
                kelvin = TemperatureConverter.fahrenheit_to_kelvin(fahrenheit)
                print(f"The temperature in Kelvin is: {kelvin:.2f}°K")

            # add a new option to convert from kelvin to fahrenheit
            elif choice == "6":
                kelvin = float(input("Enter the temperature in Kelvin: "))
                fahrenheit = TemperatureConverter.kelvin_to_fahrenheit(kelvin)
                print(f"The temperature in Fahrenheit is: {fahrenheit:.2f}°F")

            elif choice == "7":
                print("Thank you for using the Temperature Converter App!")
                break

            else:
                print("Invalid choice. Please try again.")


if __name__ == "__main__":
    UserInterface.run()
