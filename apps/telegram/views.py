from telegram import Update
from django.http import JsonResponse
import json
from django.views.decorators.csrf import csrf_exempt

from apps.telegram.dispatcher import bot, dispatcher


@csrf_exempt
def message_handler(request):
    update = Update.de_json(json.loads(request.body), bot)
    dispatcher.process_update(update)
    return JsonResponse({"ok": True})
