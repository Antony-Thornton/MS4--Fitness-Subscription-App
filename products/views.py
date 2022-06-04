from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.db.models import Q
from django.db.models.functions import Lower
from .models import Product, Category, product_review
from .forms import ReviewForm, ProductForm

def all_products(request):
    """ A view to show all products, including sorting and search queries """

    products = Product.objects.all()
    query = None
    categories = None
    sort = None
    direction = None

    if request.GET:
        if 'sort' in request.GET:
            sortkey = request.GET['sort']
            sort = sortkey
            if sortkey == 'name':
                sortkey = 'lower_name'
                products = products.annotate(lower_name=Lower('name'))
            if sortkey == 'category':
                sortkey = 'category__name'
            if 'direction' in request.GET:
                direction = request.GET['direction']
                if direction == 'desc':
                    sortkey = f'-{sortkey}'
            products = products.order_by(sortkey)
            
        if 'category' in request.GET:
            categories = request.GET['category'].split(',')
            products = products.filter(category__name__in=categories)
            categories = Category.objects.filter(name__in=categories)

        if 'q' in request.GET:
            query = request.GET['q']
            if not query:
                messages.error(request, "You didn't enter any search criteria!")
                return redirect(reverse('products'))
            
            queries = Q(name__icontains=query) | Q(description__icontains=query)
            products = products.filter(queries)

    current_sorting = f'{sort}_{direction}'

    context = {
        'products': products,
        'search_term': query,
        'current_categories': categories,
        'current_sorting': current_sorting,
    }

    return render(request, 'products/products.html', context)


def product_detail(request, product_id):
    """ A view to show individual product details """
    # https://stackoverflow.com/questions/54735780/display-query-set-object-in-django-template Helped with the review bug where objects werent showing
    product = get_object_or_404(Product, pk=product_id)
    review = product_review.objects.all()
    context = {
        'product': product,
        'object_list': review,
    }

    review_form = ReviewForm()
    if request.method == 'POST':
        review_form = ReviewForm(data=request.POST)
        if review_form.is_valid():
            new_review = review_form.save(commit=False)
            new_review.sku = product
            new_review.save()
            messages.success(request, 'Thank you for your review.')
        else:
            review_form = ReviewForm()
    return render(request, 'products/product_detail.html', context)


def add_product(request):
    """ Add a product to the store """
    form = ProductForm()
    template = 'products/add_product.html'
    context = {
        'form': form,
    }

    return render(request, template, context)


# Moved this to the function above.
# def productReview(request):

#     template = 'products/product_detail.html'
#     messages.success(request, 'Thansdffdsd')
#     if request.method == 'POST':

#         messages.success(request, 'Thank you for your review.')

#         form_data = {
#             'sku': request.POST['product_id'],
#             'review': request.POST['review'],
#         }

#         review_form = ReviewForm(form_data)
#         if review_form.is_valid():
#             contact = review_form.save(commit=False)
#             contact.save()
#             request.session['save_info'] = 'save-info' in request.POST
#             return render(request, template, {})
#         else:
#             messages.error(request, 'There was an error with your form. \
#                 Please resubmit')
           
#         return render(request, template, {})

#     else:
#         messages.error(request, "Not working.")

#         return render(request, template, {})