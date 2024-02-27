"""
CONSTANTS.py defines variables that are needed throughout this application
"""

# ORGANISATIONS defines a dict with all Organizations in this Project with its abbreviation and  IATI Code

ORGANIZATIONS = {
    "BMZ": ["Bundesministerium für wirtschaftliche Zusammenarbeit und Entwicklung", "bmz", "DE-1"],
    "IAD": ["Inter-American Development Bank", "iad", "XI-IATI-IADB"],
    "ADB": ["Asian Development Bank", "adb", "XM-DAC-46004"],
    "AfDB": ["African Development Bank", "afdb", "XM-DAC-46002"],
    "EIB": ["European Investment Bank", "eib", "XM-DAC-918-3"],
    "WB": ["The World Bank", "wb", "44000"],
    "WBTF": ["World Bank Trust Funds", "wbtf", "XI-IATI-WBTF"],
    "GIZ-NON-BMZ": ["Non BMZ GIZ Activity", "giz-non-bmz", "XM-DAC-5-52"],
    "AA": ["Auswärtiges Amt", "aa", "XM-DAC-5-7"]
}

# IATI_ATTRIBUTES contains all relevant IATI Attributes that have to be fetched

IATI_ATTRIBUTES = [
    "iati_identifier",
    "title_narrative",
    "title_narrative_xml_lang",
    "reporting_org_narrative",
    "reporting_org_ref",
    "contact_info_organisation_narrative",
    "contact_info_department_narrative",
    "description_narrative_xml_lang",
    "description_narrative",
    "recipient_country_code",
    "recipient_region_code",
    "location_name_narrative",
    "activity_status_code",
    "document_link_url",
    "last_updated_datetime",
    "activity_date_type",
    "activity_date_iso_date",
    "sector_code",
    "sector_vocabulary",
]