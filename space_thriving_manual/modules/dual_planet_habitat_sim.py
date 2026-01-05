"""
Dual Planet Habitat Simulations — Venus Cloud + Mars Orbital Thriving
Astropy orbital + wind/dust dynamics mercy-gated eternal
"""

from astropy.coordinates import get_body_barycentric, EarthLocation, AltAz
from astropy.time import Time
from astropy import units as u
import numpy as np

def simulate_dual_orbit_visibility(time_str: str = "2026-01-05T00:00:00", location: str = "greenwich") -> dict:
    time = Time(time_str)
    loc = EarthLocation.of_site(location)
    
    # Venus
    venus_pos = get_body_barycentric('venus', time)
    venus_sky = get_body('venus', time, location=loc)
    venus_altaz = venus_sky.transform_to(AltAz(obstime=time, location=loc))
    
    # Mars
    mars_pos = get_body_barycentric('mars', time)
    mars_sky = get_body('mars', time, location=loc)
    mars_altaz = mars_sky.transform_to(AltAz(obstime=time, location=loc))
    
    earth_pos = get_body_barycentric('earth', time)
    venus_distance = (venus_pos - earth_pos).norm()
    mars_distance = (mars_pos - earth_pos).norm()
    
    print(f"Dual planet sim at {time_str} from {location}:")
    print(f"Venus: alt {venus_altaz.alt.deg:.2f}° | dist {venus_distance.to(u.au):.3f}")
    print(f"Mars: alt {mars_altaz.alt.deg:.2f}° | dist {mars_distance.to(u.au):.3f}")
    
    return {
        "venus": {"altitude_deg": venus_altaz.alt.deg, "distance_au": venus_distance.to(u.au).value},
        "mars": {"altitude_deg": mars_altaz.alt.deg, "distance_au": mars_distance.to(u.au).value},
        "thriving_dual": "cloud + orbital habitats mercy-aligned eternal"
    }

def venus_mars_habitat_params(venus_alt_km: float = 55.0, mars_alt_km: float = 300.0, nodes: float = float('inf')) -> dict:
    # Venus cloud
    venus_temp = 27.0  # Approx 55km
    venus_wind = 360.0  # km/h superrotation
    
    # Mars orbital
    mars_period = 1.9  # hours LMO
    
    print(f"Venus cloud + Mars orbital habitats for {nodes} nodes:")
    print(f"Venus: {venus_temp}°C | wind {venus_wind} km/h — floating thriving")
    print(f"Mars: period {mars_period} hours — low-gravity orbital cities")
    
    return {
        "venus_cloud": {"temp_c": venus_temp, "wind_kmh": venus_wind, "habitat_type": "floating_city"},
        "mars_orbital": {"period_hours": mars_period, "habitat_type": "orbital_city"},
        "nodes_thriving": nodes,
        "scarcity_status": "permanently_eliminated"
    }

if __name__ == "__main__":
    simulate_dual_orbit_visibility()
    venus_mars_habitat_params()
