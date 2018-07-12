import xadmin

from .models import Reservation, Evaluation


class ReservationAdmin():
    list_display = ['user', 'date', 'field', 'type', 'client_name', 'client_level', 'mobile', 'add_time']
    list_filter = ['user', 'date', 'field', 'type', 'client_name', 'client_level']
    search_fields = ['date', 'field', 'type', 'client_name', 'client_level']
    list_editable = ['type']


class EvaluationAdmin():
    list_display = ['reservation', 'evaluation', 'remarks', 'add_time']
    list_filter = ['evaluation']

xadmin.site.register(Reservation, ReservationAdmin)
# xadmin.site.register(Evaluation, EvaluationAdmin)