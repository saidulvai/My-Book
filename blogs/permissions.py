from rest_framework import permissions

class IsAuthor(permissions.BasePermission):
    def has_permission(self, request, view):
        if request.method in permissions.SAFE_METHODS:
            return True
        flag = request.user.is_authenticated and hasattr(request.user, 'account') and request.user.profile.user_type == 'Author'
        print(request.user.username)
        print(request.user.is_authenticated)
        print(hasattr(request.user, 'account'))
        print(request.user.profile.user_type == 'Author')
        print("inside has permission", flag)
        return flag
    
    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        flag = request.user.is_authenticated and hasattr(request.user, 'account') and request.user.profile.user_type == 'Author'
        print("inside object permission", flag)
        return flag


class IsAdmin(permissions.BasePermission):
    def has_permission(self, request, view):
        if request.method in permissions.SAFE_METHODS:
            return True
        return request.user.is_authenticated and hasattr(request.user, 'account') and request.user.profile.user_type == 'Admin'
    
    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        return request.user.is_authenticated and hasattr(request.user, 'account') and request.user.profile.user_type == 'Admin'

