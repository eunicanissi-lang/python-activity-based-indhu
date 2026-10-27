
# Progressive Water Tariff Analysis

# Water consumption slabs (rate per unit)
SLABS = [
    (100, 5),       # First 100 units: Rs. 5 per unit
    (200, 8),       # Next 100 units: Rs. 8 per unit
    (float("inf"), 12)  # Above 200 units: Rs. 12 per unit
]

FIXED_FEE = 100
PENALTY_LIMIT = 250
PENALTY_RATE = 500
EXCESSIVE_USAGE_LIMIT = 200


# Water consumption of multiple households (units)
households = {
    "Household A": 80,
    "Household B": 150,
    "Household C": 280,
    "Household D": 220,
    "Household E": 350
}


def calculate_bill(consumption):
    """Calculate bill using progressive slabs and penalties."""
    remaining = consumption
    water_charge = 0
    previous_limit = 0

    for limit, rate in SLABS:
        slab_units = min(remaining, limit - previous_limit)
        water_charge += slab_units * rate
        remaining -= slab_units

        if remaining <= 0:
            break

        previous_limit = limit

    fixed_fee = FIXED_FEE
    penalty = PENALTY_RATE if consumption > PENALTY_LIMIT else 0

    total_bill = water_charge + fixed_fee + penalty

    return water_charge, fixed_fee, penalty, total_bill


def analyze_households(households):
    """Compare consumption and identify excessive usage."""
    total_consumption = 0
    total_revenue = 0

    print("=" * 85)
    print("           PROGRESSIVE WATER TARIFF ANALYSIS")
    print("=" * 85)

    print(
        f"{'Household':<15}{'Units':>8}{'Water Charge':>16}"
        f"{'Fixed Fee':>12}{'Penalty':>12}{'Total Bill':>14}"
    )
    print("-" * 85)

    bills = {}

    for name, consumption in households.items():
        water, fixed, penalty, total = calculate_bill(consumption)

        bills[name] = total
        total_consumption += consumption
        total_revenue += total

        print(
            f"{name:<15}{consumption:>8}"
            f"{water:>16.2f}{fixed:>12.2f}"
            f"{penalty:>12.2f}{total:>14.2f}"
        )

    print("-" * 85)

    average = total_consumption / len(households)

    print(f"\nTotal Consumption : {total_consumption} units")
    print(f"Average Usage     : {average:.2f} units")
    print(f"Total Revenue     : Rs. {total_revenue:.2f}")

    # Compare consumption patterns
    highest = max(households, key=households.get)
    lowest = min(households, key=households.get)

    print(f"\nHighest Consumption: {highest} ({households[highest]} units)")
    print(f"Lowest Consumption : {lowest} ({households[lowest]} units)")

    # Identify excessive usage
    print("\nHouseholds with Excessive Water Usage:")
    found = False

    for name, consumption in households.items():
        if consumption > EXCESSIVE_USAGE_LIMIT:
            print(f"- {name}: {consumption} units")
            found = True

    if not found:
        print("No excessive usage detected.")

    # Rank households by consumption
    print("\nConsumption Ranking (Highest to Lowest):")

    ranking = sorted(
        households.items(),
        key=lambda item: item[1],
        reverse=True
    )

    for rank, (name, consumption) in enumerate(ranking, start=1):
        print(f"{rank}. {name}: {consumption} units")


# Run the analysis
analyze_households(households)
