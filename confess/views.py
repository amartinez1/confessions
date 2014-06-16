# Create your views here.


from django.views.generic import TemplateView, FormView, DetailView, ListView
from django.shortcuts import render,render_to_response
from .models import Post
from django.core.urlresolvers import reverse_lazy
from django.template import RequestContext
from .forms import ConfessForm
# from uuslug import uuslug
# Import PILLOW to render and image of the text
# from PIL import Image,ImageDraw
from endless_pagination.decorators import page_template


class PostListView(ListView):
	model = Post
	template_name="post_list.html"
	paginate_by = 15

@page_template('post_page.html')  # just add this decorator
def postList(
               request, template='confess.html', extra_context=None):
	
    context = {}
    if extra_context is not None:
        context.update(extra_context)

    obj = Post.objects.all()
    context['objects']=obj
    return render_to_response(
        template, context, context_instance=RequestContext(request))

@page_template('post_page.html')  # just add this decorator
def popularList(
               request, template='confess.html', extra_context=None):
	
    context = {}
    if extra_context is not None:
        context.update(extra_context)

    obj = Post.objects.filter(category='PO')
    context['objects']=obj
    return render_to_response(
        template, context, context_instance=RequestContext(request))
@page_template('post_page.html')  # just add this decorator
def newList(
               request, template='confess.html', extra_context=None):
	
    context = {}
    if extra_context is not None:
        context.update(extra_context)

    obj = Post.objects.filter(category='NE')
    context['objects']=obj
    return render_to_response(
        template, context, context_instance=RequestContext(request))




class ConfessForm(FormView):
	template_name="post_form.html"
	form_class=ConfessForm
	success_url=reverse_lazy('list')
	def form_valid(self,form):
		category ='NE'
		 # every post will be set to the new category, 
		# the popular will be handpicked by admin
		post=Post()
		post.title=form.cleaned_data['title']
		post.text=form.cleaned_data['text']
		post.total_likes = 1
		post.category = category
		# This piece of code can turn any text to image
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
 	template_name = 'post_detail.html'
 	model= Post