from django.contrib import admin
from .models import TripPackage, TripPackageAddition, TripPackageDetail, TripPackageMainImg, TripPackageReview
from django.utils.translation import ugettext_lazy as _


class TripPackageMainImgInline(admin.TabularInline):
    model = TripPackageMainImg
    extra = 0
    min_num = 1


class TripPackageDetailInline(admin.TabularInline):
    model = TripPackageDetail
    extra = 0
    min_num = 1


class TripPackageAdditionInline(admin.TabularInline):
    model = TripPackageAddition
    extra = 0


class TripPackageReviewInline(admin.TabularInline):
    model = TripPackageReview


@admin.register(TripPackage)
class TripInfoAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'guide', 'created_at', 'last_modified_at')
    list_display_links = ('id', 'title',)
    list_filter = ('id', 'created_at',)
    search_fields = ('title', 'guide',)
    fieldsets = (
        (_('상품 정보'), {'fields': ('title', 'sub_title', 'city', 'price', 'address', 'guide', 'created_at', 'last_modified_at', 'hash_tag_set',)}),
        (_('유저 반응'), {'fields': ('like_user_set',)}),
    )
    ordering = ('-id',)
    readonly_fields = ('created_at', 'last_modified_at', )
    inlines = (TripPackageMainImgInline, TripPackageDetailInline, TripPackageAdditionInline, )


@admin.register(TripPackageMainImg)
class TripPackageMainImgAdmin(admin.ModelAdmin):
    list_display = ('id', 'trip_package', 'image',)
    list_display_links = ('id', 'trip_package',)
    search_fields = ('trip_package', )
    fieldsets = (
        (_('상품'), {'fields': ('trip_package',)}),
        (_('이미지'), {'fields': ('image',)}),
    )
    ordering = ('-id',)


@admin.register(TripPackageDetail)
class TripPackageDetailAdmin(admin.ModelAdmin):
    list_display = ('id', 'trip_package', 'image', 'text')
    list_display_links = ('id', 'trip_package',)
    search_fields = ('trip_package',)
    fieldsets = (
        (_('상품'), {'fields': ('trip_package',)}),
        (_('이미지'), {'fields': ('image',)}),
    )
    ordering = ('-id',)


@admin.register(TripPackageAddition)
class TripPackageAdditionAdmin(admin.ModelAdmin):
    list_display = ('id', 'trip_package', 'title', 'text')
    list_display_links = ('id', 'trip_package',)
    search_fields = ('trip_package',)
    fieldsets = (
        (_('상품'), {'fields': ('trip_package',)}),
        (_('이미지'), {'fields': ('title', 'text',)}),
    )
    ordering = ('-id',)


@admin.register(TripPackageReview)
class TripPackageReviewAdmin(admin.ModelAdmin):
    list_display = ('id', 'trip_package', 'user', 'rating', 'created_at', 'last_modified_at',)
    list_display_links = ('id', 'trip_package',)
    search_fields = ('trip_package', )
    fieldsets = (
        (_('상품'), {'fields': ('trip_package',)}),
        (_('리뷰 정보'), {'fields': ('user', 'rating', 'image', 'text', 'created_at', 'last_modified_at',)}),
    )
    ordering = ('-id',)
    readonly_fields = ('user', 'created_at', 'last_modified_at',)
