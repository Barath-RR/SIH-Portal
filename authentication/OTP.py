import math
from random import random
from django.core.mail import send_mail


class OTP:

    _otp = ""

    def generate_otp(self):
        digits = "0123456789"
        for i in range(4):
            self._otp += digits[math.floor(random() * 10)]
        return self._otp

    def match_otp(self, entered_otp):
        if self._otp == entered_otp:
            self.reset_otp()
            return True
        self.reset_otp()
        return False

    def send_otp(self, user_email):
        otp = self.generate_otp()
        try:
            send_mail(
                "Your OTP for verifying your email",
                "Here is your OTP: " + otp,
                "noreply@sih.gov.in",
                [user_email],
                fail_silently=False
            )
        except Exception as e:
            print(e)
        return True

    def reset_otp(self):
        self._otp = ""
        return True


otp = OTP()
