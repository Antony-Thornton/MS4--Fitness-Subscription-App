# The Veggie Guy Fitness App
# Testing

## Introduction

Full website testing can be seen below. For the main README cick <a href="https://github.com/Antony-Thornton/MS4--Fitness-Subscription-App/blob/main/README.md" target="_blank">here</a>. Full testing has been conducted AFTER the application was uploaded to Heroku.

<img src="https://external-content.duckduckgo.com/iu/?u=https%3A%2F%2Fimages.pexels.com%2Fphotos%2F1308118%2Fpexels-photo-1308118.jpeg%3Fcs%3Dsrgb%26dl%3Dcode-coder-codes-1308118.jpg%26fm%3Djpg&f=1&nofb=1" alt="Testing" >

<br>

# Table of Contents

-   [1. Testing](#testing)
    -   [1.1. Considerations](#considerations)
-   [2. Pre Herkou Checks](#refactor)
    -   [2.1 Code validation](#code)   
-   [3. Manual](#manual)


            


#### [Go To Top](#table-of-contents "Go To Top")


<a name="testing"></a>

# 1. Testing

<a name="considerations"></a>

## 1.1 Considerations

* Testing has been based on a minimum size of an iPhone SE and a maximum width of 1440px as per my mentor’s advice. Custom CSS has been created to accommodate multiple screen sizes

* Python Code in the app.py file has been validated by using <a href="http://pep8online.com/" target="_blank">PEP8 Online</a> and the inbuilt problems tracker in GitPod

* HTML code has been validated using <a href="https://validator.w3.org/" target="_blank">W3C Markup Validation Service</a>

* CSS code has been validated using <a href="https://jigsaw.w3.org/CSS-validator//" target="_blank">W3C CSS Validation Service</a>

* Javascript code has been validated using <a href="https://jshint.com/" target="_blank">JS Hint</a>

* Site response has been validated using <a href="http://ami.responsivedesign.is/" target="_blank">Am I Responsive</a>

### iPhone SE

Add image of iphone se here


### 1440p

Add image of 1440p here


<a name="refactor"></a>

# 2. Pre Herkou Checks

## PEP8 Online results

| App | .py file | Result
| :-- | :-- | :--
Cart | apps.py | Ok
 || context.py | Ok - Ignored commented text
 || urls.py | Ok
 || Views.py | Ok
Checkout | init.py | Ok
 || admin.py | Ok
 || apps.py | Ok
 ||forms.py | Ok
 || models.py | Ok
 || signals.py | Ok
 || urls.py | Ok
 || views.py | Ok
 || webhook_handler.py | Ok
 || webhooks.py | Ok
Contact | admin.py | Ok
|| apps.py | Ok
|| forms.py | Ok
|| models.py | Ok
|| urls.py | Ok
|| views.py | Ok
Main App | asgi.py | Ok
|| settings.py | Ok
|| urls.py | Ok
|| wsgi.py | Ok
Home | apps.py | Ok
|| models.py | Ok
|| urls.py | Ok
|| views.py | Ok
| Products | admin.py | Ok
|| apps.py | Ok
|| forms.py | Ok
|| models.py | Ok
|| urls.py | Ok
|| views.py | Ok
|| widgets.py | Ok
| Profiles | apps.py | Ok
|| forms.py | Ok
|| models.py | Ok
|| urls.py | Ok
|| views.py | Ok
| Manage.py | Manage.py | Ok

## Post Pep8 chenages testing
Running basic checks to see if everything is still working as expected.

| Page | What happened? | Fix
| :-- | :-- | :--
Add/edit items | Template Name variable in widgets.py was too long so I broke it onto the next line. This caused a pathing error when loading the pages. |  Need to confirm with mentor/community. Left as too long with a comment for the moment.
Links | n/a | n/a 
Review form | n/a | n/a 
Product details functions | n/a | n/a 
Cart Functions | n/a | n/a 
Secure Checkout Functions | n/a | n/a 
Add/edit functions | n/a | n/a 
My profile | n/a | n/a 

<br>
<br>

<a name="code"></a>

## 2.1 Code validation


## HTML Validator results

| Page | Date Checked | Result | Comment
| :--- | :--- | :--- | :-- 
cart.html |||
checkout_success.html
checkout.html
contact.html
index.html
custom_clearable_file_input.html
add_product.html
edit_product.html
product_detail.html
products.html
profile.html
main-nav.hmtl
mobile-top-header.html
base.html

<br>

## CSS Validator results
| Page | Date Checked | Result | Comment
| :--- | :--- | :--- | :-- 
checkout.css
profile.css
base.css

<br>

### JavaScript results
| Page | Date Checked | Result | Comment
| :--- | :--- | :--- | :-- 
countryfield.js


<br>
<br>

<a name="manual"></a>

# 3. Manual Testing

## Navigation Bar
All Pages:

| Page | Outcome | Result Desktop | Result iPad | Result S9+ Phone 
| :--- | :--- | :--- | :--- | :---
Home
All products
Nutrition Plans
Exercise Equipement
Contact
Product Management
My Profile
Log out
Register
Edit product


<br>
<br>

## Footer Links
All Pages:

| Page | Outcome | Result Desktop | Result iPad | Result S9+ Phone 
| :--- | :--- | :--- | :--- | :---
Home
All products
Nutrition Plans
Exercise Equipement
Contact
Product Management
My Profile
Log out
Register
Edit product

<br>
<br>

## Home Page
| Page | Outcome | Result Desktop | Result iPad | Result S9+ Phone 
| :--- | :--- | :--- | :--- | :---
Browse all products link should direct to all products page. |
Browse all nutrition books link should direct to all books page. |
Browse all Exercise Equipment link should direct to all equipment page. |


<br>
<br>

## All Products

| Page | Outcome | Result Desktop | Result iPad | Result S9+ Phone 
| :--- | :--- | :--- | :--- | :---
All products in admin should show correctly. This includes all associated expected text such as name, price and category.
If the super user is logged in an edit and delete product should be visible. Both the links should work
If a super user is NOT logged in an edit and delete product should NOT be visible.
Clicking on a catgory should filter all results for that category.
Clicking on a picture should take the user to that product detail page.
Each of the drop down links should filter or sort by whatever the user selects.


<br>
<br>

## Nutrition Plans
| Page | Outcome | Result Desktop | Result iPad | Result S9+ Phone 
| :--- | :--- | :--- | :--- | :---
All products in admin should show correctly. This includes all associated expected text such as name, price and category.
If the super user is logged in an edit and delete product should be visible. Both the links should work
If a super user is NOT logged in an edit and delete product should NOT be visible.
Clicking on a catgory should filter all results for that category.
Clicking on a picture should take the user to that product detail page.
Each of the drop down links should filter or sort by whatever the user selects.

<br>
<br>

## Exercise Plans
| Page | Outcome | Result Desktop | Result iPad | Result S9+ Phone 
| :--- | :--- | :--- | :--- | :---
All products in admin should show correctly. This includes all associated expected text such as name, price and category.
If the super user is logged in an edit and delete product should be visible. Both the links should work
If a super user is NOT logged in an edit and delete product should NOT be visible.
Clicking on a catgory should filter all results for that category.
Clicking on a picture should take the user to that product detail page.
Each of the drop down links should filter or sort by whatever the user selects.

<br>
<br>

## Contact
| Page | Outcome | Result Desktop | Result iPad | Result S9+ Phone 
| :--- | :--- | :--- | :--- | :---
The user should be able to fill out a form including name, email and message. 
The form should not submit if any field is empty.

<br>
<br>


## Product Details
| Page | Outcome | Result Desktop | Result iPad | Result S9+ Phone 
| :--- | :--- | :--- | :--- | :---
The page should load with; the image, the name, the price, the description and any reviews found in the database.
If the super user is logged in an edit and delete product should be visible. Both the links should work
If a super user is NOT logged in an edit and delete product should NOT be visible.
The qauntity should not drop below zero
The quantity buttons should adjust the total up and down
The keep shopping button should take the user to the all products page
The add to cart button should add the total quantity of items to the user cart.
The user should be able to submit a review but NOT a blank review.


<br>
<br>

## Shopping Cart
| Page | Outcome | Result Desktop | Result iPad | Result S9+ Phone 
| :--- | :--- | :--- | :--- | :---
If the cart is empty a cart should display with a keep shopping button.
The keep shopping button should take the user to the products page.
The cart should display the product information and quantity that the users selected.
If the price is over £50 the delivery should be free.
The subtotal button should not drop below zero and the plus above 99 when the qty is updated.
The Qty should update to the left.
Delete item should remove all of that item from the cart. 
The keep shopping button should take the user to the products page.
The secure checkout button should take the user to the checkout page.

<br>
<br>

## Checkout
| Page | Outcome | Result Desktop | Result iPad | Result S9+ Phone 
| :--- | :--- | :--- | :--- | :---
The contents of the shopping cart should display as an order summary in the checkout page. 
Each of the form fields should allow user input.
The adjust cart button should take the user back to their cart.
The complete order button should submit all of the details for payment and take the user to a checkout success page where the order information will be displayed. 


<br>
<br>

## Profile Page
| Page | Outcome | Result Desktop | Result iPad | Result S9+ Phone 
| :--- | :--- | :--- | :--- | :---
The profile page should display any order stored in the database for the current logged in user.
The order number should take the user to their previously submitted order and have their details displayed.
The User should be able to update their basic default delivery information and click the update information link.

<br>
<br>

## Search bar
| Page | Outcome | Result Desktop | Result iPad | Result S9+ Phone 
| :--- | :--- | :--- | :--- | :---
The search bard should display any products with text associated with a database item in a product page.

<br>
<br>

## Product Management
| Page | Outcome | Result Desktop | Result iPad | Result S9+ Phone 
| :--- | :--- | :--- | :--- | :---
This page should allow a SUPER USER ONLY access to add a product.
The form should error if a price over 6 digits is added. 
All of the categories should display from the database.
A form with all data base items should be displayed for the user to add to the database.
The user should be able to add an image.

<br>
<br>

## Edit Product
| Page | Outcome | Result Desktop | Result iPad | Result S9+ Phone 
| :--- | :--- | :--- | :--- | :---
This page should allow a SUPER USER ONLY access to add a product.
The form should display information about the item the user selected to edit.
The form should error if a price over 6 digits is added. 
All of the categories should display from the database.
A form with all data base items should be displayed for the user to change in the database.
The user should be able to add an image.

<br>
<br>


## Register
| Page | Outcome | Result Desktop | Result iPad | Result S9+ Phone 
| :--- | :--- | :--- | :--- | :---
The user should be displayed with a page allowing them to register.

<br>
<br>

## Login Page
| Page | Outcome | Result Desktop | Result iPad | Result S9+ Phone 
| :--- | :--- | :--- | :--- | :---
The user should be displayed with a page allowing them to log in. 

<br>
<br>

## Logout Page
| Page | Outcome | Result Desktop | Result iPad | Result S9+ Phone 
| :--- | :--- | :--- | :--- | :---
The user should be displayed with a page allowing them to log out. 

<br>
<br>
