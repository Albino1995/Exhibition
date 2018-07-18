from django.shortcuts import render
from django.views.generic.base import View
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from pure_pagination import Paginator, EmptyPage, PageNotAnInteger

from .models import Reservation
from .forms import ReservationForm
from utils.LoginRequiredMixin import LoginRequiredMixin
from utils.CalculationDay import calculation_date, serialize_date


class ReservationView(LoginRequiredMixin, View):
    """
    预约
    """
    @staticmethod
    def get(request):
        return render(request, 'reservation.html', {})

    @staticmethod
    def post(request):
        reservation_form = ReservationForm(request.POST)
        if reservation_form.is_valid():
            reservation = Reservation()
            reservation.user = request.user
            reservation.date = request.POST.get('date', '')
            if calculation_date(reservation.date) != '':
                return render(request, 'reservation.html', {'msg': calculation_date(reservation.date),
                                                            'reservation_form': reservation_form})
            reservation.field = request.POST.get('field', '')
            query = Reservation.objects.filter(date=reservation.date, field=reservation.field).exclude(type='已取消')
            if query:
                return render(request, 'reservation.html', {'msg': '该场次已被预约，请选择其他场次',
                                                            'reservation_form': reservation_form})
            reservation.client_name = request.POST.get('client_name', '')
            reservation.client_level = request.POST.get('client_level', '')
            reservation.department = request.POST.get('department', '')
            reservation.applicant = request.POST.get('applicant', '')
            reservation.mobile = request.POST.get('mobile', '')
            reservation.remarks = request.POST.get('remarks', '')
            reservation.save()
            return HttpResponseRedirect(reverse('record'))
        else:
            return render(request, 'reservation.html', {'reservation_form': reservation_form})


class CheckView(LoginRequiredMixin, View):
    """
    查看预约
    """
    @staticmethod
    def get(request):
        return render(request, 'index.html', {'new_date': 0})

    @staticmethod
    def post(request):
        res = ['empty'] * 2
        date = request.POST.get('date', '')
        reserve = request.POST.get('reserve', '')
        if reserve == '1':
            field = '9:00 - 12:00' if request.POST.get('field', '') == 'first_field' else '14:00 - 17:00'
            reservation_form = {'data': {'date': date, 'field': field}}
            return HttpResponseRedirect(reverse('reservation'))
            # return render(request, 'reservation.html', {'reservation_form': reservation_form})
            # return render_to_response(request, 'reservation.html', {'reservation_form': reservation_form})
        if calculation_date(date) != '':
            return render(request, 'index.html', {'msg': calculation_date(date), 'new_date': 0})
        query = Reservation.objects.filter(date=date)
        for q in query:
            if q.field.startswith('9'):
                res[0] = 'full'
            elif q.field.startswith('14'):
                res[1] = 'full'
        return render(request, 'index.html', {'res': res, 'date': serialize_date(date), 'new_date': date, 'flag': True})


class RecordView(LoginRequiredMixin, View):
    """
    预约记录
    """
    @staticmethod
    def get(request):
        records = Reservation.objects.filter(user=request.user).order_by('-add_time')
        # 分页
        try:
            page = request.GET.get('page', 1)
        except PageNotAnInteger:
            page = 1
        p = Paginator(records, 5, request=request)
        page = p.page(page)
        return render(request, 'record.html', {'records': records, 'all_record': page})

    @staticmethod
    def post(request):
        """
        取消记录
        """
        records = Reservation.objects.get(id=request.POST.get('id', ''))
        records.type = '已取消'
        records.save()
        return HttpResponseRedirect(reverse('record'))
