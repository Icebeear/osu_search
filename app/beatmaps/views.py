from beatmaps.models import Beatmap
from django.views.generic.list import ListView
from django.db.models import Q
from datetime import datetime
from django.views.generic import TemplateView

class FormValues:

    def get_languages(self):
        # return Beatmap.objects.values("language").distinct().order_by("language")
        return [{"name": language} for language in ["japanese", "instrumental", 
                                                    "english", "russian", "korean",
                                                    "chinese", "german", "polish",
                                                    "french", "italian", "spanish",
                                                    "swedish", "other"]]

    def get_genres(self):
        # return Beatmap.objects.values('genre').distinct().order_by("genre")
        return [{"name": genre} for genre in ["anime", "rock", "metal", 
                                              "pop", "video game", "electronic", 
                                              "hip hop", "classical", 
                                              "jazz", "folk", "novelty"]]
    
    def get_map_types(self):
        # return Beatmap.objects.values('map_type').distinct().order_by("map_type")
        return [{"type": map_type} for map_type in ["ranked", "approved", "qualified", 
                                                    "loved", "pending", "WIP"]]
    
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
    
    def get_map_conditions(self):
        return None 


class MapsView(FormValues, TemplateView):
    template_name = "beatmaps/index.html"
    

class FilterMapsView(FormValues, ListView):
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


        self.start_ar = self.request.GET.get("start_ar") or 0 
        self.end_ar = self.request.GET.get("end_ar") or 10 

        self.start_star = self.request.GET.get("start_star") or 0 
        self.end_star = self.request.GET.get("end_star") or 10 

        self.start_od = self.request.GET.get("start_od") or 0 
        self.end_od = self.request.GET.get("end_od") or 10 

        
        self.start_cs = self.request.GET.get("start_cs") or 0 
        self.end_cs = self.request.GET.get("end_cs") or 10 

        self.start_hp = self.request.GET.get("start_hp") or 0 
        self.end_hp = self.request.GET.get("end_hp") or 10 

        self.volume = self.request.GET.get("volume") or 30

        self.scroll_state = self.request.GET.get("scroll_state")


        language_list = self.request.GET.getlist("language") or [data["name"] for data in self.get_languages()]
        genre_list = self.request.GET.getlist("genre") or [data["name"] for data in self.get_genres()]
        map_types_list = self.request.GET.getlist("map_type") or [data["type"] for data in self.get_map_types()]

        queryset = Beatmap.objects.all().distinct()

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


        queryset = queryset.filter(
            Q(language__in=language_list),
            Q(genre__in=genre_list),
            Q(map_type__in=map_types_list),

            Q(submit_date__range=[self.start_date, self.end_date]),
            Q(total_length__range=[self.start_length, self.end_length]),
            Q(bpm__range=[self.start_bpm, self.end_bpm]),
            Q(play_count__range=[self.start_plays, self.end_plays]),
            Q(favourite_count__range=[self.start_favorites, self.end_favorites]),

            Q(star_difficulty__range=[self.start_star, self.end_star]),
            Q(ar__range=[self.start_ar, self.end_ar]),
            Q(od__range=[self.start_od, self.end_od]),
            Q(cs__range=[self.start_cs, self.end_cs]),
            Q(hp__range=[self.start_hp, self.end_hp]),
        )



        self.order = self.request.GET.get('query_order') 
        self.order_state = self.request.GET.get('order_state')
        self.order = f"-{self.order}" if not self.order_state else self.order 


        queryset = queryset.order_by(self.order)
        

        return queryset
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context["htmx"] = bool(self.request.htmx)

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


        context["start_star"] = self.start_star
        context["end_star"] = self.end_star

        context["start_ar"] = self.start_ar
        context["end_ar"] = self.end_ar

        context["start_od"] = self.start_od
        context["end_od"] = self.end_od

        context["start_cs"] = self.start_cs
        context["end_cs"] = self.end_cs

        context["start_hp"] = self.start_hp
        context["end_hp"] = self.end_hp

        context["scroll_state"] = self.scroll_state
        context["volume"] = self.volume

        return context