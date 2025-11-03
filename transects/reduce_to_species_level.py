def reduce_to_species_level(bird_name: str) -> str:
    return " ".join(bird_name.split(" ")[:2])
