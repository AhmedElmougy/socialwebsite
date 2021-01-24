from django.shortcuts import render
from django.urls import reverse_lazy
from django.contrib import messages
from django.db import IntegrityError
from django.views import generic 
from django.shortcuts import get_object_or_404
from groups.models import Group,Membership
from groups.forms import GroupForm
# Create your views here.


class IndexView(generic.TemplateView):
    template_name = "index.html"


class GroupCreateView(generic.CreateView):
    model = Group
    form_class = GroupForm
    template_name = "groups/group_form.html"

    def form_valid(self, form):
        form.instance.auther = self.request.user
        return super().form_valid(form)   

class GroupUpdateView(generic.UpdateView):
    model = Group
    form_class = GroupForm
    template_name = "groups/group_form.html"

class GroupListView(generic.ListView):
    model = Group
    template_name = "groups/group_list.html"

class GroupDetailView(generic.DetailView):
    model = Group
    template_name = "groups/group_details.html"

class GroupDeleteView(generic.DeleteView):
    model = Group
    template_name = "groups/group_delete.html"
    success_url   = reverse_lazy("groups:group_list")

class JoinGoup(generic.RedirectView):
    pattern_name = 'groups:group_details'
    def get_redirect_url(self, *args, **kwargs):
        group = get_object_or_404(Group,pk=self.kwargs.get('pk'),slug=self.kwargs.get('slug'))
        try:
            Membership.objects.create(user=self.request.user,group=group)
        except IntegrityError:
            messages.warning(self.request,"Warning already amember of {}".format(group.name))
        else:
            messages.success(self.request,"You have successfully joined {} group".format(group.name))

        return super().get_redirect_url(*args, **kwargs)

class LeaveGoup(generic.RedirectView):
    pattern_name = 'groups:group_details'
    
    def get_redirect_url(self, *args, **kwargs):
        try:
            membership = Membership.objects.filter( user=self.request.user,group__slug=self.kwargs.get("slug")).get()
        except IntegrityError:
            messages.warning(self.request,"You are not a member of {} group".format(membership.group.name))
        else:
            membership.delete()
            messages.success(self.request,"You are no longer a member of {} group".format(membership.group.name))

        return super().get_redirect_url(*args, **kwargs)

        
    


