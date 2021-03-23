from django import template
from blog_app.models import Post, Comment

register = template.Library()


@register.inclusion_tag('blog_app/latest_posts.html')
def latest_posts():
    data = {
        'latest_posts': Post.objects.all()[:5],
    }
    return data


@register.inclusion_tag('blog_app/latest_comments.html')
def latest_comments():
    data = {
        'latest_comments': Comment.objects.filter(active=True)[:5],
    }
    return data
