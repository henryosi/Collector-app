from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
import uuid
import boto3
from.models import Auto, Show, Photo
from.forms import ServicingForm

S3_BASE_URL = 'https://s3-us-west-1.amazonaws.com/'
BUCKET = 'autocollector'


def signup(request):
  error_message = ''
  if request.method == 'POST':
    # This is how to create a 'user' form object
    # that includes the data from the browser
    form = UserCreationForm(request.POST)
    if form.is_valid():
      # This will add the user to the database
      user = form.save()
      # This is how we log a user in via code
      login(request, user)
      return redirect('index')
    else:
      error_message = 'Invalid credentials - try again'
  # A bad POST or a GET request, so render signup.html with an empty form
  form = UserCreationForm()
  context = {'form': form, 'error_message': error_message}
  return render(request, 'registration/signup.html', context)

class AutoCreate (LoginRequiredMixin, CreateView):
    model = Auto
    fields = ['name', 'model', 'description', 'age']

    def form_valid(self, form):
      # Assign the logged in user
      form.instance.user = self.request.user
      # Let the CreateView do its job as usual
      return super().form_valid(form)

class AutoUpdate (LoginRequiredMixin, UpdateView):
    model = Auto
    fields = ['model', 'description', 'age']

class AutoDelete (LoginRequiredMixin, DeleteView):
    model = Auto
    success_url = '/autos/'

# Create your views here.
def home (request):
    return render (request, 'home.html')

def about (request):
    return render(request, 'about.html')

@login_required
def autos_index(request):
    autos = Auto.objects.filter(user=request.user)
    return render (request, 'autos/index.html', { 'autos': autos })

@login_required
def autos_detail(request, auto_id):
    auto = Auto.objects.get(id=auto_id)
    shows_auto_doesnt_have = Show.objects.exclude(id__in = auto.shows.all().values_list('id'))
    servicing_form = ServicingForm()
    return render (request, 'autos/detail.html', { 
      'auto': auto, 
      'servicing_form':servicing_form,
      'shows': shows_auto_doesnt_have
      })

@login_required
def add_servicing(request, auto_id):
      # create the ModelForm using the data in request.POST
  form = ServicingForm(request.POST)
  # validate the form
  if form.is_valid():
    # don't save the form to the db until it
    # has the cat_id assigned
    new_servicing = form.save(commit=False)
    new_servicing.auto_id = auto_id
    new_servicing.save()
  return redirect('detail', auto_id=auto_id)

@login_required
def add_photo(request, auto_id):
	# photo-file was the "name" attribute on the <input type="file">
  photo_file = request.FILES.get('photo-file', None)
  if photo_file:
    s3 = boto3.client('s3')
    # need a unique "key" for S3 / needs image file extension too
    key = uuid.uuid4().hex[:6] + photo_file.name[photo_file.name.rfind('.'):]
    # just in case something goes wrong
    try:
      s3.upload_fileobj(photo_file, BUCKET, key)
      # build the full url string
      url = f"{S3_BASE_URL}{BUCKET}/{key}"
      # we can assign to cat_id or cat (if you have a cat object)
      photo = Photo(url=url, auto_id=auto_id)
      photo.save()
    except:
      print('An error occurred uploading file to S3')
  return redirect('detail', auto_id=auto_id)

@login_required
def assoc_show(request, auto_id, show_id):
  Auto.objects.get(id=auto_id).shows.add(show_id)
  return redirect('detail', auto_id=auto_id)

@login_required
def unassoc_show(request, auto_id, show_id):
  Auto.objects.get(id=auto_id).shows.remove(show_id)
  return redirect('detail', auto_id=auto_id)

class ShowList(LoginRequiredMixin, ListView):
  model = Show

class ShowDetail(LoginRequiredMixin, DetailView):
  model = Show

class ShowCreate(LoginRequiredMixin, CreateView):
  model = Show
  fields = '__all__'

class ShowUpdate(LoginRequiredMixin, UpdateView):
  model = Show
  fields = ['name', 'date']

class ShowDelete(LoginRequiredMixin, DeleteView):
  model = Show
  success_url = '/shows/'