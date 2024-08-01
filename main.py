from MH410D import MH410D_CO2

if __name__ == "__main__":
    sensor = MH410D_CO2()

    # Reading gas concentration
    concentration_ppm = sensor.read_gas_concentration()
    if concentration_ppm is not None:
        print(f"Gas concentration: {concentration_ppm} ppm")
        print(f"Gas concentration: {sensor.ppm_to_percent(concentration_ppm)} %")

        # Example conversion to mg/m3 for carbon dioxide (CO2), molar mass 44 g/mol
        concentration_mg_m3 = sensor.ppm_to_mg_m3(concentration_ppm, molar_mass=44)
        print(f"Gas concentration: {concentration_mg_m3} mg/m3")

    # Sensor calibration
    sensor.calibrate_zero()
    sensor.calibrate_span()

    # Closing the port
    sensor.close()