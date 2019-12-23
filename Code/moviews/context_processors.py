def include_login_form(request):
    from forms import CustomAuthForm
    form = CustomAuthForm()
    return {'form2': form}


def include_signup_form(request):
    from users.forms import CustomUserCreationForm
    form = CustomUserCreationForm()
    return {'form': form}