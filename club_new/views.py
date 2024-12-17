from django.shortcuts import render, get_object_or_404
from .models import Club, Slider

# View to display the list of all clubs
def club_list(request):
    clubs = Club.objects.all()
    return render(request, 'club_new/club_list.html', {'clubs': clubs})


def club_detail(request, club_id):
    # Fetch the club details
    club = get_object_or_404(Club, id=club_id)
    
    # Fetch sliders for this specific club
    sliders = Slider.objects.filter(club=club, is_active=True)
    
    # Pass the data to the template
    context = {
        'club': club,
        'sliders': sliders,
    }
    return render(request, 'club_new/club_detail.html', context)
