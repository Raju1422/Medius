from django.shortcuts import render
from django.core.mail import send_mail
from django.http import HttpResponse
import pandas as pd
from django.template.loader import render_to_string
from django.conf import settings
# Create your views here.
from django.template.loader import render_to_string
from pandas import DataFrame

def generate_summary_report(df: DataFrame):
    total_records = len(df)
    unique_states = df['Cust State'].nunique()
    unique_pins = df['Cust Pin'].nunique()
    max_dpd = df['DPD'].max()
    min_dpd = df['DPD'].min()
    avg_dpd = df['DPD'].mean()
    state_summary = df.groupby('Cust State')['DPD'].agg(['count', 'min', 'max', 'mean']).reset_index()
    state_summary.columns = ['Cust State', 'Total Records', 'Min DPD', 'Max DPD', 'Avg DPD']
    state_summary_html = state_summary.to_html(index=False, classes='table table-striped', border=0)

    context = {
        'total_records': total_records,
        'unique_states': unique_states,
        'unique_pins': unique_pins,
        'max_dpd': max_dpd,
        'min_dpd': min_dpd,
        'avg_dpd': round(avg_dpd, 2),
        'state_summary_html': state_summary_html
    }

    summary_html = render_to_string('summary_email_template.html', context)
    
    return summary_html

def home(request):
    if request.method == "POST" and request.FILES.get('file'):
        file = request.FILES['file']
        if file.name.endswith('.csv'):
            df = pd.read_csv(file)
        elif file.name.endswith(('.xls', '.xlsx')):
            df = pd.read_excel(file)
        else:
            return render(request, 'home.html', {'error':'Unsupported File Format'})
        try : 
            summary =generate_summary_report(df)
            subject = "Python Assignment - Nambala Santosh Ramaraju"
            message = "Summary of the uploaded file report "           
            recipient_list = ['tech@themedius.ai']
            send_mail(subject, message, settings.EMAIL_HOST_USER, recipient_list,  html_message=summary)
            return render(request, 'home.html', {'message': 'Summary of the file has been sent to tech@themedius.ai'})
        except Exception as e:
            return render(request,'home.html',{'error':'Error while sending email'})
    return render(request,'home.html')


