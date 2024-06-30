from django import forms

class BookForm(forms.Form):
    
    book_name=forms.CharField()
    
    author_name=forms.CharField()
    
    price=forms.IntegerField()
    
    
    
