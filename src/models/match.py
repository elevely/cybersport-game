from dataclasses import dataclass

from models.organization import Organization


@dataclass
class Match:
    organization_a: Organization
    organization_b: Organization