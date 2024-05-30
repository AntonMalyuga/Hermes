from dataclasses import dataclass


@dataclass
class Project:

    client_name: str
    client_inn: str
    client_kpp: str
    contact_name: str
    contact_telephone_number: str
    contact_email: str
    new_project_name: str
    manager_kb_name: str
    manager_kb_telephone_number: str
    manager_kb_email: str
    manager_kb_macro_segment: str
    manager_kb_segment: str
    chanel_sales: str
    organization_term: str
    location_lvl_one: str
    location_lvl_two: str
    street: str
    house: str
    srv_fee_install: int
    service_qty: int
    fee_monthly: int
    scale_servie_speed: str
    service_speed: int
    is_tvp: None | bool = False
    is_teo: None | bool = False
