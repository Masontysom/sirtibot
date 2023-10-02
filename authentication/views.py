from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from sertibot import settings
from django.core.mail import send_mail
from django.contrib.sites.shortcuts import get_current_site
from django.template.loader import render_to_string
from django.utils.http import urlsafe_base64_decode, urlsafe_base64_encode 
from django.utils.encoding import *
from . tokens import generate_token
from django.core.mail import EmailMessage, send_mail
from django.utils.encoding import force_str


# Create your views here.
def home(request):
    return render(request, "authentication/index.html")

def signup(request):

    if request.method == 'POST':
        #username = request.POST.get('username')
        username = request.POST['username']
        fname = request.POST['fname']
        lname = request.POST['lname']
        email = request.POST['email']
        pass1 = request.POST['pass1']
        pass2 = request.POST['pass2']

        if User.objects.filter(username=username):
            messages.error(request,"Username already exists, Please enter another username")
            return redirect('home')

        if User.objects.filter(email=email):
            messages.error(request,"Email already exists, Please enter another email")
            return redirect('home')

        if len(username)>10:
            messages.error(request,"Username too long, must be at least 10 characters")
            return redirect('home')

        if pass1 != pass2:
            messages.error(request,"Password mismatch")
            return redirect('home')

        if not username.isalnum():
            messages.error(request,"Username must be alpha-numeric!!")
            return redirect('home')



        myuser = User.objects.create_user(username, email, pass1)
        myuser.first_name = fname
        myuser.last_name = lname
        myuser.is_active = False
        myuser.save()

        messages.success(request,"Your account has been created. We have sent you Conformation email, Please conform your email to activate your account")


        #email
        subject = "Welcome to Sirtibot!!"
        message = "Hello "+ myuser.first_name + "\n" + "Welcome to sertibot!! \n Thank you for visiting our website \n we have sent you an email a conformation email just after this mail.\n Click on the email to verify your account \n \n Thanking You "       
        from_email = settings.EMAIL_HOST_USER
        to_list = [myuser.email]
        send_mail(subject, message, from_email, to_list, fail_silently=True)

        #Email Address Conformation

        current_site = get_current_site(request)
        email_subject = "Confirm your email address @ Sirtibot "
        message2 = render_to_string('email_confirmation.html', {
            'name': myuser.first_name,
            'domain': current_site.domain,
            'uid':urlsafe_base64_encode(force_bytes(myuser.pk)),
            'token': generate_token.make_token(myuser)
        
        })

        email = EmailMessage(
            email_subject, 
            message2,
            settings.EMAIL_HOST_USER,
            [myuser.email],
        )
        email.fail_silently = True
        email.send()

        return redirect('signin')

    return render(request, "authentication/signup.html")

from django.contrib.auth.decorators import login_required

@login_required
def dashboard(request):
    user_id = request.session.get('user_id')
    username = request.session.get('username')

    if user_id and username:
        # Access the user-related data
        user_data = {
            'username': username,
            'firstname': request.user.first_name,
            'email': request.user.email,
            # Other fields from UserProfile
        }

        context = {
            'user_data': user_data,
        } # Replace YourModel with your actual model
        return render(request, "dashboard/index.html", context,)

    # Handle the case where session data is missing
    messages.error(request, "Session data missing. Please sign in again.")
    return redirect('home')



def signin(request):
    if request.method == 'POST':
        username = request.POST['username']
        pass1 = request.POST['pass1']

        user = authenticate(username=username, password=pass1)

        if user is not None:
            login(request, user)
            fname = user.first_name

            # Create or update session data in the database
            session_key = request.session.session_key
            if not session_key:
                request.session.save()

            # Create a session and store user-related data
            request.session['user_id'] = user.id
            request.session['username'] = user.username

            messages.success(request, "Sign in successful.")
            return render(request, "dashboard/index.html",{'fname': fname})
            
            


        else:
            messages.error(request, "Invalid username or pass")
            return redirect('home')

    return render(request, "authentication/signin.html")


@login_required
def signout(request):
    # Clear session data and log the user out
    request.session.clear()
    logout(request)
    messages.success(request, "Log out successfully")
    return redirect('home')


def activate(request, uidb64, token):
    try:
        uid = force_str(urlsafe_base64_decode(uidb64))
        myuser = User.objects.get(pk=uid)
    except( TypeError, ValueError, OverflowError, User.DoesNotExist):
        myuser = None

    if myuser is not None and generate_token.check_token(myuser, token):
        myuser.is_active = True
        myuser.save()
        login(request, myuser)
        return redirect('home')
    else:
        return render(request, 'activation_failed.html')

def aboutus(request):
    return render(request, 'aboutus.html')

def contactus(request):
    return render(request, 'contactus.html')

def dashboard(request):
    return render(request, "dashboard/index.html")

