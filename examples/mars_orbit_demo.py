from space_thriving_manual.modules.mars_habitat_sim import simulate_mars_orbit_transfer, mars_orbital_habitat

simulate_mars_orbit_transfer("2026-01-04")
mars_orbital_habitat(altitude_km=300.0, nodes=10**12)
print("Mars orbital habitats thriving — red planet abundance eternal!")
