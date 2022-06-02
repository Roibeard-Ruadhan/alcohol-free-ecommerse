https://github.com/Roibeard-Ruadhan/alcohol-free-ecommerse

# The Alcohol Free Shop
**The Alcohol Free Shop** is an ecommerce website allowing users to purchase Alcohol-Free drinks developed for my e-commerse Project 5 as part of the Code Institute - Diploma in Software Development (Full stack) Diploma.

## About

Link to [live site](https://alcohol-free-shop.herokuapp.com/)

## **Contents**

- [**UX (User Experience)**](#ux-user-experience)
  - [**User Stories**](#user-stories)
  - [**Site Owner Goals**](#site-owner-goals)
- [**Design Choices**](#design-choices)
  - [**Fonts**](#fonts)
  - [**Colours**](#colours)
  - [**Imagery**](#imagery)
  - [**Wireframes**](#wireframes)
- [**Technologies**](#technologies)
  - [**Languages**](#languages)
  - [**Database**](#database)
  - [**Libraries**](#libraries)
  - [**Tools**](#tools)
- [**Features**](#features)
  - [**Site Navigation**](#site-navigation)
  - [**Features Implemented**](#features-implemented)
  - [**Future Features**](#future-features)
  - [**Responsive Design**](#responsive-design)
- [**Version Control**](#version-control)
- [**Testing**](#testing)
- [**Deployment**](#deployment)
  - [**Running Locally**](#running-locally)
- [**Credits**](#credits)
  - [**Code**](#code)
  - [**Content**](#content)
  - [**Images**](#images)
  - [**Inspiration**](#inspiration)
  - [**Acknowledgements**](#acknowledgements)
  

## **UX (User Experience)**


### **User Stories**
- All users
    - As a user
    -
    -

- As a first time user
  

- As a returning user
 


### **Site Owner Goals** 



[Back to contents](#contents)


## **Design Choices**


### **Fonts**




### **Colours**


### **Imagery**



### **Wireframes**


- Desktop view
- for each page


- Mobile view
  


[Back to contents](#contents)


## **Technologies**

- [Django](https://www.djangoproject.com) - Framework used.
- [Stripe](https://stripe.com/) - Used for adding payment functionality.
- [AWS](https://aws.amazon.com/) - Used for hosting static and media files.
- [Balsamiq](https://balsamiq.com) – Used for creating the wireframes.
- [Heroku](https://signup.heroku.com/) - Where the live site is deployed.
- [Bootstrap 4](https://getbootstrap.com) - Bootstrap grid system, utility classes, nav-bar, toasts, cards, badges and tables.
- [Django Crispy Forms](https://django-crispy-forms.readthedocs.io/en/latest/) - Used for rendering forms.
- [Fontawesome](https://fontawesome.com/) - Used for icons.
- [Google Fonts](https://fonts.google.com) - The 2 fonts used throughout the website are from Google fonts.
- [Git](https://git-scm.com/) - Used for version control.
- [GitHub](https://github.com) - Used to store the project repository.
- [Gitpod IDE](https://www.gitpod.io/) - Development environment where the site was built.
- [Gimp 2.1](https://www.gimp.org/) - Used for editing, scaling images.
- [icons8](https://icons8.com) - Used for creating a favicon.
- [Bulkresizephoto's](https://bulkresizephotos.com/en) - Used for compressing & transering images to png.
- [Chrome Dev Tools](https://developers.google.com/web/tools/chrome-devtools) - Used throughout the development of the website to quickly see changes, find problems and debug. Also used to view website in different device views.
- [Lighthouse](https://developers.google.com/web/tools/lighthouse) in Chrome Dev Tools - Used for site performance review.
- [W3C HTML validator](https://validator.w3.org/) - Used to validate code.
- [W3C CSS validator](https://jigsaw.w3.org/css-validator/) - Used to validate code.
- [JSHint](https://jshint.com/) – Used to validate Javascript code
- [Coolors](https://coolors.co/) - Used for selecting complimentary colour palettes.
- [Facebook page](https://www.facebook.com/Alcohol-Free-Shop-101298052611366) - Used Facebook page to promote website

### **Languages**

- [HTML5](https://developer.mozilla.org/en-US/docs/Web/HTML)
  - Used as the main markup language for the website content.
- [CSS3](https://developer.mozilla.org/en-US/docs/Web/CSS)
  - Used to style the individual webpages.
- [Python 3](https://www.python.org/)
    - Used to run the site and database
- [JavaScript](https://developer.mozilla.org/en-US/docs/Web/JavaScript)
    - Used to show the questions through pagination and for the game play.

### **Database**

- [Amazon]


### **Libraries**



### **Services**


### **Tools**


[Back to contents](#contents)

## **Features**

### **Site Navigation**





### **Features Implemented**



[Back to contents](#contents)


### Features 


[Back to contents](#contents)





[Back to contents](#contents)



[Back to contents](#contents)

### **Error Pages**

#### *404.html*


#### *500.html*

### **Future Features**


### **Responsive Design**


[Back to contents](#contents)


## **Database Layout**


[Back to contents](#contents)

## **Version Control**


### Gitpod Workspaces


### Gitpod branching and committing to GitHub


[Back to contents](#contents)

## **Testing**

- Testing and Bugs can be found [here](TESTING.md)


## **Deployment**

### Github
The project was developed using [GitPod](https://gitpod.io/) and pushed to [GitHub](https://github.com/) then deployed on Heroku using these instructions:

1. Create a requirements.txt file using command *pip3 freeze --local > requirements.txt*
2. Create a Procfile with the terminal command *echo web: python app.py > Procfile* and at this point checking the Procfile to make sure there is no stray line as this can cause issues when deploying to Heroku.
3. The new requirements file and Procfile committed to GitHub.
4. New app created in Heroku by clicking "New" and "Create New App" and giving it an original name and setting the region to closest to location.
5. From Heroku dashboard click "Deploy" -> "Deployment Method" and select "GitHub"
6. Search for GitHub repo and connect.
7. In the dashboard click "Settings" -> "Reveal Config Vars"
8. Set config vars:

### Heroku Deployment

1.	Login to Heroku.com and click New -> Create New App

* Add a name
* Select region
* Click Create App

2.	To add the postgres database in Heroku:

In the Resources tab -> Add ons:
*   Search for postgres
*   Select Heroku Postgres
*   Select the free option
*   Click submit

3.	In the gitpod environment install dj_database_url and psycopy2 packages using the commands:

        pip3 install psycopy2-binary

        pip3 install dj_database_url

4.	Freeze these requirements into the requirements.txt file by running the following command:

    pip3 freeze —local > requirements.txt

This will ensure all the dependencies currently used by the app are in the requirements.txt file.

5.	Update the settings.py file by adding:

        import dj_database_url

And setting up the new database settings:

        DATABASES = {
            ‘default’ = dj_databse_url.parse(‘<postgres_url>’)
        }

Comment out the original database setting for now so that we are connected to the postgres database.

6.	Now run migrations for the new postgres database. First showmigrations to see that the migrations still need to be applied using

        python3 manage.py showmigrations

Apply the migrations using:

        python3 manage.py migrate

7.  Create a superuser:

        python3 manage.py createsuperuser

8.	To get the data from the original sqlite database used in Gitpod:

*   Reconnect to the original sqlite database in settings.py
*   Backup the sqlite database and load it into a db.json file using the command:

        ./manage.py dumpdata --exclude auth.permission --exclude contenttypes --indent 2 > db.json

* Then connect back to the postgres database in settings.py 
* Load the data from the db.json file into the postgres database using the command:

        ./manage.py loaddata db.json

9.	Then we can run the site using the postgres database.

10.	Setup settings.py file to use either the sqlite database when running on gitpod or the postgres database when running on Heroku by using the following code:

        If 'DATABASE_URL' in os.environ:
	
            DATABASES = {
                'default': dj_database_url.parse(os.environ.get('DATABASE_URL'))
            }
	
	    else:
	
            DATABASES = {
                'default': {
                    'ENGINE': 'django.db.backends.sqlite3',
                    'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
                }
            }

Ensuring the DATABASE_URL environment variable is set in the Heroku config vars.

11.	 Install gunicorn which acts as our webserver:

    pip3 install gunicorn

And then:

    pip3 freeze —local > requirements.txt

To save it in the requirements.txt file.

12.	Create a Procfile and add the following code to it which tells Heroku to create a web dyno which will run gunicorn and serve our app.

        Web: gunicorn <app_name>.wsgi:application

13.	 Initially disable collectstatic in Heroku, this can be done in the cli:

* Heroku login -i
* Enter Heroku login details
* And run:

        Heroku config:set DISABLE_COLLECTSTATIC = 1

14.	 Update allowed hosts in settings.py to 

        ALLOWED_HOSTS = [‘<heroku_app_name>.herokuapp.com’, ‘localhost’]

15.	Git add, git commit and git push files to GitHub so they are available to Heroku which will use them to build the app.

16.	 Initialise the Heroku git remote in the CLI:

    Heroku git:remote -a <heroku_app_name>

17.	 Push to Heroku:

    git push Heroku main

The app is now deployed via Heroku.

18.	Can no longer set up automatic deployments on Heroku. So each time you open your workspace on Gitpod VS you should:

* Heroku login -i
* Enter Heroku login details
* git add.
* git commit -m "<Your Update here>"
* git push 
* git push Heroku main

19.	In Heroku Config Vars set up a SECRET_KEY & add to env.py file for backup

## Amazon Web Services (AWS) 

### Initial Setup

1.	Create an account on aws.amazon.com

* Click create account
* Enter details
* Enter billing details
* Verify account via SMS
* Select a plan
* Sign up

2.	In the AWS  Management Console

* Open the S3 Service
* Select Create bucket
* Add a name for the bucket
* Enable All Public Access and acknowledge
* Click Create Bucket

3.	Set up the bucket:

    #### Properties Tab:

    * Static website hosting -> Edit -> Enable
    * Set index.html as Index Document
    * Save Changes 

    #### Permissions Tab:

    * CORS -> Edit
    * And set:

    ```
    [
    {
        "AllowedHeaders": [
            "Authorization"
        ],
        "AllowedMethods": [
            "GET"
        ],
        "AllowedOrigins": [
            "*"
        ],
        "ExposeHeaders": []
    }
    ]
    ```

    #### Permissions Tab:

    * Bucket Policy -> Edit -> Policy Generator – note the ARN
    * Policy type: S3 bucket
    * Allow all principles by setting it to *
    * Action: Get object
    * Enter ARN from above
    * Add Statement
    * Generate Policy
    * Copy the policy and paste it into the bucket policy editor
    * Add /* at the end of the resource key to allow access to all resources.
    * Save changes

    #### Permissions Tab:

    * Access Control List (ACL) -> Edit
    * In the public access section select list.
    * Save changes.
	
### Setup AWS Identity Access Management (IAM)

1.	Create a user group:

* Click user groups -> Create group
* Name the group
* Create group

2.	Create a policy:

* Click Policies -> Create Policy
* Select JSON tab -> Import managed policy
* Import the S3 Full Access Policy
* Get the bucket ARN from the bucket policy and add it to the resource key as a list where the first item in the list is the ‘ARN’
And the second item is the ‘ARN/*’
* Click next
* Review Policy
* Name the policy -> Create Policy

3.	Attach the policy to the group we created:

* User Groups -> Click on the group -> Permissions
* Add permissions -> Attach Policy -> Select the one just created
* Add permissions

4.	Create a User to add to the Group:

* On the Users tab -> Add User -> Create a name for the user
* Allow Programmatic Access
* Click Next
* Add the user to the group just created
* Click next -> Create User
* Download the .csv file containing the access key and secret access key. This file can only be downloaded now.

### Connecting Django to S3

1.	Install boto3 and django-storages packages

        pip3 install boto3
        pip3 install django-storages
        pip3 freeze > requirements.txt

* Add storages to the list of installed apps in settings.py

2.	In Heroku Config Vars add the variables

        AWS_ACCESS_KEY_ID
        AWS_SECRET_ACCESS_KEY

* Using the values from the .csv file downloaded from AWS.

3.	Delete the DISABLE_COLLECTSTATIC variable from the config vars and deploy the Heroku app.

4.	In the S3 bucket create a folder called `media` and upload any required media files to it. Under Manage Public Permissions -> Select grant public read access to these objects -> Upload.



### How to run the project locally


[Back to contents](#contents)


## **Credits**

### **Code**


### **Content**


### **Images**




### **Acknowledgements**
I don't have much time to write this but I can't thank the Tutor team enough for their incredible guidance & support throughout this project. To my Mentor Gurjot_mentor for all his advice, feedback & support. To Kasia for her endless inspiration & advice. Many thanks to the Slack community & to the Tutor team at Code Institute for their help throughout the development process 


### **Disclaimer**
This project is for educational purposes only.


[Back to contents](#contents)