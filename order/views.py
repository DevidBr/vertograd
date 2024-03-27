from django.contrib.auth import logout
from django.core.paginator import Paginator
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from django.views import View
from order.forms import OrderChangeForm, OrderCreateForm, \
    OrderStatusFilterForm, OrderRelevantFilterForm, SearchOrderByPkForm
from order.models import Order


class MyOrdersView(View):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.unprocessed_orders = len(Order.objects.filter(status=False))
        self.order_status_filter_form = OrderStatusFilterForm()
        self.order_relevant_filter_form = OrderRelevantFilterForm()
        self.search_order_by_pk_form = SearchOrderByPkForm()

    def get(self, request):
        if request.user.is_staff:
            orders = Order.objects.all()
            paginator = Paginator(orders, 15)
            page_number = request.GET.get("page")
            page_obj = paginator.get_page(page_number)
            return render(request, 'order/my_orders.html',
                          {'orders': orders,
                           'unprocessed_orders': self.unprocessed_orders,
                           'order_status_filter_form': self.order_status_filter_form,
                           'order_relevant_filter_form': self.order_relevant_filter_form,
                           'search_order_by_pk_form': self.search_order_by_pk_form,
                           'page_obj': page_obj})
        else:
            return redirect('blog:home')

    def post(self, request):
        if request.user.is_staff:
            filter_arg = (list(request.POST)[1])
            if filter_arg == 'filter_status_arg':
                orders = Order.objects.filter(
                    status=request.POST['filter_status_arg'])
            elif filter_arg == 'search_pk':
                return redirect(Order.objects.get(
                    pk=request.POST['search_pk']))
            elif filter_arg == 'filter_relevant_arg':
                orders = Order.objects.filter(
                    relevant=request.POST['filter_relevant_arg'])
            else:
                orders = Order.objects.all()
            paginator = Paginator(orders, 15)
            page_number = request.GET.get("page")
            page_obj = paginator.get_page(page_number)
            return render(request, 'order/my_orders.html',
                          {'orders': orders,
                           'unprocessed_orders': self.unprocessed_orders,
                           'order_status_filter_form': self.order_status_filter_form,
                           'order_relevant_filter_form': self.order_relevant_filter_form,
                           'search_order_by_pk_form': self.search_order_by_pk_form,
                           'page_obj': page_obj})
        else:
            return redirect('blog:home')


def order_detail_view(request, order_id):
    order = get_object_or_404(Order, pk=order_id)
    form = OrderChangeForm(initial={
        'order_pk': order.pk,
        'comment': order.comment,
        'status': order.status,
        'relevant': order.relevant})
    return render(request, 'order/order_detail.html', {'order': order,
                                                       'form': form})


def order_change_view(request):
    if request.method == 'POST':
        form = OrderChangeForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            order = Order.objects.get(pk=cd['order_pk'])
            order.comment = cd['comment']
            order.status = cd['status']
            order.relevant = cd['relevant']
            order.save()
            return redirect(reverse('order:my_orders'))
        else:
            return render(request, 'order/order_save_error.html',
                          {'error': 'Что-то пошло не так.'})
    else:
        return redirect(reverse('order:my_orders'))


def order_delete_confirm(request, order_pk):
    order = get_object_or_404(Order, pk=order_pk)
    return render(request, 'order/order_delete_confirm.html', {'order': order})


def order_delete_view(request, order_pk):
    if request.user.is_superuser and request.method == 'POST':
        order = get_object_or_404(Order, pk=order_pk)
        order.delete()
        return redirect(reverse('order:my_orders'))
    else:
        return render(request, 'order/order_save_error.html',
                      {'error': 'Удаление не удалось.'})


def order_create_page_view(request):
    if request.user.is_superuser and request.method == 'POST':
        form = OrderCreateForm(request.POST)
        if form.is_valid():
            new_order = form.save()
            report = f'Заявка №{new_order.pk} успешно создана.'
            return render(request, 'order/order_change_success.html', {
                'report': report
            })
    form = OrderCreateForm()
    return render(request, 'order/order_create_page.html', {'form': form})


def staff_logout(request):
    logout(request)
    return redirect('blog:home')










