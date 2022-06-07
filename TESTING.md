The project was tested thoroughly and the results are presented below:

## Table of contents:

 * [Validation](#validation)
    + [HTML](#html)
      - [W3C Markup Validation Service](#w3c-markup-validation-service)
    + [CSS](#css)
      - [W3C CSS Validation Service](#w3c-css-validation-service)
    + [JavaScript](#javascript)
      - [JSHint](#jshint)
    + [Python](#python)
    + [Lighthouse](#lighthouse)
      - [Desktop](#desktop)
      - [Mobile](#mobile)
  * [Testing of User stories & UX values](#testing-of-user-stories-&-ux-values)
      - [General](#general)
      - [Products](#products)
      - [Reviews](#reviews)
      - [Bag](#bag)
      - [Checkout](#checkout)
      - [Blog](#blog)
      - [Contact](#contact)
  * [Testing process](#testing-process)
    + [Manual Testing](#manual-testing)
      - [Navigation bar](#navigation-bar)
      - [Footer](#footer)
      - [Home](#home)
      - [Sign up page](#sign-up-page)
      - [Login page](#login-page)
      - [Logging out](#logging-out)
      - [Products](#products-1)
      - [Bag](#bag)
      - [Checkout](#checkout)
      - [Profile](#profile)
      - [Blog Management](#blog-management)
      - [Product Management](#product-management)
      - [Blog](#blog)
      - [Contact](#contact)
      - [Toasts](#toasts)
      - [CRUD Functionality](#crud-functionality)
      - [Responsiveness](#responsiveness)
      - [Browsers and devices](#browsers-and-devices)
      - [Stripe Testing](#stripe-testing)
      - [Defensive Programming](#defensive-programming)
    + [Bugs](#bugs)
      - [Fixed Bugs](#fixed-bugs)
      - [Known Bugs](#known-bugs)

## Validation

### HTML

#### W3C Markup Validation Service 

* [W3C Markup Validation Service](https://validator.w3.org/) was used to validate the HTML of the project. Each page was validated by its URL and produced no errors or warnings. When each HTML page was validated by direct input, all errors produced were due to templating.

![HTML Validation](readme/testing-images/)

### CSS

#### W3C CSS Validation Service

* [W3C CSS Validation Service](https://jigsaw.w3.org/css-validator/) was used to validate the CSS of the project. As well as showing no errors when validating the projects CSS through its URI, there was also no errors when each CSS file was validated through direct input.

![CSS Validation](readme/testing-images/validation/)

### JavaScript

#### JSHint

* All JavaScript files or snippets of JavaScript at the bottom of HTML files were validated successfully through [JSHint](https://jshint.com/).

![JavaScript Validation](readme/testing-images/validation/)

### Python

* All Python files were validated through the use of [PEP8 online](http://pep8online.com/) and all passed successfully.

![Python Validation](readme/testing-images/validation/)

* A Gitpod built-in linter called pylint was also used to fix bugs within the python code and provided many suggestions on how to improve the code. For instance it advised to place a docstring at the top of all the python files.

![Pylint Example](readme/testing-images/validation/)

### Lighthouse

* Lighthouse was also used to test the project on both desktop and mobile.

#### Desktop

![Lighthouse Desktop Result](readme/testing-images/validation/)

#### Mobile

![Lighthouse Mobile Result](readme/testing-images/validation/)

## Testing of User stories & UX value

* Starting from an unregistered customer...

    #### General

    * *As a user I can I want to be clear what the site is for so that I can avoid wasting time if it does not offer me value*

        * On arrival of the website, the user is able to understand the purpose of the website. This is due to the use of imagery, logo, the homepage CTA and the navigation links available to the user to visit.

        ![Homepage background](readme/assets/testing-images/user-story/home-page.jpg)

    * *As a shopper I can easily register for an account so that have a personal account to be able to view my profile*

        * 

        ![Sign up location](readme/testing-images/)
    
    * *As a shopper I can follow on Facebook so that I can be up to date with announcements & share with my followers*

        * The

        ![Homepage background](readme/testing-images/user-story/)

    * *As a shopper I can sign up for a newsletter so that I can avail of the discount & updates on new products etc*

        * The

        ![Homepage background](readme/testing-images/user-story/)

    * *As a shopper I can have a personalized user profile so that I can view my personal order history and order confirmations and save my payment information*

        * 

        ![Sign up location](readme/testing-images/)

    * *As a shopper I can receive an email confirmation after registering so that I can verify that my account registration was successful*

        * 

        ![Sign up location](readme/testing-images/)

    * *As a shopper I can easily recover my password in case I forget it so that I can access my personal account information*

        * 

        ![Sign up location](readme/testing-images/)

    * *As a shopper I can easily login or logout so that have a personal account & be able to view my profile*

        * 

        ![Sign up location](readme/testing-images/)


    ### Products

    * *As a shopper I can view individual drink details so that identify the price, category, description product rating, drink image, customer ratings & reviews*

        * 

        ![Sign up location](readme/testing-images/)

    * *As a shopper I can easily select the quantity of drink I wish to purchase so that I can ensure I don't accidentally select the wrong product or quantity*

        * 

        ![Sign up location](readme/testing-images/)

    * *As a shopper I can easily see what I have searched for and the number of results so that I can quickly decide whether the product I want is available*

        * 

        ![Sign up location](readme/testing-images/)

    * *As a shopper I can search for a drink by name or description so that I can find a specific drink I would like to purchase*

        * 

        ![Sign up location](readme/testing-images/)

    * *As a shopper I can sort a specific category of a drink so that I can find the best priced or best-rated product in a specific category*

        * 

        ![Sign up location](readme/testing-images/)

    * *As a shopper I can sort the list of available drinks so that I can easily identify the best rated or the best priced or even in categories from a-z*

        * 

        ![Sign up location](readme/testing-images/)


    ### Reviews
    * *As a user I can rate, rank, review & read reviews, so that I can inform others of my experience while learning from others experiences*

        * The

        ![Homepage background](readme/testing-images/user-story/)

    ### Bag
     * *As a shopper I can adjust the quantity of individual items in my bag so that I can easily make changes to my purchase before checkout*

        * 

        ![Sign up location](readme/testing-images/)

    * *As a shopper I can view items in shopping bag to be purchased so that I can identify the total cost of my purchase and all items I will receive*

        * 

        ![Sign up location](readme/testing-images/)

    * *As a shopper I can easily view the total of my purchases at any time so that avoid spending too much*

        * 

        ![Sign up location](readme/testing-images/)
    ### Checkout
    * *As a shopper I can enter my details when making a payment while momentarily setting up an account so that I do not have to set up an acount in advance or in the future*

        *

        ![Sign up location](readme/testing/ux-testing/)

    * *As a shopper I can receive an email confirmation after checking out so that I can keep the confirmation of what I have purchased for my records*

        * 

        ![Sign up location](readme/testing-images/)

    * *As a shopper I can view an order confirmation after checkout so that I can have peace of mind that I have not made any errors*

        * 

        ![Sign up location](readme/testing-images/)

    * *As a shopper I can feel my personal and payment information is safe and secure so that I can confidently provide the needed information to make a purchase*

        * 

        ![Sign up location](readme/testing-images/)

    * *As a shopper I can easily enter my payment information so that I can checkout quickly with no hassle*

        * 

        ![Sign up location](readme/testing-images/)

    ### Blog
    * *As a user/non user I can view comments on an individual post so that I can read other peoples opinion*

        * 

        ![Sign up location](readme/testing-images/)

    * *As a User I can view a list of posts so that I can select one to read based on the synopsis*

        * 

        ![Sign up location](readme/testing-images/)

    * *As a user I can leave comments on a post so that I can be involved & express my view*

        * 

        ![Sign up location](readme/testing-images/)

    ### Contact
    * *As a shopper I can contact the shop so that I can make a query in relation to the business or products etc*

        * 

        ![Sign up location](readme/testing-images/)






   
## Manual Testing

## Testing process

### Manual Testing

### Navigation bar

### Footer

### Home

### Sign up page
    * *As a shopper I can receive an email confirmation after registering so that I can verify that my account registration was successful*

        * 

        ![Sign up location](readme/testing-images/)

### Login page

### Logging out

### Products
* *As a staff member I can get a notification if I edit or delete a product so that I can undo my error if I press delete by accident*
### Reviews

### Bag

### Checkout

### Profile
    * *As a shopper I can easily recover my password in case I forget it so that I can access my personal account information*

        * 

        ![Sign up location](readme/testing-images/)

    * *As a shopper I can easily login or logout so that have a personal account & be able to view my profile*

        * 

        ![Sign up location](readme/testing-images/)

    * *As a shopper I can easily register for an account so that have a personal account to be able to view my profile*

        * 

        ![Sign up location](readme/testing-images/)
### Blog Management
* *As a site admin I can approve or disapprove comments so that I can filter out somewhat objectionable comments*
### Product Management
    * *As an admin I can add a new drink so that I can allow customers a wider selection to choose from*

        * 

        ![Sign up location](readme/testing-images/)

### Blog

    * *As an admin I can delete a drink(product) so that I can remove items that are no longer for sale*

        * 

        ![Sign up location](readme/testing-images/)

### Contact

### Toasts

### CRUD Functionality

### Responsiveness

### Browsers and devices

### Stripe Testing

### Defensive Programming

## Bugs

### Fixed Bugs

### Known Bugs

    
