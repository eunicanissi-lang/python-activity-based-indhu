
CLASS_RATES = {
    "Sleeper": 1.00,
    "AC3": 2.00,
    "AC2": 3.00,
    "AC1": 4.00
}
def distance_charge(distance):
    if distance <= 100:
        return 20
    elif distance <= 500:
        return 50
    else:
        return 100
RESERVATION_FEE = 40
CHILD_AGE = 5
SENIOR_AGE = 60
CHILD_DISCOUNT = 0.50
SENIOR_DISCOUNT = 0.40
def calculate_fare(distance, travel_class, age):
    if distance <= 0:
        raise ValueError("Distance must be greater than zero.")

    if travel_class not in CLASS_RATES:
        raise ValueError("Invalid travel class.")

    # Basic fare based on distance and class
    basic_fare = distance * CLASS_RATES[travel_class]

    # Add distance-based charge and reservation fee
    extra_charge = distance_charge(distance)
    total = basic_fare + extra_charge + RESERVATION_FEE

    # Apply age-based concession to basic fare
    discount = 0

    if age < 0:
        raise ValueError("Age cannot be negative.")
    elif age < CHILD_AGE:
        discount = basic_fare  # Free basic fare
    elif age >= SENIOR_AGE:
        discount = basic_fare * SENIOR_DISCOUNT

    final_fare = total - discount

    return round(basic_fare, 2), round(discount, 2), round(final_fare, 2)


def cancellation_penalty(fare, cancellation_percent):
    if not 0 <= cancellation_percent <= 100:
        raise ValueError("Cancellation percentage must be between 0 and 100.")

    penalty = fare * cancellation_percent / 100
    refund = fare - penalty

    return round(penalty, 2), round(refund, 2)


def main():
    passengers = []

    distance = float(input("Enter journey distance in km: "))

    if distance <= 0:
        print("Distance must be greater than zero.")
        return

    n = int(input("Enter number of passengers: "))

    if n <= 0:
        print("Number of passengers must be positive.")
        return

    for i in range(n):
        print(f"\nPassenger {i + 1}")

        name = input("Enter passenger name: ")
        age = int(input("Enter passenger age: "))

        print("Classes: Sleeper, AC3, AC2, AC1")
        travel_class = input("Enter travel class: ").strip()

        try:
            basic, discount, fare = calculate_fare(
                distance, travel_class, age
            )

            passengers.append({
                "name": name,
                "age": age,
                "class": travel_class,
                "basic": basic,
                "discount": discount,
                "fare": fare
            })

            print(f"Basic Fare: Rs. {basic:.2f}")
            print(f"Age Concession: Rs. {discount:.2f}")
            print(f"Total Fare: Rs. {fare:.2f}")

        except ValueError as error:
            print("Error:", error)

    # Display passenger fare summary
    print("\n----- Reservation Summary -----")
    total_fare = 0

    for passenger in passengers:
        print(
            f"{passenger['name']} | "
            f"Age: {passenger['age']} | "
            f"Class: {passenger['class']} | "
            f"Fare: Rs. {passenger['fare']:.2f}"
        )
        total_fare += passenger["fare"]

    print(f"\nTotal Reservation Amount: Rs. {total_fare:.2f}")

    # Optional cancellation calculation
    cancel = input("\nCalculate cancellation refund? (yes/no): ").lower()

    if cancel == "yes":
        percent = float(
            input("Enter cancellation penalty percentage (0-100): ")
        )

        try:
            penalty, refund = cancellation_penalty(total_fare, percent)

            print(f"Cancellation Penalty: Rs. {penalty:.2f}")
            print(f"Refund Amount: Rs. {refund:.2f}")

        except ValueError as error:
            print("Error:", error)


if __name__ == "__main__":
    main()




