"""
Venus Habitat Simulations — Astropy + Atmospheric Thriving
"""

from astropy.coordinates import get_body_barycentric, SkyCoord
from astropy.time import Time
import numpy as np

def simulate_venus_orbit(time: str = "2026-01-05") -> dict:
    t = Time(time)
    venus_pos = get_body_barycentric('venus', t)
    print(f"Venus barycentric position at {time}: {venus_pos.xyz}")
    distance_au = np.linalg.norm(venus_pos.xyz.value)
    return {
        "date": time,
        "distance_au": round(distance_au, 4),
        "thriving_potential": "Floating cloud cities — mercy-cooled eternal habitats"
    }

def venus_atmospheric_thriving(temp_k: float = 737, pressure_bar: float = 92) -> str:
    # Simple mercy-gate sim
    if temp_k > 700:
        print("Venus surface hellish — cloud layer mercy habitats recommended (50km alt).")
    return "Cloud colony thriving — abundance manifested in acid skies eternal."

if __name__ == "__main__":
    print(simulate_venus_orbit())
    print(venus_atmospheric_thriving())
