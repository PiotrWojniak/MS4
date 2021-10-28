
<p align="center">
<img src="https://images89.fotosik.pl/548/0b5110f8ec8b529am.jpg">
</p>

## ***Welcome to Family Craft e-commerce store made straight from the heart***

Code Institute - Milestone Project 4

The assumption of the project is to introduce a new brand to the market and sell hand-made products. The user will have a choice of different product categories through interior design, clothing, and accessories. A detailed description of what material was used to make it, how it was made and the size,

---
# ***Website Showcase***

<img src="https://images90.fotosik.pl/547/5217d7155e6bb172.jpg">

---
# ***UX***

+ ## Project goals

The virus pandemic has hit everyone, especially small family businesses. Due to the decline in direct sales, the family decided to make their products available through an online store.The aim of the project is to sell handmade products made by the whole family and enable users to buy the product online as a registered user and without loggin. Allow user to check the purchase history after registering in to the website, receivie confirmation e-mail and if nesserly contact with the owner.

+ ## User Stories

|  __User Story ID__  | __As A/An__ |__I want to be able to...__ | __So then I can...__ |
|-----|--|---------------------------|----------------------------|
|    | __Viewing and Navigation__ |
| 1. | Shopper | View a list of all product | Easily select some of them to purchase|
| 2. | Shopper | View individual product details | See decription, chose a size, identity price and product image. |
| 3. | Shopper | Easily identify all special offers and clearance | recieved a savings on product I'd like to buy |
| 4. | Shopper | View the total of my purchases at any time | Take control of my spending |
|    | __Registration and user account__ |
| 5. | Site User | Register for an account | Create my personal account to view my purchase histrory, save payment and shipping information |
| 6. | Site User | Receive an email confirmation after registering | Verify that my account registration was successful |
| 7. | Site User | Easily login/logout or reset my password in case I forget it | Access to personal account information and recover my password |
|    | __Admin and Store Management__ |
| 8. | Store Owner | Add product | Add new items to my store |
| 9. | Store owner | Edit/Update and Delete a product | Change product description, price, images and remove items that are no longer for sale |
|    | __Sorting and Searching__ |
| 10.| Shopper | Sort the list of available products and specific category | Easily sort list of the product in that category by name or price |
| 11.| Shopper | Sort multiple categories of products | Sort product by price, name and by categories for all available product | 
| 12.| Shopper | Search for a product by name or description and see number of results | Find a specific product I'd like to purchase and see how many product is available |
|    | __Purchasing and Checkout__ |
| 13.| Shopper | Easly select the size and quantity | Ensure I dont select the wrong product, quantity or size |
| 14.| Shopper | View item in my bag and update them if needed | Identify the total cost of my purchase and all items I will received, and change quantity or remove items from bag if needed. |
| 15.| Shopper | View an order confirmation after checkout and receive email after checkout | Make sure I haven't made any mistakes with my order and keep the purchase confirmation of what I bought for my own record. |
| 16.| Shopper | Feel my personal and paymant information is safe and secure. | Confidentialy provide the needs information to make a purchase |

---
# ***Design***

+ Django Admin Panel

    <details>
       <img src="https://images90.fotosik.pl/548/007b4212f193de18med.jpg">
    </details>  

+ Side map
<img src="https://images91.fotosik.pl/548/52857ed1a71eeffa.png">

### Colours
In this project we deside use an Orange and Green colours. Orange It is a colorful term not only for joy, but also for fascination and determination that are buttons is style with them. Green is associated with nature and has a calming effect. As our products are mostly of natural origin, it was chosen as the background of the buttons.
<details>
    <summary>Palette</summary>
    <img src="https://images90.fotosik.pl/547/b683ed423e91aa61.png">
   
   - Honeydew #EEFFED - background color in product card.
   - Almond #EDDAC9 - background of all the cards and forms.
   - Deep Saffron #FB9237 - background of hover buttons.
   - Kombu Green #2C462B - background of footer, delivery baner.
   - Phanthalo Green #20321F - base colour.
</details

### Font
   In this project i use two fonts:
   LATO - default text on the side.
   LOBSTER - this font is excelent maching for type of the product on the page. It's used as Brant Logo, footer, navigation bar, my account and bag.


### Wireframe
The wireframe model is created as part of the project planning. Its task is to graphically present the appearance of the application on three different devices: computer - high resolution, tablet - medium resolution, mobile - low resolution. The application will be built on the basis of the created sketch.

<details><summary>Sketch</summary>
   <br>
      <details>
         <summary>Home</summary>
         <img src="https://images91.fotosik.pl/548/a042e7a62506fa48.png">
      </details>   
      <details>
         <summary>All Products</summary>
         <img src="https://images91.fotosik.pl/548/a1b189c9fab85de1.png">
      </details>  
      <details>
         <summary>Product view</summary>
         <img src="https://images92.fotosik.pl/549/9ed56145fe25e7ed.png">   
      </details>
      <details>
         <summary>Sign in / Password reset</summary>
         <img src="https://images90.fotosik.pl/548/ce5be83a43f90401.png">   
      </details>
      <details>
         <summary>Bag</summary>
         <img src="https://images91.fotosik.pl/548/fb52ff83d756ded3.png">
      </details>  
      <details>
         <summary>Checkout</summary>
         <img src="https://images92.fotosik.pl/549/bc1079861edd3297.png">
      </details>  
      <details>
         <summary>Profile & Add product</summary>
         <img src="https://images92.fotosik.pl/549/7e89288214340521.png">
      </details>
      <details>
         <summary>Register</summary>
         <img src="https://images90.fotosik.pl/548/254f36a493def443.png">
      </details>
</details>
                    
### Data Base schema
<details>
   <summary>Sketch</summary>
   <img src="https://images91.fotosik.pl/548/7cb05f5db4635f75med.png">
</details>
                    

### Differences between design and the end result
There were a few changes to the plan during production. The background colors and card design have been changed for a cleaner look. A new option of contacting the store has also been added.
    
### Wireframe update
<details><summary>Sketch</summary>
   <br>
      <details>
         <summary>Home</summary>
         <img src="https://images92.fotosik.pl/549/4dd9db87876100f5.png">
      </details>   
      <details>
         <summary>All Products</summary>
         <img src="https://images90.fotosik.pl/548/c1ea634b211982cd.png">
      </details>  
      <details>
         <summary>Product view</summary>
         <img src="https://images89.fotosik.pl/549/4b7002ccab1e11e1.png">   
      </details>
      <details>
         <summary>Sign in / Password reset</summary>
         <img src="https://images89.fotosik.pl/549/527308ffb6e9ee6a.png">   
      </details>
      <details>
         <summary>Bag</summary>
         <img src="https://images90.fotosik.pl/548/4a3ee11349f17a43.png">
      </details>  
      <details>
         <summary>Checkout</summary>
         <img src="https://images91.fotosik.pl/548/23615ed52d8da72e.png">
      </details>  
      <details>
         <summary>Profile & Add product</summary>
         <img src="https://images90.fotosik.pl/548/98313450bde5bc78.png">
      </details>
      <details>
         <summary>Register</summary>
         <img src="https://images90.fotosik.pl/548/30db9e1e2c71cd39.png">
      </details>
      <details>
         <summary>Register</summary>
         <img src="https://images92.fotosik.pl/549/bff612878d6b0a53.png">
      </details>
</details>

---
# ***Features***

## Existing features

+ App is fully responsive to all different sizes.
    
+ Supported by Edge, Chrom, Firefox and Safari
    
+ ***Navigation Bar***
Navigation bar works as intended. When you click on the site name, you will be taken directly to the home page. When you press the home button from the drop-down menu, you'll be taken to the home page. The site has four categories, all products, clothing, household items and specials listed in the Large Appliances Center and a drop-down menu for medium and small appliances. In the upper right corner there is a login that takes the user to the page where he can log in or register.

+ ***Home page***
The home page has a background image and a welcome text with a large shop now button that will automatically take the user to the product page. At the top of the page there is a logo, a search bar, product categories, an icon with login access and the total value of the basket. At the bottom there is a footer with links to social media and a form of contact with the store. It is there also knows the copyright.


+ ***All products***
The all product's page has a bar that allows you to sort your products, and counter for all products currently displayed. In the lower right corner, is a button that allows you to return to the top of the page without scrolling through the content.


+ ***Bag and checkout***
The basket is available by clicking on the bag icon. The user will be taken to the cart summary, which shows the total amount to be paid with the product value and delivery. You can update or delete a product in the cart at the same time. If everything is correct, we proceed to finalize the order. We can place an order as a logged-in user or without. We need to complete the form and make the payment. There is also adjust bag button, which will go back to the cart.    
    

+ ***Log In***
Access to login is available by hovering the pointer over large devices or pressing the button on medium and small my account. The user will be redirected to the login page where they can complete their data and, if they wish, they can be remembered. In addition, there are buttons for registration and password reset.


+ ***Register***
 Access to registration is possible through the same button on my account. The user will be redirected to the registration page, where he has to complete his data. Additionally, above the form and at the bottom, there is a login button if the user already has his own login.


+ ***Profile page***
The profile tab consists of two parts. The first one contains shipping details, which we will update if necessary. The second part is your purchasing history.


+ ***Edit/Delete***
Editing and deleting products is strictly limited to users authorized by the store. After logging in, each card with the product has two buttons for editing and removing.


+ ***Add product***
To add a product, you must have the same permissions as when editing. Access to this option can be provided by the product management on my account. After selecting the option, the user will be redirected to the form with the following options:
product categories, product number, name, description, size options, price evaluation and a picture in the form of a link or upload directly from the computer using a button.
 

+ ***Log out*** 
The logout option is in my account. After clicking on logout, the user will be asked to confirm its choice or cancel and return to the home page.
    
+ ***Contact***
If the user needs to contact the shop, he can do it by pressing the envelope icon at the bottom of the screen. A form with a choice of query, name, email address and message will be displayed.

+ ***Error page***

    + 404 error page is a custom page for a non-existing domain and is present with easy navigation button back to the home page.
        <details>
         <img src="https://images91.fotosik.pl/548/de190e2186124c3d.jpg">
      </details>
          
    + 500 error page is a custom page for Internal Server Error which is a very general HTTP status code that means something has gone wrong on the web site's server.

## Features nice to have
 + ***Use a Social media login***
 + ***Link contact form to the order number***
 + ***Allow users to rate the product***
---
# ***Technology***
<details>
   <summary>Languages</summary>

+ <img src="https://img.icons8.com/color/48/000000/html-5--v1.png"/> [HTML](https://en.wikipedia.org/wiki/HTML) - to creating structure and layout of the webpsite.
+ <img src="https://img.icons8.com/color/48/000000/css3.png"/> [CSS](https://en.wikipedia.org/wiki/CSS) - to styling the HTML.
+ <img src="https://img.icons8.com/color/48/000000/javascript.png"/> [JavaScript](https://en.wikipedia.org/wiki/JavaScript) - to interactive web applications.
+ <img src="https://img.icons8.com/color/48/000000/python.png"/> [Python](https://en.wikipedia.org/wiki/Python_(programming_language)) - to run queries to the database.
</details>
<details>
   <summary>Frameworks, Libraries & Programs</summary>
   
+ <img src="https://images91.fotosik.pl/495/94f9449ae6eadb99.png"/> [Jinja](https://en.wikipedia.org/wiki/Jinja_(template_engine)) - as a templates engine for Python.
+ <img src="https://images92.fotosik.pl/496/ff9586f55010cb7e.png"> [Flask](https://en.wikipedia.org/wiki/Flask_(web_framework)) - 
+ <img src="https://images92.fotosik.pl/496/0e0b55372d3fa10f.png"> [Werkzeug](https://werkzeug.palletsprojects.com/en/1.0.x/) - 
+ <img src="https://img.icons8.com/color/48/000000/mongodb.png"/> [mongoDB](https://en.wikipedia.org/wiki/MongoDB)  - 
+ <img src="https://images90.fotosik.pl/495/31f55faa8a7f0f25.png"/> [Materialize](https://materializecss.com/) -  
+ <img src="https://images91.fotosik.pl/495/ff7e331eae631581.png"> [JQuery](https://en.wikipedia.org/wiki/JQuery) - is a JavaScript library designed to simplify HTML DOM tree traversal and manipulation
+ <img src="https://images90.fotosik.pl/496/0bfff63014e8ea32.png"> [RandomKeygen](https://randomkeygen.com/) - to generate password for flash and session function of flask
+ <img src="https://images90.fotosik.pl/496/9090f1a039521721.png"> [Heroku](https://en.wikipedia.org/wiki/Heroku) - as a deploying cloud platform to supporting several programming languages
+ <img src="https://images91.fotosik.pl/495/349a636c9586126b.png"> [GitHub](https://en.wikipedia.org/wiki/GitHub) - to create and host project
+ <img src="https://images89.fotosik.pl/496/b2208ad81e139641.png"> [Balsamiq](https://en.wikipedia.org/wiki/Balsamiq) - to create wireframes during design process
+ <img src="https://images90.fotosik.pl/496/ded7f996b572ca06.png"> [Favicon](https://favicon.io/logo-generator/) - for logo generator
+ <img src="https://images91.fotosik.pl/495/b1d4fe3fd419b9da.png"> [Google font](https://fonts.google.com/) - for font style.
+ <img src="https://images92.fotosik.pl/496/98be9f646b97e1fa.jpg"> [Visual studio](https://visualstudio.microsoft.com) - console for writing code.
</details>

---
# ***Testing*** 
<details>
   <summary>Validation</summary>

   *All walidation is made on Heroku app*
1. [**To validate Html**](https://validator.w3.org/)

   + Warnings:
      1: Clousing </div> tag without opening.
      * FIX - Remove unused tag
   + Errors:
       1: Bad value for sttribut href on link elemen.   
      *Fix - Typo error - missing % at the end.
2. [**To validate CSS**](https://jigsaw.w3.org/css-validator/)
   <p><a href="https://jigsaw.w3.org/css-validator/check/referer">
        <img style="border:0;width:88px;height:31px"
            src="https://jigsaw.w3.org/css-validator/images/vcss"
            alt="Valid CSS!" /></a></p>
    <p><a href="https://jigsaw.w3.org/css-validator/check/referer">
        <img style="border:0;width:88px;height:31px"
            src="https://jigsaw.w3.org/css-validator/images/vcss-blue"
            alt="Valid CSS!" /></a></p>
    
3. [**To validate Js**](https://jshint.com/)
   Js was validate with out fails. Only one variable was return as undefine but its not affectink functionality of project.
      <img src="https://images89.fotosik.pl/549/698638d91af2bc14.gif">
   
4. [**To validate Python using PEP8, flake8, pylint**](http://pep8online.com/)
   The results of the Python validation was return without errors but some of the modules return warning as: 'django.test.TestCase' imported but unused. I belive those type of the warning is not affecting functionality of my code so I decide not delete them as there be used in feature testing. I also attached a flake8_pylint_Test.txt [here](https://github.com/PiotrWojniak/MS4/blob/main/readme_files/flake8_pylint_Test.txt) file to explore of the all warnings. 
  
</details>
<details>
   <summary>Lighthouse</summary>
   
   + Home page
      
      <img src="https://images91.fotosik.pl/548/89255e1b6599d95a.png">
         
   + Product page
      
      <img src="https://images89.fotosik.pl/548/29a2ba090feb2c69.png">
         
   + Admin panel
      
      <img src="https://images92.fotosik.pl/549/8c5d6c631289d47a.png">

</details>
<details>
   <summary>Testing Devices and web browser</summary>
1. App was tested at Asus laptop, Macbook pro, custom PC, Samsung Galaxy A7, Iphone XS
2. Browser used for testing:
   + Chrome - no isuues
   + Safari - no issues
   + Edge - no issues
   + Firefox - no issue.
</details>
<details>
   <summary>Errors and fix</summary>
    + No error to fix
</details>
<details>
   <summary>Bugs and Problems</summary>
    + No bugs or issue 
</details>

# ***Testing user story*** 

<details>
    <summary>Viewing and Navigation</summary>
    
1. The user selects products to view from the list available on the navigation bar.
2. The image and the price of the product are already available on all products page. To see the exact details, click on the product image. The card contains the exact description of the product, its rating if available, size to choose from, also if available.
3. All special offers and sales are available by selecting the special offers option from the navigation bar.
4. The total cost of purchases will shown in the upper right corner of the application after adding product in to the bag.
    
    <img src="https://images91.fotosik.pl/548/77373cbe00dd664f.jpg">
</details>

<details>
    <summary>Registration and user account</summary>
    
 5. To register, click on my account icon and choose registration from the menu. After filling the form and the click sing up, info massage appear and activation link will be sent to your email. After activating the account and logging in, the delivery options with the address and telephone number as well as the history of purchase will appear in the profile.
 6. Criteria met above
    [Confirmation email](https://github.com/PiotrWojniak/MS4/blob/main/readme_files/confemail.txt)
 7. Clicking my account and chose login. In login page fill the form and click sign in to login if password is need to reset click forget password. Then put your registration email address and click reset my password, after that email with resetting password will be sent. If you finish shopping, logout option is in my account.
</details>

<details>
    <summary>Admin and Store Management</summary>
  
  8. Only authorized users can add, edit and delete products. To add a product, please select product management from my account. A new tab will open with all the information needed to add a product, such as: category, sku, name, description, whether the product contains size, price, rating and a picture as a link or uploaded from a computer. After clicking Add a product, a message will appear with the information that the product has been added. This option is available both from the store's website and from the django administration panel.
  9. After logging in, each card with the product has two buttons for editing and removing. In edit process you can change everything, removing image and add new.
  
</detals>

<details>
    <summary>Sorting and searching</summary>
    
</detals>

<details>
    <summary>Purchasing and Checkout</summary>
    
</detals>
 ---
# ***Deployment***

## To create a repository:
1. Go to the GitHub web page and login.
2. Click Repository on the right side of the profile.
3. Click New green button on right side.
4. Inside Create a new repository.
   + Choose your repository name.
   + Choose Public that anyone can view the repository or Private and choose who can see and commit in to the repository.
   + Choose the option in Initialize repository and add Readme, .gitignore and license if you not importing from existing repository.
5. Click create repository button on bottom.

## To deploy a website on GitHub Pages, follow these steps:
1. Go to the repository page
2. Click on settings icon in the top of the page
3. Find "GitHub Pages" section
4. Click on the "Source" dropdown menu
5. Select "master branch" option
6. A green success message should appear in the "GitHub Pages" section with the link to the live preview of the project.

## Heroku:

1.	Create an account:
   + In the browser type: Heroku.com.
   + Click Sing up button on the top of web page.
   + Filling the form and click create free account.
   + Check email box for confirmation email. If email is not received in 15min check spam folder or contact Heroku directly.
   + From the email click the link, then create new password and click the button below for Set password and log in.
2.	Create an application:
   + Click Create new app.
   + In the create new app window we need to give the unique name to the app and in the name we cannot use spaces, but instead, use hyphens. Choose a region United States or Europe and then click the Create app button.
3.	Install Heroku 
   + In the terminal by typing in console: npm install -g Heroku
4. Create requirements.txt and Procfile:
   + In the terminal by typing in console: pip3 freeze --local > requirements.txt
   + In the terminal by typing in console: echo web: python app.py > Procfile  - the Procfile must be assigned a capital P.
5. Go back to the Heroku web and from app klick deploy tab and select the Deployment method 'GitHub'.
6. Under Deployment method in Connecting to GitHub make sure your profile is display correctly and then your repository name and click 'Search'.
7. Your Repo should be display below so click 'Connect' to connect.
8. Go to the Settings tab and on Config Vars click Reveal Config Vars 
   + Enter variebles Key and Value contained in the env.py file:
      - IP
      - PORT
      - SECRET_KEY
      - MONGO_URI
      - MONGO_DBNAME
 9. Push requirements.txt and Procfile to the repository.
 10. Go back to Heroku Deploy section and croll down to the Automatic deploys and click 'Enable Automatic Deploys'.
 11. From Manual deploy section click 'Deploy Branch'.
   + Heroku will now receive the code from GitHub and start building the app using the required packages.
   + Once built the message apper 'Your app was successfully deployed' and you can click 'View' to launch your new app.

---
# ***Credits***
1. 404 and 500 templates and CSS style was made by Colorlib (https://colorlib.com) and updated for are own style.
2. Home background image downloaded from PxHere.

