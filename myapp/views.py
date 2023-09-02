from django.shortcuts import render
import logging
from django.http import HttpResponse

logger = logging.getLogger(__name__)

html = """<h1>Hello!</h1>
<br>
<h2>This is the page about the my first django project</h2>
<br>
<p>Lorem ipsum dolor sit amet, consectetur adipisicing elit. Dolores eum expedita itaque laudantium mollitia, 
sit suscipit tempore. Neque obcaecati repudiandae vero! Ab alias aperiam atque blanditiis cupiditate, et fuga 
harum inventore, ipsam ipsum iste magni maiores nam necessitatibus nulla perferendis praesentium quibusdam quos 
repudiandae similique sit tenetur voluptas voluptate voluptates.</p>
"""

html2 = """<h1>This is the page about me</h1>
<br>
<h2>My name is Alex and i am the developer of this website</h2>
<p>Lorem ipsum dolor sit amet, consectetur adipisicing elit. Dolores eum expedita itaque laudantium mollitia, 
sit suscipit tempore. Neque obcaecati repudiandae vero! Ab alias aperiam atque blanditiis cupiditate, et fuga 
harum inventore, ipsam ipsum iste magni maiores nam necessitatibus nulla perferendis praesentium quibusdam quos 
repudiandae similique sit tenetur voluptas voluptate voluptates.</p>
"""


def index(request):
    logger.info('Index page accessed')
    return HttpResponse(html)


def about(request):
    logger.info('About page accessed')
    return HttpResponse(html2)
