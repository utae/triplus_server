from django.contrib import admin
from trip_info.models import TripInfo, TripInfoDetail, TripInfoComment
from django.utils.translation import ugettext_lazy as _


class TripInfoDetailInline(admin.TabularInline):
    model = TripInfoDetail


class TripInfoCommentInline(admin.TabularInline):
    model = TripInfoComment


@admin.register(TripInfo)
class TripInfoAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'author', 'created_at', 'last_modified_at', 'main_img',)
    list_display_links = ('id', 'title',)
    list_filter = ('id', 'created_at',)
    search_fields = ('title', 'author',)
    fieldsets = (
        (_('게시물 정보'), {'fields': ('title', 'author', 'city', 'created_at', 'last_modified_at', 'main_img', 'hash_tag_set',)}),
        (_('유저 반응'), {'fields': ('like_user_set',)}),
    )
    ordering = ('-id',)
    filter_horizontal = ()
    readonly_fields = ('created_at', 'last_modified_at', )
    inlines = (TripInfoDetailInline, TripInfoCommentInline, )


@admin.register(TripInfoDetail)
class TripInfoDetailAdmin(admin.ModelAdmin):
    list_display = ('id', 'trip_info', 'text', 'image',)
    list_display_links = ('id', 'trip_info',)
    search_fields = ('trip_info', )
    fieldsets = (
        (_('관련 게시물'), {'fields': ('trip_info',)}),
        (_('페이지 정보'), {'fields': ('text', 'image',)}),
    )
    ordering = ('-id',)
    filter_horizontal = ()


@admin.register(TripInfoComment)
class TripInfoCommentAdmin(admin.ModelAdmin):
    list_display = ('id', 'trip_info', 'user', 'text', 'created_at', 'last_modified_at',)
    list_display_links = ('id', 'trip_info',)
    search_fields = ('trip_info', )
    fieldsets = (
        (_('관련 게시물'), {'fields': ('trip_info',)}),
        (_('댓글 정보'), {'fields': ('user', 'text', 'created_at', 'last_modified_at',)}),
    )
    ordering = ('-id',)
    readonly_fields = ('user', 'created_at', 'last_modified_at',)
