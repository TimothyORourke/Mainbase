from posts.forms import PostForm

def context_forms(request):
    return {
        'post_form' : PostForm,
    }