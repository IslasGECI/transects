def count_rodent_captures_by_site(traps_status_data):
    identify_captures(traps_status_data)
    return traps_status_data.groupby(by=["Sitio"])[["captures"]].sum()


def identify_captures(traps_status_data):
    is_not_capture = traps_status_data["status_trampa"] != "Captura"
    traps_status_data.loc[is_not_capture, "captures"] = 0
    is_capture = traps_status_data["status_trampa"] == "Captura"
    traps_status_data.loc[is_capture, "captures"] = 1
