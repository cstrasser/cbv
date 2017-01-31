from django.db import models
from django.contrib.auth.models import User

class Company(models.Model): 
    uuid                = models.CharField(max_length = 38, primary_key = True, editable = False)
    active              = models.BooleanField(default = True)
    isVendor            = models.BooleanField(default = False)
    edit_date           = models.DateTimeField(auto_now = True,editable = False)
    name                = models.CharField(max_length = 99)
    abn_number  	    = models.CharField(max_length = 40, editable = False) # austrailian business number 
    is_individual       = models.CharField(max_length = 40, default = False)
    address_street      = models.CharField(max_length = 60, blank = True)
    address_city        = models.CharField(max_length = 60, default = 'Brockville')
    address_state       = models.CharField(max_length = 25, default = 'Ont')
    address_postcode    = models.CharField(max_length = 10, blank = True)	
    address_country 	= models.CharField(max_length = 25, default = 'Canada')
    fax_number          = models.CharField(max_length = 16, blank = True)
    address             = models.CharField(max_length = 60, blank = True)
    billing_address 	= models.CharField(max_length = 99, blank = True)
    badges              = models.CharField(max_length = 99, blank = True , editable = False)
    tax_rate_uuid       = models.CharField(max_length = 38, blank = True, editable = False)
    m8_parent_uuid	    = models.CharField(max_length = 38, editable = False, default = '')
    parent_company      = models.ForeignKey('self', blank=True, null=True )
    
    def __str__(self):# need some code in m8requests to actually make this work
         # if not self.parent_company:
         #     return self.name
         # else:
            return self.name
  
class Company_Contact(models.Model):
    uuid                = models.CharField(max_length = 38, primary_key=True)
    active              = models.BooleanField()  
    edit_date           = models.DateTimeField(auto_now = False, auto_now_add=True,)	
    company_uuid        = models.CharField(max_length = 36 , blank = True)
    company             = models.ForeignKey(Company, null = True)
    first               = models.CharField(max_length = 40, blank = True) #	First name	
    last                = models.CharField(max_length = 40, blank = True) #	Last name	
    phone               = models.CharField(max_length = 16, blank = True)
    mobile              = models.CharField(max_length = 16, blank = True)
    email               = models.EmailField(blank = True)
    contact_type        = models.CharField(max_length = 60, blank = True)
    is_primary_contact  = models.CharField(max_length = 38)
    
    def __str__(self):
        return (self.first + ' ' + self.last)

class Item(models.Model): #additional information requied on an M8 part 
    M8UUID               = models.CharField(max_length = 38, blank = True)
    item_code            = models.CharField(max_length = 65, blank= True) #part number
    description          = models.CharField(max_length = 120, default = '')
    purchase_price       = models.DecimalField(max_digits = 8, decimal_places=2, default= 0.00)
    lastModified         = models.DateTimeField(auto_now=True)
    sells_for            = models.DecimalField(max_digits = 8, decimal_places=2, default= 0.00)
    vendor               = models.CharField(max_length = 60, blank = True)
    
    def __str__(self):
        return self.item_code
#=============================================================================   
class LineItem(models.Model):
    parent               = models.ForeignKey('Quote', default = 1)
    lineNumber           = models.IntegerField()
    item                 = models.ForeignKey(Item, default =1)
    qty                  = models.IntegerField(default = 1)
    note                 = models.CharField(max_length = 150, default = '', blank = True) # any details user needs to add about this lin for this quore .. dont mistake for "LineItem.item.description"
    cost                 = models.DecimalField(max_digits = 8, decimal_places = 2, default= 0.00)
    multiplier           = models.DecimalField(max_digits = 6, decimal_places = 3, default= 1.522) #if multiplier set to 0 allow fixed price to stay multiplier only on quotes 
    sell_price           = models.DecimalField(max_digits = 8, decimal_places = 2, default= 0.00)
    hideOnPrint          = models.BooleanField(default = False) # this way we can hide lines or prices on the printed quote or PO
    hidePriceOnPrint     = models.BooleanField(default = False)
    isOption             = models.BooleanField(default = False) # for quotes if this line will be in options section
    #property sellprice = cost * multipier ...idea
   
    def __str__ (self):
        #return (str(self.parent.pk ) +'-'+str(self.lineNumber))
        return(str(self.lineNumber)+' '+str(self.item))
    
    @property
    def extended_price(self):
        return(self.cost * self.multiplier * self.qty)
    
    def sell_price2(self): #probably should make this calculation on save override method
        if multiplier == 0: #if multiplier set to 0 this is signal from user that sell price is fixed 
            return (self.sell_price)
        else:       
            return(self.cost * self.multiplier)
   
   # class Meta:
    #    Abstract= True # needs abstract to allow Lineitem on both Quote and PO
 #======================================================       

class Quote(models.Model):
    #use ID for quote number
    customer             = models.ForeignKey(Company, null = True) #wrong qoute has contact and contact has company 
    dateCreated          = models.DateTimeField(auto_now_add = True)
    createdby            = models.ForeignKey(User)
    m8_CustomerUUID      = models.CharField(max_length=36, editable = False)
    title                = models.CharField(max_length=80) #Quick one line title to describe the quotation
    description          = models.CharField(max_length=60, blank = True) # preamble description visible to customer always works with title 
    related_M8UUID       = models.CharField(max_length=38, editable = False) # is there a related M8 Object ?
    lines                = models.ForeignKey(LineItem,on_delete=models.CASCADE, null = True, editable = False)
    total                = models.DecimalField(max_digits=8, decimal_places=2, default= 0.00) #if fixed price we need this
    note                 = models.TextField(blank = True)
    private_Note         = models.TextField(blank = True)
    active               = models.BooleanField(default = True)
    status               = models.CharField(max_length = 15, default = '', choices = [
                                                                ('DRAFT','Draft'),('WAITING','Waiting'),
                                                                ('ORDER','Order'),('DECLINED','Declined'),
                                                                ('STALE','Stale')])   
    
    
    def __str__(self):
        return (self.title )#+ ' ' + self.customer)
    
class POLine(LineItem):
    associated_quote      = models.ForeignKey(Quote) #at this point it is an order but the original info is derived from the related quote
    vendor_part_number    = models.CharField(max_length = 30, default = '') #supplier part number
    purchase_notes        = models.CharField(max_length = 75,default = '')
    purchase_price        = models.DecimalField(max_digits = 8, decimal_places=2, default= 0.00) #final price we pay should be recorded
    received              = models.BooleanField(default = False)
    
class PO(models.Model):  #needs a merge method so we can send one PO for many jobs
    #vendor #M8 vendor or create our own vendor table ?? or Connect vendors from Xero ??
    dateIssued            = models.DateField(auto_now=False, auto_now_add=True, ) # check this syntax
    notes                 = models.TextField()
    line                  = models.ForeignKey(POLine,on_delete=models.CASCADE, null = True)
    # vendor               = models.ForeignKey(Company)
    status                = models.CharField(max_length = 15, default = 'Draft', choices = [
                                                                ('DRAFT','Draft'),('WAITING','Waiting'),
                                                                ('REC','Received'),('BO','Backorder')])   
    
    
   



