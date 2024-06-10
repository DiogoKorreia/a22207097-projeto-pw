from django.contrib.auth.decorators import login_required
from django.core.exceptions import PermissionDenied

def group_required(*group_names):
    def decorator(view_func):
        @login_required
        def _wrapped_view(request, *args, **kwargs):
            if request.user.groups.filter(name__in=group_names).exists():
                return view_func(request, *args, **kwargs)
            raise PermissionDenied
        return _wrapped_view
    return decorator
