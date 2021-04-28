from django.shortcuts import render
from .models import Group
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, DetailView, UpdateView, DeleteView
import profiles.models
import posts.models, posts.forms
from django.urls import reverse_lazy
from django.contrib import messages

# Create your views here.

class GroupListView(ListView, LoginRequiredMixin):
    model = Group
    template_name = 'groups/groups_list.html'
    context_object_name = 'groups'

    def get_queryset(self):
        queryset = Group.objects.all()
        return queryset

    def get_context_data(self , **kwargs):
        context = super().get_context_data(**kwargs)

        context['is_empty'] = False
        if len(self.get_queryset()) == 0:
            context['is_empty'] = True

        return context

def post_comment_create_and_list_view(request):
    all_posts = Group.objects.get_group_posts()
    profile = profiles.Profile.objects.get(user=request.user)
    post_form = posts.PostModelForm()
    comment_form = posts.CommentModelForm()
    post_added = False
    
    profile = profiles.Profile.objects.get(user=request.user)
    
    if "submit_post_form" in request.POST:
        post_form = posts.PostModelForm(request.POST ,request.FILES)
        if post_form.is_valid():
            instance = post_form.save(commit=False)
            instance.author = profile
            instance.save()
            post_form = posts.PostModelForm()
            post_added = True   
        
    if "submit_comment_form" in request.POST:
        comment_form = posts.CommentModelForm(request.POST)
        if comment_form.is_valid():
            instance = comment_form.save(commit=False)
            instance.user = profile
            instance.post = posts.Post.objects.get(id=request.POST.get('post_id'))
            instance.save()          
            comment_form = posts.CommentModelForm()   
        
    context = {
        'all_posts' : all_posts,
        'profile' : profile,
        'post_form': post_form,
        'comment_form' : comment_form, 
        'post_added' : post_added,
    }
    return render(request, 'groups/groups_list.html',context)

class PostUpdateView(LoginRequiredMixin, UpdateView):
    model = posts.models.Post
    form_class = posts.forms.PostModelForm
    template_name = 'groups/group-post-update.html'
    success_url = reverse_lazy('groups/groups:all-groups-view')
    
    def form_valid(self, form):
        profile = profiles.Profile.objects.get(user=self.request.user)
        if form.instance.author == profile:
            return super().form_valid(form)
        
        else:
            form.add_error(None,'Only this post author can update it')
            return super().form_invalid(form)
            

class PostDeleteView(LoginRequiredMixin, DeleteView):
    model = posts.models.Post
    template_name = 'groups/group-post-delete.html'
    success_url = reverse_lazy('groups/groups:all-groups-view')

    def get_post(self, *args, **kwargs):
        pk = self.kwargs.get('pk')
        post_obj = posts.models.Post.objects.get(pk=pk)
        if not post_obj.author.user == self.request.user:
            messages.warning(self.request, 'Only this post author can delete it')
        return post_obj