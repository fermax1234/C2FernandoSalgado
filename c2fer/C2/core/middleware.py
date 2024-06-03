from django.contrib.auth import logout

class CloseSessionMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        # Cerrar la sesión al inicio de cada solicitud
        logout(request)
        response = self.get_response(request)
        return response