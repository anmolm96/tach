from modguard import Boundary
from .domain_one.interface import domain_one_interface
from .domain_three.api import public_for_domain_two

# modguard-ignore
from .domain_two.other import internal_api

Boundary()