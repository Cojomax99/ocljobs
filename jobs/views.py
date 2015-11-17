from django.conf import settings
from django.core.exceptions import ObjectDoesNotExist
from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic.edit import FormView

from jobs.forms import QueryForm
from jobs.models import get_model_from_entry, JobsQuery

from collections import namedtuple
import json
import requests


class HomeView(FormView):
    form_class = QueryForm
    template_name = "home.html"
    success_url = "/"


def search(request):
    form = QueryForm()

    if 'description' in request.GET and 'location' in request.GET:
        description = request.GET.get('description', None)
        location = request.GET.get('location', None)
        full_time = request.GET.get('full_time', False)

        try:
            data = get_cached_search_results(description, location, full_time)
            print("Using cached results!")
        except ObjectDoesNotExist:
            print("Object doesn't exist, fetching!")
            data = get_search_results(description, location, full_time)

        return render(request, 'home.html', {
            'description': description,
            'data': data,
            'location': location,
            'full_time': full_time,
            'form': form
        })
    else:
        return HttpResponse('Something went wrong!')


def get_search_results(description=None, location=None, full_time=False):
    """ Hit the GitHub API for search results """
    url = settings.JOBS_API_ROOT + "?"

    if description:
        url += "description={}&".format(description)

    if location:
        url += "location={}&".format(location)

    if full_time:
        url += "full_time=true"

    response = requests.get(url)

    Entry = namedtuple('Entry', ['title', 'company', 'company_url', 'url', 'how_to_apply', 'created_at',
                                 'location', 'id', 'company_logo', 'description', 'type'])

    entry_dict = json.loads(json.dumps(response.json()), object_hook=lambda x: Entry(**x))

    query = cache_query(description, location, full_time)

    # add entries to the database for use later
    for entry in entry_dict:
        cache_entry(query, entry)

    return entry_dict


def get_cached_search_results(description=None, location=None, full_time=False):
    """ Retrieve cached search results for a query from the database """
    query = JobsQuery.objects.get(description=description, location=location, full_time=full_time)

    return list(query.jobsentry_set.all())

def cache_query(description=None, location=None, full_time=False):
    """ Cache the query in the database """
    query, created = JobsQuery.objects.get_or_create(description=description, location=location, full_time=full_time)
    return query


def cache_entry(query, entry):
    """ Cache the entries to the query in the database """
    temp = get_model_from_entry(query, entry)
    temp.save()
