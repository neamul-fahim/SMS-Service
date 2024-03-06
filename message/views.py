from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.views import View
from .models import Message, Number, HomePageDesign
from twilio.twiml.messaging_response import MessagingResponse
from django.views.decorators.csrf import csrf_exempt
from datetime import datetime


class WebhookView(View):
    def post(self, request):
        try:
            response = MessagingResponse()

            from_number = request.POST.get("From", None)
            to_number = request.POST.get("To", None)
            message_body = request.POST.get('Body', None)
            print(
                f'from: {from_number}, to_number: {to_number}, message_body: {message_body}')

            number, _ = Number.objects.get_or_create(number=to_number)

            # Create the Message object associated with the Number
            try:
                message = Message.objects.create(
                    from_number=from_number,
                    to_number=number,  # Associate with the Number object
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

        for number in numbers:
            messages = Message.objects.filter(
                to_number=number)
            # ----------------------- message count
            number.message_count = messages.count()

            last_message = messages.order_by('-timestamp').first()

            if last_message:
                time_difference = datetime.now().date() - last_message.timestamp.date()
                days = time_difference.days
                last_message_time_passed = f"{days} {'day' if days == 1 else 'days'} ago"
            else:
                last_message_time_passed = "0 SMS"
            # --------- last_message_time_passed
            number.last_message_time_passed = last_message_time_passed

            time_difference = datetime.now().date() - number.timestamp.date()

            years_passed = time_difference.days // 365
            months_passed = time_difference.days // 30
            days_passed = time_difference.days

            # Determine the appropriate message based on the time passed
            if years_passed > 0:
                time_message = f"{years_passed} {'year' if years_passed == 1 else 'years'} ago"
            elif months_passed > 0:
                time_message = f"{months_passed} {'month' if months_passed == 1 else 'months'} ago"
            else:
                time_message = f"{days_passed} {'day' if days_passed == 1 else 'days'} ago"

            number.time_passed = time_message  # ----------- time passed since number added

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

        number = Number.objects.get(number=number)
        messages = Message.objects.filter(
            to_number=number)

        context = {
            'number': number,
            # 'messages': (messages)
        }
        return render(request, self.template_name, context)


class MessageView(View):
    def get(self, request, number):
        print(f"------------------------------{number}")
        number = Number.objects.get(number=number)
        messages = Message.objects.filter(
            to_number=number)
        # return JsonResponse({'number_instance': number, 'messages': list(messages)})
        message_list = [{'from_number': message.from_number, 'message_body': message.message_body,
                         'timestamp': message.timestamp} for message in messages]
        number = {
            'number': number.number,
            'country': number.country,
        }
        print(
            f'--------------------------{number}---------------{message_list}')

        return JsonResponse({'number': number, 'messages': message_list})
