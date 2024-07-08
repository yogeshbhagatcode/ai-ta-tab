from lms.djangoapps.courseware.tabs import EnrolledTab
from django.utils.translation import gettext_noop
from django.conf import settings
from typing import Optional
from urllib.parse import urlencode
from opaque_keys.edx.keys import CourseKey


class AITab(EnrolledTab):
    """
    The main courseware view.
    """
    type = 'ai_ta_plugin'
    title = gettext_noop('AI TA Plugin')
    priority = 40
    view_name = 'ai_ta_plugin'
    is_hideable = False
    is_default = True
    is_dynamic = True

    @property
    def link_func(self):
        def _link_func(course, reverse_func):
            # return "http://apps.local.overhang.io:8080/ai/"
            # return f"http://{settings.MFE_CONFIG['BASE_URL']}:8080/ai-ta/"
            return get_ai_ta_mfe_url(course)
        return _link_func

    @classmethod
    def is_enabled(cls, course, user=None):
        """
        Courseware tabs are viewable to everyone, even anonymous users.
        """
        return True


# def _get_url_with_view_query_params(path: str, view: Optional[str] = None) -> str:
#     """
#     Helper function to build url if a url is configured

#     Args:
#         path (str): The path in the discussions MFE
#         view (str): which view to generate url for

#     Returns:
#         (str) URL link for MFE

#     """
#     if settings.DISCUSSIONS_MICROFRONTEND_URL is None:
#         return ''
#     url = f"{settings.DISCUSSIONS_MICROFRONTEND_URL}/{path}"

#     query_params = {}
#     if view == "in_context":
#         query_params.update({'inContext': True})

#     if query_params:
#         url = f"{url}?{urlencode(query_params)}"

#     return url


def get_ai_ta_mfe_url(course_key: CourseKey, view: Optional[str] = None) -> str:
    """
    Returns the url for the specified course in the ai-ta MFE.

    Args:
        course_key (CourseKey): course key of course for which to get url
        view (str): which view to generate url for

    Returns:
        (str) URL link for MFE. Empty if the base url isn't configured
    """
    if settings.AI_TA_MICROFRONTEND_URL is None:
        return ''
    url = f"{settings.AI_TA_MICROFRONTEND_URL}/{course_key}/"

    query_params = {}
    if view == "in_context":
        query_params.update({'inContext': True})

    if query_params:
        url = f"{url}?{urlencode(query_params)}"

    return url
