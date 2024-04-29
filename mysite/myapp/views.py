from django.shortcuts import render
from .models import Comment, BlogUser
from django.db.models import Q


def filter_date_comm_blog(request):
    user = BlogUser.objects.all()[0]
    blog = user.blogs.all()[0]
    comment = blog.comments.all()[:2]

    return render(request, 'filter_date_comm_blog.html', {'comment': comment, 'blog': blog, 'user': user})


def comment_text(request):
    inner_text = Comment.objects.all().values_list('comment', flat=True)[:5]

    return render(request, 'comments_text.html', {'inner_text': inner_text})


def start_middle_end(request):
    start = Comment.objects.filter(comment__startswith='Start')
    middle = Comment.objects.filter(comment__contains='Middle')
    finish = Comment.objects.filter(comment__endswith='Finish')

    return render(request, 'start_middle_end.html', {'start': start, 'middle': middle, 'finish': finish})


def comment_with_date(request):
    inner_text = Comment.objects.all()

    return render(request, 'comments_with_date.html', {'inner_text': inner_text})


def comment_update_sme(request):
    inner_text = Comment.objects.filter(Q(text__contains='Start') | Q(text__contains='Middle') | Q(text__contains='Finish'))

    for i in inner_text:
        print(i.text)

    comm_in_general = Comment.objects.all()

    return render(request, 'comments_update_sme.html', {'inner_text': inner_text, 'comm_in_general': comm_in_general})


def comment_without_k_with_c(request):
    inner_text = Comment.objects.filter(comment__contains='k').exclude(comment__contains='c').delete()

    return render(request, 'comment_without_k_with_c.html', {'inner_text': inner_text})
