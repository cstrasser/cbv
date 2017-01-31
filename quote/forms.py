from django import forms
from django.forms import ModelForm
from django.views.generic.edit import CreateView
from django.views.generic.detail import DetailView
from django.forms import inlineformset_factory


from .models import Quote, LineItem

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







class TestForm(forms.Form):
    edit_state = not(True) #read as edit state is true the not is there for readability
    thing = forms.CharField(max_length = 25, label = 'thing label', disabled = edit_state)
    other_thing = forms.ChoiceField((
                    ('FR', 'Freshman'),
                    ('SO', 'Sophomore'),
                    ('JR', 'Junior'),
                    ('SR', 'Senior'),)
                                  ,disabled = edit_state)
    

class EditModelForm(ModelForm): # hang onto this has some good ideas

    def __init__(self, *arg, **kwrg):
        super(EditModelForm, self).__init__(*arg, **kwrg)
        if hasattr(self, 'readonly'):
            for x in self.readonly:
                self.fields[x].widget.attrs['disabled'] = True

    def clean(self):
        data = super(EditModelForm, self).clean()
        if hasattr(self, 'readonly'):
            for x in self.readonly:
                data[x] = getattr(self.instance, x)
        return data


#==============================================
class Qform(ModelForm):
    class Meta:
        model = Quote
        fields = ['customer','title','total','status']
        
        
class Qformdetail(DetailView):
    class Meta:
        model = Quote
        fields = ['customer','title','total','status']
    
#=====================================================      
class QuoteLineform(ModelForm):
    class meta:
        fields = ['item','note','cost','multiplier','sell_price','hideonPrint','hidePriceOnPrint']
 


      #inlineformset_factory(Quote,LineItem,fields=('linenumber','item','qty'))
 

# from quote.models import Quote
# from quote.models import LineItem 
# from django.forms import inlineformset_factory
# lineformset = inlineformset_factory(Quote,LineItem,fields=('lineNumber','item','qty'))
# from django.shortcuts import render, Http404 , get_object_or_404
# gottenquote = get_object_or_404(Quote, title ='Testquote')
# formset = lineformset(instance =gottenquote)
# print(formset)
#the above works in the shell ....






class QuoteForm(forms.ModelForm):
    
    class Meta:
        Model = Quote
        exclude =  ['m8_CustomerUUID','related_M8UUID']
        
        
        

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