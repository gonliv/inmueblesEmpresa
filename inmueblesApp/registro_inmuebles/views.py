from django.contrib.auth import login, authenticate
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import messages
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.views import View
from django.views.generic import TemplateView
from .models import Usuario, ContactForm, Inmueble
from .services import crear_usuario
from .forms import RegistroForm, ModificarUsuarioForm, ContactFormForm, RegistroForm, InmuebleForm



# Create your views here.
def index(request):
    return render(request, 'index.html')

def about(request):
    return render(request, 'about.html', {})

def contact(request):
    if request.method == 'POST':
        form = ContactFormForm(request.POST)
        if form.is_valid():
            contact_form = ContactForm.objects.create(** form.cleaned_data)
            return HttpResponseRedirect('/success')
        else: 
            for field in form.errors:
                for error in form.errors[field]:
                    messages.error(request, f"{form.fields[field].label}: {error}")
    else:
        form = ContactFormForm()
    return render(request, 'contact.html', {'form': form})

def success(request):
    return render(request, 'success.html', {})

class LoginRequiredMixin(View):
    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)

class Welcome(LoginRequiredMixin, TemplateView):
    template_name = "welcome.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['user'] = self.request.user
        return context

@login_required
def welcome(request):
    return render(request, 'welcome.html', {'user': request.user})  

def registro(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            email = form.cleaned_data['username']  
            password = form.cleaned_data['password']
            user = Usuario.objects.create_user(email=email, password=password)
            login(request, user)
            return redirect('welcome')
    else:
        form = AuthenticationForm()
    return render(request, 'registro.html', {'form': form})

def mi_vista(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']
        nombres = request.POST['nombres']
        apellidos = request.POST['apellidos']
        rut = request.POST['rut']
        direccion = request.POST['direccion']
        telefono = request.POST['telefono']
        tipo_usuario = request.POST['tipo_usuario']

        nuevo_usuario = crear_usuario(email, password, nombres, apellidos, rut, direccion, telefono, tipo_usuario)

def vista_registro(request):
    if request.method == 'POST':
        form = RegistroForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password'])
            user.save()
            login(request, user)
            return redirect('success')
    else:
        form = RegistroForm()
    return render(request, 'registro.html', {'form': form})

@login_required
def perfil_usuario(request):
    usuario = request.user
    if request.method == 'POST':
        form = ModificarUsuarioForm(request.POST, instance=usuario)
        if form.is_valid():
            form.save()
            messages.success(request, '¡Tus datos se han actualizado correctamente!')
            return redirect('profile')
    else:
        form = ModificarUsuarioForm(instance=usuario)
    return render(request, 'profile.html', {'form': form})

@login_required
def modificar_usuario(request):
    usuario = request.user
    if request.method == 'POST':
        form = ModificarUsuarioForm(request.POST, instance=usuario)
        if form.is_valid():
            form.save()
            messages.success(request, 'Tus datos han sido actualizados correctamente.')
            return redirect('profile')
    else:
        form = ModificarUsuarioForm(instance=usuario)
    return render(request, 'modificar_usuario.html', {'form': form})

@login_required
def agregar_inmueble(request):
    if request.user.is_arrendador:
        if request.method == 'POST':
            form = InmuebleForm(request.POST)
            if form.is_valid():
                inmueble = form.save(commit=False)
                inmueble.propietario = request.user
                inmueble.save()
                return redirect('lista_inmuebles')  
        else:
            form = InmuebleForm()
        return render(request, 'agregar_inmueble.html', {'form': form})
    else:
        return redirect('profile.html')  
    
@login_required
def lista_inmuebles(request):
    inmuebles = Inmueble.objects.filter(propietario=request.user)
    return render(request, 'lista_inmuebles.html', {'inmuebles': inmuebles})

@login_required
def editar_inmueble(request, id):
    inmueble = get_object_or_404(Inmueble, id=id)
    if request.method == 'POST':
        form = InmuebleForm(request.POST, instance=inmueble)
        if form.is_valid():
            form.save()
            return redirect('lista_inmuebles')
    else:
        form = InmuebleForm(instance=inmueble)
    return render(request, 'editar_inmueble.html', {'form': form})

def eliminar_inmueble(request, id):
    inmueble = get_object_or_404(Inmueble, id=id)
    if request.method == 'POST':
        inmueble.delete()
        return redirect('lista_inmuebles')

    return render(request, 'eliminar_inmueble.html', {'inmueble': inmueble})