from django.shortcuts import render
from django.http import HttpResponse
from django.views import View
from .models import Message, Number
from twilio.twiml.messaging_response import MessagingResponse
from django.views.decorators.csrf import csrf_exempt


class WebhookView(View):
    def post(self, request):
        try:
            response = MessagingResponse()

            from_number = request.POST.get("From", None)
            to_number = request.POST.get("To", None)
            message_body = request.POST.get('Body', None)
            print(
                f'from: {from_number}, to_number: {to_number}, message_body: {message_body}')

            # Exception handling for creating the TwilioMessage object
            try:
                Message.objects.create(
                    from_number=from_number,
                    to_number=to_number,
                    message_body=message_body
                )
            except Exception as e:
                print(f"Error creating TwilioMessage object: {e}")
                return HttpResponse("Internal Server Error", status=500)

            return HttpResponse(str(response), status=200)
        except Exception as e:
            print(f"Error processing Twilio webhook: {e}")
            return HttpResponse("Internal Server Error", status=500)

    def get(self, request):
        return HttpResponse("Method not allowed", status=405)


class HomeView(View):
    template_name = 'message/home.html'

    def get(self, request, *args, **kwargs):
        numbers = Number.objects.all()
        context = {
            'numbers': numbers
        }
        return render(request, self.template_name, context)


class ChatWindowView(View):
    template_name = 'message/chat_window.html'

    def get(self, request, number):
        messages = Message.objects.filter(
            to_number=number).values('message_body', 'timestamp')
        # return JsonResponse({'number_instance': number, 'messages': list(messages)})
        print(f'--------------------------{number}---------------{messages}')
        context = {
            # 'number_instance': number,
            'messages': list(messages)
        }
        return render(request, self.template_name, context)
