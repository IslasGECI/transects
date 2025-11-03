from transects.reduce_to_species_level import reduce_to_species_level


def test_reduce_to_species_level():
    subspecies_name = "Amazona oratrix tresmariae"
    obtained = reduce_to_species_level(subspecies_name)
    expected = "Amazona oratrix"
    assert obtained == expected
