
"""
Mining Production & Haulage Calculator
Version: 1.0

Purpose:
Estimate truck haulage productivity using cycle time,
fleet size, payload capacity, operating hours and utilization.
ES:
Estimar la productividad del transporte mediante camiones utilizando el tiempo de ciclo,
el tamaño de la flota, la capacidad de carga útil, las horas de operación y el nivel de utilización.

Note:
This is an educational model. It does not account for
truck interactions, queues, road conditions or breakdown
distributions.
ES:
Este es un modelo educativo. No contempla
las interacciones entre camiones, las colas, las condiciones de la vía ni
la distribución de las averías.
"""


def get_positive_float(prompt):
    """Ask for a positive numerical value."""
    while True:
        try:
            value = float(input(prompt))

            if value <= 0:
                print("Please enter a value greater than zero.")
                continue

            return value

        except ValueError:
            print("Invalid input. Please enter a number.")


def get_positive_int(prompt):
    """Ask for a positive integer."""
    while True:
        try:
            value = int(input(prompt))

            if value <= 0:
                print("Please enter an integer greater than zero.")
                continue

            return value

        except ValueError:
            print("Invalid input. Please enter a whole number.")


def get_percentage(prompt):
    """Ask for a percentage between 0 and 100."""
    while True:
        try:
            value = float(input(prompt))

            if 0 <= value <= 100:
                return value / 100

            print("Please enter a percentage between 0 and 100.")

        except ValueError:
            print("Invalid input. Please enter a number.")


def calculate_cycle_time(
    loading_time,
    loaded_haul_time,
    dumping_time,
    empty_return_time,
    waiting_time
):
    """Calculate the complete truck cycle time in minutes."""
    return (
        loading_time
        + loaded_haul_time
        + dumping_time
        + empty_return_time
        + waiting_time
    )


def calculate_productivity(
    truck_capacity,
    number_of_trucks,
    cycle_time,
    operating_hours,
    utilization
):
    """Calculate estimated hourly and daily production."""

    cycles_per_hour_per_truck = 60 / cycle_time

    theoretical_hourly_production = (
        truck_capacity
        * cycles_per_hour_per_truck
        * number_of_trucks
    )

    effective_hourly_production = (
        theoretical_hourly_production * utilization
    )

    daily_production = (
        effective_hourly_production * operating_hours
    )

    daily_cycles_per_truck = (
        cycles_per_hour_per_truck
        * operating_hours
        * utilization
    )

    return {
        "cycles_per_hour_per_truck": cycles_per_hour_per_truck,
        "theoretical_hourly_production": theoretical_hourly_production,
        "effective_hourly_production": effective_hourly_production,
        "daily_production": daily_production,
        "daily_cycles_per_truck": daily_cycles_per_truck,
    }


def print_report(
    truck_capacity,
    number_of_trucks,
    cycle_time,
    operating_hours,
    utilization,
    results
):
    """Display the production report."""

    print("\n" + "=" * 52)
    print("       MINING PRODUCTION & HAULAGE CALCULATOR")
    print("=" * 52)

    print("\nINPUT SUMMARY")
    print("-" * 52)
    print(f"Truck payload capacity:       {truck_capacity:.2f} t")
    print(f"Number of trucks:             {number_of_trucks}")
    print(f"Cycle time:                   {cycle_time:.2f} min")
    print(f"Operating hours per day:      {operating_hours:.2f} h")
    print(f"Utilization:                  {utilization * 100:.1f}%")

    print("\nPRODUCTIVITY RESULTS")
    print("-" * 52)
    print(
        "Cycles per hour per truck:    "
        f"{results['cycles_per_hour_per_truck']:.2f}"
    )
    print(
        "Theoretical production:       "
        f"{results['theoretical_hourly_production']:.2f} t/h"
    )
    print(
        "Effective production:        "
        f"{results['effective_hourly_production']:.2f} t/h"
    )
    print(
        "Estimated daily production:  "
        f"{results['daily_production']:.2f} t/day"
    )
    print(
        "Effective cycles/truck/day:  "
        f"{results['daily_cycles_per_truck']:.2f}"
    )

    print("\nMODEL ASSUMPTIONS")
    print("-" * 52)
    print("- All trucks have the same payload and cycle time.")
    print("- Utilization is applied to the theoretical production.")
    print("- Truck queues and interactions are not simulated.")
    print("- Results are estimates, not operational guarantees.")
    print("=" * 52)


def main():
    """Run the calculator."""

    print("=" * 52)
    print("       MINING PRODUCTION & HAULAGE CALCULATOR")
    print("=" * 52)

    print("\nEnter the operating parameters:\n")

    # Fleet parameters
    truck_capacity = get_positive_float(
        "Truck payload capacity (tonnes): "
    )

    number_of_trucks = get_positive_int(
        "Number of trucks: "
    )

    # Cycle components, in minutes
    loading_time = get_positive_float(
        "Loading time (min): "
    )

    loaded_haul_time = get_positive_float(
        "Loaded haul time (min): "
    )

    dumping_time = get_positive_float(
        "Dumping time (min): "
    )

    empty_return_time = get_positive_float(
        "Empty return time (min): "
    )

    waiting_time = get_positive_float(
        "Waiting time per cycle (min): "
    )

    # Operating parameters
    operating_hours = get_positive_float(
        "Operating hours per day: "
    )

    utilization = get_percentage(
        "Utilization percentage (0-100): "
    )

    # Calculations
    cycle_time = calculate_cycle_time(
        loading_time,
        loaded_haul_time,
        dumping_time,
        empty_return_time,
        waiting_time
    )

    results = calculate_productivity(
        truck_capacity,
        number_of_trucks,
        cycle_time,
        operating_hours,
        utilization
    )

    # Report
    print_report(
        truck_capacity,
        number_of_trucks,
        cycle_time,
        operating_hours,
        utilization,
        results
    )


if __name__ == "__main__":
    main()
