<h1>Url Shortener</h1>
<p>This was one of my favorite projects to build, I really enjoyed the challenges [mapping unique ids to long URLs] and seeing how much complexity it can become.</p>

<h1>Installation guide</h1>
<h3> TO start this project, it need python and pip installed on the system </h3>
<h2>Prerequisites</h2>
<h3> Set the virtual environment by " python3 -m venv env"</h3>
<h4>Activate the environment in window "env/Scripts/activate "</h4>
<h4>Activate the environment in MacOs/Linux "source env/bin/activate "</h4>
<h3> After activing env install django by " pip install django"</h3>
<h4> check the version of django by "django-admin --version" </h4>


<h3>set the database by "python manage.py makemigrations "</h3>
<h3> apply the database by " python manage.py migrate "</h3>
<h3> create superuser by " python manage.py createsuperuser" </h3>

<h1> Application guidance for run</h1>
<p> after successfully setup the application, again do "python manage.py runserver" in command for run the server</p>
<li> user need to register for shortener url by clicking register </li>
<li>do register and login </li>
<li>now user can enter the urs_shortener page for shortener url</li>
<li>now user can short url generate qr_code, customize url, set available expire time and delete the the url</li>
<li> user can see their activity in the urs_shortener page or list of UrL from nav which only appear after user is login</li>
<li> in list of url page user can search the short url from search bar</li>
<li> user can see basic analytics such as click count, url created and customize time and url clicked time</li>
<h1>some images of the project </h1>
<p> home page without user login</p>
<img src="images/Screenshot (271).png" alt="description of image">
<p> home page with user login</p>
<img src="images/Screenshot (272).png" alt="description of image">
<p> Url Shortener page with form and activity of user</p>
<img src="images/Screenshot (273).png" alt="description of image">
<p> Urllist page with search url and activity of user</p>
<img src="images/Screenshot (274).png" alt="description of image">
<p> edit page</p>
<img src="images/Screenshot (275).png" alt="description of image">
<p> qr_code page</p>
<img src="images/Screenshot (276).png" alt="description of image">
 
 <p> expired url</p>
<img src="images/Screenshot (277).png" alt="description of image">
 







