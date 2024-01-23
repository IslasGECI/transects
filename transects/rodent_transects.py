def count_rodent_captures_by_site(traps_status_data):
    identify_captures(traps_status_data)
    grouped_count = traps_status_data.groupby(by=["Sitio"])[["status_trampa"]].sum()
    return grouped_count.rename(columns={"status_trampa": "captures"})


def identify_captures(traps_status_data):
    is_not_capture = traps_status_data["status_trampa"] != "Captura"
    traps_status_data.loc[is_not_capture, "status_trampa"] = 0
    is_capture = traps_status_data["status_trampa"] == "Captura"
    traps_status_data.loc[is_capture, "status_trampa"] = 1
