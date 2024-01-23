def count_rodent_captures_by_site(traps_status_data):
    traps_status_data.loc[traps_status_data["status_trampa"] != "Captura", "status_trampa"] = 0
    traps_status_data.loc[traps_status_data["status_trampa"] == "Captura", "status_trampa"] = 1
    grouped_count = traps_status_data.groupby(by=["Sitio"])[["status_trampa"]].sum()
    return grouped_count.rename(columns={"status_trampa": "captures"})
