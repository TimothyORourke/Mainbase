from .models import UserPreferences

def user_pref(request):
    if request.user.is_authenticated:
        preferences = UserPreferences.objects.get(user=request.user)
    else:
        preferences = None

    return {
        'user_pref' : preferences,
    }