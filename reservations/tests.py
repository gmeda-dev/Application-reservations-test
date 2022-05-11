
from datetime import date

from django.test import TestCase
from django.urls import reverse


from reservations.models import Rental, Reservation

class TestReservations(TestCase):
    def setUp(self) -> None:
        self.rental1 = Rental.objects.create(name='Rental-1')
        self.rental2 = Rental.objects.create(name='Rental-2')

        self.reservation1 = Reservation.objects.create(
            id='Res-1',
            date_check_in=date(2022, 1, 1),
            date_check_out=date(2022, 1, 13),
            rental=self.rental1
        )
        self.reservation2 = Reservation.objects.create(
            id='Res-2',
            date_check_in=date(2022, 1, 20),
            date_check_out=date(2022, 2, 10),
            rental=self.rental1
        )
        self.reservation3 = Reservation.objects.create(
            id='Res-3',
            date_check_in=date(2022, 2, 20),
            date_check_out=date(2022, 3, 10),
            rental=self.rental1
        )
        self.reservation4 = Reservation.objects.create(
            id='Res-4',
            date_check_in=date(2022, 1, 2),
            date_check_out=date(2022, 1, 20),
            rental=self.rental2
        )
        self.reservation5 = Reservation.objects.create(
            id='Res-5',
            date_check_in=date(2022, 1, 20),
            date_check_out=date(2022, 2, 11),
            rental=self.rental2
        )
        

    def test_order_reservations(self):
        url = reverse('reservations:index')
        response = self.client.get(url)

        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.context['reservations']), 5)

        self.assertDictEqual(response.context['reservations'][0], {
            'rental_name': self.reservation1.rental.name,
            'reservation_id': self.reservation1.id,
            'check_in': str(self.reservation1.date_check_in),
            'check_out': str(self.reservation1.date_check_out),
            'previous_reservation': '-',
        })
        self.assertDictEqual(response.context['reservations'][1], {
            'rental_name': self.reservation2.rental.name,
            'reservation_id': self.reservation2.id,
            'check_in': str(self.reservation2.date_check_in),
            'check_out': str(self.reservation2.date_check_out),
            'previous_reservation': self.reservation1.id,
        })
        self.assertDictEqual(response.context['reservations'][2], {
            'rental_name': self.reservation3.rental.name,
            'reservation_id': self.reservation3.id,
            'check_in': str(self.reservation3.date_check_in),
            'check_out': str(self.reservation3.date_check_out),
            'previous_reservation': self.reservation2.id,
        })
        self.assertDictEqual(response.context['reservations'][3], {
            'rental_name': self.reservation4.rental.name,
            'reservation_id': self.reservation4.id,
            'check_in': str(self.reservation4.date_check_in),
            'check_out': str(self.reservation4.date_check_out),
            'previous_reservation': '-',
        })
        self.assertDictEqual(response.context['reservations'][4], {
            'rental_name': self.reservation5.rental.name,
            'reservation_id': self.reservation5.id,
            'check_in': str(self.reservation5.date_check_in),
            'check_out': str(self.reservation5.date_check_out),
            'previous_reservation': self.reservation4.id,
        })

    def test_order_reservations_new_reservation(self):
        # add new reservation between 2022-01-13 (res-1 OUT) and 2022-01-20 (res-2 IN)
        reservation15 = Reservation.objects.create(
            id='Res-15',
            date_check_in=date(2022, 1, 13),
            date_check_out=date(2022, 1, 20),
            rental=self.rental1
        )

        url = reverse('reservations:index')
        response = self.client.get(url)

        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.context['reservations']), 6)

        self.assertDictEqual(response.context['reservations'][0], {
            'rental_name': self.reservation1.rental.name,
            'reservation_id': self.reservation1.id,
            'check_in': str(self.reservation1.date_check_in),
            'check_out': str(self.reservation1.date_check_out),
            'previous_reservation': '-',
        })
        self.assertDictEqual(response.context['reservations'][1], {
            'rental_name': reservation15.rental.name,
            'reservation_id': reservation15.id,
            'check_in': str(reservation15.date_check_in),
            'check_out': str(reservation15.date_check_out),
            'previous_reservation': self.reservation1.id,
        })
        self.assertDictEqual(response.context['reservations'][2], {
            'rental_name': self.reservation2.rental.name,
            'reservation_id': self.reservation2.id,
            'check_in': str(self.reservation2.date_check_in),
            'check_out': str(self.reservation2.date_check_out),
            'previous_reservation': reservation15.id,
        })
        self.assertDictEqual(response.context['reservations'][3], {
            'rental_name': self.reservation3.rental.name,
            'reservation_id': self.reservation3.id,
            'check_in': str(self.reservation3.date_check_in),
            'check_out': str(self.reservation3.date_check_out),
            'previous_reservation': self.reservation2.id,
        })
        self.assertDictEqual(response.context['reservations'][4], {
            'rental_name': self.reservation4.rental.name,
            'reservation_id': self.reservation4.id,
            'check_in': str(self.reservation4.date_check_in),
            'check_out': str(self.reservation4.date_check_out),
            'previous_reservation': '-',
        })
        self.assertDictEqual(response.context['reservations'][5], {
            'rental_name': self.reservation5.rental.name,
            'reservation_id': self.reservation5.id,
            'check_in': str(self.reservation5.date_check_in),
            'check_out': str(self.reservation5.date_check_out),
            'previous_reservation': self.reservation4.id,
        })
