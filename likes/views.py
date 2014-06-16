# Create your views here.
from django.http import HttpResponse
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.db.models import  Sum
from hashlib import md5
from confess.models import Post
from .models import Like
from django.views.generic import TemplateView
from django.core import serializers
import json


def retrieve_token(request):
	value=''.join((request.META['REMOTE_ADDR'], request.META.get('HTTP_USER_AGENT', '')))  	
  	token=md5(value).hexdigest()
  	return token
class like(TemplateView):

	def get(self,request,*args,**kwargs):
		vote = +1
		count = 0
		label = 'Unlike'
		post_id = request.GET['confession_id']
		# print "confess_id = "+confess_id
		user_token = retrieve_token(request)
		posts=Post.objects.get(id=int(post_id))
		
		# get the like post, todavia hay que tirar un 404 expection error
		# check if the like exist given a post object and a user token
		if Like.objects.filter(post=posts, user_token=user_token).exists():
			user_like = Like.objects.get(post=posts, user_token=user_token)

			if int(user_like.post.id) ==int(post_id) and user_like.user_token==user_token:
				print "entered if..."
				if user_like.liked==False:
					user_like.vote=vote
					user_like.liked=True
					user_like.label = label
					user_like.save()
					print "user like saved!!!"
					count =like_count(request,posts)
					data = {
							'count':count,
							'label':label}
					
					result = json.dumps(data)
					
					print result
					
					return HttpResponse(result,content_type='application/json')
					
				else:

					
					print "sent to unlike method"
					label  = 'Like'
					user_like.label = label
					user_like.save()
					count=unlike(request,posts,user_token)
					data = {
							'count':count,
							'label':label}
					result = json.dumps(data)
					return HttpResponse(result, content_type='aplication/json')	

		else:
			print "create it!!"
			post=Like(post=Post.objects.get(id=post_id),user_token=user_token,vote=vote, liked=True)
			post.label = label
			post.save()
			print post.post, post.user_token,post.vote, post.id
			post_id = post.id

			print "saved!!!"
			count =like_count(request,post)
			data = {'count':count,
					'label':label}
			result = json.dumps(data)
			return HttpResponse(result,content_type='aplication/json')



def unlike(request,posts,user_token):
	# Arreglarlo para que reciva ya el objeto al que se le hara el downvote
	down_vote = 0
	# user_token = retrieve_token(request)
	post_obj = Post.objects.get(id=posts.id)
	post=Like.objects.get(post=post_obj,user_token=user_token)
	post.vote =down_vote
	post_obj.total_likes = post_obj.total_likes+down_vote
	total_likes = like_count(request,post_obj)
	post_obj.save()
	post.liked=False
	post.save()
	print "downvoted!!!"
	count = like_count(request,post_obj)
	

	return count
	

def like_count(request,post): #,post

	like = Like.objects.filter(post=post)
	likes=0
	#prueba--contando likes likes =Like.objects.filter(post=13).aggregate(Sum('vote'))['vote__sum']
	if like.exists():
		likes =like.aggregate(Sum('vote'))['vote__sum'] or 0
		# right way ------>		post.total_likes=likes
		# sum and add it to the current likes (not so good)

	
		
		post.total_likes=likes
		post.save()
		# likes = post.total_likes

		return likes 
	else:
		post.total_likes=likes
		post.save()
		return likes






class fill_modal(TemplateView):
	def get(self,request,*args,**kwargs):
		
		post_id = request.GET['id']
		post = Post.objects.get(id=post_id)
		data = serializers.serialize('json',[post,],fields=('pk','title','text','posted','total_likes'))
		struct= json.loads(data)
		data = json.dumps(struct[0])
		# print "serialized!!"
		# print data
		return HttpResponse(data,content_type='application/json')
	
class user_like(TemplateView):
	def get(self,request,*args,**kwargs):

		token = retrieve_token(request)
		
		post_id = request.GET['id']

		like_obj = Like.objects.get(post=post_id,user_token=token)
		
		data = {'label':like_obj.label}
		result = json.dumps(data)
		return HttpResponse(result,content_type='aplication/json')
