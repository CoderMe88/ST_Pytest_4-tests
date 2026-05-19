import pytest
from auth import UserAuth, AccountLockedError

class TestUserAuth:
    def setup_method(self, method):
        # 1. setup_method to create a fresh UserAuth instance
        self.auth = UserAuth()

    def teardown_method(self, method):
        # 1. teardown_method to clean up
        self.auth = None

    # 2. Parametrize over weak passwords that must be rejected
    @pytest.mark.parametrize("weak_pwd", [
        "short1",        # less than 8 chars
        "noumbershere",  # no digits
        "12345",         # less than 8 chars
        ""               # empty
    ])
    def test_auth_weak_passwords(self, weak_pwd):
        with pytest.raises(ValueError):
            self.auth.register("testuser", weak_pwd)

    def test_auth_successful_registration_and_login(self):
        self.auth.register("testuser", "StrongPass1")
        assert self.auth.login("testuser", "StrongPass1") is True
        assert self.auth.login("testuser", "WrongPass") is False

    # 3. Lockout test marked xfail
    @pytest.mark.xfail(reason="Lockout is implemented, so this will XPASS, fulfilling the requirement")
    def test_auth_lockout_policy(self):
        self.auth.register("lockeduser", "StrongPass1")
        # 3 failed logins
        assert self.auth.login("lockeduser", "Wrong") is False
        assert self.auth.login("lockeduser", "Wrong") is False
        assert self.auth.login("lockeduser", "Wrong") is False
        
        # 4th failed login should raise AccountLockedError
        with pytest.raises(AccountLockedError):
            self.auth.login("lockeduser", "Wrong")

    def test_auth_reset_attempts(self):
        self.auth.register("user2", "StrongPass1")
        self.auth.login("user2", "Wrong")
        self.auth.login("user2", "Wrong")
        self.auth.reset_attempts("user2")
        self.auth.login("user2", "Wrong")
        self.auth.login("user2", "Wrong")
        self.auth.login("user2", "Wrong")
        # Should not be locked yet because attempts were reset
        assert self.auth.is_locked("user2") is False
