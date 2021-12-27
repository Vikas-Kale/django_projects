from django.shortcuts import redirect, render

# Create your views here.

def Usersignup(request):
    if request.user.is_authenticated:
        return redirect('/')
    else:
        if request.method=="POST":   
            username = request.POST['username']
            email = request.POST['email']
            first_name=request.POST['first_name']
            last_name=request.POST['last_name']
            password1 = request.POST['password1']
            password2 = request.POST['password2']
 
            if password1 != password2:
                messages.info(request, "Passwords do not match.")
                return redirect('/signup')
 
            user = User.objects.create_user(username, email, password1)
            user.first_name = first_name
            user.last_name = last_name
            user.save()
            return render(request, 'user_login.html')     
    return render(request, "signup.html")

def User_login(request):
    if request.user.is_authenticated:
        return redirect('/')
    else:
        if request.method=="POST":
            user_username = request.POST['user_username']
            user_password = request.POST['user_password']
 
            user = authenticate(username=user_username, password=user_password)
 
            if user is not None:
                login(request, user)
                messages.success(request, "Successfully Logged In")
                return redirect("/for_users")
            else:
                messages.error(request, "Please provide a valid username and password")
    return render(request, "user_login.html")

@login_required(login_url = '/user_login')
def Users(request):
    books = Book.objects.all()
    total_books = books.count()
 
    return render (request, "for_user.html", {'books':books, 'total_books':total_books})

total_books = books.count()
if (localStorage.getItem('cart') == null) {
   var cart = {};
 } else {
   cart = JSON.parse(localStorage.getItem('cart'));
   updateCart(cart);
 }