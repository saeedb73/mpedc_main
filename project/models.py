from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Project(models.Model):
    title = models.CharField(max_length=100, default='سیم به کابل', help_text='عنوان')
    contract_type = models.CharField(max_length=100, default='کلید در دست', help_text='نوع قرارداد')
    place_of_make_contract = models.CharField(max_length=100, default='ستاد شرکت', help_text='محل عقد قرارداد')
    contractor = models.CharField(max_length=100, help_text='پیمانکار')
    contract_id = models.CharField(max_length=50, help_text='شماره قرارداد')
    contract_start_date = models.DateField(help_text='تاریخ قرارداد')
    contract_length = models.IntegerField(help_text='مدت قرارداد - ماه')
    contract_cost = models.FloatField(help_text="مبلغ قرارداد - میلیون ریال")
    place_of_project = models.CharField(max_length=100, help_text='محل اجرای پروژه')
    contract_volume = models.IntegerField(help_text='حجم قرارداد - کیلومتر')
    physical_progress = models.FloatField(help_text='درصد پیشرفت فیزیکی', default=0.0)
    financial_progress = models.FloatField(help_text='درصد پیشرفت مالی', default=0.0)
    recycled_conductor = models.FloatField(help_text='مقدار سیم برکناری', default=0.0)

    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title + ' - ' + self.contract_id

    def check_variable(self):
        return self.financial_progress / self.physical_progress


class Report(models.Model):
    title = models.CharField(max_length=100, default='گزارش روزانه', help_text='عنوان')
    report_type = models.CharField(max_length=50, choices=[('tir', 'تیر'), ('conductor', 'هادی'), ('trans', 'ترانس')], help_text='نوع گزارش')
    date = models.DateField(auto_now_add=True)
    physical_progress = models.FloatField(max_length=6, help_text='درصد پیشرفت')
    description = models.TextField(max_length=300, blank=True)

    project = models.ForeignKey(Project, on_delete=models.CASCADE)

    def __str__(self):
        return self.title + ' ' + str(self.id) + ' ' + self.report_type
