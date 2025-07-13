from django.shortcuts import redirect
from django.contrib import messages

class BookOwnerMixin():

    def dispatch(self, request, *args, **kwargs):
        obj = self.get_object()
        if obj.added_by != request.user:
            messages.error(request, 'Ви можете редагувати лише власні книги')
            return redirect('library:book_detail', pk=obj.pk)
        return super().dispatch(request, *args, **kwargs)
    

class ReviewOwnerMixin():

    def dispatch(self, request, *args, **kwargs):
        obj = self.get_object()
        if obj.user != request.user:
            messages.error(request, 'Ви можете редагувати лише власні відгуки')
            return redirect('library:book_detail', pk=obj.pk)
        return super().dispatch(request, *args, **kwargs)
