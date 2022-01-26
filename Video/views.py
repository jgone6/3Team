import os
# from google.analytics.data_v1beta import BetaAnalyticsDataClient, RunRealtimeReportRequest
# from google.analytics.data_v1beta.types import DateRange
# from google.analytics.data_v1beta.types import Dimension
# from google.analytics.data_v1beta.types import Metric
# from google.analytics.data_v1beta.types import MetricType
# from google.analytics.data_v1beta.types import RunReportRequest

from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.db.models import Q
from django.http import JsonResponse
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
# from Video.forms import VideoForm
from django.views.decorators.http import require_POST
import requests
import json
from Video.models import Video
import requests
import json
from .forms import VideoForm
from apiclient.discovery import build
from oauth2client.service_account import ServiceAccountCredentials


def get_service(api_name, api_version, scopes, key_file_location):
    """Get a service that communicates to a Google API.

    Args:
        api_name: The name of the api to connect to.
        api_version: The api version to connect to.
        scopes: A list auth scopes to authorize for the application.
        key_file_location: The path to a valid service account JSON key file.

    Returns:
        A service that is connected to the specified API.
    """

    credentials = ServiceAccountCredentials.from_json_keyfile_name(
        key_file_location, scopes=scopes)

    # Build the service object.
    service = build(api_name, api_version, credentials=credentials)

    return service


def get_first_profile_id(service):
    # Use the Analytics service object to get the first profile id.

    # Get a list of all Google Analytics accounts for this user
    accounts = service.management().accounts().list().execute()

    if accounts.get('items'):
        # Get the first Google Analytics account.
        account = accounts.get('items')[0].get('id')
        print(account)

        # Get a list of all the properties for the first account.
        properties = service.management().webproperties().list(
            accountId=account).execute()

        if properties.get('items'):
            # Get the first property id.
            property = properties.get('items')[0].get('id')

            # Get a list of all views (profiles) for the first property.
            profiles = service.management().profiles().list(
                accountId=account,
                webPropertyId=property).execute()

            if profiles.get('items'):
                # return the first view (profile) id.
                return profiles.get('items')[0].get('id')

    return None

def get_results(service, profile_id):
    # Use the Analytics Service Object to query the Core Reporting API
    # for the number of sessions within the past seven days.
    return service.data().ga().get(
        ids='ga:' + profile_id,
        start_date='7daysAgo',
        end_date='today',
        metrics='ga:pageviews',
        dimensions='ga:pagePath'

    ).execute()



def get_report(analytics):
  """Queries the Analytics Reporting API V4.

  Args:
    analytics: An authorized Analytics Reporting API V4 service object.
  Returns:
    The Analytics Reporting API V4 response.
  """
  return analytics.reports().batchGet(
      body={
        'reportRequests': [
        {
          'viewId': VIEW_ID,
          'dateRanges': [{'startDate': '30daysAgo', 'endDate': 'today'}],
          'metrics': [{'expression': 'ga:pageviews'}],
          'dimensions': []
        }]
      }
  ).execute()
def get_visitors(response):
  visitors = 0 # in case there are no analytics available yet
  for report in response.get('reports', []):
    columnHeader = report.get('columnHeader', {})
    metricHeaders = columnHeader.get('metricHeader', {}).get('metricHeaderEntries', [])

    for row in report.get('data', {}).get('rows', []):
      dateRangeValues = row.get('metrics', [])

      for i, values in enumerate(dateRangeValues):
        for metricHeader, value in zip(metricHeaders, values.get('values')):
          visitors = value

  return str(visitors)
def dashboard(request):
    analytics = initialize_analyticsreporting()
    response = get_report(analytics)
    visitors = get_visitors(response)
    print(visitors)
    return render(request,'manager/dashboard.html', {'visitors':visitors})
def analyze(request):
    os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "C:/Users/SLINFO/PycharmProjects/blog/인증용json파일"
    activeUsers = ''
    client = BetaAnalyticsDataClient()

    reportRequest = RunRealtimeReportRequest(
        property=f"properties/300659810",
        dimensions=[Dimension(name="country")],
        metrics=[Metric(name="activeUsers")],
    )
    response = client.run_realtime_report(reportRequest)

    print(f"{response.row_count} rows received")
    for dimensionHeader in response.dimension_headers:
        print(f"Dimension header name: {dimensionHeader.name}")
    for metricHeader in response.metric_headers:
        metric_type = MetricType(metricHeader.type_).name
        print(f"Metric header name: {metricHeader.name} ({metric_type})")
    # [END analyticsdata_print_run_report_response_header]

    # [START analyticsdata_print_run_report_response_rows]
    print("Report result:")
    for row in response.rows:
        for dimension_value in row.dimension_values:
            print(dimension_value.value)

        for metric_value in row.metric_values:
            print(metric_value.value)
            activeUsers = metric_value.value

    return render(request,'manager/analyze.html', {'activeUsers' : activeUsers})



def get_service(api_name, api_version, scopes, key_file_location):
    """Get a service that communicates to a Google API.

    Args:
        api_name: The name of the api to connect to.
        api_version: The api version to connect to.
        scopes: A list auth scopes to authorize for the application.
        key_file_location: The path to a valid service account JSON key file.

    Returns:
        A service that is connected to the specified API.
    """

    credentials = ServiceAccountCredentials.from_json_keyfile_name(
        key_file_location, scopes=scopes)

    # Build the service object.
    service = build(api_name, api_version, credentials=credentials)

    return service


# def get_first_profile_id(service):
#     # Use the Analytics service object to get the first profile id.
#
#     # Get a list of all Google Analytics accounts for this user
#     accounts = service.management().accounts().list().execute()
#
#     if accounts.get('items'):
#         # Get the first Google Analytics account.
#         account = accounts.get('items')[0].get('id')
#
#         # Get a list of all the properties for the first account.
#         properties = service.management().webproperties().list(
#             accountId=account).execute()
#
#         if properties.get('items'):
#             # Get the first property id.
#             property = properties.get('items')[0].get('id')
#
#             # Get a list of all views (profiles) for the first property.
#             profiles = service.management().profiles().list(
#                 accountId=account,
#                 webPropertyId=property).execute()
#
#             if profiles.get('items'):
#                 # return the first view (profile) id.
#                 return profiles.get('items')[0].get('id')
#
#     return None



def get_first_profile_id(service):
    # Use the Analytics service object to get the first profile id.

    # Get a list of all Google Analytics accounts for this user
    accounts = service.management().accounts().list().execute()

    if accounts.get('items'):
        # Get the first Google Analytics account.
        account = accounts.get('items')[0].get('id')

        # Get a list of all the properties for the first account.
        properties = service.management().webproperties().list(
            accountId=account).execute()

        if properties.get('items'):
            # Get the first property id.
            property = properties.get('items')[0].get('id')

            # Get a list of all views (profiles) for the first property.
            profiles = service.management().profiles().list(
                accountId=account,
                webPropertyId=property).execute()

            if profiles.get('items'):
                # return the first view (profile) id.
                return profiles.get('items')[0].get('id')

    return None
def get_results(service, profile_id):
    # Use the Analytics Service Object to query the Core Reporting API
    # for the number of sessions within the past seven days.
    return service.data().ga().get(
        ids='ga:' + profile_id,
        start_date='7daysAgo',
        end_date='today',
        metrics='ga:sessions').execute()

def print_results(results):

    if results:
        # print ('View (Profile):', results.get('profileInfo').get('profileName'))
        print('View (Profile):', results.get('profileInfo'))
        print ('Total Sessions:', results.get('rows')[0][0])

    else:
        print ('No results found')


def main(a):
    # Define the auth scopes to request.
    scope = 'https://www.googleapis.com/auth/analytics.readonly'
    key_file_location = 'C:/Users/slinfo/Documents/GitHub/3Team/Video/active-landing-339302-f8a2d8c6730f.json'

    # Authenticate and construct service.
    service = get_service(
        api_name='analytics',
        api_version='v3',
        scopes=[scope],
        key_file_location=key_file_location)

    profile_id = get_first_profile_id(service)

    print_results(get_results(service, profile_id))


    return render(a, 'Video/api.html', {'results': profile_id})

#
# redirect('/Video/get_service')


if __name__ == '__main__':
    main()


def test2(request):
    return render(request, 'Video/test2.html')


def getTag(request, tags):
    print(tags)
    posts = Video.objects.all().filter(tag=tags)

    json = []
    for post in posts:
        json_post = {'id': post.id, 'title': post.title, 'tag': post.tag, 'file': post.file.name,
                     'file2': post.file2.name}
        json.append(json_post)

    return JsonResponse({'message': json})


@login_required(login_url='/users/login')
def upload(request):
    if request.method == "GET":
        videoform = VideoForm()  # 입력칸에 아무것도 없는 상태로 준다
        return render(request, 'video/upload.html',
                      {'form': videoform})
    elif request.method == 'POST':
        videoform = VideoForm(request.POST, request.FILES)

        if videoform.is_valid():
            video = videoform.save(commit=False)
            video.writer = request.user
            video.save()
            return redirect('/Video/mylist')
        else:
            videoform = VideoForm()
            return render(request, 'Video/upload.html', {'form': videoform})


def ss(request):
    posts = Video.objects.all()
    return render(request, 'video/list.html', {'posts': posts})


def posts(request):
    posts = Video.objects.all()  # board table에서 모든 데이터를 다 가져옴

    return render(request, 'video/list.html',
                  {'posts': posts})


def myposts(request):
    posts = Video.objects.all()  # board table에서 모든 데이터를 다 가져옴

    return render(request, 'video/mylist.html',
                  {'posts': posts})


def read(request, bid):
    post = Video.objects.get(Q(id=bid))
    posts = Video.objects.all()
    # posts = Board.objects.all()
    return render(request, 'Video/read.html', {'read': post, 'posts': posts, 'bid' : bid } )
    # #board/read.html페이지를 보여주고 Board.objects.get( Q(id=bid))의 값
    # 을 'read'로 저장한다.


def readmine(request, bid):
    post = Video.objects.get(Q(id=bid))
    # posts = Board.objects.all()
    return render(request, 'Video/readmine.html', {'read': post})
    # #board/read.html페이지를 보여주고 Board.objects.get( Q(id=bid))의 값
    # 을 'read'로 저장한다.


# def list_tag(request, tag) :
#     post = Video.objects.get(Q(tag=tag))
#     return render(request, 'Video/list_music.html',{'list' : post})

def list_music(request):
    posts = Video.objects.all()  # board table에서 모든 데이터를 다 가져옴

    return render(request, 'video/list_music.html',
                  {'posts': posts})


def list_var(request):
    posts = Video.objects.all()  # board table에서 모든 데이터를 다 가져옴

    return render(request, 'video/list_var.html',
                  {'posts': posts})


def list_geo(request):
    posts = Video.objects.all()  # board table에서 모든 데이터를 다 가져옴

    return render(request, 'video/list_geo.html',
                  {'posts': posts})


def list_edu(request):
    posts = Video.objects.all()  # board table에서 모든 데이터를 다 가져옴

    return render(request, 'video/list_edu.html',
                  {'posts': posts})


@login_required(login_url='/users/login')
def delete(request, bid):
    post = Video.objects.get(Q(id=bid))
    if request.user != post.writer:
        return render(request, 'Video/list.html')
    post.delete()
    return redirect('/Video/list')


# @login_required(login_url='/users/login')
# def update(request, bid) :
#     post = Video.objects.get(Q(id=bid))  #게시글 하나를 가져오는것
#     if request.method == "GET" :
#         videoForm = VideoForm()
#         #특정 조건 id에 해당하는 값을 저장한다.
#         return render(request,'Video/update.html',{'videoForm' : videoForm})
#     elif request.method == "POST" :
#         videoForm = VideoForm(request.POST, request.FILES)
#         print(videoForm.cleaned_data['title'])
#         if videoForm.is_valid():   #boardForm안에 값이 유효한다
#             post.title = videoForm.cleaned_data['title']
#             post.tag = videoForm.cleaned_data['tag']
#             post.file = videoForm.cleaned_data['file']
#             post.file2 = videoForm.cleaned_data['file2']
#             post.writer = request.user
#             post.save()
#             print("1")
#             return redirect('/Video/list')
#
#             # return render(request, 'Video/list.html',)
#         else:
#             return redirect('/')

@login_required(login_url='/users/login')
def update(request, bid):
    post = Video.objects.get(Q(id=bid))  # 게시글 하나를 가져오는것

    if request.user != post.writer:
        return render(request, 'Video/list.html')

    if request.method == "GET":
        videoForm = VideoForm(instance=post)
        # 특정 조건 id에 해당하는 값을 저장한다.
        return render(request, 'Video/update.html', {'videoForm': videoForm})
    elif request.method == "POST":
        videoForm = VideoForm(request.POST, request.FILES)

        # boardForm에서 사용자가 보내온 데이터를 받느다
        if videoForm.is_valid():  # boardForm안에 값이 유효한다면
            post.title = videoForm.cleaned_data['title']
            post.tag = videoForm.cleaned_data['tag']
            post.file = videoForm.cleaned_data['file']
            post.file2 = videoForm.cleaned_data['file2']
            post.save()
            return redirect('/Video/list')

            # return render(request, 'Video/list.html',)


# def update(request, bid):
#     post = Video.objects.get(Q(id=bid))  # 게시글 하나를 가져오는것
#     if request.user != post.writer:
#         return render(request, 'Video/list.html')
#     post.delete()
#     if request.method == "GET":
#         # boardForm = BoardForm()      #입력칸에 아무것도 없는 상태로 준다
#         videoForm = VideoForm(instance=post)  # 입력칸에 아무것도 없는 상태로 준다
#         return render(request, 'video/update.html', {'videoForm': videoForm})
#     elif request.method == "POST":
#         videoForm = VideoForm(request.POST)
#         # boardForm에서 사용자가 보내온 데이터를 받느다
#         if videoForm.is_valid():  # boardForm안에 값이 유효한다면
#             post.title = videoForm.cleaned_data['title']
#             post.tag = videoForm.cleaned_data['tag']
#             post.file = videoForm.cleaned_data['file']
#
#             post.save()
#             # return redirect('/board/read/' + str(bid))
#             return redirect('/Video/list')

def requestapi1(request):
    return render(request, 'Video/test5.html')
