from models import Post

from django.shortcuts import render_to_response

def index(request):
	POSTS_PER_PAGE = 1
	page = int(request.GET.get('page', 0))
	posts = Post.objects.all().order_by('-date_added')[page*POSTS_PER_PAGE:(page+1)*(POSTS_PER_PAGE)]
	total_pages = max(0, (Post.objects.all().count() - 1)) / POSTS_PER_PAGE + 1

	return render_to_response('blog/index.html', {
			'posts':posts,
			'total_pages':total_pages,
			'current_page':page
		})

