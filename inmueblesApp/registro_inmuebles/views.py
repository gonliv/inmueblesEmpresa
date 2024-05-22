from django.contrib.auth import login, authenticate
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import messages
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import UserUpdateForm, ContactFormForm, RegistroForm
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.views import View
from django.views.generic import TemplateView
from .models import Usuario, ContactForm
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