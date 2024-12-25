import logging

logger = logging.getLogger(__name__)


class UserService:

    def __init__(self, user):
        self.user = user
