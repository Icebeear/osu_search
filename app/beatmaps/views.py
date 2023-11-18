from beatmaps.models import Beatmap
from django.views.generic.list import ListView
from django.db.models import Q
from datetime import datetime
from django.views.generic import TemplateView

class GenreLanguage:

    def get_languages(self):
        return Beatmap.objects.values("language").distinct()

    def get_genres(self):
        return Beatmap.objects.values('genre').distinct()
    
    def get_map_types(self):
        return Beatmap.objects.values('map_type').distinct()
    
    def get_order_values(self):
        return [
            {
                "val": "favourite_count",
                "name": "Favorites",
            },

            {
                "val": "play_count",
                "name":  "Play count",
            },

            {
                "val": "submit_date",
                "name":  "Date",
            },

            {
                "val": "total_length",
                "name":  "Length",
            },

            {
                "val": "star_difficulty",
                "name":  "Star",
            },
            
            {
                "val": "bpm",
                "name":  "BPM",
            },

            {
                "val": "ar",
                "name":  "AR",
            },

            {
                "val": "od",
                "name":  "OD",
            },

            {
                "val": "cs",
                "name":  "CS",
            },

            {
                "val": "hp",
                "name":  "HP",
            },
        ]
    

class MapsView(GenreLanguage, TemplateView):
    template_name = "beatmaps/index.html"
    

class FilterMapsView(GenreLanguage, ListView):
    template_name = "beatmaps/beatmaps.html"
    model = Beatmap
    context_object_name = 'maps'
    paginate_by = 10
    
    def get_queryset(self):
        self.title_input = self.request.GET.get("search-title") or ""
        self.artist_input = self.request.GET.get("search-artist") or ""
        self.source_input = self.request.GET.get("search-source") or ""
        self.mapper_input = self.request.GET.get("search-mapper") or ""  

        self.start_date = self.request.GET.get("start_date") or "2007-10-06"
        self.end_date = self.request.GET.get("end_date") or datetime.now().strftime("%Y-%m-%d")

        self.start_length = self.request.GET.get("start_length") or 0
        self.end_length = self.request.GET.get("end_length") or 4000

        self.start_bpm = self.request.GET.get("start_bpm") or 0
        self.end_bpm = self.request.GET.get("end_bpm") or 500

        self.start_favorites = self.request.GET.get("start_favorites") or 0
        self.end_favorites = self.request.GET.get("end_favorites") or 100_000

        self.start_plays = self.request.GET.get("start_plays") or 0
        self.end_plays = self.request.GET.get("end_plays") or 100_000_000


        language_list = self.request.GET.getlist("language") or [data["language"] for data in self.get_languages()]
        genre_list = self.request.GET.getlist("genre") or [data["genre"] for data in self.get_genres()]
        map_types_list = self.request.GET.getlist("map_type") or [data["map_type"] for data in self.get_map_types()]

        queryset = Beatmap.objects.all()

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

        '''вроде работает, перепроверить'''

      

        queryset = queryset.filter(
            Q(language__in=language_list),
            Q(genre__in=genre_list),
            Q(map_type__in=map_types_list),

            Q(submit_date__range=[self.start_date, self.end_date]),
            Q(total_length__range=[self.start_length, self.end_length]),
            Q(bpm__range=[self.start_bpm, self.end_bpm]),
            Q(play_count__range=[self.start_plays, self.end_plays]),
            Q(favourite_count__range=[self.start_favorites, self.end_favorites]),
        ).distinct()



        self.order = self.request.GET.get('query_order') 
        self.order_state = self.request.GET.get('order_state')
        self.order = f"-{self.order}" if not self.order_state else self.order 


        queryset = queryset.order_by(self.order)
        

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
        context['query_order'] = self.order.replace("-", "")

        context['start_length'] = self.start_length if self.start_length != 0 else ""
        context['end_length'] = self.end_length if self.end_length != 4000 else ""

        context['start_bpm'] = self.start_bpm if self.start_bpm != 0 else ""
        context['end_bpm'] = self.end_bpm if self.end_bpm != 500 else ""

        context['start_favorites'] = self.start_favorites if self.start_favorites != 0 else ""
        context['end_favorites'] = self.end_favorites if self.end_favorites != 100_000 else ""

        context['start_plays'] = self.start_plays if self.start_plays != 0 else ""
        context['end_plays'] = self.end_plays if self.end_plays != 100_000_000 else ""

        context['genres'] = self.request.GET.getlist("genre")
        context['languages'] = self.request.GET.getlist("language")
        context['map_types'] = self.request.GET.getlist("map_type")

        context["htmx"] = bool(self.request.htmx)

        
        return context
    