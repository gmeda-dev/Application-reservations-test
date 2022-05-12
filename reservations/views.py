from django.db.models import OuterRef, Subquery
from django.views import View
from django.shortcuts import render

from reservations.models import Reservation

class IndexView(View):
    def get_context_data(self):
        reservations_list = []

        previous_reservation = Subquery(
            Reservation.objects.filter(
                date_check_out__lte=OuterRef('date_check_in'),
                rental=OuterRef('rental')
            )
            .order_by('-date_check_in')
            .values('id')[:1]
        )

        reservations = (
            Reservation.objects.all()
            .order_by('rental__name', 'date_check_in')
            .select_related('rental')
            .annotate(previous_reservation=previous_reservation)
        )
        
        for reservation in reservations:
            reservations_list.append({
                'rental_name': reservation.rental.name,
                'reservation_id': reservation.id,
                'check_in': str(reservation.date_check_in),
                'check_out': str(reservation.date_check_out),
                'previous_reservation': (
                    reservation.previous_reservation 
                    if reservation.previous_reservation else '-'
                ),
            })

        return {
            'reservations': reservations_list
        }

    def get(self, request):
        return render(request, 'index.html', self.get_context_data())
