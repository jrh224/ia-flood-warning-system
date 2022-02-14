def plot_water_levels(station, dates, levels):
    # Plots water level data against time for a given station. Ensure both input arrays are equal length.
    import matplotlib.pyplot as plt
    from datetime import datetime, timedelta



    plt.plot(dates, levels)
    plt.axhline(y=station.typical_range[0], color='grey', linestyle='--')
    plt.axhline(y=station.typical_range[1], color='grey', linestyle='--')


    plt.xlabel('date')
    plt.ylabel('water level (m)')
    plt.xticks(rotation=45)
    plt.title(station.name)

    plt.tight_layout()
    plt.show()
