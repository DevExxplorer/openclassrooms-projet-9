from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from authentificate.models import User
from followers.forms import SearchForm


@login_required
def page_views(request):
    # users = User.objects.all()
    form = SearchForm(request.POST or None)

    if request.method == 'POST':
        search_value = request.POST['search']

        try:
            user = User.objects.get(username=search_value)
            print(user)
        except:
            print("Question does not exist")
    else:
        form = SearchForm(None)

    return render(
        request,
        'followers/page.html',
        {
            'form': form,
            'show_label': False
        }
    )


'''
form = SubscribeForm(request.POST)

if form.is_valid():
user = form.save()
login(request, user)

return redirect("home")
else:
form = SubscribeForm()
'''
