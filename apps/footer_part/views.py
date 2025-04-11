from django.shortcuts import render

cookies_update = 'cookies update'
conditions_update = 'conditions update'
privacy_update = 'privacy update'

# Create your views here.
def index(request):
    return render(request, 'footer.html',{
        'index_page': 'Pied de page',
    })

def cookie_policy(request):
    return render(request, 'cookies.html', {
        'index_page': 'Politique de cookies',
        "update_date" : cookies_update,
    })

def general_conditions(request):
    return render(request, 'general_conditions.html', {
        'index_page': 'Conditions generales',
        "update_date" : conditions_update,
    })

def privacy_chart(request):
    return render(request, 'privacy.html', {
        'index_page': 'Charte de confidentialite',
        "update_date" : privacy_update,
    })