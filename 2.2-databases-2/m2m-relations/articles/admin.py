from django.contrib import admin
from django.core.exceptions import ValidationError
from django.forms import BaseInlineFormSet

from .models import Article, Scope, Tag


class ScopeInlineFormset(BaseInlineFormSet):
    def clean(self):
        main_cnt = 0
        for form in self.forms:
            is_main = form.cleaned_data.get('is_main')
            if is_main:
                main_cnt += 1

        if main_cnt < 1:
            raise ValidationError('Должен быть хотя бы один основной тег')
        elif main_cnt > 1:
            raise ValidationError('Основной тег должен быть только один')

        return super().clean()  # вызываем базовый код переопределяемого метода


class ScopeInline(admin.TabularInline):
    model = Scope
    formset = ScopeInlineFormset


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    inlines = [ScopeInline]


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    pass
