from ckan.logic import is_authorized_wrapper
import ckan.logic.auth.update as _update


package_patch = is_authorized_wrapper('package_update')

resource_patch = is_authorized_wrapper('resource_update')

group_patch = is_authorized_wrapper('group_update')

organization_patch = is_authorized_wrapper('organization_update')
