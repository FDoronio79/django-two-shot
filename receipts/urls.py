from django.urls import path
from receipts.views import (
    show_receipt,
    create_receipt,
    ExpenseCategoryListView,
    AccountListView,
    create_expensecategory,
    create_account,
)


urlpatterns = [
    path("", show_receipt, name="home"),
    path("create/", create_receipt, name="create_receipt"),
    path("categories/", ExpenseCategoryListView.as_view(), name="expensecategory_list"),
    path("accounts/", AccountListView.as_view(), name="account_list"),
    path("categories/create/", create_expensecategory, name="create_category"),
    path("accounts/create/", create_account, name="create_account"),
]