[![Build Status](https://travis-ci.org/benhasselgren/full-stack-milestone.svg?branch=master)](https://travis-ci.org/benhasselgren/full-stack-milestone)
<h6>Ben Hasselgren</h6>
<h1> Full Stack Framework Milestone  </h1>

<h3>Purpose</h3>
<p>
    The purpose of this project is to create a website for a startup called Unicorn Attractor. Unicorn Attractor is a company that sells software.
    The point of this website is to allow users become apart of the companys community. It allows users to register and then share bugs or features
    they have found or want in the unicorn attractor software. These bugs are shared with all the other users. The bugs and features can be upvoted,
    viewed in detail and commented on. This overall allows the companys users to create an onine community which allows for bugs to be fixed easily and also
    allow the company to see what the users want and allow them to improve their software creating an effective relationship between the business and customer.
</p>

<h3>Functionality/Technologies</h3>
<p>
    This website has lots of functionality. One functioniality is that it's resposnive. It uses bootsrap which is a web development library. 
    Using the provided classes and javascript code, the website has a very resposive interface and adapts to screen sizes.
    The website allows the user to create an account which they can then log into and add, view, upvote and comment on features and bugs. This website was built using Django Framework
    so it consisits of lots of apps. The user app has authentication built in, so users have a secure account. They can also update their password if they have forgotten it. Another functionality is the ability to upvote bugs and features.
    The user can upvote a bug for free but if they want to upvote a feature they have to pay a fee of £10. If they do decide to pay the chosen feature is added to a cart. This cart can be accesed in the nav and
    using django sessions, it can be modified and viewed by the user. The user can then continue to checkout form the cart if they do decide to pay for the upvote.
    The checkout is a simple design. It uses stripes api. Stripe allows easy payments online. It does all the security and authentication in the backend and returns errors and succesfull payment messages. 
    This allows the user to clearly see if their payment is going through properly. Another piece of functionality is the features and bugs themselves. Using djangos built in models and forms,
    users can easily make bugs and features. My tables use relationships to allows users to create their own unique bugs and features and allows for comments and upvotes. My homepages when a user is logged out aso have
    functionality. My community page has graphs that show stats about fetaures, bugs and users. Using chart.js, attractive graphs can be created. The data used in the graphs come from
    an ajax request storing data. The data is formed by using Djangos query language that queries my database and returns stats on features/bugs(number of upvotes, etc.).
</p>

<h3>Testing/Deployment</h3>
<p>
    This website was tested in different ways. MySqlWorkbench(GUI) was installed to view the database in a more readable way. This allowed me to check
    if the functionality in my code was working as I could see if the correct data was being added, removed in the database. I also used chrome developer tools
    to test if there was anything wrong with my html, css or javascript files. I also made use of djangos error page that appeared when my code had errors in it. This helped me spot things wrong in my code quickly.
    I also used djangos built in test case package. This allowed me to create multiple tests for my views, urls, forms etc. Once all my tests were created I could run them in the terminal
    and see if they were returning the correct output. It was important to try and test as much as possible in this project so splitting the tests into different files made this
    easier. I also connect my github repo to Travis CI. This allowed me to automotically test my program behind the scenes and see if my code was all correct. The success build tag above
    shows if it is passing travic ci tests.
</p>
<p>
    This website was deployed to heroku. I created a heroku app and then pushed my code to it. To ensure this worked I had to do a couple things. I created a procfile and a 
    requirements.txt file. This allowed heroku to install the correct packages and run my project accordingly. I also had to install the whitenoise package so heroku could find
    my static files. To also get my models working I had to migrate my database from sqlite to herokus postgres database.
</p>