def calculate_trapping_success(traps_status_data):
    joined_capture_and_effort = join_rodent_captures_and_effort(traps_status_data)
    joined_capture_and_effort["trapping_success"] = (
        joined_capture_and_effort["captures"] / joined_capture_and_effort["effort"]
    ) * 100
    return joined_capture_and_effort


def count_rodent_captures_by_site(traps_status_data):
    identify_captures(traps_status_data)
    return traps_status_data.groupby(by=["Sitio"])[["captures"]].sum()


def identify_captures(traps_status_data):
    is_capture = traps_status_data["status_trampa"] == "Captura"
    traps_status_data.loc[is_capture, "captures"] = 1


def calculate_rodent_effort_by_site(traps_status_data):
    traps_status_data.dropna(subset=["status_trampa"], inplace=True)
    traps_status_data["effort"] = 1
    return traps_status_data.groupby(by=["Sitio"])[["effort"]].sum()


def join_rodent_captures_and_effort(traps_status_data):
    captures = count_rodent_captures_by_site(traps_status_data)
    effort = calculate_rodent_effort_by_site(traps_status_data)
    return captures.join(effort)
