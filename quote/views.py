from django.shortcuts import render, Http404
from django.forms import formset_factory, modelformset_factory
from django.views.generic import DetailView


from .forms import QuoteForm ,TestForm, Qform
from .m8requests2 import update_local_tables
from .models import Company, Company_Contact, Quote, LineItem
from .forms import QuoteForm ,QuoteCreate

# class QuoteDetail(DetailView):
#     model = Quote

class MyQuoteCreate(QuoteCreate):
      template_name = 'testform.html'



def home(request):
    myform = TestForm
    return render (request, 'testform.html',{'formimade':myform})

def qfrm(request):
    quote = Quote.objects.get(title = 'Testing')
    form = Qform(instance = quote)
    #form.fields['customer'].widget.attrs['disabled'] = True
    for field in form.fields: #do not allow edits on open
        form.fields[field].widget.attrs['disabled'] = True
    return render(request,'testform.html',{'formimade':form})





def quotedetail(request):#QuoteForm = formset_factory()
    #customer= Company.objects.get(pk = '02fba271-8795-43f3-acb9-b5340513b24b')
    #quote  = Quote.objects.get(customer = customer, title = 'Test Quote', createdby = request.user)
    quote = Quote.objects.get(pk=1700)
    #quote._set_pk_val(1700)
    print (quote.lines)
    # for line in quote.lines:
    # print(line) 
    # quote.save()
    # for x in range(6):
    #      lineitem = LineItem.objects.create(lineNumber = x,qty =1, parent = quote)        
    #      lineitem.save()
    return render(request,'quoteform.html', {})


def m8update(request):
    update_local_tables()
    return render(request,'quoteform.html',{})


def modelstest(request):
    q1= Company.objects.get(pk = '02fba271-8795-43f3-acb9-b5340513b24b')
    #q2 = Company_Contact.objects.filter( company_uuid  ='02fba271-8795-43f3-acb9-b5340513b24b' )
    #import pdb; pdb.set_trace()
    person_set = q1.company_contact_set.all().order_by("last")
    for guy in person_set:
        print (q1,guy, guy.phone,guy.email)
    return render(request,'base.html',{})  

#def formset_view(request):
#     TestFormset = formset_factory(TestForm, extra=2)
#     formset = TestFormset(request.POST or None)
#     if formset.is_valid():
#         for form in formset:
#             print(form.cleaned_data)
#     context = {
#         "formset": formset
#     }
#     return render(request, "formset_view.html", context)


def quote(request):
    pass
    
    
    