#!/usr/bin/env python3
"""
Simulation of energy consumption for mycelium growth phase.
Currently uses fixed growth duration and constant environmental temperature.
"""

def simulate_growth_energy(growth_duration_days, temperature_celsius):
    """
    Simulate energy consumption for mycelium growth.
    
    Args:
        growth_duration_days (float): Number of days for growth phase.
        temperature_celsius (float): Constant environmental temperature in Celsius.
    
    Returns:
        dict: Contains total energy (kWh), climate control energy (kWh), and other metrics.
    """
    # Constants
    BASE_ENERGY_PER_DAY = 10.0  # kWh per day for basic operation (lights, pumps, etc.)
    CLIMATE_CONTROL_COEFF = 0.5  # kWh per day per degree from ideal (ideal = 25°C)
    IDEAL_TEMPERATURE = 25.0
    
    # Calculate climate control energy
    temp_diff = abs(temperature_celsius - IDEAL_TEMPERATURE)
    climate_control_energy = CLIMATE_CONTROL_COEFF * temp_diff * growth_duration_days
    
    # Calculate base energy
    base_energy = BASE_ENERGY_PER_DAY * growth_duration_days
    
    total_energy = base_energy + climate_control_energy
    
    return {
        'total_energy_kWh': total_energy,
        'base_energy_kWh': base_energy,
        'climate_control_energy_kWh': climate_control_energy,
        'growth_duration_days': growth_duration_days,
        'temperature_celsius': temperature_celsius
    }


def main():
    """Example usage."""
    # Default values
    growth_days = 14.0
    temp = 28.0
    
    result = simulate_growth_energy(growth_days, temp)
    print("Mycelium Growth Energy Simulation")
    print("=" * 40)
    print(f"Growth duration: {result['growth_duration_days']} days")
    print(f"Temperature: {result['temperature_celsius']} °C")
    print(f"Base energy: {result['base_energy_kWh']:.2f} kWh")
    print(f"Climate control energy: {result['climate_control_energy_kWh']:.2f} kWh")
    print(f"Total energy: {result['total_energy_kWh']:.2f} kWh")


if __name__ == '__main__':
    main()