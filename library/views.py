from django.shortcuts import render
from django.views import View
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from library.models import Book
from django.core.paginator import Paginator

# Create your views here.


class ApiView(View):

    def get(self, request):
        return JsonResponse({"message": "Hello there!"})


api_view = csrf_exempt(ApiView.as_view())


class BookApiView(View):
    page_size = 10

    def get_params(self):
        page = None
        keyset = False
        page_param = self.request.GET.get("page", "1")
        try:
            page = int(page_param)
        except ValueError as e:
            page = 1
        keyset_param = self.request.GET.get("keyset", "false")
        try:
            keyset = keyset_param == "true"
        except Exception as e:
            pass
        return page, keyset

    def get_page_using_offset(self, page_number):
        result = []
        page_meta = dict()
        query = Book.objects.all().order_by('-id')
        paginator = Paginator(query, self.page_size)
        if page_number not in paginator.page_range:
            page_number = 1

        page = paginator.get_page(page_number)
        for item in page:
            result.append({
                "title": item.title,
                "publisher": item.publisher,
                "library": item.library.name
            })
        page_meta.update({
            "page": page_number,
            "has_next": page.has_next(),
            "has_previous": page.has_previous(),
            "page_range": [
                paginator.page_range[0], paginator.page_range[-1]
            ]
        })
        return result, page_meta

    def get(self, request):
        page, keyset = self.get_params()
        page_data, page_meta = self.get_page_using_offset(page)
        response = {
            "data": page_data,
            "page_meta": page_meta,
            "using_keyset": keyset
        }
        return JsonResponse(
            response, status=200, content_type="application/json"
        )


book_list_view = csrf_exempt(BookApiView.as_view())
