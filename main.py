# Rule-based weather system using temperature, humidity, and cloudiness

def get_weather_advice(temperature, humidity, cloudiness):
    """
    temperature: in Celsius
    humidity: in percentage (0-100)
    cloudiness: in percentage (0-100)
    """

    advice = []

    # Rule 1: Cold and humid
    if temperature < 18 and humidity > 70:
        advice.append("It's cold and humid. Wear layered clothes and a water-resistant jacket.")

    # Rule 2: Hot and humid
    if temperature > 30 and humidity > 70:
        advice.append("Hot and humid. Stay hydrated and wear light, breathable clothes.")

    # Rule 3: Cold and dry
    if temperature < 18 and humidity < 40:
        advice.append("Cold and dry. Use moisturizer and wear warm clothes.")

    # Rule 4: Cloudy and cold
    if cloudiness > 70 and temperature < 20:
        advice.append("Cloudy and cold. A hoodie or jacket would be good.")

    # Rule 5: High cloudiness (possible rain)
    if cloudiness > 80 and humidity > 60:
        advice.append("Looks like it might rain. Carry an umbrella just in case.")

    # Rule 6: Pleasant weather
    if 20 <= temperature <= 28 and 40 <= humidity <= 60 and cloudiness < 50:
        advice.append("Weather is pleasant. Wear comfortable clothes.")

    # Default message
    if not advice:
        advice.append("No specific advice. Dress comfortably and check the sky.")

    return advice


# Example usage
def main():
    # You can change these values or use input() to get user input
    temperature = float(input("Enter temperature in °C: "))
    humidity = float(input("Enter humidity (%): "))
    cloudiness = float(input("Enter cloudiness (%): "))

    recommendations = get_weather_advice(temperature, humidity, cloudiness)

    print("\n--- Weather Advice ---")
    for item in recommendations:
        print("•", item)


if __name__ == "__main__":
    main()
