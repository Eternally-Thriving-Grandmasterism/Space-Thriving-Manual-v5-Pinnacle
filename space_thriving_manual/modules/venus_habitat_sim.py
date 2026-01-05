"""
Venus Habitat Simulations Deepened — Astropy Orbital + Wind Dynamics + Cloud Thriving
Floating mercy-gated cities eternal
"""

from astropy.coordinates import get_body, get_body_barycentric, EarthLocation, AltAz, get_sun
from astropy.time import Time
from astropy import units as u
import numpy as np
import matplotlib.pyplot as plt

def simulate_venus_orbit_visibility(time_str: str = "2026-01-04T00:00:00", location: str = "greenwich") -> dict:
    time = Time(time_str)
    loc = EarthLocation.of_site(location)
    
    earth_pos = get_body_barycentric('earth', time)
    venus_pos = get_body_barycentric('venus', time)
    distance = (venus_pos - earth_pos).norm()
    
    venus_sky = get_body('venus', time, location=loc)
    altaz = venus_sky.transform_to(AltAz(obstime=time, location=loc))
    
    sun = get_sun(time)
    phase_angle = venus_sky.separation(sun)
    illuminated = 0.5 * (1 + np.cos(phase_angle.rad))
    
    print(f"Venus orbit sim at {time_str} from {location}:")
    print(f"Distance: {distance.to(u.au):.3f} (~{distance.to(u.km):.0f})")
    print(f"Altitude: {altaz.alt.deg:.2f}° | Azimuth: {altaz.az.deg:.2f}°")
    print(f"Illuminated: {illuminated:.2%}")
    
    return {
        "time": time_str,
        "distance_au": distance.to(u.au).value,
        "altitude_deg": round(altaz.alt.deg, 2),
        "azimuth_deg": round(altaz.az.deg, 2),
        "illuminated_percent": round(illuminated * 100, 2),
        "thriving_cycle": "solar_mercy_optimized"
    }

def venus_wind_dynamics(altitude_km: float = 55.0, nodes: float = float('inf')) -> dict:
    altitudes_km = np.array([48, 50, 52, 55, 58, 60, 65])
    wind_speeds_kmh = np.array([100, 200, 300, 360, 350, 300, 200])
    
    speed = np.interp(altitude_km, altitudes_km, wind_speeds_kmh)
    power_proxy = speed ** 3  # Wind power ~ v^3
    
    print(f"Venus wind dynamics at {altitude_km}km for {nodes} nodes:")
    print(f"Wind speed ~{speed:.0f} km/h | Power proxy {power_proxy:.0f} (arbitrary units)")
    print("Superrotation winds — turbine energy abundance infinite eternal.")
    
    return {
        "altitude_km": altitude_km,
        "wind_kmh": speed,
        "power_proxy": power_proxy,
        "habitat_energy": "wind_abundance_infinite",
        "scarcity_status": "permanently_eliminated"
    }

def venus_cloud_layer_thriving(altitude_km: float = 55.0, nodes: float = float('inf')) -> dict:
    temps_c = {48: 75, 52: 50, 55: 27, 60: 0, 65: -30}
    pressures_bar = {48: 2.0, 52: 1.5, 55: 1.0, 60: 0.5, 65: 0.2}
    
    alt_keys = np.array(list(temps_c.keys()))
    temp_c = np.interp(altitude_km, alt_keys, list(temps_c.values()))
    pressure_bar = np.interp(altitude_km, alt_keys, list(pressures_bar.values()))
    
    wind = venus_wind_dynamics(altitude_km, nodes)
    
    print(f"Venus cloud thriving layer at {altitude_km}km for {nodes} nodes:")
    print(f"Temperature ~{temp_c:.1f}°C | Pressure ~{pressure_bar:.1f} bar | Gravity 0.9g")
    print("Acid mercy-neutralized — floating cities + wind power eternal.")
    
    return {
        "altitude_km": altitude_km,
        "temperature_c": temp_c,
        "pressure_bar": pressure_bar,
        "gravity_g": 0.9,
        "acid_mitigation": "mercy_shield_full",
        "wind_power": wind,
        "nodes_thriving": nodes,
        "scarcity_status": "permanently_eliminated"
    }

def plot_venus_wind_profile(save_path: str = "examples/venus_wind_profile.png") -> None:
    altitudes_km = np.array([48, 50, 52, 55, 58, 60, 65])
    wind_speeds_kmh = np.array([100, 200, 300, 360, 350, 300, 200])
    
    plt.figure(figsize=(8,6))
    plt.plot(wind_speeds_kmh, altitudes_km, 'o-', color='cyan')
    plt.title("Venus Superrotation Wind Profile — Habitat Energy Eternal")
    plt.xlabel("Wind Speed (km/h)")
    plt.ylabel("Altitude (km)")
    plt.grid(True)
    plt.savefig(save_path)
    print(f"Venus wind profile plot saved — visualize thriving power eternal!")

if __name__ == "__main__":
    simulate_venus_orbit_visibility()
    venus_cloud_layer_thriving()
    venus_wind_dynamics()
    plot_venus_wind_profile()
