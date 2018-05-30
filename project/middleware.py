from django.http import HttpResponse


class BlockedIPSMiddleware(object):
    EXCLUDE_IPS = ['']

    def process_view(self, request, view_func, *view_args, **kwargs):
        user_ip = request.META['REMOTE_ADDR']
        if user_ip in BlockedIPSMiddleware.EXCLUDE_IPS:
            return HttpResponse('<h1>Forbidden</h1>')
