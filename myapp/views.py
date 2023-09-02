from django.shortcuts import render
import logging
from django.http import HttpResponse

logger = logging.getLogger(__name__)



def index(request):
    logger.info('Index page accessed')
    return HttpResponse(html)


def about(request):
    logger.info('About page accessed')
    return HttpResponse(html2)