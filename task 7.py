
# Environmental Monitoring Data Analyzer

# Nested lists of environmental readings
# Format: [Location, [Reading1, Reading2, Reading3, ...]]

air_quality_data = [
    ["Location A", [45, 55, 60, 50]],
    ["Location B", [110, 125, 130, 115]],
    ["Location C", [75, 80, 85, 70]],
    ["Location D", [180, 195, 200, 190]]
]

water_quality_data = [
    ["River A", [6.8, 7.0, 7.2, 6.9]],
    ["River B", [5.2, 5.5, 5.0, 5.3]],
    ["Lake A", [7.5, 7.8, 8.0, 7.6]],
    ["Lake B", [9.0, 9.2, 8.9, 9.1]]
]


def classify_air_quality(value, thresholds):
    """Classify air quality using supplied thresholds."""
    if value <= thresholds[0]:
        return "Good"
    elif value <= thresholds[1]:
        return "Moderate"
    elif value <= thresholds[2]:
        return "Poor"
    else:
        return "Very Poor"


def classify_water_quality(value, thresholds):
    """Classify water pH using supplied thresholds."""
    if thresholds[0] <= value <= thresholds[1]:
        return "Normal"
    else:
        return "Outside Normal Range"


def analyze_data(data, data_type, thresholds):
    """Calculate averages, extremes, and classifications."""

    all_readings = []

    print("\n" + "=" * 75)
    print(f"{data_type.upper()} MONITORING REPORT")
    print("=" * 75)

    print(
        f"{'Location':<15}{'Average':>12}"
        f"{'Minimum':>12}{'Maximum':>12}{'Classification':>24}"
    )
    print("-" * 75)

    for location, readings in data:
        if not readings:
            print(f"{location:<15} No readings available")
            continue

        average = sum(readings) / len(readings)
        minimum = min(readings)
        maximum = max(readings)

        all_readings.extend(readings)

        # Classify the average reading
        if data_type == "Air Quality":
            category = classify_air_quality(average, thresholds)
        else:
            category = classify_water_quality(average, thresholds)

        print(
            f"{location:<15}{average:>12.2f}"
            f"{minimum:>12.2f}{maximum:>12.2f}"
            f"{category:>24}"
        )

    if all_readings:
        print("-" * 75)
        print(f"Overall Average: {sum(all_readings) / len(all_readings):.2f}")
        print(f"Overall Minimum: {min(all_readings):.2f}")
        print(f"Overall Maximum: {max(all_readings):.2f}")


# User-defined threshold values
# Air-quality example thresholds (illustrative PM2.5 values)
AIR_THRESHOLDS = [30, 60, 90]

# Water pH normal range (illustrative)
WATER_THRESHOLDS = [6.5, 8.5]


# Run analyses
analyze_data(
    air_quality_data,
    "Air Quality",
    AIR_THRESHOLDS
)

analyze_data(
    water_quality_data,
    "Water Quality",
    WATER_THRESHOLDS
)
