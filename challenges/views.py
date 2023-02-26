from django.shortcuts import render
from django.http import Http404, HttpResponseNotFound, HttpResponseRedirect
from django.urls import reverse

monthly_challenges_dict = {
    "january": ["drink water"],
    "february": ["walk 15 min a day", "eat 1 onion a day", "wake up before 5:00"],
    "march": ["sleep 8 hours a day"],
    "april": ["go to the gym twice a week"],
    "may": ["run 30 min a day"],
    "june": ["read 5 books"],
    "july": ["drink no energy drinks"],
    "august": ["drink no alcohol"],
    "september": ["20 push ups a day"],
    "october": ["go to sleep before 23:00"],
    "november": ["eat no sugar"],
    "december": None
}

# Create your views here.


def index(request):
    months = list(monthly_challenges_dict.keys())

    return render(request, "challenges/index.html", {
        "months": months
    })


def monthly_challenge_num(request, month):
    months = list(monthly_challenges_dict.keys())

    if month > len(months):
        return HttpResponseNotFound("Invalid number")

    redirect_month = months[month - 1]
    redirect_path = reverse("month-challenge", args=[redirect_month])
    return HttpResponseRedirect(redirect_path)


def monthly_challenge(request, month):
    try:
        challenge_text = monthly_challenges_dict[month]
        return render(request, "challenges/challenge.html", {
            "text": challenge_text,
            "month_name": month
        })
    except KeyError:
        raise Http404()
