from django.shortcuts import render,redirect

from django.views.generic import View

from myapp.models import Book

from myapp.forms import BookForm

# Create your views here.


class BookListView(View):
    
    def get(self,request,*args, **kwargs):
        
        qs=Book.objects.all()
        
        return render(request,'book_list.html',{"form":qs})
    
    
class BookCreateView(View):
    
    def get(self,request,*args, **kwargs):
        
        form_instance=BookForm()
        
        return render(request,"book_add.html",{"form":form_instance})
    
    def post(self,request,*args, **kwargs):
        
        form_instance=BookForm(request.POST)
        
        if form_instance.is_valid():
            
            data=form_instance.cleaned_data
            
            qs=Book.objects.create(**data)
            
            return redirect("book-list")
        
        
        
class BookEditView(View):
    
    def get(self,request,*args, **kwargs):
        
        # form_instance=BookForm()
        
        id=kwargs.get("pk")
        
        book_object=Book.objects.get(id=id)
        
        dictionary={
            "book_name":book_object.book_name,
            
            "author_name":book_object.author_name,
            
            "price":book_object.price
        }
        
        form_instance=BookForm(dictionary)
        return render(request,"book_edit.html",{"form":form_instance})
        
        
        
class BookDeleteView(View):
    
    def get(self,request,*args, **kwargs):
        
        id=kwargs.get("pk")
        
        Book.objects.get(id=id).delete()
        
        return redirect("book-list")
        