from django.shortcuts import render
from beatmaps.models import Beatmap
from django.views.generic.list import ListView
from django.db.models import Q
from datetime import datetime
from django.views.generic import TemplateView

# class MapsListView(ListView):
#     model = Beatmap
#     context_object_name = 'maps'
#     template_name = 'beatmaps/index.html'


class GenreLanguage:

    def get_languages(self):
        return Beatmap.objects.values("language").distinct()

    def get_genres(self):
        return Beatmap.objects.values('genre').distinct()
    
    def get_map_types(self):
        return Beatmap.objects.values('map_type').distinct()
    

class MapsView(GenreLanguage, TemplateView):
    template_name = "beatmaps/index.html"
    

class FilterMapsView(GenreLanguage, ListView):
    template_name = "beatmaps/beatmaps.html"
    model = Beatmap
    context_object_name = 'maps'
    paginate_by = 10

    # def get_template_names(self):
    #     if self.request.htmx:
    #         return 'beatmaps/beatmaps.html'
    #     return 'beatmaps/beatmaps.html'
    
    def get_queryset(self):
        self.title_input = self.request.GET.get("search-title") or ""
        self.artist_input = self.request.GET.get("search-artist") or ""
        self.source_input = self.request.GET.get("search-source") or ""
        self.mapper_input = self.request.GET.get("search-mapper") or ""  

        self.start_date = self.request.GET.get("start_date") or "2007-10-06"
        self.end_date = self.request.GET.get("end_date") or datetime.now().strftime("%Y-%m-%d")

        self.start_length = self.request.GET.get("start_length") or 0
        self.end_length = self.request.GET.get("end_length") or 4000


        language_list = self.request.GET.getlist("language") or [data["language"] for data in self.get_languages()]
        genre_list = self.request.GET.getlist("genre") or [data["genre"] for data in self.get_genres()]
        map_types_list = self.request.GET.getlist("map_type") or [data["map_type"] for data in self.get_map_types()]

        queryset = Beatmap.objects.all()

        # print(self.start_date)
        # print(self.end_date)
        # print(self.start_date < self.end_date)

        filter_fields = {
            'artist_input': 'artist__icontains',
            'title_input': 'title__icontains',
            'source_input': 'source__icontains',
            'mapper_input': 'mapper__icontains',
        }

        for field, filter_type in filter_fields.items():
            input_value = getattr(self, field)
            if input_value:
                queryset = queryset.filter(**{filter_type: input_value})

        # if self.artist_input:
        #     queryset = queryset.filter(artist__startswith=self.artist_input.title())

        # if self.title_input:
        #     queryset = queryset.filter(title__startswith=self.title_input)

        # if self.source_input:
        #     queryset = queryset.filter(source__startswith=self.source_input)

        # if self.mapper_input:
        #     queryset = queryset.filter(mapper__startswith=self.mapper_input)


        # filter_fields = {
        #     'artist_input': 'artist__startswith',


        '''вроде работает, перепроверить'''


        # print("После фильтрации по title:", queryset)  # Отладочный вывод

        # print(self.request.GET.getlist("language")) 

        queryset = queryset.filter(
            Q(language__in=language_list),
            Q(genre__in=genre_list),
            Q(map_type__in=map_types_list),

            Q(submit_date__range=[self.start_date, self.end_date]),
            Q(total_length__range=[self.start_length, self.end_length]),
        ).distinct()


        # queryset = queryset.filter(submit_date__range=[self.start_date, self.end_date])
        # queryset = queryset.filter(total_length__range=[self.start_length, self.end_length])

        self.order = self.request.GET.get('query_order') 

        self.order_state = self.request.GET.get('order_state')

        self.order = f"-{self.order}" if not self.order_state else self.order 

        queryset = queryset.order_by(self.order)
        
        

        

        # if self.order_state:
        #     queryset = queryset.order_by(self.order)
        # else:
        #     queryset = queryset.order_by(f"-{self.order}")

        # print("После фильтрации по языку и жанру:", queryset)  # Отладочный вывод
        
        return queryset.distinct()
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context['search_title'] = self.title_input 
        context['search_artist'] = self.artist_input
        context['search_source'] = self.source_input
        context['search_mapper'] = self.mapper_input

        context['start_date'] = self.start_date
        context['end_date'] = self.end_date

        context['order_state'] = self.order_state

        context['genres'] = self.request.GET.getlist("genre")
        context['languages'] = self.request.GET.getlist("language")
        context['map_types'] = self.request.GET.getlist("map_type")

        context["htmx"] = bool(self.request.htmx)

        
        return context
    
    

# {% if genre.genre in request.POST.getlist('genre') %}
# checked
# {% endif %}>


    # def get_context_data(self, *args, **kwargs):
    #     context = super().get_context_data(*args, **kwargs)
    #     print(self.request.GET.getlist("language"))
    #     context["language"] = '&'.join([f"language={x}&" for x in self.request.GET.getlist("language")])
    #     context["genre"] = '&'.join([f"genre={x}&" for x in self.request.GET.getlist("genre")])
    #     return context