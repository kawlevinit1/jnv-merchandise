from django.shortcuts import render , redirect , HttpResponseRedirect

from django.contrib.auth.hashers import make_password
from store.models.customer import Customer
from django.views import  View


def signup(request):
    if request.method == 'GET':
        return render(request,'signup.html')
    else:
        postData = request.POST
        firstname = postData.get('firstname')
        lastname = postData.get('lastname')
        phone = postData.get('phone')
        email = postData.get('email')
        password = postData.get('password')
        #valdation
        value = {
            'firstname':firstname,
            'lastname':lastname,
            'phone':phone,
            'email':email}
        error_message =None
        customer = Customer(firstname=firstname,lastname=lastname,phone=phone,email=email,password=password)        
        isExists = customer.isExists()
        if isExists:
            error_message = 'Email Already taken'
        #saving
        if not error_message:
            customer.password = make_password(customer.password)
            customer.register()
            return render(request,'signup.html')
        else:
            data = {
                    'error':error_message,
                    'values':value
            }
            return render(request,'signup.html', data)