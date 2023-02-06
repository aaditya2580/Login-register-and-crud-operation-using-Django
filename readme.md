Requirement to Run this Project:
1.python
2.Django
3.virtualenv


install Setuptools
To install Python packages on your computer, Setuptools is needed. Download the latest version of Setuptools for your Python version and follow the installation instructions given there.

Install PIP
PIP is a package manager for Python that uses the Python Package Index to install Python packages. PIP will later be used to install Django from PyPI. If you’ve installed Python 3.4, pip is included so you may skip this section.

Open a command prompt and execute easy_install pip. This will install pip on your system. This command will work if you have successfully installed Setuptools.

Alternatively, go to http://www.pip-installer.org/en/latest/installing.html for installing/upgrading instructions.

Install Django
Django can be installed easily using pip.

In the command prompt, execute the following command: pip install django. This will download and install Django.

After the installation has completed, you can verify your Django installation by executing django-admin --version in the command prompt.


Step for setup
 1.  cd File

 2. pip3 install -r requirements.txt

 3. python3 manage.py migrate

 4. python3 manage.py makemigrations

 5. python3 manage.py migrate

 6. python3 manage.py runserver

 7. Login to http://127.0.0.1:8000
