from django.shortcuts import redirect, render
from django.http import HttpResponse
from django.urls import reverse_lazy
from .models import *
from .forms import *

from django.views.generic import ListView
from django.views.generic import CreateView
from django.views.generic import DetailView
from django.views.generic import UpdateView
from django.views.generic import DeleteView

from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
# Create your views here.
def index(request):
    return render(request, "aplicacion/base.html")

@login_required
def wines(request):
    ctx = {"wines": Vino.objects.all()}
    return render(request, "aplicacion/wines.html",ctx)

@login_required
def wineForm(request):
    if request.method == "POST":
        wine = Vino(categoria=request.POST['categoria'],uva=request.POST['uva'])
        wine.save()
        return HttpResponse("The new wine has been successfully entered!")
    
    return render(request, "aplicacion/wineForm.html")

@login_required
def wineForm2(request):
    if request.method == "POST":
        miForm = WineForm(request.POST)
        if miForm.is_valid():
            wine_categoria = miForm.cleaned_data.get('categoria')
            wine_uva = miForm.cleaned_data.get('uva')
            wine = Vino(categoria=wine_categoria, uva=wine_uva)
            wine.save()
            return render(request, "aplicacion/base.html")
    else:
            miForm = WineForm()

    return render(request, "aplicacion/wineForm2.html", {"form":miForm})

@login_required
def sparkling(request):
    ctx = {"sparkling": Espumante.objects.all()}
    return render(request, "aplicacion/sparkling.html", ctx)

@login_required
def whisky(request):
    ctx = {"whisky": Whisky.objects.all()}
    return render(request, "aplicacion/whisky.html", ctx)

@login_required
def spirits(request):
    ctx = {"spirits": Spirit.objects.all()}
    return render(request, "aplicacion/spirits.html", ctx)

@login_required
def beers(request):
    ctx = {"beers": Cerveza.objects.all()}
    return render(request, "aplicacion/beers.html", ctx)

@login_required
def ourcreator(request):
    ctx = {"ourcreator": OurCreator.objects.all()}
    return render(request, "aplicacion/ourcreator.html", ctx)

@login_required
def searchCategoria(request):
    return render(request, "aplicacion/searchCategoria.html")

@login_required
def search2(request):
    if request.GET['categoria']:
        categoria = request.GET['categoria']
        wines =Vino.objects.filter(categoria__icontains=categoria)
        return render(request, "aplicacion/resultsCategoria.html", {"categoria": categoria, "wines":wines})
    return HttpResponse("No data was entered to search!")


#_____ Class Based View

class WineList(LoginRequiredMixin,ListView):
    model = Vino

class WineCreate(LoginRequiredMixin,CreateView):
    model = Vino
    fields =['categoria', 'uva']
    success_url = reverse_lazy('wines')

class WineDetail(LoginRequiredMixin,DetailView):
    model = Vino 

class WineUpdate(LoginRequiredMixin,UpdateView):
    model = Vino
    fields =['categoria', 'uva']
    success_url = reverse_lazy('wines')

class WineDelete(LoginRequiredMixin,DeleteView):
    model = Vino
    success_url = reverse_lazy('wines')

class BeerList(LoginRequiredMixin,ListView):
    model = Cerveza

class BeerCreate(LoginRequiredMixin,CreateView):
    model = Cerveza
    fields =['estilo', 'color']
    success_url = reverse_lazy('beers')

class BeerDetail(LoginRequiredMixin,DetailView):
    model = Cerveza

class BeerUpdate(LoginRequiredMixin,UpdateView):
    model = Cerveza
    fields =['estilo', 'color']
    success_url = reverse_lazy('beers')

class BeerDelete(LoginRequiredMixin,DeleteView):
    model = Cerveza
    success_url = reverse_lazy('beers')

class SpiritList(LoginRequiredMixin,ListView):
    model = Spirit

class SpiritCreate(LoginRequiredMixin,CreateView):
    model = Spirit
    fields =['categoria', 'producto', 'marca']
    success_url = reverse_lazy('spirits')

class SpiritDetail(LoginRequiredMixin,DetailView):
    model = Spirit

class SpiritUpdate(LoginRequiredMixin,UpdateView):
    model = Spirit
    fields =['categoria', 'producto', 'marca']
    success_url = reverse_lazy('spirits')

class SpiritDelete(LoginRequiredMixin,DeleteView):
    model = Spirit
    success_url = reverse_lazy('spirits')

class SparklingList(LoginRequiredMixin,ListView):
    model = Espumante

class SparklingCreate(LoginRequiredMixin,CreateView):
    model = Espumante
    fields =['categoria', 'varietal', 'marca']
    success_url = reverse_lazy('sparkling')

class SparklingDetail(LoginRequiredMixin,DetailView):
    model = Espumante

class SparklingUpdate(LoginRequiredMixin,UpdateView):
    model = Espumante
    fields =['categoria', 'varietal', 'marca']
    success_url = reverse_lazy('sparkling')

class SparklingDelete(LoginRequiredMixin,DeleteView):
    model = Espumante
    success_url = reverse_lazy('sparkling')

class WhiskyList(LoginRequiredMixin,ListView):
    model = Whisky

class WhiskyCreate(LoginRequiredMixin,CreateView):
    model = Whisky
    fields =['categoria', 'marca']
    success_url = reverse_lazy('whisky')

class WhiskyDetail(LoginRequiredMixin,DetailView):
    model = Whisky

class WhiskyUpdate(LoginRequiredMixin,UpdateView):
    model = Whisky
    fields =['categoria', 'marca']
    success_url = reverse_lazy('whisky')

class WhiskyDelete(LoginRequiredMixin,DeleteView):
    model = Whisky
    success_url = reverse_lazy('whisky')

#_____ Login, Logout, Registracion
#

def login_request(request):
    if request.method == "POST":
        miForm = AuthenticationForm(request,data=request.POST)
        if miForm.is_valid():
            usuario = miForm.cleaned_data.get('username')
            clave = miForm.cleaned_data.get('password')
            user = authenticate(username=usuario, password=clave)
            if user is not None:
                login(request, user)

                try:
                    avatar = Avatar.objects.get(user=request.user.id).imagen.url
                except:
                    avatar = '/media/avatares/default.png'
                finally:
                    request.session['avatar'] = avatar
                    
                return render(request, "aplicacion/base.html", {"mensaje": f"Welcome {usuario}"})
            else:
                return render(request, "aplicacion/login.html", {"form":miForm, "mensaje": "Data invalid"})
        else:
            return render(request, "aplicacion/login.html", {"form":miForm, "mensaje": "Data invalid"})
        
    miForm = AuthenticationForm()

    return render(request, "aplicacion/login.html", {"form":miForm})

def register(request):
    if request.method == 'POST':
        form = RegisterUsersForm(request.POST)
        if form.is_valid():
            usuario = form.cleaned_data.get('username')
            form.save()
            return render(request, "aplicacion/base.html", {"mensaje":"User successfully created"})
    else:
        form = RegisterUsersForm()

    return render(request, "aplicacion/registro.html", {"form": form})

#______ Registro de usuarios
#

@login_required
def editarPerfil(request):
    usuario = request.user
    if request.method == "POST":
        form = UserEditForm(request.POST)
        if form.is_valid():
            usuario.email = form.cleaned_data.get('email')
            usuario.password1 = form.cleaned_data.get('password1')
            usuario.password2 = form.cleaned_data.get('password2')
            usuario.first_name = form.cleaned_data.get('first_name')
            usuario.last_name = form.cleaned_data.get('last_name')
            usuario.save()
            return render(request, "aplicacion/base.html", {'mensaje': f"Usuario {usuario.username} actualizado correctamente"})
        else:
            return render(request, "aplicacion/editarPerfil.html", {'form': form})
    else:
        form = UserEditForm(instance=usuario)
    return render(request, "aplicacion/editarPerfil.html", {'form': form, 'usuario':usuario.username})


@login_required
def agregarAvatar(request):
    if request.method == "POST":
        form = AvatarFormulario(request.POST, request.FILES)
        if form.is_valid():
            u = User.objects.get(username=request.user)
            avatarViejo = Avatar.objects.filter(user=u)
            if len(avatarViejo) > 0:
                avatarViejo[0].delete()

            avatar = Avatar(user=u, imagen=form.cleaned_data['imagen'])
            avatar.save()

            imagen = Avatar.objects.get(user=request.user.id).imagen.url
            request.session['avatar'] = imagen

            return render(request, "aplicacion/base.html")
    else:
        form = AvatarFormulario()
    return render(request, "aplicacion/agregarAvatar.html", {'form': form})