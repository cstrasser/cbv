from django import forms
from django.forms import ModelForm
from django.views.generic.edit import CreateView



from .models import Quote

YEAR_IN_SCHOOL_CHOICES = (
    ('FR', 'Freshman'),
    ('SO', 'Sophomore'),
    ('JR', 'Junior'),
    ('SR', 'Senior'),
)

class QuoteCreate(CreateView):
    model = Quote
    fields = ['customer','title','total','status','createdby']
    noodles = 'spaghetti'
    def form_valid(self,form):
        form.instance.createdby = self.request.user
        return super(QuoteCreate,self).form_valid(form)

class QuoteLineform(ModelForm):
    class meta:
        fields = ['item','note','cost','multiplier','sell_price','hideonPrint','hidePriceOnPrint']



class TestForm(forms.Form):
    edit_state = not(True) #read as edit state is true the not is there for readability
    thing = forms.CharField(max_length = 25, label = 'thing label', disabled = edit_state)
    other_thing = forms.ChoiceField((
                    ('FR', 'Freshman'),
                    ('SO', 'Sophomore'),
                    ('JR', 'Junior'),
                    ('SR', 'Senior'),)
                                  ,disabled = edit_state)
    

class EditModelForm(ModelForm):

    def __init__(self, *arg, **kwrg):
        super(EditModelForm, self).__init__(*arg, **kwrg)
        if hasattr(self, 'readonly'):
            for x in self.readonly:
                self.fields[x].widget.attrs['disabled'] = 'disabled'

    def clean(self):
        data = super(EditModelForm, self).clean()
        if hasattr(self, 'readonly'):
            for x in self.readonly:
                data[x] = getattr(self.instance, x)
        return data



class Qform(ModelForm):
    def __init__(self, *args, **kwargs):
        super(Qform, self).__init__(*args, **kwargs)
        self.fields['title'].queryset= Quote.objects.filter(Q(name='Testquote'))
    
    
    
    class Meta:
        model = Quote
        fields = ['customer','title','total','status']
        
       
    


 # dateCreated = models.DateTimeField(auto_now_add = True)
 #    createdby = models.ForeignKey(User)
 #    m8_CustomerUUID = models.CharField(max_length=36)
 #    title  = models.CharField(max_length=80) #Quick one line title to describe the quotation
 #    description  = models.CharField(max_length=60) # preamble description visible to customer always works with title 
 #    related_M8UUID = models.CharField(max_length=38) # is there a related M8 Object ?
 #    total = models.IntegerField() #if fixed price we need this
 #    note = models.TextField( blank = True)
 #    private_Note = models.TextField(blank = True)
 #    active = models.BooleanField(default = True)    

class QuoteForm(forms.ModelForm):
    
    class Meta:
        Model = Quote
        exclude =  ['m8_CustomerUUID','related_M8UUID']