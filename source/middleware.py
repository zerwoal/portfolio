from django.utils.deprecation import MiddlewareMixin

class SaveLastPageMiddleware(MiddlewareMixin):
    def process_request(self, request):
        if 'last_page' in request.session:
            request.last_page = request.session['last_page']
        else:
            request.last_page = None

    def process_response(self, request, response):
        if request.method == 'GET' and not request.headers.get('X-Requested-With') == 'XMLHttpRequest':
            request.session['last_page'] = request.build_absolute_uri()
        return response