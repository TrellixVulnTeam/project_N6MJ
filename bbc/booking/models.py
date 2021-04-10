from django.db import models
from member.models import Member, Group
from django.contrib.auth.models import User
# Create your models here.


class AllCourtInfo(models.Model):
    class Meta:
        db_table = 'bbc_allcourtinfo'

    force_close = models.BooleanField(default=False)  # for close allcourt
    range_booking = models.DurationField()  # range can booking before
    payment_member_duration = models.DurationField()  # must pay in this duration(mem)
    payment_guest_duration = models.DurationField()  # must pay in this duration(g)
    refund_duration = models.DurationField()  # refund duration only
    refund_percent = models.DecimalField(
        max_digits=4, decimal_places=2)  # percent can refund in time
    open_time = models.TimeField()
    close_time = models.TimeField()
    # use when member create group(not include header)
    num_of_creategroup = models.PositiveIntegerField()
    announce = models.CharField(max_length=1000)  # for annouce information
    ads = models.CharField(max_length=500)  # for promote something
    rules = models.CharField(max_length=1000)  # store rule when go to court
    # store image qrcode for payment
    qrcode = models.ImageField(null=True, upload_to='qrcode')


class EachCourtInfo(models.Model):
    class Meta:
        db_table = 'bbc_eachcourtinfo'
    court_number = models.IntegerField(unique=True)
    price_normal = models.DecimalField(max_digits=5, decimal_places=2)
    price_ds_mem = models.DecimalField(max_digits=5, decimal_places=2)
    price_ds_group = models.DecimalField(max_digits=5, decimal_places=2)
    price_ds_time = models.DecimalField(max_digits=5, decimal_places=2)
    time_ds_start = models.TimeField()
    time_ds_end = models.TimeField()
    is_maintain = models.BooleanField(default=False)


class Booking(models.Model):
    class Meta:
        db_table = 'bbc_booking'
    name = models.CharField(max_length=100)  # for show who's booked
    email = models.EmailField()
    tel = models.CharField(max_length=15)
    member = models.ForeignKey(
        Member, on_delete=models.CASCADE, null=True)  # null if guest
    # null if not group booking
    group = models.ForeignKey(Group, on_delete=models.CASCADE, null=True)
    court = models.ForeignKey(
        EachCourtInfo, on_delete=models.CASCADE)  # what court
    booking_datetime = models.DateTimeField()  # datetime booking
    exp_datetime = models.DateTimeField()  # for pay in this time
    price_normal = models.DecimalField(
        max_digits=5, decimal_places=2)  # each booking slot
    price_ds = models.DecimalField(
        max_digits=5, decimal_places=2)  # each booking slot
    price_pay = models.DecimalField(
        max_digits=5, decimal_places=2)  # each booking slot
    # 0 = booking, 1 = confirmed, 2 = canceled, 3 = checkedPayment false(checking not found transaction)
    payment_state = models.IntegerField(default=0)
    timestamp = models.DateTimeField(auto_now=True)  # time now when booking
    # bookingid for identify your court was booked
    bookingid = models.CharField(max_length=32)
    # identify your payment (can repeated)
    paymentid = models.CharField(max_length=32, null=True)
    # use when delete by member or admin but stored
    is_deleted = models.BooleanField(default=False)


class Payment(models.Model):
    class Meta:
        db_table = 'bbc_payment'
    paymentid = models.CharField(max_length=32, unique=True)
    payment_otp = models.IntegerField()  # for write in your slip for easier checking
    # time when send slip for checking can be approximate
    timestamp = models.DateTimeField(auto_now=True)
    pay = models.DecimalField(max_digits=5, decimal_places=2)
    # change when check success by admin
    is_checked = models.BooleanField(default=False)
    # changee when checking found transaction if not change state in booking table to 3
    is_founded = models.BooleanField(default=True)


class Refund(models.Model):
    class Meta:
        db_table = 'bbc_refund'
    payment = models.ForeignKey(
        Payment, on_delete=models.CASCADE)
    detail = models.CharField(max_length=20)  # customer bankingid
    timestamp = models.DateTimeField(
        auto_now=True)  # for check is in refund time
    is_refunded = models.BooleanField(
        default=False)  # change when refund success
