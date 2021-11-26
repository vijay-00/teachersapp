from django.contrib import admin
from fourthapp.models import loandetails, memberdetails, profiledetails, transactions, outstanding


# Register your models here.
# admin.site.register(loandetails)
# admin.site.register(memberdetails)
# admin.site.register(profiledetails)
# admin.site.register(transactions)
# admin.site.register(outstanding)

@admin.register(loandetails)
class LoanDetails(admin.ModelAdmin):
    list_display = ['userid', 'loan_no', 'loan_amount', 'loan_tenure', 'loan_roi', 'loan_date', 'surety_no',
                    'surety_name']
    list_filter = ['loan_no']
    list_editable = ('loan_no',)
    search_fields = ['loan_no']


@admin.register(memberdetails)
class MemberDetails(admin.ModelAdmin):
    list_display = ['userid', 'memberno', 'memebername', 'mobileno']
    list_filter = ['memberno']
    list_editable = ('memberno',)
    search_fields = ['memberno']


@admin.register(profiledetails)
class ProfileDetails(admin.ModelAdmin):
    list_display = ['userid', 'memberno', 'membername', 'memberclass', 'employeecode', 'soceityname']
    list_filter = ['membername']
    list_editable = ('membername',)
    search_fields = ['membername']


@admin.register(transactions)
class Transactions(admin.ModelAdmin):
    list_display = ['userid', 'date', 'amount', 'heading', 'transactionmode', 'receiotorcharges', 'description']
    list_filter = ['date']
    list_editable = ('date',)
    search_fields = ['date']


@admin.register(outstanding)
class OutStanding(admin.ModelAdmin):
    list_display = ['userid', 'lop', 'los', 'td', 'share']
    list_filter = ['userid']
    search_fields = ['userid']
