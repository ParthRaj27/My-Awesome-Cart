from django.shortcuts import render
from .models import Product, Contact ,Orders , OrderUpdate
from math import ceil
import json


# Create your views here.
from django.http import HttpResponse


def index(request):
    allProds = []
    catprods = Product.objects.values('category', 'id')
    cats = {item["category"] for item in catprods}
    
    for cat in cats:
        sub_cats = Product.objects.filter(category=cat).values('sub_category').distinct()
        for sub_cat in sub_cats:
            prod = Product.objects.filter(category=cat, sub_category=sub_cat['sub_category'])
            n = len(prod)
            nSlides = n // 4 + ceil((n / 4) - (n // 4))
            
            if len(prod) != 0:
                allProds.append([prod, range(1, nSlides), nSlides])
    
    params = {'allProds': allProds}
    return render(request, "shop/index.html", params)
def searchMatch(query, item):
    print(query)
    '''return true only if query matches the item'''
    if query in item.desc.lower() or query in item.product_name.lower() or query in item.category.lower():
        return True
    else:
        return False

def search(request):
    query = request.GET.get('search')
    allProds = []
    catprods = Product.objects.values('category', 'id')
    cats = {item['category'] for item in catprods}
    for cat in cats:
        prodtemp = Product.objects.filter(category=cat)
        prod = [item for item in prodtemp if searchMatch(query, item)]

        n = len(prod)
        nSlides = n // 4 + ceil((n / 4) - (n // 4))
        if len(prod) != 0:
            allProds.append([prod, range(1, nSlides), nSlides])
    params = {'allProds': allProds, "msg": ""}
    if len(allProds) == 0 or len(query)<4:
        params = {'msg': "Please make sure to enter relevant search query" ,'query' : query}
    return render(request, 'shop/search.html', params)



def about(request):
    return render(request, 'shop/about.html')
def contact(request):
    if request.method=="POST":
        # print(request)
        name=request.POST.get('name', '')
        email=request.POST.get('email', '')
        phone=request.POST.get('phone', '')
        desc=request.POST.get('desc', '')
        contact = Contact(name=name, email=email, phone=phone, desc=desc)
        contact.save()
        hey=True;
        return render(request, "shop/contact.html" ,{'hey':hey})
    return render(request, "shop/contact.html")


def tracker(request):
    if request.method=="POST":
        orderId = request.POST.get('orderId', '')
        email = request.POST.get('email', '')
        try:
            order = Orders.objects.filter(order_id=orderId, email=email)
            if len(order)>0:
                update = OrderUpdate.objects.filter(order_id=orderId)
                updates = []
                for item in update:
                    updates.append({'text': item.update_desc, 'time': item.timestamp})
                    response = json.dumps({"status":"success", "updates": updates, "itemsJson": order[0].items_json}, default=str)
                return HttpResponse(response)
            else:
                return HttpResponse('{"status":"noitem"}')
        except Exception as e:
            return HttpResponse('{"status":"error"}')

    return render(request, 'shop/tracker.html')

# def catagory(request):
#     products= Product.objects.all()
#     allProds=[]
#     catprods= Product.objects.values('category', 'id')
#     cats= {item["category"] for item in catprods}
#     for electronics  in cats:
#         prod=Product.objects.filter(category=electronics)
#         n = len(prod)
#         nSlides = n // 4 + ceil((n / 4) - (n // 4))
#         if len(prod) != 0:
#             allProds.append([prod, range(1, nSlides), nSlides])
#     params={'allProds':allProds }
#     return render(request, 'shop/catagory.html') 
# def bill(request):
#     # return HttpResponse("We are at search")
#     return render(request, 'shop/bill.html')    

def ProductView(request , myid):
    # if we have no any primary key than django automatic generate id key with name id
    # fetch the product using id
    product=Product.objects.filter(id=myid)
    
    return render(request, 'shop/prodview.html' ,{'product':product[0]})
# at above the initializtion of product is list and we knew we cam fetch one thind from one id so we will give this zero
# first product is the product where we will use to access in templates and another one is the main Product which is initialized at above

def Checkout(request):
    if request.method=="POST":
        items_json= request.POST.get('itemsJson', '')
        name=request.POST.get('name', '')
        amount = request.POST.get('amount', '')
        email=request.POST.get('email', '')
        address=request.POST.get('address1', '') + " " + request.POST.get('address2', '')
        city=request.POST.get('city', '')
        state=request.POST.get('state', '')
        zip_code=request.POST.get('zip_code', '')
        phone=request.POST.get('phone', '')
        order = Orders(items_json= items_json, name=name, email=email, address= address, city=city, state=state, zip_code=zip_code, phone=phone,amount=amount)
        order.save()
        update=OrderUpdate(order_id=order.order_id , update_desc ="The order has been plaxed!")
        update.save()
        thank=True
        id=order.order_id
        return render(request, 'shop/checkout.html', {'thank':thank, 'id':id})
    return render(request, 'shop/checkout.html')
from django.shortcuts import render
from .models import Product

def subcategory_products(request, sub_category):
    products = Product.objects.filter(sub_category=sub_category)
    print(sub_category)
    context = {'products': products, 'sub_category': sub_category}
    return render(request, 'shop/subcategory_products.html', context)
