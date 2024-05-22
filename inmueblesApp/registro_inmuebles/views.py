from django.contrib.auth import login, authenticate
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import UserUpdateForm, ContactFormForm, RegistroForm
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.views import View
from django.views.generic import TemplateView
from .models import ContactForm
from .services import crear_usuario
from .forms import RegistroForm
from .forms import ModificarUsuarioForm


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
        form = RegistroForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.email = form.cleaned_data['correo_electronico']
            user.set_password(form.cleaned_data['password1'])
            user.save()
            login(request, user)
            return redirect('welcome')
    else:
        form = RegistroForm()
    return render(request, 'registro.html', {'form': form})

def mi_vista(request):
    if request.method == 'POST':
        # Obtener datos del formulario
        email = request.POST['email']
        password = request.POST['password']
        nombres = request.POST['nombres']
        apellidos = request.POST['apellidos']
        rut = request.POST['rut']
        direccion = request.POST['direccion']
        telefono = request.POST['telefono']
        tipo_usuario = request.POST['tipo_usuario']

        # Crear el usuario utilizando la función de servicios
        nuevo_usuario = crear_usuario(email, password, nombres, apellidos, rut, direccion, telefono, tipo_usuario)

def vista_registro(request):
    if request.method == 'POST':
        form = RegistroForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password'])
            user.save()
            login(request, user)
            # Redirigir a alguna página de éxito
            return redirect('success')
    else:
        form = RegistroForm()
    return render(request, 'registro.html', {'form': form})

def perfil_usuario(request):
    usuario = request.user
    if request.method == 'POST':
        form = ModificarUsuarioForm(request.POST, instance=usuario)
        if form.is_valid():
            form.save()
            return render(request, 'profile.html', {'form': form, 'mensaje': 'Datos actualizados correctamente'})
    else:
        form = ModificarUsuarioForm(instance=usuario)
    return render(request, 'profile.html', {'form': form})