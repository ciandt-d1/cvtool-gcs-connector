# coding: utf-8

"""
    Kingpick Admin API

    Provides APIs for tenant maintenance

    OpenAPI spec version: 0.1.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

# import models into sdk package
from .models.project import Project
from .models.projects import Projects
from .models.settings import Settings
from .models.tenant import Tenant
from .models.tenants import Tenants

# import apis into sdk package
from .apis.auth_api import AuthApi
from .apis.default_api import DefaultApi
from .apis.project_api import ProjectApi
from .apis.tenant_api import TenantApi

# import ApiClient
from .api_client import ApiClient

from .configuration import Configuration

configuration = Configuration()