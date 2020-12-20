from django.forms import ModelForm
from hotel import models



class MakeBooking(ModelForm):
    class Meta:
        model = models.Booking
        exclude = ['return_date']
    
    # def __init__(self, *args, **kwargs):
    #     super(MakeBooking, self).__init__(*args, **kwargs)
    #     booked_rooms_ids = models.Booking.objects.filter(check_out_date = None).values_list("room_number", flat = True)
    #     self.fields['room_number'].queryset = models.Booking.objects.exclude(id__in = booked_rooms_ids)

class AddReview(ModelForm):
    class Meta:
        model = models.Review
        exclude = ['date_created', 'booking_ref']