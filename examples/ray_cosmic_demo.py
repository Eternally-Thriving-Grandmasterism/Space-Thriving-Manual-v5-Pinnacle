from space_thriving_manual import SpaceThrivingEngine

engine = SpaceThrivingEngine()
times = ["2026-01-04", "2026-07-04", "2027-01-04", "2027-07-04"]
orbits = engine.distributed_ray_orbits(times)
print(orbits)

batch = engine.mega_ray_habitat_batch(num_actors=12)
print(f"Mega batch results: {len(batch)} actors — thriving distributed eternal!")
