from django.shortcuts import render
from receipts.models import ExpenseCategory, Account, Receipt
from django.contrib.auth.decorators import login_required

@login_required
def show_receipt(request):
    receipts = Receipt.objects.all()
    context = {"receipts": receipts}
    return render(request, 'receipts/list.html', context)
