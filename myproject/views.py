import json
import re
from django.http import HttpResponse
from django.shortcuts import render
from django.conf import settings
from django.template import loader, RequestContext
from django.views.decorators.http import require_http_methods, require_POST
from myproject.models import Review, User

@require_POST
def pt_hook(request):
    data = json.loads(request.body)
    print data
    users = User.objects.all()
    story_id = data['primary_resources'][0]['id']
    status = data['highlight']
    found_story = Review.objects.filter(story_id=story_id)
    created_timestamp = data['occurred_at']
    if User.objects.filter(name=data['performed_by']['name']):
        created_by = User.objects.get(name=data['performed_by']['name'])
    else:
        created_by = None
    pv_link = data['primary_resources'][0]['url']
    project_name = data['primary_resources'][0]['name']
    story_type = data['primary_resources'][0]['story_type']
    message = data['message']
    github_link = re.findall('http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+', message)
    if github_link:
        github_link = github_link[0]
    else:
        github_link = None
    if found_story:
        found_story = Review.objects.filter(story_id=story_id)[0]
        if status == 'delivered':
            found_story.delete()
            return HttpResponse("Story was delivered")
        else:
            for user in users:
                if 'review' and user.tag_name in message:
                    review_by = user
                    found_story.review_by = review_by
                    found_story.created_timestamp = created_timestamp
                    found_story.created_by = created_by
                    found_story.pv_link = pv_link
                    found_story.project_name = project_name
                    found_story.status = status
                    found_story.github_link = github_link
                    found_story.save()
                    return HttpResponse('Update story')
    else:
        for user in users:
            if 'review' in message and user.tag_name in message and 'remove' not in status:
                review_by = user
                Review.objects.create(created_timestamp=created_timestamp, created_by=created_by, pv_link=pv_link,
                                      project_name=project_name, status=status, story_type=story_type, story_id=story_id,
                                      review_by=review_by, github_link=github_link)
    return HttpResponse("Got Data")


def home(request):
    print 'test'
    users = User.objects.all()
    results = []
    for user in users:
        total_reviews = Review.objects.filter(review_by=user.id).count()
        results.append({'user': user, 'reviews': total_reviews})

    return render(request, 'index.html', {'results': results})


def reviews(request):
    user_id = request.GET.get('user')
    sorted_reviews = []
    if user_id:
        reviews = Review.objects.filter(review_by=int(user_id))
        sorted_reviews = sorted(reviews, key=lambda x: x.created_timestamp)

    return render(request, 'reviews.html', {'reviews': sorted_reviews})

