from django.http import HttpRequest, HttpResponse, JsonResponse
from django.views.decorators.http import require_GET


@require_GET
def healthcheck(request: HttpRequest) -> HttpResponse:  # ruff:ignore[unused-function-argument]
    return JsonResponse({'status': 'ok'})
