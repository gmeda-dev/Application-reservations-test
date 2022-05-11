from django.views import View
from django.shortcuts import render

from reservations.models import Reservation

class IndexView(View):
    def get_context_data(self):
        reservations_list = []
        for reservation in Reservation.objects.all().order_by('rental__name', 'date_check_in'):
            previous_reservations = Reservation.objects.filter(
                rental=reservation.rental,
                date_check_out__lte=reservation.date_check_in
            ).exclude(id=reservation.id).order_by('date_check_in')

            reservations_list.append({
                'rental_name': reservation.rental.name,
                'reservation_id': reservation.id,
                'check_in': str(reservation.date_check_in),
                'check_out': str(reservation.date_check_out),
                'previous_reservation': previous_reservations.latest('date_check_in').id if previous_reservations.exists() else '-',
            })

        return {
            'reservations': reservations_list
        }

    def get(self, request):
        return render(request, 'index.html', self.get_context_data())
