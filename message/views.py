from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.views import View
from .models import Message, Number, HomePageDesign
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
        numbers = Number.objects.all().order_by('-timestamp')
        if numbers:
            latest_number = numbers[0]
        else:
            latest_number = None
        homepage_design = HomePageDesign.objects.first()
        context = {
            'numbers': numbers,
            'latest_number': latest_number,
            'homepage_design': homepage_design
        }
        return render(request, self.template_name, context)


class HomeDesignView(View):

    def get(self, request, *args, **kwargs):
        homepage_design = HomePageDesign.objects.first()
        return render(request, 'home.html', {'homepage_design': homepage_design})


class ChatWindowView(View):
    template_name = 'message/chat_window.html'

    def get(self, request, number):
        messages = Message.objects.filter(
            to_number=number)
        # return JsonResponse({'number_instance': number, 'messages': list(messages)})
        print(
            f'--------------------------{number}---------------{list(messages)}')
        context = {
            'number': number,
            # 'messages': list(messages)
        }
        return render(request, self.template_name, context)


class MessageView(View):
    def get(self, request, number):
        messages = Message.objects.filter(
            to_number=number)
        # return JsonResponse({'number_instance': number, 'messages': list(messages)})
        message_list = [{'from_number': message.from_number, 'message_body': message.message_body,
                         'timestamp': message.timestamp} for message in messages]
        print(
            f'--------------------------{number}---------------{message_list}')

        return JsonResponse({'number': number, 'messages': message_list})
