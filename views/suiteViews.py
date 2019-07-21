import pytz
import uuid
from datetime import datetime
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, redirect, render

from mgrtests.models import TestSuite


@login_required
def suite(request):
    setattr(request, 'view', 'suite')
    setattr(request, 'title', 'Suites')

    return render(request, 'testMgr/suite.html')
