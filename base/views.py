from django.views.generic import DetailView, ListView, FormView
from django.views.generic.detail import SingleObjectMixin
from django.views.generic.base import TemplateView
from django.shortcuts import get_object_or_404
from django.core.urlresolvers import reverse
from django.shortcuts import render
from django.db.models import F

from django_ajax.decorators import ajax

from .models import *
from .forms import *


class NewIdea(FormView):
    template_name = "base/index.html"
    form_class = IdeaForm

    def post(self, request, *args, **kwargs):
        self.success_url = request.path
        return super().post(request, *args, **kwargs)

    def form_valid(self,form):
        form.save(commit=True)
        return super().form_valid(form)
    

class IdeasListView(ListView):
    
    def post(self, request, *args, **kwargs):
        view = NewIdea.as_view()
        return view(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["form"] = IdeaForm(auto_id="idea_%s")
        return context
    

class PopularIdeasView(IdeasListView):
    template_name = "base/index.html"
    model = Idea
    queryset = Idea.objects.order_by("-displayed")


class NewIdeasView(IdeasListView):
    template_name = "base/index.html"
    model = Idea
    queryset = Idea.objects.order_by("-created")


class TopIdeasView(IdeasListView):
    template_name = "base/index.html"
    model = Idea
    queryset = Idea.objects.order_by("-rating__rating")


class DetailDisplay(DetailView):
    template_name = "base/detail_idea.html"
    model = Idea

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        
        self.object.displayed = F("displayed") + 1
        self.object.save()

        context["form"] = CommentForm()
        return context


class DetailComment(SingleObjectMixin, FormView):
    template_name = "base/detail_idea.html"
    form_class = CommentForm
    model = Idea

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        return super().post(request, *args, **kwargs)

    def form_valid(self, form):
        comment = form.save(commit=False)
        comment_count = Comment.objects.filter(idea=self.object).count()
        comment.idea = self.object
        comment.position = comment_count
        comment.save()
        
        reply_id = self.request.POST.get("reply_id")
        if reply_id is not None and reply_id != '':
            mentioned_comment = get_object_or_404(Comment, id=reply_id)
            Reply.objects.create(comment=mentioned_comment, reply=comment)
        
        return super().form_valid(form)

    def get_success_url(self):
        return reverse("idea-detail", kwargs={"pk": self.object.pk})
    
    
class DetailIdeaView(DetailView):

    def get(self, request, *args, **kwargs):
        view = DetailDisplay.as_view()
        return view(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        view = DetailComment.as_view()
        return view(request, *args, **kwargs)


class InfoView(TemplateView):
    template_name = "base/info.html"


@ajax
def load_new_comments(request):
    idea_id = request.POST.get("idea")
    count = request.POST.get("count")
    new_comments = Comment.objects.filter(idea__id=idea_id, position__gte=count)
    replies = { comment.id: [ reply.reply.id for reply in comment.replies.all() ]  for comment in new_comments }
    new_comments = new_comments.values("id","content","author")
    for comment in new_comments:
        comment["content"] = comment["content"].replace("\r\n","<br>")
    
    return {
        "new_comments": new_comments,
        "replies": replies,
        "count": new_comments.count(),
    }
