from allauth.account.adapter import DefaultAccountAdapter


class AccountAdapter(DefaultAccountAdapter):

    def clean_username(self, username, shallow=True):
        return super().clean_username(username, shallow)
