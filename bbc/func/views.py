from django.views import View
from member import models as mem_models
from booking import models as bk_models
from rest_framework import viewsets  # for monitor api
from . import serializers as s  # for monitor api

# Create your views here.


class GroupViewSet(viewsets.ModelViewSet):
    queryset = mem_models.Group.objects.all().order_by('id')
    serializer_class = s.GroupSerializer


class GroupMemberViewSet(viewsets.ModelViewSet):
    queryset = mem_models.GroupMember.objects.all().order_by('id')
    serializer_class = s.GroupMemberSerializer


class MemberViewSet(viewsets.ModelViewSet):
    queryset = mem_models.Member.objects.all().order_by('id')
    serializer_class = s.MemberSerializer


class ConfirmPayViewSet(viewsets.ModelViewSet):
    queryset = bk_models.ConfirmPay.objects.all().order_by('id')
    serializer_class = s.ConfirmPaySerializer


class CourtDetailViewSet(viewsets.ModelViewSet):
    queryset = bk_models.CourtDetail.objects.all().order_by('id')
    serializer_class = s.CourtDetailSerializer


class OtherDetailViewSet(viewsets.ModelViewSet):
    queryset = bk_models.OtherDetail.objects.all().order_by('id')
    serializer_class = s.OtherDetailSerializer


class HistoryGuessViewSet(viewsets.ModelViewSet):
    queryset = bk_models.HistoryGuess.objects.all().order_by('id')
    serializer_class = s.HistoryGuessSerializer


class HistoryMemberViewSet(viewsets.ModelViewSet):
    queryset = bk_models.HistoryMember.objects.all().order_by('id')
    serializer_class = s.HistoryMemberSerializer


class HistoryGroupViewSet(viewsets.ModelViewSet):
    queryset = bk_models.HistoryGroup.objects.all().order_by('id')
    serializer_class = s.HistoryGroupSerializer


class RequestMemberViewSet(viewsets.ModelViewSet):
    queryset = bk_models.RequesMember.objects.all().order_by('id')
    serializer_class = s.RequestMemberSerializer


class RefundViewSet(viewsets.ModelViewSet):
    queryset = bk_models.Refund.objects.all().order_by('id')
    serializer_class = s.RefundSerializer


class StatusViewSet(viewsets.ModelViewSet):
    queryset = bk_models.Status.objects.all().order_by('id')
    serializer_class = s.StatusSerializer


# class RefundViewSet(viewsets.ModelViewSet):
#     queryset = bk_models.Refund.objects.all().order_by('id')
#     serializer_class = s.RefundSerializer


# class PriceViewSet(viewsets.ModelViewSet):
#     queryset = bk_models.Price.objects.all().order_by('id')
#     serializer_class = s.PriceSerializer


# class TimeViewSet(viewsets.ModelViewSet):
#     queryset = bk_models.Time.objects.all().order_by('id')
#     serializer_class = s.TimeSerializer
