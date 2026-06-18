from services.org_factory import create_test_org

organization_names = [
    "NAVI",
    "Spirit",
    "Vitality",
    "G2",
    "FaZe",
    "MOUZ",
    "Astralis",
    "Falcons",
    "Liquid",
    "The MongolZ"
] 

ORGANIZATIONS = [
    create_test_org(org)
    for org in organization_names
]