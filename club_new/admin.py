from django.contrib import admin
from .models import Club, Moderator, Member, Slider


class ModeratorInline(admin.TabularInline):
    model = Moderator
    extra = 1
    fields = ('name', 'designation', 'image')
    # readonly_fields = ('image',)

class MemberInline(admin.TabularInline):
    model = Member
    extra = 2
    fields = ('name', 'designation', 'image')
    # readonly_fields = ('image',)

@admin.register(Club)
class ClubAdmin(admin.ModelAdmin):
    list_display = ('name', 'established_year')
    inlines = [ModeratorInline, MemberInline]  # Add the PhotoInline here


@admin.register(Slider)
class SliderAdmin(admin.ModelAdmin):
    list_display = ['title', 'order', 'is_active']
    list_editable = ['order', 'is_active']