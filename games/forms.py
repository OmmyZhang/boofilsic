from django import forms
from django.contrib.postgres.forms import SimpleArrayField
from django.utils.translation import gettext_lazy as _
from .models import Game, GameMark, GameReview
from common.models import MarkStatusEnum
from common.forms import *


def GameMarkStatusTranslator(status):
    trans_dict = {
        MarkStatusEnum.DO.value: _("在玩"),
        MarkStatusEnum.WISH.value: _("想玩"),
        MarkStatusEnum.COLLECT.value: _("玩过")
    }
    return trans_dict[status]


class GameForm(forms.ModelForm):
    # id = forms.IntegerField(required=False, widget=forms.HiddenInput())

    other_info = JSONField(required=False, label=_("其他信息"))

    class Meta:
        model = Game
        fields = [
            'title',
            'source_site',
            'source_url',
            'other_title',
            'developer',
            'publisher',
            'release_date',
            'genre',
            'platform',
            'cover',
            'brief',
            'other_info'
        ]

        widgets = {
            'other_title': forms.TextInput(attrs={'placeholder': _("多个别名使用英文逗号分隔")}),
            'developer': forms.TextInput(attrs={'placeholder': _("多个开发商使用英文逗号分隔")}),
            'publisher': forms.TextInput(attrs={'placeholder': _("多个发行商使用英文逗号分隔")}),
            'genre': forms.TextInput(attrs={'placeholder': _("多个类型使用英文逗号分隔")}),
            'platform': forms.TextInput(attrs={'placeholder': _("多个平台使用英文逗号分隔")}),
            'cover': PreviewImageInput(),
        }


class GameMarkForm(MarkForm):

    STATUS_CHOICES = [(v, GameMarkStatusTranslator(v))
                      for v in MarkStatusEnum.values]

    status = forms.ChoiceField(
        label=_(""),
        widget=forms.RadioSelect(),
        choices=STATUS_CHOICES
    )

    class Meta:
        model = GameMark
        fields = [
            'id',
            'game',
            'status',
            'rating',
            'text',
            'is_private',
        ]
        labels = {
            'rating': _("评分"),
        }
        widgets = {
            'game': forms.TextInput(attrs={"hidden": ""}),
        }


class GameReviewForm(ReviewForm):

    class Meta:
        model = GameReview
        fields = [
            'id',
            'game',
            'title',
            'content',
            'is_private'
        ]
        labels = {
            'book': "",
            'title': _("标题"),
            'content': _("正文"),
            'share_to_mastodon': _("分享到长毛象")
        }
        widgets = {
            'game': forms.TextInput(attrs={"hidden": ""}),
        }
