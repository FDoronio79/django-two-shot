from django.shortcuts import render, redirect
from receipts.models import ExpenseCategory, Account, Receipt
from receipts.forms import ReceiptForm, ExpenseCategoryForm
from django.views.generic.list import ListView
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
        receipt = form.save(commit=False)
        receipt.purchaser = request.user
        form.save()
        return redirect('home')
    context = {
        'form': form
    }
    return render(request, "receipts/create.html", context)


class ExpenseCategoryListView(ListView):
    model = ExpenseCategory
    template_name = 'receipts/categories_list.html'
    context_object_name = 'receipts'

    def get_queryset(self):
        return ExpenseCategory.objects.filter(owner=self.request.user)


class AccountListView(ListView):
    model = Account
    template_name = 'receipts/accounts_list.html'
    context_object_name = 'receipts'

    def get_queryset(self):
        return Account.objects.filter(owner=self.request.user)

@login_required
def create_expensecategory(request):
    form = ExpenseCategoryForm(request.POST or None)
    if form.is_valid():
        receipt = form.save(commit=False)
        receipt.owner = request.user
        form.save()
        return redirect('expensecategory_list')
    context = {
        'form': form
    }
    return render(request, "receipts/create_expensecat.html", context)