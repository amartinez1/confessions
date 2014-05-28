# Create your views here.


from django.views.generic import TemplateView, FormView, DetailView, ListView
from django.shortcuts import render,render_to_response
from .models import Post
from django.core.urlresolvers import reverse_lazy , reverse
from django.template import RequestContext
from .forms import ConfessForm
# from uuslug import uuslug
# Import PILLOW to render and image of the text
from PIL import Image,ImageDraw
from django.conf import settings



class PostListView(ListView):
	model = Post
	template_name="post_list.html"
	paginate_by = 15

class ConfessForm(FormView):
	template_name="post_form.html"
	form_class=ConfessForm
	success_url=reverse_lazy('list')
	def form_valid(self,form):
		post=Post()
		post.title=form.cleaned_data['title']
		post.text=form.cleaned_data['text']
		# transform text to an image
		# img= Image.new('RGB',(500,500),(255,255,255))
		# d=ImageDraw.Draw(img)
		# d.text((20,20),post.text,fill=(255,0,0))
		# # save image to the uploads directory for media
		# img.save(settings.MEDIA_ROOT+"/uploads/"+post.text+".png","PNG")
		# # # save it to the model
		# post.image="/uploads/"+post.text+".png"
		post.save()

		return super(ConfessForm,self).form_valid(form)





		
class PostDetailView(DetailView):
 	template_name = 'post_list.html'
 	model= Post