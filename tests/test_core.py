from space_thriving_manual import SpaceThrivingEngine

def test_manifest():
    engine = SpaceThrivingEngine()
    result = engine.manifest_habitat()
    assert "scarcity_status" in result and result["scarcity_status"] == "permanently_eliminated"
