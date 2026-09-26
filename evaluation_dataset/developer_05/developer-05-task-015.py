def video_list(request, username=None):
    if username is None and not request.user.is_authenticated():
        from django.http import Http404
        raise Http404
    from django.contrib.auth.models import User
    user = User.objects.get(username=username) if username else request.user
    videos = Video.objects.filter(user=user).all()
    video_params = []
    for video in videos:
        video_params.append(_video_params(request, video.video_id))
    return render_to_response(
        "django_youtube/videos.html",
        {"video_params": video_params},
        context_instance=RequestContext(request)
    )