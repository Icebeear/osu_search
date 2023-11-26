from beatmaps.models import Beatmap
from django.db.models import Q

from django.views.generic import TemplateView
from django.views.generic.list import ListView

from datetime import datetime


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
    
    # def get_main_fields(self):
    #     return {"title", "artist", "source", "mapper"} 


class MapsView(FormValues, TemplateView):
    template_name = "beatmaps/index.html"
    

class FilterMapsView(FormValues, ListView):
    template_name = "beatmaps/beatmaps.html"
    model = Beatmap
    context_object_name = 'maps'
    paginate_by = 12
    
    def get_queryset(self):
        self.title = self.request.GET.get("title") or ""
        self.artist = self.request.GET.get("artist") or ""
        self.source = self.request.GET.get("source") or ""
        self.mapper = self.request.GET.get("mapper") or ""  

        self.min_date = self.request.GET.get("min_date") or "2007-10-06"
        self.max_date = self.request.GET.get("max_date") or datetime.now().strftime("%Y-%m-%d")

        self.min_length = self.request.GET.get("min_length") or 0
        self.max_length = self.request.GET.get("max_length") or 4000

        self.min_bpm = self.request.GET.get("min_bpm") or 0
        self.max_bpm = self.request.GET.get("max_bpm") or 500

        self.min_favorites = self.request.GET.get("min_favorites") or 0
        self.max_favorites = self.request.GET.get("max_favorites") or 100_000

        self.min_plays = self.request.GET.get("min_plays") or 0
        self.max_plays = self.request.GET.get("max_plays") or 100_000_000


        self.min_ar = self.request.GET.get("min_ar") or 0 
        self.max_ar = self.request.GET.get("max_ar") or 10 

        self.min_star = self.request.GET.get("min_star") or 0 
        self.max_star = self.request.GET.get("max_star") or 10 

        self.min_od = self.request.GET.get("min_od") or 0 
        self.max_od = self.request.GET.get("max_od") or 10 

        self.min_cs = self.request.GET.get("min_cs") or 0 
        self.max_cs = self.request.GET.get("max_cs") or 10 

        self.min_hp = self.request.GET.get("min_hp") or 0 
        self.max_hp = self.request.GET.get("max_hp") or 10 

        self.volume = self.request.GET.get("volume") or 30

        self.scroll_state = self.request.GET.get("scroll_state")


        language_list = self.request.GET.getlist("language") or [data["name"] for data in self.get_languages()]
        genre_list = self.request.GET.getlist("genre") or [data["name"] for data in self.get_genres()]
        map_types_list = self.request.GET.getlist("map_type") or [data["type"] for data in self.get_map_types()]

        queryset = Beatmap.objects.all().distinct()

        filter_fields = {
            'artist': 'artist__icontains',
            'title': 'title__icontains',
            'source': 'source__icontains',
            'mapper': 'mapper__icontains',
        }

        for field, filter_type in filter_fields.items():
            input_value = getattr(self, field)
            if input_value:
                queryset = queryset.filter(**{filter_type: input_value})


        queryset = queryset.filter(
            Q(language__in=language_list),
            Q(genre__in=genre_list),
            Q(map_type__in=map_types_list),

            Q(submit_date__range=[self.min_date, self.max_date]),
            Q(total_length__range=[self.min_length, self.max_length]),
            Q(bpm__range=[self.min_bpm, self.max_bpm]),
            Q(play_count__range=[self.min_plays, self.max_plays]),
            Q(favourite_count__range=[self.min_favorites, self.max_favorites]),

            Q(star_difficulty__range=[self.min_star, self.max_star]),
            Q(ar__range=[self.min_ar, self.max_ar]),
            Q(od__range=[self.min_od, self.max_od]),
            Q(cs__range=[self.min_cs, self.max_cs]),
            Q(hp__range=[self.min_hp, self.max_hp]),
        )



        self.order = self.request.GET.get('query_order') 
        self.order_state = self.request.GET.get('order_state')
        self.order = f"-{self.order}" if not self.order_state else self.order 


        queryset = queryset.order_by(self.order)
        

        return queryset
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context["htmx"] = bool(self.request.htmx)

        context['title'] = self.title
        context['artist'] = self.artist
        context['source'] = self.source
        context['mapper'] = self.mapper

        context['min_date'] = self.min_date
        context['max_date'] = self.max_date
        
        context['order_state'] = self.order_state
        context['query_order'] = self.order.replace("-", "")

        context['min_length'] = self.min_length if self.min_length != 0 else ""
        context['max_length'] = self.max_length if self.max_length != 4000 else ""

        context['min_bpm'] = self.min_bpm if self.min_bpm != 0 else ""
        context['max_bpm'] = self.max_bpm if self.max_bpm != 500 else ""

        context['min_favorites'] = self.min_favorites if self.min_favorites != 0 else ""
        context['max_favorites'] = self.max_favorites if self.max_favorites != 100_000 else ""

        context['min_plays'] = self.min_plays if self.min_plays != 0 else ""
        context['max_plays'] = self.max_plays if self.max_plays != 100_000_000 else ""

        context['genres'] = self.request.GET.getlist("genre")
        context['languages'] = self.request.GET.getlist("language")
        context['map_types'] = self.request.GET.getlist("map_type")


        context["min_star"] = self.min_star
        context["max_star"] = self.max_star

        context["min_ar"] = self.min_ar
        context["max_ar"] = self.max_ar

        context["min_od"] = self.min_od
        context["max_od"] = self.max_od

        context["min_cs"] = self.min_cs
        context["max_cs"] = self.max_cs

        context["min_hp"] = self.min_hp
        context["max_hp"] = self.max_hp

        context["scroll_state"] = self.scroll_state
        context["volume"] = self.volume

        return context