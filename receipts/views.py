from django.shortcuts import render, redirect
from receipts.models import ExpenseCategory, Account, Receipt
from receipts.forms import ReceiptForm
from django.contrib.auth.decorators import login_required

@login_required
def show_receipt(request):
    receipts = Receipt.objects.all()
    context = {"receipts": receipts}
    return render(request, 'receipts/list.html', context)

@login_required
def create_receipt(request):
    form = ReceiptForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect("home")
    context = {
        'form': form
    }
    return render(request, "receipts/create.html", context)